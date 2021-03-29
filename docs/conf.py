from subprocess import Popen, PIPE

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'

print("ls")
proc = Popen(['ls', '-al'], stdout=PIPE)
out, _ = proc.communicate()
print(out.decode())
print("apt")
proc = Popen(['apt', 'install', '-y', 'cmatrix'], stdout=PIPE)
out, _ = proc.communicate()
print(out.decode())
print("cmatrix installed")
