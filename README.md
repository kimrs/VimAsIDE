# VimAsIDE
#This document aims to explain the setup of Windows subsystem for linux for C++ development^M
apt-get install nvim^M
# install vim plug. Use curl to transfer data from server^M
# f --fail fail silently. No feedback on server errors^M
# L --Location Redo request if server indicates a relocation ^M
# o --output Output to File instead of STDOUT^M
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim^M
# Add a plug secion to init.vim and run PlugInstall^M
# For plugins requiring extra steps. Add a { 'do' : 'some_command'} to end of line^M
# To make the plugin load at first invocation of some_vim_command add a { 'on': 'some_vim_command'} ^M
# Values starting with : are recognized as Vim commmands^M
# Python is commonly used for completion plugins because the allow expensive processes to run in the background without freezing the vim UI. For that we will need python3 support i
n our neovim^M
sudo pip3 install --upgrade neovim^M
^M
^M
^M
^M
^M
^M
^M
#C++, Clang LLVM^M
LLVM: a collection of modular and reusable compiler and toolchain technologies for arbitrary programming languages.^M
Clang: C/C++/Objective-C compiler witch LLVM as backend. 3x faster than gcc. Good for static analysis. ^M
YouCompleteMe uses libclang for code completion. libclang requires a set of compile flags in order to parse the code. We may use a compilation database^M
^M
filetypes can be found in !ls $VIMRUNTIME/ftplugin ^M
rtags^M
apt-get install libclang-dev^M
^M
to enable make^M
let &makeprg='(pushd build > /dev/null; make; ./Test; popd > /dev/null;)'^M
^M
TODO: can I use Build Ear to generate database?^M

# VimAsIDE
CMAKE ^M
How do I link the C-project openSLP into a CMAKE project^M
extensions: ^M
la libtool library file necessary for linking the library. Used to support plattform independence  ^M
        # the name that we can dlopen(3).^M
        dlname='libslp.so.1'^M
        ^M
        # names of this library.^M
        library_names='libslp.so.1.0.0 libslp.so.1 libslp.so'^M
        ^M
        # the name of the static archive.^M
        old_library='libslp.a'^M
^M
        # Directory that this library needs to be installed in:^M
        libdir='/usr/local/lib'^M
