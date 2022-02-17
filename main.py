# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# #
# # class Order(object):
# #     def __init__(self,side,price,quantity,symbol,action,myid):
# #         self.side = side
# #         self.price = price
# #         self.quantity = quantity
# #         self.symbol = symbol
# #         self.action = action
# #         self.id = myid
# #     def increment_price(self,number):
# #         self.price += number
# #     def __repr__(self):
# #         return ("Order(%s,%d,%d,%s,%s,%d)" % (
# #             self.side, self.price, self.quantity, self.symbol,
# #             self.action, self.id
# #         ))
# #
# # o1=Order('sell',10,100,'MSFT','new',1)
# # o2=Order('sell',11,100,'MSFT','new',2)
# # o3=Order('sell',12,100,'MSFT','new',3)
# # print(o1.price)
# # o1.increment_price(66)
# # print(o1.price)
# # print(o2)
# # print(o3)
# #
# class FOKOrder(Order):
#     def __init__(self,side,price,quantity,symbol,action,myid,ispartial):
#         super().__init__(side,price,quantity,symbol,action,myid)
#         self.ispartial = ispartial
#     def __repr__(self):
#         return ("FOKOrder(%s,%d,%d,%s,%s,%d,%d)" % (
#             self.side, self.price, self.quantity, self.symbol,
#             self.action, self.id, self.ispartial
#         ))
# #
# # fok1 = FOKOrder('sell',10,100,'MSFT','new',1, True)
# # print(fok1)
#
#
# #
#
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')
# #     # Press ⌘F8 to toggle the breakpoint.
# #
# #
# # # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
#
# import random
# import time
#
# class Message(object):
#     def __init__(self, sending_time, sequence_number):
#         self.__sending_time = sending_time
#         self.__sequence_number = sequence_number
#
#     def getSendingTime(self):
#         return self.__sending_time
#
#     def getSequenceNumber(self):
#         return self.__sequence_number
#
#     def setSendingTime(self, number):
#         self.__sending_time = number
#
#     def setSequenceNumber(self, number):
#         self.__sequence_number = number
#
#
# class AddModifyOrderMessage(Message):
#     def __init__(self, sending_time, sequence_number, price, quantity, side, order_id):
#         self.__price = price
#         self.__quantity = quantity
#         self.__side = side
#         self.__order_id = order_id
#         super().__init__(sending_time, sequence_number)
#
#     def getPrice(self):
#         return self.__price
#
#     def getQuantity(self):
#         return self.__quantity
#
#     def getSide(self):
#         return self.__side
#
#     def getOrderId(self):
#         return self.__order_id
#
#     def setPrice(self, price):
#         self.__price = price
#
#     def setQuantity(self, quantity):
#         self.__quantity = quantity
#
#     def setSide(self, side):
#         self.__side = side
#
#     def setOrderId(self, new_id):
#         self.__order_id = new_id
#
# def inheritance_check():
#     sending_time = time.time()
#     sequence_number = random.randint(0, 50)
#     price = random.randint(100, 200)
#     quantity = random.randint(1, 10)
#     side = random.choice(["Sell", "Buy"])
#     order_trade_id = random.randint(1000, 9999)
#
#     message1 = AddModifyOrderMessage(sending_time, sequence_number, price, quantity, side, order_trade_id)
#
#     assert(issubclass(AddModifyOrderMessage, Message))
#
#     print(issubclass(AddModifyOrderMessage, Message))
#     print(message1.__dict__)
#     print({'_AddModifyOrderMessage__price': price,
#                                  '_AddModifyOrderMessage__quantity': quantity,
#                                  '_AddModifyOrderMessage__side': side,
#                                  '_AddModifyOrderMessage__order_id': order_trade_id,
#                                  '_Message__sending_time': sending_time,
#                                  '_Message__sequence_number': sequence_number})
#     assert(message1.__dict__ == {'_AddModifyOrderMessage__price': price,
#                                  '_AddModifyOrderMessage__quantity': quantity,
#                                  '_AddModifyOrderMessage__side': side,
#                                  '_AddModifyOrderMessage__order_id': order_trade_id,
#                                  '_Message__sending_time': sending_time,
#                                  '_Message__sequence_number': sequence_number})
#
# inheritance_check()

print(1+1)