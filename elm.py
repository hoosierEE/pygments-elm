# -*- coding: utf-8 -*-
"""
    pygments.lexers.elm
    ~~~~~~~~~~~~~~~~~~~

    Lexer for the Elm programming language.

"""

import re

from pygments.lexer import bygroups, RegexLexer, words, include, using
from pygments.token import Comment, Keyword, Name, Number, Operator, Punctuation, String, Text, Error

__all__ = ['ElmLexer']

class ElmLexer(RegexLexer):
    """
    For `Elm <http://elm-lang.org/>`_ source code.
    """

    name = 'Elm'
    aliases = ['elm']
    filenames = ['*.elm']
    mimetypes = ['text/x-elm']

    validName = r'\w[\w\']*'

    specialName = r'^main '

    builtinOps = (
        '%', '&&', '*', '+', '++', '-', '->', '.', '..', '//',
        '/', '/=', ':', '::', '<-', '<<', '<=', '<|', '<~', '<',
        '=', '==', '>', '>=', '>>', '\'', '\\', '^', '`', '|>',
        '||', '|', '~',
    )

    reservedWords = words((
        '_', 'as', 'case', 'class', 'data', 'default', 'deriving', 'else', 'export', 'foreign',
        'hiding', 'if', 'import', 'in', 'infix', 'infixl', 'infixr', 'instance', 'jsevent', 'let',
        'module', 'newtype', 'of', 'then', 'type', 'where',
    ), suffix=r'\b')

    tokens = { 'root': [

            # Comments
            (r'{-', Comment.Multiline, 'comment'),
            (r'--.*', Comment.Single),

            # Whitespace
            (r'\s+', Text),

            # Strings
            (r'"', String, 'doublequote'),

            # Imports
            (r'^\s*import\s*', Keyword.Namespace, 'imports'),

            # Keywords
            (reservedWords, Keyword.Reserved),

            # Types
            (r'[A-Z]\w*', Keyword.Type),

            # Main
            (specialName, Keyword.Reserved),

            # Prefix Operators
            (words((builtinOps), prefix=r'\(', suffix=r'\)'), Name.Function),

            # Infix Operators
            (words((builtinOps)), Name.Function),

            # Numbers
            include('numbers'),

            # Variable Names
            (validName, Name.Variable),

            # Parens
            (r'[,\(\)\[\]{}]', Punctuation),

        ],

        'comment': [
            (r'-(?!})', Comment.Multiline),
            (r'[^-}]', Comment.Multiline),
            (r'-}', Comment.Multiline, '#pop'),
        ],

        'imports': [
            (r'\w+\.?\w+', Name.Class, '#pop'),
        ],

        'numbers': [
            (r'_?\d+\.(?=\d+)', Number.Float),
            (r'_?\d+', Number.Integer),
        ],

        'doublequote': [
            (r'\\u[0-9a-fA-F]\{4}', String.Escape),
            (r'\\[nrfvb\\\"]', String.Escape),
            (r'[^"]', String),
            (r'"', String, '#pop'),
        ],
    }

