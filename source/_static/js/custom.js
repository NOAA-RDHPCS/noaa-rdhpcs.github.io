$(document).ready(function () {

    // Create link and text for navigation back to the RDHPCS home page
    var home_link = document.createElement("a");
    var home_text = document.createTextNode("RDHPCS Home Page");
    home_link.appendChild(home_text);
    home_link.setAttribute("href", "https://www.noaa.gov/information-technology/hpcc");

    // Open the RDHPCS home page in new tab when clicked
    home_link.setAttribute("target", "_blank");

    var separator = document.createTextNode(" | ");

    // These items are right-aligned in the RTD theme breadcrumbs
    aside = document.querySelector("body > div > section > div > div > div:nth-child(1) > ul > li.wy-breadcrumbs-aside");

    // Next to the default "Edit on GitHub", add a separator, then the RDHPCS link.
    aside.appendChild(separator);
    aside.appendChild(home_link);

    // Insert "Help email" below html_logo in sidebar navigation
    var help_link = document.createElement("a");
    var help_link_text = document.createTextNode("Need Help? ");
    var email_link_text = document.createTextNode(" Click Here.");
    help_link.appendChild(help_link_text);
    help_link.appendChild(email_link_text);
    help_link.setAttribute("href", "/help/index.html");

    wysidenavsearch = document.querySelector("body > div > nav > div > div.wy-side-nav-search > a");
    wysidenavsearch.appendChild(help_link);

    // For any external links in the main navigation, append the FontAwesome external link icon.
    function iconize_external_links(nav_level) {
        a_elements = nav_level.getElementsByTagName("A");
        for (var i = 0; i < a_elements.length; ++i) {
            if (a_elements[i].getAttribute("href").includes("http")) {
                var icon = document.createElement("i");
                icon.classList.add("fa");
                icon.classList.add("fa-external-link");
                var spacer = document.createTextNode(" ");
                a_elements[i].appendChild(spacer);
                a_elements[i].appendChild(icon);
            }
        }
    }

    iconize_external_links(document.querySelector("body > div > nav > div > div.wy-menu.wy-menu-vertical"))

});
