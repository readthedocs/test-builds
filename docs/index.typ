#set document(
  title: "Typst on Read the Docs",
  author: "Read the Docs",
)
#set page(paper: "a4", numbering: "1")
#set heading(numbering: "1.")

#align(center)[
  #text(size: 24pt, weight: "bold")[Typst on Read the Docs]

  #v(0.5em)
  A proof of concept building a PDF with Typst via `build.commands`
]

= About this scenario

This branch is a proof of concept that builds this PDF with
#link("https://typst.app")[Typst] on Read the Docs, overriding the build
process with `build.commands`.

It is loosely based on the GitHub Actions workflow from
#link("https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/visual-programming-languages-docs")[visual-programming-languages-docs],
which installs Typst from GitHub releases and compiles Markdown content
converted with Pandoc, with Mermaid diagrams rendered separately. This
scenario only exercises the Typst compilation itself, skipping the
Pandoc and Mermaid steps.

= How it works

+ The prebuilt Typst binary is downloaded from GitHub releases.
+ `typst compile` renders `docs/index.typ` into
  `$READTHEDOCS_OUTPUT/pdf/`.
+ A minimal HTML landing page is copied into
  `$READTHEDOCS_OUTPUT/html/`, with a copy of the PDF alongside it.

= QA criteria

The build is a success when:

- The build completes without errors.
- This PDF is offered as a download for the version (flyout menu) and is
  linked from the HTML landing page.
- The typesetting samples below render correctly.

= Typesetting samples

== Code

```python
def hello():
    print("Hello from Typst on Read the Docs!")
```

== Table

#table(
  columns: (auto, auto, auto),
  table.header([*Format*], [*Tool*], [*Output*]),
  [PDF], [Typst], [`$READTHEDOCS_OUTPUT/pdf/`],
  [HTML], [static page], [`$READTHEDOCS_OUTPUT/html/`],
)

== Math

The quadratic formula:

$ x = (-b plus.minus sqrt(b^2 - 4 a c)) / (2 a) $
