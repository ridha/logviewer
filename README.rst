=========
Logviewer
=========

Logviewer is a realtime log monitoring in browser.

Usage:

.. code-block:: bash

    $ logviewer -f /path/to/file.lo --port 9090
    $ tail -f /path/to/file.log | logviewer

Command line options are:

.. code-block:: bash

  -p PORT, --port PORT  Specify the webserver port (default to 8080)
  -f FILE, --file FILE  File path (default to stdin)
