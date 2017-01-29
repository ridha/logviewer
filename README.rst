=========
Logviewer
=========

Logviewer allows you to tail files to the web for sharing with other people.

Requirements:

- Python >= 3.6
- aiohttp
- aiohttp_jinja2

Install Logviewer:

.. code-block:: bash

    $ pip3 install logviewer

Usage:

.. code-block:: bash

    $ logviewer -f /path/to/file.log --port 8080
    $ tail -f /path/to/file.log | logviewer

Command line options are:

.. code-block:: bash

  -p PORT, --port PORT  Specify the webserver port (default to 8080)
  -f FILE, --file FILE  File path (default to stdin)
