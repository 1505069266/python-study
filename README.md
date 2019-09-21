## 因为pip的下载过慢,如何更换国内的pip源,类似与npm的淘宝镜像
```
如果我们一般下载一个包是这样的:
pip install matplotlib
那么可以改成这样:
pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
也就是在下面的后面加上:
-i https://pypi.tuna.tsinghua.edu.cn/simple   //这是清华服务器的源
-i http://mirrors.aliyun.com/pypi/simple/  //这是阿里云的源
-i http://pypi.douban.com/simple/   //这是豆瓣的源  值得一提的是  豆瓣全是用python开发的网站
```
### 如何永久使用国内的源: 可参考网站:https://www.cnblogs.com/schut/p/10410087.html