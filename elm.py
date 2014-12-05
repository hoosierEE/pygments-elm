# -*- coding: utf-8 -*-
"""
    pygments.lexers.elm
    ~~~~~~~~~~~~~~~~~~~

    Lexer for the Elm programming language.

"""

import re

from pygments.lexer import RegexLexer, words, include
from pygments.token import Comment, Keyword, Name, Number, Operator, Punctuation, String, Text

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

    builtinTypes = words((
        'Bool', 'Char', 'Comparable', 'Date', 'Either',
        'Element', 'False', 'Float', 'GT', 'Int',
        'Just', 'LT', 'List', 'Maybe', 'Nothing',
        'Order', 'Signal', 'String', 'Text', 'Time',
        'True', 'Tuple',
        ), suffix=r'\b')

    builtinOps = words((
        '..', ':', '::', '=', '`',
        '\\', '\'', '->', '<-', '>>',
        '<<', '|>', '<|', '||', '&&',
        '//', '%', '+', '++', '-',
        '.', '/', '/=', '<', '<=',
        '==', '>', '>=', '^', '*',
        '<~', '~',
        ))

    libraries = words((
        'Array', 'Basics', 'Bitwise', 'Char', 'Color',
        'Date', 'Debug', 'Dict', 'Either', 'Graphics.Collage',
        'Graphics.Element', 'Graphics.Input', 'Graphics.Input.Field', 'Http', 'JavaScript.Experimental',
        'Json', 'Keyboard', 'List', 'Maybe', 'Mouse',
        'Random', 'Regex', 'Set', 'Signal', 'String',
        'Text', 'Time', 'Touch', 'Trampoline', 'Transform2D',
        'WebSocket', 'Window',
        ), suffix=r'\b')


    standardLibraryFunctions = words((
        '(&&)', '(*)', '(+)', '(-)', '(.)',
        '(/)', '(<)', '(<<<)', '(<|)', '(>)',
        '(>>>)', '(^)', '(|>)', '(||)', 'above',
        'abs', 'absolute', 'acos', 'all', 'alpha',
        'and', 'any', 'append', 'arrows', 'asText',
        'asin', 'atan', 'atan2', 'average', 'balance',
        'balance_node', 'below', 'beside', 'black', 'blacken',
        'blackish', 'blue', 'bold', 'bottomLeft', 'bottomLeftAt',
        'bottomRight', 'bottomRightAt', 'brown', 'bubble', 'button',
        'buttons', 'ceiling', 'centered', 'charcoal', 'checkbox',
        'checkboxes', 'circle', 'clamp', 'clicks', 'collage',
        'color', 'color_flip', 'color_flipIfNeeded', 'combine', 'compare',
        'complement', 'concat', 'concatMap', 'connect', 'cons',
        'constant', 'contain', 'container', 'cos', 'count',
        'countIf', 'croppedImage', 'ctrl', 'curry', 'customButton',
        'customButtons', 'darkBlue', 'darkBrown', 'darkCharcoal', 'darkGray',
        'darkGreen', 'darkGrey', 'darkOrange', 'darkPurple', 'darkRed',
        'darkYellow', 'dashed', 'day', 'dayOfWeek', 'defaultLine',
        'degrees', 'del', 'delay', 'diff', 'diff',
        'dimensions', 'directions', 'div', 'dotted', 'down',
        'drop', 'dropDown', 'dropIf', 'dropLeft', 'dropRepeats',
        'dropRight', 'dropWhen', 'e', 'either', 'email',
        'empty', 'emptyFieldState', 'endsWith', 'ensureBlackRoot', 'enter',
        'every', 'field', 'fields', 'filled', 'filter',
        'findWithDefault', 'fittedImage', 'flip', 'float', 'floatList',
        'floor', 'flow', 'foldl', 'foldl1', 'foldp',
        'foldr', 'foldr1', 'form', 'fps', 'fpsWhen',
        'fromBool', 'fromCode', 'fromElement', 'fromFloat', 'fromInt',
        'fromJSObject', 'fromJSString', 'fromList', 'fromList', 'fromList',
        'fromList', 'fromPolar', 'fromRecord', 'fromString', 'fromString',
        'fst', 'get', 'gradient', 'gray', 'grayscale',
        'green', 'grey', 'greyscale', 'group', 'groupTransform',
        'head', 'header', 'height', 'heightOf', 'hiddenState',
        'hour', 'hoverable', 'hoverables', 'hsv', 'hsva',
        'id', 'identity', 'image', 'inHours', 'inMilliseconds',
        'inMinutes', 'inSeconds', 'indexes', 'indices', 'insert',
        'intersect', 'intersperse', 'inward', 'isBBlack', 'isClicked',
        'isDigit', 'isDown', 'isEmpty', 'isHexDigit', 'isJust',
        'isLeft', 'isLower', 'isNothing', 'isOctDigit', 'isRight',
        'isUpper', 'italic', 'join', 'justified', 'justs',
        'keepIf', 'keepWhen', 'keys', 'keysDown', 'last',
        'lastPressed', 'layers', 'left', 'lefts', 'length',
        'lessBlack', 'lessBlackTree', 'lift', 'lift2', 'lift3',
        'lift4', 'lift5', 'lift6', 'lift7', 'lift8',
        'lightBlue', 'lightBrown', 'lightCharcoal', 'lightGray', 'lightGreen',
        'lightGrey', 'lightOrange', 'lightPurple', 'lightRed', 'lightYellow',
        'linear', 'lines', 'link', 'link', 'logBase',
        'lookup', 'map', 'markdown', 'matrix', 'max',
        'maximum', 'maybe', 'member', 'merge', 'merges',
        'midBottom', 'midBottomAt', 'midLeft', 'midLeftAt', 'midRight',
        'midRightAt', 'midTop', 'midTopAt', 'middle', 'middleAt',
        'millisecond', 'min', 'minimum', 'minute', 'mod',
        'monospace', 'month', 'moreBlack', 'moreBlackTree', 'move',
        'moveX', 'moveY', 'multiply', 'ngon', 'not',
        'opacity', 'or', 'orange', 'otherwise', 'outlined',
        'outward', 'oval', 'overline', 'pad', 'padLeft',
        'padRight', 'partition', 'password', 'path', 'pi',
        'plainText', 'polygon', 'position', 'post', 'product',
        'pure', 'purple', 'radial', 'radians', 'range',
        'read', 'readFloat', 'readInt', 'rect', 'red',
        'redden', 'relative', 'rem', 'remove', 'remove_max',
        'repeat', 'request', 'reverse', 'rgb', 'rgba',
        'right', 'righted', 'rights', 'rotate', 'rotateLeft',
        'rotateLeftIfNeeded', 'rotateRight', 'rotateRightIfNeeded', 'rotation', 'round',
        'run', 'sampleOn', 'scale', 'scaleX', 'scaleY',
        'scanl', 'scanl1', 'second', 'segment', 'send',
        'sendGet', 'shift', 'show', 'sin', 'since',
        'singleton', 'size', 'sizeOf', 'snd', 'solid',
        'space', 'spacer', 'split', 'sprite', 'sqrt',
        'square', 'startsWith', 'state', 'step', 'strikeThrough',
        'stringDropDown', 'sub', 'sum', 'tag', 'tail',
        'take', 'tan', 'taps', 'text', 'textured',
        'tiledImage', 'timestamp', 'toBool', 'toCode', 'toElement',
        'toFloat', 'toFloat', 'toFloat', 'toForm', 'toInt',
        'toJSObject', 'toJSString', 'toList', 'toLocaleLower', 'toLocaleUpper',
        'toLower', 'toPolar', 'toRecord', 'toString', 'toText',
        'toTime', 'toUpper', 'topLeft', 'topLeftAt', 'topRight',
        'topRightAt', 'touches', 'traced', 'translation', 'trim',
        'trimLeft', 'trimRight', 'truncate', 'turns', 'typeface',
        'uncons', 'uncurry', 'underline', 'union', 'unzip',
        'up', 'values', 'wasd', 'white', 'width',
        'widthOf', 'words', 'xor', 'year', 'yellow',
        'zip', 'zipWith', '(++)', '(::)', '(<~)',
        '(~)',
        ), suffix=r'\b')

    reservedWords = words((
        'as', 'case', 'class', 'data', 'default',
        'deriving', 'else', 'export', 'foreign',
        'hiding', 'jsevent', 'if', 'import', 'in',
        'infix', 'infixl', 'infixr', 'instance', 'let',
        'module', 'newtype', 'of', 'then', 'type',
        'where', '_',
        ), suffix=r'\b')

    tokens = {
        'root': [

            # Comments TODO: just started
            (r'{-', Comment.Multiline, 'comment'),
            (r'--.*', Comment.Single),

            # Whitespace
            (r'\s+', Text),

            # Strings
            (r'"', String, 'doublequote'),

            # Types
            (builtinTypes, Keyword.Type),

            # Keywords
            (reservedWords, Keyword.Reserved),

            # Libraries
            (libraries, Keyword.Namespace),

            # Standard Library Functions
            (standardLibraryFunctions, Name.Function),

            # Main
            (specialName, Keyword.Reserved),

            # Operators
            (builtinOps, Operator),

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

