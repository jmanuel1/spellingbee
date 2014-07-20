Spelling Bee
============

Program to correct spelling from standard input, and module to provide spelling correction functionality. Written in Python.

This project requires [the spellingbeecc package](https://github.com/jmanuel1/spellingbee-cc) to be installed. That package has its own, separate license.

Usage of Program
================

Put input on stdin, corrected output goes on stdout. Go ahead and edit
`words.txt`: the list of words Spelling Bee considers correct.

Example
-------

    $ python autocorrect.py
    yuor
    
Output could be `your`, depending on your `words.txt`.

Usage of Module
===============

It's simple! Just `import spellingbee`. See the API docs (`docs/api.mdown`) for the Spelling Bee API.

Contributing
============

Contribute code, documentation and most of all, add words!

Words should be put in `words.txt`.

Documentation should be in the `docs` directory and written in Markdown. Please follow the examples set by this readme and the API Docs (`docs/api.mdown`). Write Markdown so that it works across various Markdown implementations. Docs should use either the `.md` or `.mdown` file extension.

At least run Python code through [autopep8](https://pypi.python.org/pypi/autopep8),
please. Follow the style of Python code already there.

If you wish to be in the list of contributors, email jama -dot- indo -at- hotmail -dot- com with the subject "CONTRIB-LIST".