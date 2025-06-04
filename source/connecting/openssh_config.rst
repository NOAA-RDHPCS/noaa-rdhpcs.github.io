:orphan:

.. _openssh-config:

OpenSSH Sample Configuration
----------------------------

You can use the following form to generate a basic OpenSSH client configuration
for the RDHPCS systems.  Enter your user name (e.g., ``First.Last``), and user
User ID in the form below and paste the items into your user ssh configuration
file.

.. cspell:ignore userprofile

.. note::

    On Linux and Mac OS, the user SSH configuration file can be found in
    :file:`$HOME/.ssh/config`.  On Windows, the location is
    :file:`%userprofile%\.ssh\config`.  You may need to create the :file:`.ssh`
    directory if it doesn't exist.

.. note::

    The user ID can be found by logging into an RDHPCS system and running
    the command :command:`id -u`.

.. raw:: html

    <form id="ssh_config_form" method="post">
        <div class="mb-3 input-group w-50">
            <span for="user_name"
                  class="input-group-text tooltip"
                  data-tooltip-content="#uname_tooltip_content">
                User Name
            </span>
            <input type="text"
                   id="user_name"
                   name="user_name"
                   class="form-control"
                   title="Enter First.Last username.  Capitalization is significant">
        </div>
        <div class="mb-3 input-group w-50">
            <span for="user_id"
                  class="input-group-text tooltip"
                  data-tooltip-content="#uid_tooltip_content">
                User ID (UID)
            </span>
            <input type="number"
                   id="user_id"
                   name="user_id"
                   class="form-control"
                   title="The user ID is an integer number">
        </div>
        <button class="btn btn-neutral"
                type="submit"
                onclick="return ssh_config_gen()">Generate SSH Config</button>
    </form>

    <div class="tooltip_templates">
        <span id="uname_tooltip_content">
            Enter the First.Last username.  Capitalization is significant!
        </span>
    </div>
    <div class="tooltip_templates">
        <span id="uid_tooltip_content">
            The user ID can be found by logging into an RDHPCS system and 
            running the command <code>id -u</code>.
        </span>
    </div>

    <div class="highlight" id="ssh_config_container" style="display: none;">
        <pre></pre>
    </div>

    <script>
        function ssh_host_conf(host, user, lf_port, rf_port) {

            return(`Host ${host}-rsa.boulder.rdhpcs.noaa.gov\n` +
                   `    HostName          ${host}-rsa.boulder.rdhpcs.noaa.gov\n\n` +
                   `Host ${host}-rsa.princeton.rdhpcs.noaa.gov ${host}-rsa.boulder.rdhpcs.noaa.gov\n` +
                   `    HostName          ${host}-rsa.princeton.rdhpcs.noaa.gov\n` +
                   `    LocalForward      ${lf_port} localhost:${lf_port}\n` +
                   `    RemoteForward     ${rf_port} localhost:22\n` +
                   `    User              ${user}\n\n` +
                   `Host ${host}.local\n` +
                   `    HostName          localhost\n` +
                   `    Port              ${lf_port}\n` +
                   `    User              ${user}\n\n`);
        }

        function open_ssh_config(user, id) {
            let lf_gaea = 30000;
            let rf_gaea = 20000;
            let lf_hera = 45000;
            let rf_hera = 55000;
            let lf_jet = 11300;
            let rf_jet = 21300;
            let lf_mercury = 25000;
            let rf_mercury = 35000;
            let lf_ppan = 40000;
            let rf_ppan = 50000;
            let lf_ursa = 35000;
            let rf_ursa = 45000;

            let uid = parseInt(id);

            return(ssh_host_conf("gaea", user, lf_gaea + uid, rf_gaea + uid) +
                   ssh_host_conf("hera", user, lf_hera + uid, rf_gaea + uid) +
                   ssh_host_conf("jet", user, lf_jet + uid, rf_jet + uid) +
                   ssh_host_conf("mercury", user, lf_mercury + uid, rf_mercury + uid) +
                   ssh_host_conf("ppan", user, lf_ppan + uid, rf_ppan + uid) +
                   ssh_host_conf("ursa", user, lf_ursa + uid, rf_ursa + uid));
        }

        function ssh_config_gen(){
            var user_name = document.forms["ssh_config_form"]["user_name"].value;
            var user_id = document.forms["ssh_config_form"]["user_id"].value;
            if (user_name == "" || user_id == "") {
                alert("The User Name and User ID fields must be completed.\n\n" +
                      "The User Name must be your First.Last user name, with correct capitalization.\n\n" +
                      "The User ID field must be a positive integer.");
                return false;
            }
            var ssh_config_container = document.getElementById("ssh_config_container");
            var ssh_config_display = document.querySelector('div#ssh_config_container pre')
            ssh_config_display.innerHTML = open_ssh_config(user_name, user_id);
            ssh_config_container.style.display = "block";
            return false;
        }
    </script>

    <br />
