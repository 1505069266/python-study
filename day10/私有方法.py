class SendMessage:
    # 私有方法  __加方法名  不能被外部调用
    def __send_msg(self):
        print("--正在发送短信--")

    # 共有方法
    def send_msg(self,new_money):
        if new_money > 10000:
            self.__send_msg()
        else:
            print("余额不足,请先充值")


sendMessage = SendMessage()

sendMessage.send_msg(2000)

