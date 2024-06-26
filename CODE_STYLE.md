# Documentation Style Guide

This document focuses on expected styles used in the RDHPCS documentation. This
coding standards applies to documentation files. It is not about documentation
content.


## Markup Language

The documentation in this repository uses [Python
Sphinx](https://www.sphinx-doc.org/en/master/), with the [Read the Docs
Theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/).  As much as
possible, we use the
[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
markup.


## Filenames

Filenames used in the source should use only lowercase alphanumeric
characters and `-` (minus) symbol.

Suffix filenames with the `.rst` extension.

:warning: RST files are human-readable text files.  Some programs will parse
`.rst` files with `rst2html`, which cannot interpret some of Sphinx's directives
such as `.. code-block::`.  Such readers, e.g., the GitHub platform, will not
display all content.

When you need to read HTML builds of the documentation, best practice is to
export documentation as static builds with ``sphinx-build`` command, then host
and serve these builds as static files. Refer to the [Contributing to these
docs](source/contributing/index.rst) for information on how to build and host
these pages.


## Whitespaces

### Indentation

Indent with 2-4 spaces.  Follow the indentation already established in the file.

### Blank lines

Two blank lines before overlined sections, i.e. before H1 and H2. One blank line
before other sections. See [Headings](#headings) for an example.

One blank line to separate directives.

```rst

  Some text before.

  .. note::

    Some note.
```

Exception: directives can be written without blank lines if they are only one
line long.

```rst

  .. note:: A short note.
```


## Line length

Limit all lines to a maximum of 79 characters.

Exception: tables and long URLs.


## Headings

Use the following symbols to create headings:

1. `#` with overline
2. `*` with overline
3. `=`
4. `-`
5. `^`
6. `"`

As an example:

```rst

  ##################
  H1: document title
  ##################

  Introduction text.


  *********
  Sample H2
  *********

  Sample content.


  **********
  Another H2
  **********

  Sample H3
  =========

  Sample H4
  ---------

  Sample H5
  ^^^^^^^^^

  Sample H6
  """""""""

  And some text.
```

If you need more than heading level 4 (i.e. H5 or H6), then you should consider
creating a new document.

There should be only one H1 in a document.

See also [Sphinx's documentation about
sections](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections).

### H1 Headings

The H1 headings should only be used in the `index.rst` file, and must be the
first heading of the document.  Other files in a given directory will use the H2
heading as the first heading of the document.


## Code blocks

Use the `.. code-block::` directive **and** specify the programming language. As
an example:

```rst

  .. code-block:: python

    import this
```

:information_source: Use of the `.. code::` directive may also be used.
However, it does not have as many options as the `.. code-block::` directive.

The code block directive uses [Pygments](https://pygments.org).
Please refer to the [list of supported
languages](https://pygments.org/languages/).

### Shell Code Blocks

Shell code blocks, `.. code-block:: shell`, if representing commands a user will
type shall use the `$` to represent the prompt.

## Links and references

Use links and references footnotes with the ``target-notes`` directive.
As an example:

```rst

  #############
  Some document
  #############

  Some text which includes links to `Example website`_ and many other links.

  `Example website`_ can be referenced multiple times.

  (... document content...)

  And at the end of the document...

  **********
  References
  **********

  .. target-notes::

  .. _`Example website`: http://www.example.com/
```

## Tables

As much as possible, use simple tables or grid tables.  If keeping the
lines of the tables under the 79 characters is too difficult with one
of those tables, use the list table directive (`.. list-table`).

## Page meta information

Use the meta (`.. meta`) directive to add additional meta information
to the page.

## Tests

We run several tests prior to accepting all documentation modification.  The tests include:

* build test
* lint test
* valid link test

### Build test

The information in [CONTRIBUTING.md](CONTRIBUTING.md) and
[Contributing to these docs](source/contributing/index.rst) has
instruction on how to build the pages.  All warnings and error must be
resolved.

### Lint test

We use the [doc8](https://pygments.org/languages/) style checking tool
for RST.  The included checks are:

- invalid RST format
- lines should not be longer than 79 characters
  - RST exception: line with no whitespace except in the beginning
  - RST exception: lines with http or https urls
  - RST exception: literal blocks
  - RST exception: rst target directives
- no trailing whitespace
- no tabulation for indentation
- no carriage returns (use unix newlines)
- no newline at end of file

All RST files must pass the lint checks.

### Valid link test

To run the link test, run `make linkcheck`.  All links must be valid
and resolvable.  Redirects will be allowed to sites that require the
user to login.  All other redirects must be resolved.