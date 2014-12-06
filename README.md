PYGMENTS-ELM
============
An [Elm](http://elm-lang.org) lexer for [pygments](http://pygments.org)

> Work in progress

Elm source code can be highlighted with some success by existing lexers for Haskell, but there are enough features to warrant its own lexer, I think. This is especially true for some of the F#-inspired syntax (`|>`) and some often-used standard library functions like `foldp` and `<~`.

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
