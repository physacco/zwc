zwc
===

This is a small Chinese word count tool.

这是一个简单的 **中文字数统计工具** 。

原理：忽略一段文字中的所有空白字符（包括中文全角空格），然后统计出剩下的字符个数。

经过测试，此程序的统计结果和某些字处理软件的中文字数统计结果相同。

## 安装

    pip install zwc

## 升级

    pip install --upgrade zwc

## 用法

### 命令行工具 zwc

把要统计的文本通过管道输入zwc：

    $ zwc < foo.txt
    $ cat foo.txt | zwc

如果输入数据的字符编码不是utf-8：

    $ zwc --encoding=gb18030 < foo.txt
    $ cat foo.txt | zwc --encoding=gb18030

`--encoding=gb18030` 可以简写为 `-E gb18030`

### Python模块 zwc.py

    >>> import zwc
    >>> zwc.zwc(u'樂土樂土　爰得我所')
    8

此函数只接受unicode字符串。
如果你的数据是str类型，请先用decode方法将其转换成uniocde。

    >>> uni = '樂土樂土　爰得我所'.decode('utf-8')
    >>> zwc.zwc(uni)
    8

### Vim命令 zwc

将以下代码加入vim配置文件：

    function Zwc()
      " send selected lines to system command *zwc* and print the output
      let select_beg_line = getpos("'<")[1]
      let select_end_line = getpos("'>")[1]
      let lines = getline(select_beg_line, select_end_line)
      let input = join(lines, "\n") . "\n"
      echo system("zwc", input)
    endfunction

    vmap zwc :call Zwc() <Home><Del><Del><Del><Del><Del><CR>

打开要阅读或编辑的文件，按 Shift+v键 进入行选择模式，选中若干行，然后直接按下 zwc 3个键，即可显示字数统计结果。

### Emacs命令 zwc

1. 选中一段文本 (e.g. ``C-Spc C-n``)
2. 将选中的文本发送给zwc子进程
    * ``M-x shell-command-on-region RET zwc RET``
    * ``M-| zwc RET``
