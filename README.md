# patch_to_libc

use any ubuntu glibc in any ubuntu version (with debug info)! a essential tool for glibc pwn.

## install

install eu-unstrip

install [patchelf](https://github.com/NixOS/patchelf)

make them in PATH

## usage

run given libc for version info
```
$ ./libc_64.so.6
GNU C Library (Ubuntu GLIBC 2.23-0ubuntu6) stable release version 2.23, by Roland McGrath et al.
```

`get_libc` can download specified version of ubuntu glibc into current dir.
```
get_libc 2.23-0ubuntu5
```
or 
```
get_libc 2.23-0ubuntu5 xenial
```

`patchlibc` will copy target elf, suffix it with `p`, and patch that copied elf to use current ld and libc.so.6 in current dir.
```
patchlibc ./pwn ./ld-2.23.so
```

then use `./pwnp` and enjoy another version of libc with debug info.

## internal

`down_libc.py`: download related deb package (libc6 and libc6-dbg)

`merge-libc`: extract them and merge them with eu-unstrip, and clean up

`patchlibc`: use `patchelf` to patch interpreter path and rpath
