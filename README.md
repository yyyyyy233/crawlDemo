# crawlDemo
做项目（da zuo ye），组内成员提的需求，要提取B站/知乎/微博上关于甘肃白银马拉松的相关评论，一个平台数据量>2000.
因为时间仓促，最后做了一个简单版本的爬虫。大概思路如下：

## B站

1.搜索框内搜索“白银马拉松”，得到结果页面，解析前三页的html文件，得到一堆BV号。</br>
2.把BV转成AV。</br>
3.通过调用API得到具体评论数据。</br>

## 微博

1.用m.weibo.com搜索相关话题，解析得到的网页，用正则提取出所有相关微博号。</br>
2.解析这些微博，用相关API得到评论数据。</br>

## 知乎

知乎上相关问题较多，出于爬取方便和数据量要求，选择了最多回答的问题进行分析。</br>
由于知乎自带API只能提取部分问题答案（20条）和评论（20条），出于统筹效率和数据量，选择以下算法：</br>
1.用splinter（selenium）打开相关问题页，循环下拉指定次数。</br>
2.解析相关html，用正则表达式拿到具体回答。</br>
3.调用API，爬取每个回答下的前20条评论。</br>

仅供参考，大佬莫喷~

运行此demo依赖于bs4，requests，splinter，biliBV以及其他必要库。
运行结果位于include文件夹的bilibili/zhihumls/weibomls压缩文件中。
