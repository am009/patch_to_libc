访问这里https://bugs.launchpad.net/ubuntu/xenial/amd64/libc6/2.23-0ubuntu5
18.04 改成bionic https://bugs.launchpad.net/ubuntu/bionic/amd64/libc6/2.27-3ubuntu1
把后面的glibc版本改了就可以.

https://github.com/NixOS/patchelf
编译patchelf
--set-interpreter 到ld.so(好像可以相对路径./ld-2.23.so)
--set-rpath 到 .
要把libc名字改成libc.so.6 !!

https://packages.ubuntu.com/
下载deb包
使用dpkg -X deb包 目录
解压得到ld.so等
搜索libc6或libc6-dbg得到调试信息
eu-unstrip elf symbol 可以把symbol直接和elf合成, 放到symbol文件里


好像用patchelf把rpath设置在本目录就会加载本目录的libc.so.6
直接运行会崩, gdb调试发现是在libc_start_main崩的. 看来是ld和libc要匹配

这时候装载debug-symbol:
https://clouds.eos.ubc.ca/~phil/docs/gdb/onlinedocs/gdb_17.html
不能直接装载
需要使用add-symbol-file filename -ssection address ...
然后加载text段, 其他各种段的地址
https://stackoverflow.com/questions/33049201/gdb-add-symbol-file-all-sections-and-load-address
这里使用这个脚本直接加载所有的段, 调试信息就正常归位了

## 重新改名
ubuntu16.04 => 2.23-0ubuntu10
ubuntu16.04.11.2 => 2.23-0ubuntu11.2
ubuntu16.04-update => 2.23-0ubuntu11
ubuntu18.04 => 2.27-3ubuntu1
ubuntu18.04.2 => 2.27-3ubuntu1.2
