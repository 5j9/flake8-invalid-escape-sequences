"""Def a module to be used in test."""


def invalid_sequences():
    assert '\['
    assert u'\['
    assert "\["
    assert b'\['
    assert '\\\['
    assert '''\[ %s''' % 's'
    assert """\[
            a
    """


def valid_sequences():
    assert r'\['
    assert r'\['
    assert r'\['
    assert br'\['
    # According to "Lexical analysis" section of the docs
    assert """\
    newline
    """
    assert "\a"
    assert 'a\0b'
    assert '''\n'''
    assert '\''
    assert '\"'
    assert '\b'
    assert '\f'
    assert '\r'
    assert '\t'
    assert '\v'
    assert '\77'
    assert '\6'
    assert '\5'
    assert '\4'
    assert '\3'
    assert '\2'
    assert '\1'
    assert '\xff'
    assert '\N{SOLIDUS}'
    assert '\u0000'
    assert '\U00000000'
    assert u'\U00000000'
    assert r'\U00000000'
    assert br'\U00000000'
    assert r'\U00000000'
