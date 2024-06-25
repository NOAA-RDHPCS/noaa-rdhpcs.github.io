# Writing Guide

The information contained in this writing guide lays out how the
documenatation shall be written.  Specific information on how to use
the
[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
markup language is included in the [CODE_STYLE](CODE_STYLE.md)
document.  We used the [references](#references) in the writing of
this writing guide.  Relevent sections of those documents are repeated
here.


## Target Audience

The audience for the RDHPCS document is the full range of RDHPCS
users.  This range includes first-time High Performance Computing
(HPC) users to subject matter experts.  The documentation shall be
written at a level that all users can understand and follow.


## Documentation Content

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


## Names of Example Items

### Domains

Use `example.com` and `example.org` as example domains.  The `www`
subdomain for each has been registered for use in documentation.

### Host Names

Example host names that refer to an RDHPCS host, shall include
information that defines what type of host.  For example, an RDHPCS
bastion host name shall include the text *bastion*, like
`bastion-host`.

Host names that refer to non-RDHPCS hosts shall clairly indicate how
they relate to the command or the user, for example `local-host`,
`remote-host`.

If generic host names are to be used, using objects in the solar
system are appropirate.  That is, *earth*, *venus*, etc.

### User Names

Do not use actual user names as example user names.  For RDHPCS or
NOAA user names, use `First.Last` or `User.Name`.  For non-NOAA user
names, plese use fre-software mascots, such as Tux (Linux Kernal),
Wilber (The GIMP), Geeko (SUSE), or Foxkey (Firefox).


## Writing Documentation

### Topical Structure

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

### Search Engine-Friendly Content

Users will typically begin looking for relevant documentation using
the search feature.  Use standard Search Engine Optimizaiton (SED)
techniques to create and design the content.  This will help ensure
users can find the correct documentation.

#### Create Concise and Meaningful Title Tags and Meta Descriptions

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

#### Optimize Images by adding alt text

Be sure to add alternative text to included images.  This allows
search engines to understand the content of the image, and index them
accurately.  This also improves the accessibility of the
documentation.

### Writing for a Global Audience

While the RDHPCS documentation is written in English, many of the
RDHPCS users are not native English speakers.  Remember that every
document is a candidate for localization (translation).  Make sure the
English content is correct and clear.  This will help translators
produce better output for non-native English users.

Please keep the following recommendataions in mind.

* Keep sentences short.
* Be consistent.  Use the same terminology and the same sentence
  structure for similar content.
* Keep it clear.  Avoid unprecise language, such as "should," and
  "could."
* Do not use contrly-specific words and examples.  Use common
  international examples.
* Use only as many graphics as needed.
* Do not break sentences.
* Do not break sentence with lists.  If the sentence will include a
  list, place the list at the end of the sentence.

### Bias-free Communication

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


## Language

We use American English for the RDHPCS documentation.  Where spelling
difference exist between American and Bridish English, use the
American variant.  For verbs ending in either *-ise* or *-ize*, use
the *-ize* variant.  When in doubt about the spelling or usage of a
word, use the preferred spelling from the
[Merriam-Webster](https://merriam-webseter.com/) dictionary.

### Abbreviations

Avoid using abbreviations, especially unusual ones.  Avoid creating
plurals of abbreviations unless the abbreviation is an acronym or
initialism.

#### Acronyms and Initialisms

Introduce acronyms and initialisms by providing the expansion in
parentheses after the acronym, or prior to the acronym or initialism
with the acronym or initialism in parentheses.  As examples:

* The National Oceanic and Atmospheric Administration (NOAA)
* OAR (Oceanic and Atmospheric Research)

Do not use headlines to introduce an acronym.  Headlines or captions
shall not contain both an acronym or initialism and its expansion.  If
a term is commonly written as an acronym or initialism use the acronym
or initialism in the title.

Create plural forms of acronums by adding a lowercase "s".  For
example CDs and BIOSes.  Never add an apostrophe before the "s" or
"es."

Avoid using possessive froms of acronyms.  This helps with the clarity
of the documentation.

#### Latin Abbreviations

Do not use Latin abbreviations.  Use the full English from.  For
example use "that is" instead of "i.e.".

An exception to this rule is the abbreviation *etc.*.

#### Units of measurement

You may use abbreviations of common units of measurements.

### Commas

Use commas to separate elements in a series of three or more elements,
but do not put a comman before the conjuction in most simple series.
Use commas around phrases like *for example and *that is*.
Introductory phrases at the beginning of a sentence are normally
follwed by a comma.

### Contractions

Do not use contractions.

### End of Sentence Punctuation

End sentences with a period.  Avoid using exclamation marks.  Reserve
question marks for question and answer sections.

### File and Directory Names

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

### Headings

When writing a descriptive section, use a noun-based heading title.
When writing a task-orientated section, use a verb in gerund form, for
example, "Installing Software."

Keep headings short and simple.  Do not use both an acronyn or
initialism and the expanded form in the heading.

### Hyphens

Hyphens shall be used as joiners for two or more words that form a
single concept and function together as a compound modifier before the
noun.  If the noun comes first, they hyphen is not added.  For
example, "in the upper-left corner" but "the corner in the upper
left."

Technical guidelines to help choose whether to use or not to use a hyphen.

Add the hyphen when:

* The last letter of the prefix and the first letter of the word are
  the same, as in "shell-like".  However, double-e conmbinations
  usually do not get a hyphen: "preempted," "reelected."
* The words begin with the prefixes *self-*, *ex-* (that is,
  "former"), and *all-*: "self-assigned," "ex-service,", "all-data."

Do not use hyphens when

* The prefix and the following word start with a consonant: "subpackage."
* The two-word phrase includes the adverb very and all adverbs ending
  in *-ly*: "a very good time," "an easily rememberered rule."

### Lists

When creating lists, remember the following:

* Always introduce the list in the text.
* A list, or sub-list, must contain at least two items.  If items are
  few, short and simple in structure, consider incoporating them in
  the flowing text instead of creating a list.
* If all items are nouns only, do not capitalize their first letter.
  Use sentence-style capializaion for list items that are full
  sentences and for terms in descriptive items.
* Use a period after every list item that is a sentence.  Do not use a
  period oafter the items that are not complete sentences.
* Use either all full sentences or all fragmens in the list.  Avoid
  using a mix.
* Do not use commas and semicolons to end puncuation.
* When possible, use parallel phrasing and grammatical construction
  between list items.  This provides a pattern that makes it easier to
  follow the text.
* Do not over use lists.  Lists are visually distinct and can break up
  the text flow.
* Avoid nesting lists deeper than three.  Instead, restucture the
  information using a combination of lists and running texts.

### Numbers

Write integers from zero through nine as words.  Use numerals for all
other numbers.

When the unit of a measurement is abbreviated, always use numberals
for the number.  Add a non-breaking space between the numeral and its
corresponding unit abbreviation.  Do not include a space between the
numeral and the percent (%) sign.

### Prefixes

Add a hyphen after the prefix to prefixed words only if yu foresee
misunderstandings.

### Quotations

Use quotations to quote from sources.  In all other cases, do not use
quotation marks.  For example, when writing computer input, output and
user interface elements, use different markup.  See the [Style
Guide](CODE_STYLE.md).

### Semicolons

Avoid using semicolons to join sentences.  You may use semicolons in
place of commas in very complicated series.

### Sentence Structure

Write clear and direct sentences.  Avoid complicated clauses and
overly technical terms and jargen.  Keep sentences to a length of 20
words or less.  Ensure that the relationship between subject, verb,
and object is clear.  Avoid joining sentences with semicolons.  Avoid
ending sentences with prepositions.

Avoid using parentheses.  When parentheses are necessary, move them to
the end of the sentence.  Never nest parentheses.

Always let the reader know the object of an action before describing
the action itself.  As an example write: "To save the settings, select
*OK*."

### Slashes

Do not use slashed except when they are part of a standard technical
term, such as *TCP/IP* or *client/server*.

### Tense

Use the simple present tense, even to sentences with "if" or "when"
clauses and th prerequisites of an action.  For example, "if this
happens, go there." or "Glibc is installed."

### Tone and Voice

Maintain a professional tone.  Do not use contractions.  Do not use
humor.  Be honest and avoid absolutes and exaggerations.  Focus on
positive aspects.

Use the second persion ("you") to refer to the reader.  Do not overuse
"you" and "your".  It is often implied who you are addressing in the
instuctions.

Where possible, use active voice.  If there is no emphasis on the
object of the verb or if the performer of the action is unknown, use
passive voice.

When giving a recommendation, start with "We recommend."  Do not use
passive phrasings like "it is recommended."

To refer to other parts of the document, do not use the word "here" as
a cross-reference link.  Instead, start with "For more information
(about), see" with a title or name to the document linked.

## Structure and Markup

Please refer to the [Code Style](CODE_STYLE.md) Guide for instructinos
on using the correct reStructuredText markup used in the
documentation.

## License

All RDHPCS documentation, where applicable, is released under the [CC0
1.0 Universal license](LICENSE).  This writing guide is released under
the [GNU Free Documentation
License](http://www.gnu.org/licenses/fdl.html).

## References

* [SUSE Documentation Style Guide](https://documentation.suse.com/style/)
* [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
