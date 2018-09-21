# VimAsIDE
This document aims to explain the setup of Windows subsystem for linux for C++ developm
ent
pt-get install nvim
 install vim plug. Use curl to transfer data from server
 f --fail fail silently. No feedback on server errors
 L --Location Redo request if server indicates a relocation
 o --output Output to File instead of STDOUT
url -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubuser
content.com/junegunn/vim-plug/master/plug.vim
 Add a plug secion to init.vim and run PlugInstall
 For plugins requiring extra steps. Add a { 'do' : 'some_command'} to end of line
 To make the plugin load at first invocation of some_vim_command add a { 'on': 'some_vim
_command'}
 Values starting with : are recognized as Vim commmands
 Python is commonly used for completion plugins because the allow expensive processes to
 run in the background without freezing the vim UI. For that we will need python3 suppor
t in our neovim
udo pip3 install --upgrade neovim


#C++, Clang LLVM
LLVM: a collection of modular and reusable compiler and toolchain technologies for arbit
rary programming languages.
Clang: C/C++/Objective-C compiler witch LLVM as backend. 3x faster than gcc. Good for st
atic analysis.
YouCompleteMe uses libclang for code completion. libclang requires a set of compile flag
s in order to parse the code. We may use a compilation database

filetypes can be found in !ls $VIMRUNTIME/ftplugin
rtags
apt-get install libclang-dev

to enable make
let &makeprg='(pushd build > /dev/null; make; ./Test; popd > /dev/null;)'

TODO: can I use Build Ear to generate database?


CMAKE
How do I link the C-project openSLP into a CMAKE project
extensions:
la libtool library file necessary for linking the library. Used to support plattform ind
ependence
        # the name that we can dlopen(3).
        dlname='libslp.so.1'
        
        # names of this library.
        library_names='libslp.so.1.0.0 libslp.so.1 libslp.so'

        # the name of the static archive.
        old_library='libslp.a'

        # Directory that this library needs to be installed in:
        libdir='/usr/local/lib'
