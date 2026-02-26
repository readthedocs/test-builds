# -*- coding: utf-8 -*-
import os
import sys
import time
import tracemalloc

from pyinstrument import Profiler

# Make modules in the docs/ directory importable from runblock directives,
# which execute in a subprocess that inherits the environment.
_docs_dir = os.path.dirname(os.path.abspath(__file__))
os.environ['PYTHONPATH'] = _docs_dir + os.pathsep + os.environ.get('PYTHONPATH', '')

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'

# Copy llms.txt to the HTML output
html_extra_path = ['../llms.txt']


# ── Build-phase budget limits ──────────────────────────────────────────────
# Each phase: (max_seconds, max_MB).  Generous enough to pass on RTD hardware.
_PHASE_BUDGETS = {
    'Init':         (30,  100),
    'Read sources': (60,  300),
    'Write output': (60,  300),
}

# ── Phase-tracking state ───────────────────────────────────────────────────
_tracker = {'phase_start': None, 'phases': []}


def _checkpoint(phase_name):
    """Record a completed build phase and reset the timer."""
    now = time.perf_counter()
    if _tracker['phase_start'] is not None:
        duration = now - _tracker['phase_start']
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.clear_traces()
        _tracker['phases'].append(
            dict(name=phase_name, duration_s=duration, peak_mb=peak / 1024 / 1024)
        )
    _tracker['phase_start'] = now


def _on_builder_inited(app):
    tracemalloc.start()
    _tracker['phase_start'] = time.perf_counter()


def _on_env_before_read_docs(app, env, docnames):
    _checkpoint('Init')


def _on_env_updated(app, env):
    _checkpoint('Read sources')


def _on_build_finished(app, exception):
    _checkpoint('Write output')
    if tracemalloc.is_tracing():
        tracemalloc.stop()

    if exception or app.builder.name != 'html':
        return

    # Phase-timing table
    with open(os.path.join(app.outdir, 'build_phases.html'), 'w') as fh:
        fh.write(_render_phase_table(_tracker['phases']))

    # Synthetic workload profiles (CPU and memory examples)
    _generate_synthetic_profiles(app)


def _render_phase_table(phases):
    """Return a self-contained HTML page with a phase-timing/budget table."""
    rows = []
    for p in phases:
        budget_s, budget_mb = _PHASE_BUDGETS.get(p['name'], (None, None))
        s_ok = budget_s is None or p['duration_s'] <= budget_s
        m_ok = budget_mb is None or p['peak_mb'] <= budget_mb
        ok = s_ok and m_ok
        status_cls = 'pass' if ok else 'fail'
        status_txt = '✔ PASS' if ok else '✘ FAIL'
        rows.append(
            f'<tr>'
            f'<td>{p["name"]}</td>'
            f'<td>{p["duration_s"]:.3f}</td>'
            f'<td>{"≤ " + str(budget_s) if budget_s else "—"}</td>'
            f'<td>{p["peak_mb"]:.2f}</td>'
            f'<td>{"≤ " + str(budget_mb) if budget_mb else "—"}</td>'
            f'<td class="{status_cls}">{status_txt}</td>'
            f'</tr>'
        )
    total_s = sum(p['duration_s'] for p in phases)
    rows_html = ''.join(rows)
    return f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
body{{font-family:sans-serif;margin:1em;font-size:14px}}
table{{border-collapse:collapse;width:100%}}
th{{background:#2980b9;color:#fff;padding:8px 12px;text-align:left}}
td{{padding:6px 12px;border-bottom:1px solid #ddd}}
tr:nth-child(even){{background:#f8f8f8}}
.pass{{color:#27ae60;font-weight:bold}}
.fail{{color:#e74c3c;font-weight:bold}}
tfoot td{{font-weight:bold;background:#ecf0f1}}
</style></head><body>
<table>
<thead><tr>
  <th>Phase</th><th>Duration (s)</th><th>Budget (s)</th>
  <th>Peak memory (MB)</th><th>Budget (MB)</th><th>Status</th>
</tr></thead>
<tbody>{rows_html}</tbody>
<tfoot><tr>
  <td>Total</td><td>{total_s:.3f}</td><td>—</td>
  <td colspan="2" style="font-weight:normal;font-size:0.85em;color:#555">(peak memory is per-phase; not cumulative)</td><td></td>
</tr></tfoot>
</table>
</body></html>'''


def _generate_synthetic_profiles(app):
    """Generate interactive HTML profiles for the synthetic CPU/memory workloads."""
    sys.path.insert(0, _docs_dir)
    from profiling_examples import cpu_intensive_work, memory_intensive_work

    for name, fn in (('cpu_profile', cpu_intensive_work), ('memory_profile', memory_intensive_work)):
        p = Profiler()
        p.start()
        fn()
        p.stop()
        with open(os.path.join(app.outdir, name + '.html'), 'w') as fh:
            fh.write(p.output_html())


def setup(app):
    app.connect('builder-inited', _on_builder_inited)
    app.connect('env-before-read-docs', _on_env_before_read_docs)
    app.connect('env-updated', _on_env_updated)
    app.connect('build-finished', _on_build_finished)

###########################################################################
