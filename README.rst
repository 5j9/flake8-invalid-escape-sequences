.. image:: https://travis-ci.org/5j9/flake8-invalid-escape-sequences.svg?branch=master
    :target: https://travis-ci.org/5j9/flake8-invalid-escape-sequences

flake8-invalid-escape-sequences
-------------------------------
A plugin for flake8 (v3+) that detects and reports invalid escape sequences.

Note: This plugin is not required anymore if you've upgraded to ``pycodestyle 2.4.0`` (released Apr 10, 2018). ``pycodestyle`` now issues `W605  <https://github.com/PyCQA/pycodestyle/commit/13d2bd200911850dacde31665235122d85290265>`_
warning for invalid escape sequences.

Introduction
------------
Invalid escape sequences `became deprecated in Python 3.6 <https://bugs.python.org/issue27364>`_ and will be a SyntaxError in the future.

This plugin finds those invalid sequences and reports them. Here is a sample output:

.. code-block:: bash

    test_case.py:5:12: IES: invalid escape sequence \[

Installation
------------

.. code-block:: bash

  pip install flake8-invalid-escape-sequences


Should work with all officially supported Python versions, including
Python 2.7.
