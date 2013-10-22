#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Name: 中文字数统计工具
# Description: 主要用于统计小说某章节的字数
# Example: cat foo.txt | zwc
# Author: physacco
# Date: 2011-02-08

import sys, re

# 从stdin读取原始数据(UTF-8编码)
raw_data = sys.stdin.read()
Bytes = len(raw_data)

# 将原始数据转换成unicode字符串
string = raw_data.decode('utf-8')
Chars = len(string)

# 清除空白字符(包括中文全角空格)
visible_chars = re.sub(ur'[\s\u3000]+', '', string)
VisChars = len(visible_chars)

# 打印统计结果
print "%d words | %d chars | %d bytes" % (VisChars, Chars, Bytes)
