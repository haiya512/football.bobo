ziwang太让我失望了
都不讲自己的思路, 一味的讲代码和模块。而且这些数据只在500万上,
随着500万的数据更新和样式的改变,他的书很快就会过时,没有任何作用。

具有实战意义的应该是抽取出关键字段的数据, 脱离出网站,但又要和网站结合。
有了关键字和思路, 在网站的样式变了之后就不会手忙脚乱, 无从下手了。


1. 对网页编码先进行探测,探测之后再读取, 保存为tmp/500_datetime.htm
        with open("your_file", 'rb') as fp:
            file_data = fp.read()
            result = chardet.detect(file_data)
            file_content = file_data.decode(encoding=result['encoding'])
2. 读取html网页文件或者直接获取内容, 在zc703_bs4_type.py

3. 先处理已获取的,不必全部获取数据, 对已有的数据做分析也可以。数据越多,样本越大。但并不代表已有的样本集就不行。

