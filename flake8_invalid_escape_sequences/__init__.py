"""Define a flake8 plugin to check for invalid escape sequences."""
from __future__ import unicode_literals, absolute_import

__version__ = '0.1.1'

from ast import literal_eval
from re import compile as re_compile
from token import STRING


first_quote_search = re_compile(r'[\'"]').search


# noinspection PyUnusedLocal
def plugin(logical_line, tokens):
    """Walk the tree and detect invalid escape sequences."""
    for token in tokens:
        if token[0] == STRING:  # token[0] == token.type
            string = token[1]    # token[1] == token.string
            if '\\' not in string:
                continue
            quote_start = first_quote_search(string).start()
            if 'r' in string[:quote_start]:
                continue
            quoted = string[quote_start:]
            if literal_eval(quoted) == literal_eval('r' + quoted):
                yield (
                    token[2][1],  # token[2][1] == token.start.end
                    'IES: '
                    'invalid escape sequence in literal bytes or string',
                )


plugin.name = 'flake8_invalid_escape_sequences'
plugin.version = __version__
