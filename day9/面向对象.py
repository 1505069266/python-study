# 面向过程容易被初学者接受,其往往用一段长代码来实现制定功能,开发过程的思路是将数据与函数按照执行的逻辑顺序组织在一起,数据与函数分开考虑
# 面向对象:将数据与函数绑定到一起,进行封装,这样能够快速的开发程序,减少了重复代码的重写过程

def 发送邮件(内容):
    # 发送邮件提醒
    连接邮箱服务器
    发生邮件
    关闭连接

while True:
    if cpu利用率 > 90%:
        发送邮件("CPU报警)
    
    if 键盘利用率 > 90%:
        发送邮件("键盘报警")
    
    if 内容占用 > 90%:
        发送邮件("内存报警)