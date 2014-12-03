# -*- coding: utf-8 -*-
"""
    pygments.lexers.elm
    ~~~~~~~~~~~~~~~~~~~

    Lexer for the Elm programming language.

"""

import re

from pygments.lexer import RegexLexer, words, include
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, Punctuation, String, Text

__all__ = ['ElmLexer']

class JLexer(RegexLexer):
    """
    For `Elm <http://elm-lang.org/>`_ source code.
    """

    name = 'Elm'
    aliases = ['elm']
    filenames = ['*.elm']
    mimetypes = ['text/x-elm']

    validName = r'\b[a-zA-Z]\w*'

    tokens = {
        'root': [

            # Comments TODO: just started
            (r'--.*', Comment.Single),
            (r'\n+\s*{-', Comment.Multiline, 'comment'),
            (r'\s*Note.*', Comment.Single),

            # Whitespace
            (r'\s+', Text),

            # Strings
            (r"'", String, 'singlequote'),

            # Definitions
            (r'0\s+:\s*0|noun\s+define\s*$', Name.Entity, 'nounDefinition'),
            (r'\b(([1-4]|13)\s+:\s*0)|((adverb|conjunction|dyad|monad|verb)\s+define)\b', Name.Function, 'explicitDefinition'),

            # Flow Control
            (words(('for_', 'goto_', 'label_'), suffix=validName+'\.'), Name.Label),
            (words((
                'assert', 'break', 'case', 'catch', 'catchd',
                'catcht', 'continue', 'do', 'else', 'elseif',
                'end', 'fcase', 'for', 'if', 'return',
                'select', 'throw', 'try', 'while', 'whilst',
                ), suffix='\.'), Name.Label),

            # Variable Names
            (validName, Name.Variable),

            # Standard Library
            (words((
                'ARGV', 'CR', 'CRLF', 'DEL', 'Debug',
                'EAV', 'EMPTY', 'FF', 'JVERSION', 'LF',
                'LF2', 'Note', 'TAB', 'alpha17', 'alpha27',
                'apply', 'bind', 'boxopen', 'boxxopen', 'bx',
                'clear', 'cutLF', 'cutopen', 'datatype', 'def',
                'dfh', 'drop', 'each', 'echo', 'empty',
                'erase', 'every', 'evtloop', 'exit', 'expand',
                'fetch', 'file2url', 'fixdotdot', 'fliprgb', 'getargs',
                'getenv', 'hfd', 'inv', 'inverse', 'iospath',
                'isatty', 'isutf8', 'items', 'leaf', 'list',
                'nameclass', 'namelist', 'namelist', 'names', 'nc',
                'nl', 'on', 'pick', 'pick', 'rows',
                'script', 'scriptd', 'sign', 'sminfo', 'smoutput',
                'sort', 'split', 'stderr', 'stdin', 'stdout',
                'table', 'take', 'timespacex', 'timex', 'tmoutput',
                'toCRLF', 'toHOST', 'toJ', 'tolower', 'toupper',
                'type', 'ucp', 'ucpcount', 'usleep', 'utf8',
                'uucp',
                )), Name.Function),

            # Copula
            (r'=[.:]', Operator),

            # Builtins
            (r'[-=+*#$%@!~`^&";:.,<>{}\[\]\\|/]', Operator),

            # Short Keywords
            (r'[abCdDeEfHiIjLMoprtT]\.',  Keyword.Reserved),
            (r'[aDiLpqsStux]\:', Keyword.Reserved),
            (r'(_[0-9])\:', Keyword.Constant),

            # Parens
            (r'\(', Punctuation, 'parentheses'),

            # Numbers
            include('numbers'),
        ],

        'comment': [
            (r'[^)]', Comment.Multiline),
            (r'^\)', Comment.Multiline, '#pop'),
            (r'[)]', Comment.Multiline),
        ],

        'explicitDefinition': [
            (r'\b[nmuvxy]\b', Name.Decorator),
            include('root'),
            (r'[^)]', Name),
            (r'^\)', Name.Label, '#pop'),
            (r'[)]', Name),
        ],

        'numbers': [
            (r'\b_{1,2}\b', Number),
            (r'_?\d+(\.\d+)?(\s*[ejr]\s*)_?\d+(\.?=\d+)?', Number),
            (r'_?\d+\.(?=\d+)', Number.Float),
            (r'_?\d+x', Number.Integer.Long),
            (r'_?\d+', Number.Integer),
        ],

        'nounDefinition': [
            (r'[^)]', String),
            (r'^\)', Name.Label, '#pop'),
            (r'[)]', String),
        ],

        'parentheses': [
            (r'\)', Punctuation, '#pop'),
            #include('nounDefinition'),
            include('explicitDefinition'),
            include('root'),
        ],

        'singlequote': [
            (r"[^']", String),
            (r"''", String),
            (r"'", String, '#pop'),
        ],
    }


