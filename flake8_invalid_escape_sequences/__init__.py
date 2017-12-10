"""Define a flake8 plugin to check for invalid escape sequences."""

__version__ = '0.1.3'


from re import compile as re_compile
from token import STRING


first_quote_search = re_compile(r'[\'"]').search
invalid_escape_sequence_match = re_compile(
    r'[ufb]?[\'"].*?(\\[^\\\'"abfnrtv0-7xNuU])'
).match


# noinspection PyUnusedLocal
def plugin(logical_line, tokens):
    """Walk the tree and detect invalid escape sequences."""
    for token in tokens:
        if token[0] != STRING:  # token[0] == token.type
            continue
        # token[1] == token.string # python 3
        invalid_sequence_match = invalid_escape_sequence_match(token[1])
        if invalid_sequence_match:
            yield (
                token[2][1],  # token[2][1] == token.start.end
                'IES: '
                'invalid escape sequence %s' % invalid_sequence_match.group(1),
            )
            return


plugin.name = 'flake8_invalid_escape_sequences'
plugin.version = __version__
