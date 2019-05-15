# class DefaultInit(object):
#     def __init__(self):
#         print('我是不带参的init方法。')
#
#     def __init__(self,param):
#         print(f'我是一个带参的init方法,参数值为：{param}')
#
#
# DefaultInit('HELLO')
# print('全剧终')


# DefaultInit('hello')
# print(f'调用:{s}')


# class DefaultInit(object):
#     def __init__(self):
#         print('我是不带参的init方法。')
#     def __init__(self, param):
#         print(f'我是一个带参的init方法,参数值为：{param}')
#
#
# DefaultInit('hello','world')
# print('全剧终')
# ###TypeError: __init__() takes 2 positional arguments but 3 were given
#
# class DefaultInit(object):
#     def __init__(self,param):
#         print(f'我是带参init方法:{param}')
#
#     def init__(self):
#         print('我是不带参init方法。')
#
# DefaultInit('hello')
# print('全剧终')

##########################################################问题所在##############################
# class DefaultInit(object):
#     def __init__(self,param):
#         print(f'我是带参init方法:{param}')
#
#     def __init__(self):
#         print('我是不带参init方法。')
#
#     def show(self):
#         print('好戏开始')
#
# test = DefaultInit('')
# DefaultInit.show('hello')
# print('全剧终')


##############################################################################3
############类的访问权限
# class Student():
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#
#     def info(self):
#         print(f'学生:{self.name};分数:{self.score}')
# # stu = Student()
#
# stu = Student('xiaoming',95)
# print(f'修改前分数:{stu.score}')
# stu.info()
# stu.score = 0
# print(f'修改后分数:{stu.score}')
# stu.info()



#####3
# class Student():
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#
#
#     def info(self):
#         print(f'学生:{self.name};分数:{self.score}')
# # stu = Student()
#
# stu = Student('xiaoming',95)
# print(f'修改前分数:{stu.score}')
# stu.info()
# stu.score = 0
# print(f'修改后分数:{stu.score}')
# stu.info()
###AttributeError: 'Student' object has no attribute 'score'#变量属性私有外部禁止访问只允许在内部访问以及修改

###########提供外部修改方案

# class Student():
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#
#
#     def info(self):
#         print(f'学生:{self.__name};分数:{self.__score}')
#
#     def get_score(self):####获取之前变量且显示
#         return self.__score
#
#     def set_score(self,score):####修改内部私有变量
#         self.__score = score
#
#
# stu = Student('xiaoming',95)
# print(f'修改前分数:{stu.get_score()}')
# stu.info()
# stu.set_score(60)
# print(f'修改后分数:{stu.get_score()}')
# stu.info()

#################################################3
# class Student():
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#
#
#     def info(self):
#         print(f'学生:{self.__name};分数:{self.__score}')
#
#     def get_score(self):####获取之前变量且显示
#         return self.__score
#
#     def set_score(self,score):
#         if 0<=score<=100:
#             self.__score = score
#         else:
#             print('请输入合理数字。')
#         ####修改内部私有变量
#
#
#
# stu = Student('xiaoming',95)
# print(f'修改前分数:{stu.get_score()}')
# stu.info()
# stu.set_score(-10)
# print(f'修改后分数:{stu.get_score()}')
# stu.info()
# #####私有类方法与此相同！！！


