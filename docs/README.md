# Build with Docsify


> Check out all the features from its official webpage!

This site was created following the Quickstart guide from Docsify:
https://docsify.js.org/#/quickstart

Besides following the simple Quickstart,
it adds some extra HTML tags to integrate nicely with the [Read the Docs Flyout Menu](https://docs.readthedocs.io/en/stable/flyout-menu.html).


Inside the `<head>` tag:

```html
<script crossorigin="anonymous" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script async="async" src="/_/static/javascript/readthedocs-doc-embed.js"></script>
<link rel="stylesheet" href="/_/static/css/readthedocs-doc-embed.css" type="text/css" />
<link rel="stylesheet" type="text/css" href="/_/static/css/badge_only.css" />
<script type="text/javascript">
 READTHEDOCS_DATA = {
     "project": "test-builds",
     "version": "docsify",
 }
</script>
```

Inside the `<body>` tag:

```html
<!-- Manually added to show the Read the Docs flyout -->
<div id="readthedocs-embed-flyout"></div>
```

> The Flyout Menu may not be displayed 100% integrated and styled.
> That's because I'm using the default styles. However, it can be tweaked to be awesome!
