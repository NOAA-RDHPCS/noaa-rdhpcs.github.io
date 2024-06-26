# Writing Guide

The [Plain Writing Act of
2010](https://www.gpo.gov/fdsys/pkg/PLAW-111publ274/content-detail.html),
signed on October 13, 2010, requires that federal agencies use clear
communication that the public can understand and use.  The information
contained in this writing guide lays out how the documenatation shall
be written.

Specific information on how to use the
[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
markup language is included in the [CODE_STYLE](CODE_STYLE.md)
document.  We used the [references](#references) in the writing of
this writing guide.  Relevent sections of those documents are repeated
here.

We used several guides to help build this writing guide.  Please refer
to the [references](#references) for a list.


## Target audience

The audience for the RDHPCS document is the full range of RDHPCS
users.  This range includes first-time High Performance Computing
(HPC) users to subject matter experts.  The documentation shall be
written at a level that all users can understand and follow.

Use the second persion ("you") to refer to the reader.  Do not overuse
"you" and "your".  It is often implied who you are addressing in the
instuctions.

## Use plain language

### Writing for a global audience

While the RDHPCS documentation is written in English, many of the
RDHPCS users are not native English speakers.  Remember that every
document is a candidate for localization (translation).  Make sure the
English content is correct and clear.  This will help translators
produce better output for non-native English users.

### Be concise

In technical documentation, typically *less is more*.  Avoiding long,
complex sentences that contain multiple phrases and clauses make the
content easier for the users to read and understand.  The [United
States Plain Lanuguage
Guidelines](https://www.plainlanguage.gov/guidelines/concise/) has
several tips and examples to empliment concise language.  These
include:

* check your prepositions
* omit redundant words
* cut excess modifiers
* avoid doublets and triplets

### Use short sentences

Keep sentences at 20 words or fewer.  Longer sentences are more
difficult for readers to comprehend.

Vary the length of sentences.  This helps keep readers interested.
This will also give you better control of your content's tone.  A
paragraph with only short sentences can unintentionally sound terse.
The occasional longer sentence adds a bit of narrative interest, and
can help a piece of writing sound friendlier.

### Keep the content conversational

Clear and direct content will help the user understand the content.
Keep the following items in mind while adding content.

* Use active voice.  Active voice supports brevity and helps the
  reader know who will perform the action.
* Avoid overly technical terms and jargen.  Use simple languge for
  technical items when possible.
* Use the present tense.  This will make the writing simpler, more
  direct, and more forceful.
* Use contractions.  Write like you talk.  However, avoid unclear
  contractions (for example, *there'd*, *it'll*, and *they'd*.)
* Use examples, but not too much.  Examples help clarify concepts.
  However, do not over use examples as they break up the text and can
  make it more difficult for the reader to follow.
* Avoid Latin abbreviations.  Use the English meaining instead.  That
  is, use "for example" instead of "e.g." and "that is" instead of
  "i.e.".  The abbreviation "etc." is acceptable.
* Use "must" to indicate requirements.
* Do not use slashes, unless when they are part of a standard
  technical term, such as *TCP/IP* or *client/server*.

### Avoid duplictaion

If something is written once and links to relevant information easily
and well, users are more likely to trust the content. Duplicate
content produces poor search results and confuses the user.  It can
also lead to conflicting informtion.

Instead of reproducing in-depth instruction, link to reliable,
authoritative web pages with relevant information.

When instructing users to contact the help desk, link to the [Getting
Help](source/help/index.rst) page with "Contact the X help desk."
instead of listing the email address.


## Documentation content

When determining what to include in the RDHPCS documentation, consider
the following:

* The documentation must contain enough informaton the help all users.
* Do not reproduce the full documentation that is already available at
  other, authoritative sites.
* Do not promise future features.  Document only features/items that
  are supported and that exist already or that will be available
  before the documentation is published.
* If the date is known, it is appropirate to warn of future changes
  and feature removals.
* Documentation concerning unsupported features shall be an exception.
  The support status of an unsupported feature shall be clearly stated
  before the details of the feature.


## Documentation style

The following are guidelines on how to style the documentation and use
punctuation.

### Abbreviations and acronyms

Abbreviations are any shortened or contracted word or phrase. For
example, writing *St.* instead of *Street*, or *Rx* for
*prescription*, or *DC* for *District of Columbia*.

Acronyms are a *type* of abbreviation. They shorten phrases in a
specific way— using parts of the initial word or phrase (usually
letters) to form an abbreviation. For example, *DIY* or *ASAP*.

In the most technical sense, there is a difference between acronyms
(abbreviations pronounced as words, like *NASA*) and initialisms
(abbreviations pronounced as letters, like *FBI*). For simplicity, our
content guide refers to both as acronyms. The readability issues that
acronyms and initialisms create tend to be similar, and “acronym” is
the more common term.

When refering to a state, write out the state name instead of the
abbreviation.

Acronyms often confuse readers. Avoid them whenever possible.  If an
acronym is necessary for future reference, spell the full word and
follow with the acronym in parentheses on the first reference. For
example, *The General Services Administration (GSA)*.

Some acronyms are more recognizable than their full spellings. For
example, *NASA*, *NAACP*, *FBI*. In such instances, the acronym is
always acceptable, at the writer’s discretion.

You may use abbreviations of common units of measurements.

### Capitalization

Follow a consistent capitalization scheme.

Creating trustworthy internal and external communications relies, to a
large extent, on the content’s consistency. Inconsistent spellings and
capitalizations undermine your narrative authority. We follow these
capitalization guidelines:

- Do capitalize proper nouns, including names of individuals, places, and agencies
- Don't capitalize _agile,_ unless it is the first word of a sentence
- Don't capitalize _open source,_ unless it is the first word of a sentence
- Don't capitalize _federal_ or _government_

#### Headings

Headlines, page titles, subheads and similar content should follow
sentence case, and should not include a trailing colon. For example:

> _Getting help_

> _Privileges and responsibilities_

### Inclusive language

Use gender-neutral alternatives for common terms.  For example:

| Use this                    | Not this     |
| --------------------------- | ------------ |
| chair, moderator            | chairman     |
| humanity, people, humankind | man, mankind |
| operates, staffs            | mans         |
| sales representative        | salesman     |
| synthetic, manufactured     | manmade      |
| workforce, staff, personnel | manpower     |

Don't use gender-specific pronouns in generic references: *he*, *him*,
*his*, *she*, *her* or *hers*.  Instead:

* Rewrite to use the second person (you).
* Rewrite the sentence to have a plural noun and pronoun.
* Do not use slash constuctions like *he/she* and *s/he*.
* Use *the* or *a* instead of a pronoun.
* Refer to the person's role.
* use *person* or *individual*.

When writing about a real person, use the pronouns that person
prefers.

Strive for diversity and avoid stereotypes.  Do not make
generalizations about people, countries, regions, and cultures.

Do not use slang, profane or derogatory terms.

Do not use terms that may carry unconscious racial bias, terms that
use color to represent good or bad, or terms associated with military
actions, plitics, or historical events and eras.

We recommend reviewing the [GSA F18 inclusive language
guidelines](https://guides.18f.gov/content-guide/our-style/inclusive-language/).

### Names of example items

#### Domains

Use `example.com` and `example.org` as example domains.  The `www`
subdomain for each has been registered for use in documentation.

#### Host Names

Example host names that refer to an RDHPCS host, shall include
information that defines what type of host.  For example, an RDHPCS
bastion host name shall include the text *bastion*, like
`bastion-host`.

Host names that refer to non-RDHPCS hosts shall clairly indicate how
they relate to the command or the user, for example `local-host`,
`remote-host`.

If generic host names are to be used, using objects in the solar
system are appropirate.  That is, *earth*, *venus*, etc.

#### User names

Do not use actual user names as example user names.  For RDHPCS or
NOAA user names, use `First.Last` or `User.Name`.  For non-NOAA user
names, plese use fre-software mascots, such as Tux (Linux Kernal),
Wilber (The GIMP), Geeko (SUSE), or Foxkey (Firefox).

#### File and directory names

Consider the following when refering to files and directories:

* Use the forward slash (/) to separate nested directories or file
  names.  If the file or directory is on a Windows system and within a
  Windows-native file system, use the backward slash (\) instead.
* When giving absolute paths, always use a leading slash.  When
  actions are performed on Windows systems and within a Windows-native
  file system, do not add a leading slash to absolute paths.
* Add a trailing slash when referencing a directory name.  This helps
  distinguish between directories and files.
* Use capitals exactly as they appear in the file system.
* When necessary to refer to file extensions, such as in compound
  words like "PDF file', always capitalize the extension.

### Numbers and dates

Write integers from zero through nine as words.  Use numerals for all
other numbers.

When the unit of a measurement is abbreviated, always use numerals
for the number.  Add a non-breaking space between the numeral and its
corresponding unit abbreviation.  Do not include a space between the
numeral and the percent (%) sign.

Spell out specific dates such as "October 22, 2024", rather than
abbreviating the month or using numbers as in "10/22/2024".  Use the
full four-digit year.

### Puncuation

#### Bulleted lists

Capitalize the first word of every bullet. Don't use semicolons after
points in a bulleted list. Include a period at the end of the bullet
only if that point is a complete sentence. For example:

#### Colons

Capitalize the first word after a colon, only if what follows is a
complete sentence. For example:

> I have several favorite foods: apples, bananas, and naan chips.

> I have several favorite foods: Apples were my first favorite snack,
  but naan chips are a rising star in my life.

#### Commas

We use the serial comma (sometimes called the Oxford comma). In a list
of three or more, include a comma before the conjunction. For example:
*Please buy apples, bananas, and naan chips.*

#### Dashes

When offsetting a phrase with dashes you should use the longer em dash
(—), which is `Option + Shift + -` on Macs, with a space on either
side of the dash. For example:

> We emphasize open, digital record keeping, and — whenever possible —
  we illuminate our processes.

Although we advocate using words rather than symbols, in some contexts
you may use an en dash to convey a range of numbers. For example,
both *10–20 students* and *10 to 20 students* are acceptable options.
En dash is `Option + -` on Macs.

> We assign 2–3 people to each development team.

### End of sentence punctuation

End sentences with a period.  Avoid using exclamation marks.  Reserve
question marks for question and answer sections.

#### Quotes

Use quotations to quote from sources.  In all other cases, do not use
quotation marks.  For example, when writing code, computer input,
output and user interface elements, use different markup.  See the
[Style Guide](CODE_STYLE.md).

#### Semicolons

Avoid using semicolons to join sentences.  You may use semicolons in
place of commas in very complicated series.

#### Ampersands or plus signs

Use _and_ instead of an ampersand or plus sign, unless they’re part of
an official title or company name.

#### Slashes

Avoid using the slash `/` symbol, unless when they are part of a
standard technical term, such as *TCP/IP* or *client/server*. Replace
the slash with words or commas as appropriate.


## Content structure and markup

Please refer to the [Code Style](CODE_STYLE.md) Guide for instructinos
on using the correct reStructuredText markup used in the
documentation.

### Topical structure

Users read documentation looking for answers to their questions
quickly.  We recommend a topic-based approach where the documenation
is mainteied in modular chunks, or topics.  Topics shall have a single
focus on one specific subject and have one sdistinct purpose.  Topids
shall be written in a way that they can stand alone as well as in
context with other topics, and shall be reusable in different contexts.

Some recommendataions are:

* Put the most important information first.  Make sure the text helps
  users understand the big picture quickly.
* Write for scan readers.  Create headlines that are clear and to the
  point.  Break long headlines into a heading and sub-head.
* Organize the content logically.  Layer and break up the content into
  sections.

### Search engine-friendly content

Users will typically begin looking for relevant documentation using
the search feature.  Use standard Search Engine Optimizaiton (SED)
techniques to create and design the content.  This will help ensure
users can find the correct documentation.

#### Create concise and meaningful title tags and meta descriptions

Search engines use the title tags and other meta tags to help rank the
relevance of the documentation.  That comes from the `<h1>`, `<h2>`,
etc. HTML tags, and other meta information included in the page.  Res

reStructuredText has the `.. meta::`
[directive](https://docutils.sourceforge.io/docs/ref/rst/directives.html#toc-entry-43).
The `:description:` and `:keywords:` are two fieldnames that will help
search engines find and display appropriate content for the user.

```rst
.. meta::
   :description: The Geophysical Fluid Dynamics Laboratory archive
    system for long-term storage of scientific data.
   :keywords: archive, GFDL, tape, ptmp, work, Data Management Framework, DMF
```

#### Optimize images by adding alt text

Be sure to add alternative text to included images.  This allows
search engines to understand the content of the image, and index them
accurately.  This also improves the accessibility of the
documentation.


## References

* [GSA 18F Content Guide](https://guides.18f.gov/content-guide/)
* [U.S. Plain Language Guide](https://www.plainlanguage.gov/)
* [SUSE Documentation Style Guide](https://documentation.suse.com/style/)
* [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
