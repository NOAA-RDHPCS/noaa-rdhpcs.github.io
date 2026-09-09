:orphan:

.. meta::
   :description: Interactive form to generate a sample OpenSSH client
    configuration for NOAA RDHPCS systems with system-specific hostnames
    and proxy settings.
   :keywords: OpenSSH, SSH configuration, config file, Bastion, proxy,
    RDHPCS systems

.. _openssh-config:

OpenSSH Sample Configuration
----------------------------

You can use the following form to generate a basic OpenSSH client configuration
for the RDHPCS systems. Enter your user name (for example, ``First.Last``) and
user ID in the form below. Copy the generated configuration into your SSH
configuration file.

.. cspell:ignore userprofile

.. note::

    On Linux and macOS, the user SSH configuration file is located at
    :file:`$HOME/.ssh/config`. On Windows, the location is
    :file:`%userprofile%\\.ssh\\config`. You may need to create the
    :file:`.ssh` directory if it does not exist.

.. note::

    You can find your user ID by logging into an RDHPCS system and running
    the command :command:`id -u`.

.. raw:: html

    <style>
        #ssh_config_form .input-group-text {
            min-width: 8em;
            justify-content: flex-start;
            height: 38px !important;
            box-sizing: border-box !important;
        }
        #ssh_config_form .form-control {
            min-width: 12em;
            flex: 0 0 auto;
            width: 12em;
            height: 38px !important;
            box-sizing: border-box !important;
        }
        #ssh_config_form .system-checkboxes {
            display: flex;
            flex-wrap: wrap;
            gap: 1em;
            margin-left: 1em;
            align-items: center;
        }
        #ssh_config_form .system-checkboxes label {
            display: flex;
            align-items: center;
            gap: 0.3em;
            cursor: pointer;
        }
    </style>
    <form id="ssh_config_form" aria-label="SSH configuration generator">
        <div class="mb-3 input-group">
            <label for="user_name" class="input-group-text">
                User Name
            </label>
            <input type="text"
                   id="user_name"
                   name="user_name"
                   class="form-control"
                   pattern="[A-Za-z]+\.[A-Za-z]+"
                   placeholder="First.Last"
                   required
                   aria-describedby="user_name_help"
                   title="Enter your First.Last username. Capitalization matters.">
            <small id="user_name_help"
                   style="margin-left: 1em; display: flex; align-items: center;">
                Enter your RDHPCS username in First.Last format.
            </small>
        </div>
        <div class="mb-3 input-group">
            <label for="user_id" class="input-group-text">
                User ID (UID)
            </label>
            <input type="number"
                   id="user_id"
                   name="user_id"
                   class="form-control"
                   min="1"
                   max="65535"
                   required
                   aria-describedby="user_id_help"
                   title="Enter your numeric user ID (1-65535).">
            <small id="user_id_help"
                   style="margin-left: 1em; display: flex; align-items: center;">
                Find your user ID by running&nbsp;<code>id -u</code>&nbsp;on an RDHPCS system.
            </small>
        </div>
        <div class="mb-3 input-group">
            <span class="input-group-text">
                Systems
            </span>
            <div class="system-checkboxes" role="group" aria-label="Select systems to include">
                <label>
                    <input type="checkbox" id="system_all" name="systems" value="all" checked>
                    All
                </label>
                <label>
                    <input type="checkbox" id="system_gaea" name="systems" value="gaea">
                    Gaea
                </label>
                <label>
                    <input type="checkbox" id="system_hera" name="systems" value="hera">
                    Hera
                </label>
                <label>
                    <input type="checkbox" id="system_mercury" name="systems" value="mercury">
                    Mercury
                </label>
                <label>
                    <input type="checkbox" id="system_ppan" name="systems" value="ppan">
                    PPAN
                </label>
                <label>
                    <input type="checkbox" id="system_ursa" name="systems" value="ursa">
                    Ursa
                </label>
            </div>
        </div>
        <div id="button_container" style="margin-top: 1em; display: flex; justify-content: space-between; align-items: center;">
            <button class="btn btn-neutral"
                    type="button"
                    id="generate_btn">Generate SSH Config</button>
            <button type="button"
                    id="copy_btn"
                    class="btn btn-neutral"
                    style="display: none;"
                    aria-label="Copy configuration to clipboard">
                Copy to Clipboard
            </button>
        </div>
    </form>

    <div id="ssh_config_container" class="highlight" style="display: none;">
        <pre id="ssh_config_output" tabindex="0" aria-live="polite"></pre>
    </div>

    <script>
    (function() {
        'use strict';

        /**
         * RDHPCS System Configuration
         *
         * To add a new system:
         * 1. Add an entry to the SYSTEMS object below.
         * 2. Each system needs: name, bastionPrefix, localForwardBase, remoteForwardBase
         *
         * Port assignments use a base port plus the user's UID. The fix_port
         * function handles overflow past port 65535.
         */
        const SYSTEMS = {
            gaea: {
                name: 'gaea',
                bastionPrefix: 'gaea-mfa',
                localForwardBase: 30000,
                remoteForwardBase: 20000
            },
            hera: {
                name: 'hera',
                bastionPrefix: 'hera-mfa',
                localForwardBase: 45000,
                remoteForwardBase: 55000
            },
            mercury: {
                name: 'mercury',
                bastionPrefix: 'mercury-mfa',
                localForwardBase: 25000,
                remoteForwardBase: 35000
            },
            ppan: {
                name: 'ppan',
                bastionPrefix: 'analysis-mfa',
                localForwardBase: 40000,
                remoteForwardBase: 50000
            },
            ursa: {
                name: 'ursa',
                bastionPrefix: 'ursa-mfa',
                localForwardBase: 35000,
                remoteForwardBase: 45000
            }
        };

        const SITES = ['princeton', 'fairmont'];
        const DOMAIN = 'rdhpcs.noaa.gov';

        /**
         * Sanitize user input to prevent XSS.
         * Only allows alphanumeric characters and periods.
         */
        function sanitizeUsername(input) {
            return input.replace(/[^A-Za-z.]/g, '');
        }

        /**
         * Capitalize first letter of each name part (First.Last format).
         * Converts "first.last" to "First.Last".
         */
        function capitalizeUsername(username) {
            return username.split('.').map(function(part) {
                if (part.length === 0) return part;
                return part.charAt(0).toUpperCase() + part.slice(1);
            }).join('.');
        }

        /**
         * Validate username format (First.Last pattern).
         */
        function isValidUsername(username) {
            return /^[A-Za-z]+\.[A-Za-z]+$/.test(username);
        }

        /**
         * Validate user ID is within acceptable range.
         */
        function isValidUid(uid) {
            const id = parseInt(uid, 10);
            return !isNaN(id) && id >= 1 && id <= 65535;
        }

        /**
         * Adjust port numbers that exceed the valid range.
         * Wraps ports over 65535 back into the 2001-65535 range.
         */
        function fixPort(port) {
            if (port > 65535) {
                return ((port - 65535) % 63535) + 2001;
            }
            return port;
        }

        /**
         * Generate SSH config block for a single system.
         */
        function generateSystemConfig(system, user, uid) {
            const localPort = fixPort(system.localForwardBase + uid);
            const remotePort = fixPort(system.remoteForwardBase + uid);
            const bastionPrefix = system.bastionPrefix;

            let config = '';

            // Fairmont-only host entry
            config += `Host ${bastionPrefix}.fairmont.${DOMAIN}\n`;
            config += `    HostName          ${bastionPrefix}.fairmont.${DOMAIN}\n\n`;

            // Princeton host entry (with Fairmont as alias)
            config += `Host ${bastionPrefix}.princeton.${DOMAIN} `;
            config += `${bastionPrefix}.fairmont.${DOMAIN}\n`;
            config += `    HostName          ${bastionPrefix}.princeton.${DOMAIN}\n`;
            config += `    LocalForward      ${localPort} localhost:${localPort}\n`;
            config += `    RemoteForward     ${remotePort} localhost:22\n`;
            config += `    User              ${user}\n`;
            config += `# CAC / PIV / PKCS11 Providers for macOS and Linux.\n`;
            config += `    Match exec "uname | grep Darwin"\n`;
            config += `      PKCS11Provider    /usr/lib/ssh-keychain.dylib\n`;
            config += `    Match exec "uname | grep Linux"\n`;
            config += `      PKCS11Provider    /usr/lib64/pkcs11/opensc-pkcs11.so\n\n`;

            // Local tunnel alias
            config += `Host ${system.name}.local\n`;
            config += `    HostName          localhost\n`;
            config += `    Port              ${localPort}\n`;
            config += `    User              ${user}\n\n`;

            return config;
        }

        /**
         * Get list of selected systems from checkboxes.
         * Returns all system keys if "All" is checked, otherwise returns
         * only the checked individual systems.
         */
        function getSelectedSystems() {
            const allCheckbox = document.getElementById('system_all');
            if (allCheckbox.checked) {
                return Object.keys(SYSTEMS);
            }
            const selected = [];
            for (const key of Object.keys(SYSTEMS)) {
                const checkbox = document.getElementById('system_' + key);
                if (checkbox && checkbox.checked) {
                    selected.push(key);
                }
            }
            return selected;
        }

        /**
         * Generate SSH configuration for selected systems.
         */
        function generateFullConfig(username, uid, selectedSystems) {
            let config = '';
            for (const key of selectedSystems) {
                if (SYSTEMS[key]) {
                    config += generateSystemConfig(SYSTEMS[key], username, uid);
                }
            }
            return config;
        }

        /**
         * Display validation error to the user.
         */
        function showError(message) {
            alert(message);
        }

        /**
         * Handle form submission.
         */
        function handleGenerate() {
            const usernameInput = document.getElementById('user_name');
            const uidInput = document.getElementById('user_id');
            const container = document.getElementById('ssh_config_container');
            const output = document.getElementById('ssh_config_output');

            const rawUsername = usernameInput.value.trim();
            const rawUid = uidInput.value.trim();

            // Validate username
            if (!rawUsername) {
                showError('Please enter your username.');
                usernameInput.focus();
                return;
            }

            const sanitizedUsername = sanitizeUsername(rawUsername);

            if (!isValidUsername(sanitizedUsername)) {
                showError(
                    'Invalid username format.\n\n' +
                    'Enter your username as First.Last (for example, John.Smith).\n' +
                    'Only letters and one period are allowed.'
                );
                usernameInput.focus();
                return;
            }

            // Capitalize first letter of each name part
            const username = capitalizeUsername(sanitizedUsername);

            // Validate UID
            if (!rawUid) {
                showError('Please enter your user ID.');
                uidInput.focus();
                return;
            }

            if (!isValidUid(rawUid)) {
                showError(
                    'Invalid user ID.\n\n' +
                    'The user ID must be a number between 1 and 65535.\n' +
                    'Find your ID by running: id -u'
                );
                uidInput.focus();
                return;
            }

            const uid = parseInt(rawUid, 10);

            // Get selected systems
            const selectedSystems = getSelectedSystems();
            if (selectedSystems.length === 0) {
                showError('Please select at least one system.');
                return;
            }

            // Generate and display config using textContent (XSS-safe)
            const config = generateFullConfig(username, uid, selectedSystems);
            output.textContent = config;
            container.style.display = 'block';
            document.getElementById('copy_btn').style.display = 'inline-block';
            document.getElementById('button_container').scrollIntoView({ behavior: 'smooth', block: 'start' });
        }

        /**
         * Copy generated config to clipboard.
         */
        async function handleCopy() {
            const output = document.getElementById('ssh_config_output');
            const copyBtn = document.getElementById('copy_btn');

            try {
                await navigator.clipboard.writeText(output.textContent);
                const originalText = copyBtn.textContent;
                copyBtn.textContent = 'Copied!';
                setTimeout(() => {
                    copyBtn.textContent = originalText;
                }, 2000);
            } catch (err) {
                // Fallback for older browsers
                const range = document.createRange();
                range.selectNode(output);
                window.getSelection().removeAllRanges();
                window.getSelection().addRange(range);
                document.execCommand('copy');
                window.getSelection().removeAllRanges();
                copyBtn.textContent = 'Copied!';
                setTimeout(() => {
                    copyBtn.textContent = 'Copy to Clipboard';
                }, 2000);
            }
        }

        // Initialize event listeners when DOM is ready
        document.addEventListener('DOMContentLoaded', function() {
            const generateBtn = document.getElementById('generate_btn');
            const copyBtn = document.getElementById('copy_btn');
            const allCheckbox = document.getElementById('system_all');
            const systemCheckboxes = document.querySelectorAll('input[name="systems"]:not([value="all"])');

            if (generateBtn) {
                generateBtn.addEventListener('click', handleGenerate);
            }

            if (copyBtn) {
                copyBtn.addEventListener('click', handleCopy);
            }

            // Handle "All" checkbox behavior
            if (allCheckbox) {
                allCheckbox.addEventListener('change', function() {
                    if (this.checked) {
                        // Uncheck all individual system checkboxes when "All" is checked
                        systemCheckboxes.forEach(function(cb) {
                            cb.checked = false;
                        });
                    }
                });
            }

            // Handle individual system checkbox behavior
            systemCheckboxes.forEach(function(cb) {
                cb.addEventListener('change', function() {
                    if (this.checked) {
                        // Uncheck "All" when any individual system is checked
                        allCheckbox.checked = false;
                    }
                    // If no individual systems are checked, check "All"
                    const anyChecked = Array.from(systemCheckboxes).some(function(c) {
                        return c.checked;
                    });
                    if (!anyChecked) {
                        allCheckbox.checked = true;
                    }
                });
            });

            // Allow Enter key to trigger generation
            const form = document.getElementById('ssh_config_form');
            if (form) {
                form.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        e.preventDefault();
                        handleGenerate();
                    }
                });
            }
        });
    })();
    </script>

    <br />
