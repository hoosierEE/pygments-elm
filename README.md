PYGMENTS-ELM
============
An [Elm](http://elm-lang.org) lexer for [pygments](http://pygments.org)

> Work in progress

Inspired by the not-wonderful syntax highlighting for Elm on GitHub, as well as the opportunity to contribute to an open-source project and brush up on my Python a bit, this project hopes to make the world a better place.

**EDIT** There's already an issue open for this at [pygments](https://bitbucket.org/birkenfeld/pygments-main/issue/986/support-for-elm-language).

Status
------
* standard libraries - some done, need exhaustive list
* operators - done, needs to be checked and possibly updated as Elm matures
* markdown blocks - not done, currently treated as a string
* webgl blocks - not done
* other? blocks - not done

for Vim users
-------------
Put this at the bottom of your `.vimrc`, to quickly update the lexer and apply the changes to the example file:

```viml
" update Pygments lexer
nnoremap <Leader>a :call LexerUpdate()<CR>
function! LexerUpdate()
    :silent execute "!./updateLexer elm.py"
    :redraw!
endfunction
```

...then, go to your browser and refresh to see the changes.

Contributing
------------
Fork & Pull!
