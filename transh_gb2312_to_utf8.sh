#!/bin/bash
CWD=`pwd`
a=$*
function check_gb2312() {
    gb=0
    cr=0
    files=$1
    for file in $files;do
        [ -d $file ] && continue
        echo $file | grep "\.utf8$" && continue
        echo $file | grep "\.sh$" && continue
        #echo $file | grep "\.sh$" && continue
        enca $file |grep GB2312 && { echo "$file is GB2312 code"; gb=1;} || { echo "$file is not GB2312 code"; gb=1;}
        enca $file |grep CRLF && { echo "$file is crlf"; cr=1;} || { echo "$file is crlf"; cr=1; }
        [ $gb -eq 1 ] && iconv -f GB18030 -t UTF-8 $file > ${file}.utf8
        [ $cr -eq 1 ] && dos2unix -k $file
    done
}
check_gb2312 $a
