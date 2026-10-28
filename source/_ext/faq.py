"""
FAQ Sphinx Extension
====================

Provides a custom ``faq`` directive for creating FAQ entries with:
- Consistent dropdown styling
- Cross-referenceable IDs via ``:ref:`faq-id```
- Hidden search tags for improved discoverability

Usage::

    .. faq:: How do I get an RDHPCS account?
       :id: get-account
       :tags: account application new user

       See :ref:`Applying for a user account <applying_for_user_account>`.

Reference the FAQ entry with ``:ref:`get-account``` or ``:ref:`faq-get-account```.

"""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class FAQDirective(SphinxDirective):
    """
    Custom directive for FAQ entries.

    Creates a dropdown with consistent styling, an optional reference target,
    and hidden search tags.
    """

    has_content = True
    required_arguments = 1  # The question text
    final_argument_whitespace = True
    option_spec = {
        "id": directives.unchanged,
        "tags": directives.unchanged,
        "open": directives.flag,
    }

    def run(self):
        question = self.arguments[0]
        faq_id = self.options.get("id", "")
        tags = self.options.get("tags", "")
        is_open = "open" in self.options

        # Create the container node
        container = nodes.container()
        container["classes"].append("faq-entry")

        # Add a target node for cross-referencing if id is provided
        if faq_id:
            # Create target with faq- prefix
            target_id = f"faq-{faq_id}"
            target = nodes.target("", "", ids=[target_id, faq_id])
            container += target

            # Register the target for cross-referencing
            self.state.document.note_explicit_target(target)

            # Add to the standard domain for :ref: role
            # Use the labels dict directly (works across Sphinx versions)
            domain = self.env.get_domain("std")
            domain.labels[faq_id] = (
                self.env.docname,
                faq_id,
                question,
            )
            domain.labels[target_id] = (
                self.env.docname,
                target_id,
                question,
            )
            # Also add to anonlabels for basic reference resolution
            domain.anonlabels[faq_id] = (self.env.docname, faq_id)
            domain.anonlabels[target_id] = (self.env.docname, target_id)

        # Build the dropdown using sphinx-design's DropdownDirective
        # We'll create the RST and parse it
        dropdown_rst = []
        dropdown_rst.append(f".. dropdown:: {question}")
        dropdown_rst.append("   :class-container: faq-item")
        if is_open:
            dropdown_rst.append("   :open:")
        dropdown_rst.append("")

        # Add hidden tags container if tags provided
        if tags:
            dropdown_rst.append("   .. container:: faq-tags")
            dropdown_rst.append("")
            dropdown_rst.append(f"      {tags}")
            dropdown_rst.append("")

        # Add the content with proper indentation
        for line in self.content:
            dropdown_rst.append(f"   {line}")

        # Parse the constructed RST
        self.state_machine.insert_input(
            dropdown_rst,
            self.state_machine.document.attributes["source"],
        )

        return [container]


class FAQCategoryDirective(SphinxDirective):
    """
    Directive to mark FAQ category sections with consistent styling.

    Usage::

        .. faq-category:: Accounts

    """

    has_content = False
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        title = self.arguments[0]

        # Create section node
        section = nodes.section()
        section["ids"].append(nodes.make_id(f"faq-category-{title}"))

        # Create title
        title_node = nodes.title(text=title)
        section += title_node

        return [section]


def setup(app):
    """Set up the FAQ extension."""
    app.add_directive("faq", FAQDirective)
    app.add_directive("faq-category", FAQCategoryDirective)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
