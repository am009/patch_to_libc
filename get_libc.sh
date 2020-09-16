#!/bin/bash

if [ $# -lt 1 ]; then
    echo "usage: $0 <version> [codename]"
    echo "example $0 2.27-3ubuntu1 bionic"
    echo "example $0 2.23-0ubuntu5 xenial"
    exit 0
fi

LIBCSPATH=/mnt/D/ctf/tools/libcs

if [ ! -d "$LIBCSPATH/$1" ]; then
    echo "start to get libc..."
    python3 "$LIBCSPATH/down_libc.py" $1 $2
fi

if [ -d "$LIBCSPATH/$1" ]; then
    cp $LIBCSPATH/$1/ld-* .
    if [ ! -f ./libc.so.6 ]; then
        cp $LIBCSPATH/$1/libc-* ./libc.so.6
    else
        mv ./libc.so.6 ./libc.so.6.bak
        cp $LIBCSPATH/$1/libc-* ./libc.so.6
    fi
    echo "ok!"
else
    echo "download error!!"
fi
