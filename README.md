# jvd-report

This repo contains a script to genereate beautiful reports from jupyter html experted notebooks, and also serves as a CDN for the css/js/img needed in the reports.

This allows to generate a standalone html reports, than can be later shared with colleagues.

## How to use

Export a ipynb into html, rename it to `input.html`, put it inside jvd-report and run `render.py`.

## Project Title

To add a project title, add a markdown cell into de ipynb with the tag `<h1 id='title'>Project Title</h1>`.

## Table of contents

To add a table of contents as a left-side navigation bar, add a markdown cell in the ipynb before exporting with the following content:

```html
<div id="index_div">
<ul>
<li><a href='#ref1'>Section1</a></li>
<li><a href='#ref1'>Section2</a></li>
<li><a href='#ref1'>Section3</a></li>
</ul>
</div>
```

Then you can add the following markdown preceding each section:

```html
<a id='loading'></a>
```

`render.py` will automatically generate the right-bar table of contents.
