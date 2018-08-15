#Python标准库学习
## 第一章 文本
### capwords()函数 
- 作用 
	- 将一串字符首字格式化为大写。
- 实现方式
	- 将一串字符以空格或者以指定的分隔符分隔，然后调用join函数输出
	- 实现代码
		```
	def capwords(s, sep=None):
    return (sep or ' ').join(x.capitalize() 
    for x in 	s.split(sep))
		```
- 示例程序如下：

```
fileName: string_capwords.py

import string
s = 'The quick brow fox jumped over the lazy dog.'
print(s)
print(' '.join(x.capitalize() for x in s.split(' ')))
print(string.capwords(s))

OUTPUT:
		The quick brow fox jumped over the lazy dog.
		The Quick Brow Fox Jumped Over The Lazy Dog.
		The Quick Brow Fox Jumped Over The Lazy Dog.
```