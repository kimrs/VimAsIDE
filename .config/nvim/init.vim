
call plug#begin('~/.config/nvim/plugged')
Plug 'scrooloose/nerdtree', {'on': 'NERDTreeToggle', 'for':'clojure'}
Plug 'Valloric/YouCompleteMe', { 'for': 'cpp', 'do': './install.py --clang-completer' }
Plug 'lyuts/vim-rtags', { 'for': 'cpp' }
call plug#end()
let g:python_host_prog = '/usr/bin/python2'
let g:python3_host_prog = '/usr/bin/python3'

let &makeprg='(pushd build > /dev/null; make; ./Test; popd > /dev/null;)'
set background=dark
