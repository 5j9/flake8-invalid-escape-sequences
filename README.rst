flake8_invalid_escape_sequences
-------------------------------
A plugin for flake8 (v3+) that detects and reports invalid escape sequences.


Introduction
------------
Invalid escape sequences `became deprecated in Python 3.6 <https://bugs.python.org/issue27364>`_ and will be a syntax error in the future.

Currently this plugin does not report the exact sequence that is causing the issue, just the line number and column of the literal string which has the invalid sequence.


Installation
------------

.. code-block:: bash

  pip install flake8_invalid_escape_sequences


Should work with all officially supported Python versions.
