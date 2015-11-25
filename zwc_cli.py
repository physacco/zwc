#!/usr/bin/env python
# encoding: utf-8

# Name: 中文字数统计工具
# Description: 可用于统计小说某章节的字数
# Example: zwc < foo.txt
# Author: physacco
# Date: 2015-11-25

import six
import sys
import zwc
import getopt
import locale

def show_usage():
    print('''Usage: zwc [options] < filename

Options:
    -E, --encoding <enc>          Set input character encoding
    -h, --help                    Show this help message and exit
    -v, --version                 Show version message and exit
''')

def show_version():
    print('zwc %s' % zwc.__version__)

def main():
    encoding = locale.getpreferredencoding()

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'E:hv',
            ['encoding=', 'help', 'version'])
    except getopt.GetoptError as e:
        print(str(e))
        exit(2)

    for o, a in opts:
        if o in ['-h', '--help']:
            show_usage()
            exit()
        elif o in ['-v', '--version']:
            show_version()
            exit()
        elif o in ['-E', '--encoding']:
            encoding = a

    # 从stdin读取原始数据(UTF-8编码)
    if six.PY2:
        raw_data = sys.stdin.read()
    else:
        raw_data = sys.stdin.buffer.read()
    Bytes = len(raw_data)

    # 将原始数据转换成unicode字符串
    try:
        string = raw_data.decode(encoding)
        Chars = len(string)
    except Exception as e:
        print('error: %s' % e)
        exit(1)

    # 中文字数统计(不含全角空格)
    VisChars = zwc.zwc(string)

    # 打印统计结果
    print('%d words | %d chars | %d bytes' % (VisChars, Chars, Bytes))

if __name__ == '__main__':
    main()
