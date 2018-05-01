
# tup1 = ('physics', 'chemistry', 1997, 2000);
# print(id(tup1))
# tup1 = ('physics', 'chemistry', 1994, 2000);
# print(id(tup1))
# list1=[3,4,5]
# print(id(list1))
# list1=[2,4,3,4,5]
# print(id(list1))

# def my_function(param=[]):
#     param.append("thing")
#     return param
# print(my_function())
# print(my_function())

# myiterator = [x*x for x in range(3)]
# for i in myiterator:
#     print(i)
#
# mygenerator = (x*x for x in range(3))
# for i in mygenerator:
#     print(i)

from dirsync import sync
sync('c:\src', 'c:\des','sync')
