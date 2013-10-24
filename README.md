zwc
===

这是一个简单的 **中文字数统计工具** 。

原理：忽略一段文字中的所有空白字符（包括中文全角空格），然后统计出剩下的字符个数。

经过测试，此程序的统计结果和某些字处理软件的中文字数统计结果相同。

## 用法

### 命令行工具 zwc

把要统计的文本通过管道输入zwc：

    zwc < foo.txt
    cat foo.txt | zwc

如果输入数据的字符编码不是utf-8：

    zwc --encoding=gb18030 < foo.txt
    cat foo.txt | zwc --encoding=gb18030

### Python模块 zwc.py

    >>> import zwc
    >>> zwc.zwc(u'樂土樂土　爰得我所')
    8

此函数只接受unicode字符串。
如果你的数据是str类型，请先用decode方法将其转换成uniocde。

    >>> uni = '樂土樂土　爰得我所'.decode('utf-8')
    >>> zwc.zwc(uni)
    8
