# find  查找
```
find / -name txt  从根目录下开始查找 名字为txt的文件
find / -name "*name*"   从根目录下找名字中有name的文件
sudo find / -name txt  用管理员权限查找名字为txt的文件
find ./ -name txt  从当前目录开始,查找名字为txt的文件
find / -size 2M  从根目录开始,查找大小等于2M的文件
find / -size +2M  从根目录开始,查找大小大于2M的文件
find / -size -2M  从根目录开始,查找大小小于2M的文件
find ./ -size +4k -size 5M  从当前目录开始,找到大小大于4K小于5M的文件
find ./ -perm 777  查找当前目录下,权限为777的文件或者目录
```
# tar  打包
```
打包
tar -cvf test.tar *.py
解包
tar -xvf test.tar
压缩
tar -zcvf test.tar.gz *.py
```
# cal -y 2019 查看日历
# date 查看当前时间
```
date > test.txt 将时间存到test.txt
cal -y 2019 > date.txt 将日历存到date.txt
date "+%Y=====%m=====%d"  > date.txt   一定要写+   %Y表示年份  %y表示后面的年  如17  19   %m表示月份  %d表示日期
cal  查看日历
```
# ps : 查看进程信息
```
查看所有的进程
ps -aux  :显示一次电脑的进程情况  然后结束
top  :一直显示当前电脑的进程情况  实时更新
kill -9 pid  :关闭pid的程序  -9是强制关闭
```

# reboot 重启
# shutdown -h now 立刻关机
# shutdown -h +20  20分钟后关机

# df  查看磁盘 df -h  查看磁盘 详细
# du  查看当前路径的使用情况
# ifconfig  查看网络连接
# ping 172.124.26.54  测试能不能连接(局域网)
# 创建用户
```
useradd zhuxiaole -m  创建了一个用户
sudo passwd zhuxiaole  修改zhuxiaole的密码
cat /etc/passwd  查看是不是有用户为zhuxiaole的用户
家目录为后面的/home/zhuxiaole
who  查看当前有几个端口访问linux
su -   切换到root账号
su zhuxiaole  切换到zhuxiaole账号
su - zhuxiaole  切换到zhuxiaole账号并且到他的家目录下
```
# 删除用户
```
userdel adc(用户名)   删除adc用户,但不会自动删除用户的主目录
userdel -r adc(用户名)  删除adc用户,同时删除用户的主目录
```
# 组
```
groupadd  YYY  创建一个YYY组
cat /etc/group  查看组
groupdel YYY  删除YYY组
groupmod  查看所有组名 
```
# 权限
```
   有d表示文件夹 没有就是文件        文件拥有者的权限     同组者的权限    其他人的权限
           d                            rwx               rwx            rwx
u文件拥有者     g 同组    o  其他人
chmod  权限
chmod u=r,g=r,o=r xx.txt
chmod 127 xx.txt    4是r2是w1是x
```
# 编辑  vi和vim是一样的意思
```
vim 2.py   创建并且打开2.py文件  默认处在命令模式
i   按i进入编辑模式
esc   按esc退出
:wq   保存并退出  w表示保存   q表示退出
```
 * 命令模式
 ```
 进入编辑模式的操作: i在光标前面  a在光标后面   o另起一行  I大写i在这行的首部   A大写a在这行的尾部  O大写o在这行上面的一行
 dd 剪切光标所在的一行内容
 yy 复制光标所在的一行
 p  粘贴
 4yy 复制 光标所在行开始向下的4行
 2dd 剪切 光标所在的行向下两行
 x  删除当前的光标的后面  每次只会删除一个
 X  删除当前的光标的前面  每次只会删除一个
 h左j下k上l右
 H 当前屏幕最上面
 M 当前屏幕中间
 L 当前屏幕下面
 ctrl + f 向下翻一页
 ctrl + b 向上翻一页
 18G  跳到18行
 G 跳转到代码的最后一行
 gg 快速回到整个代码的第一行
 w 向后跳一个单词的长度,即调到下一个单词的开始
 b 向前跳一个单词的长度,即调到下一个单词的开始

 u 撤销刚刚的操作  类似ctrl + Z
 ctrl + r 反撤销
 v 按字符移动,选择文本
 V 按行移动,选中文本可视模式可以配合 d,y,>>,<< 实现对文本的删除,复制,左右移动
 . 重复上一次操作
 >>  文本行右移
 <<  文本行左移

 r  替换一个字符
 R  替换光标以及后面的字符

 /hello 查找hello  a往下走 A往上走
 :%s/hello/world/g  替换所有hello替换成world
 :1,16s/hello/world/g   替换1-16行所有的hello成world
 shift + zz 相当于:wq
 ```
 * 编辑(插入)模式
 ```

 ```
 * 末行模式
 ```
 插入模式按esc键进入末行模式
 输入:wq  保存退出  进入命令模式
 输入:wq! 强制保存退出
 输入:q! 强制退出  不保存
 ```
