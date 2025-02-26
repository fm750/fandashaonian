# # name=input('your name:')
# age=int(input('your age:'))
#
# if age< 18:
#     print('禁止进入')
# else:1
#     print('go')
# score=int(input('your score'))
# if score==100:
#     print('good')
# elif score==90:
#     print('bye')
# else:
# #     print('bad')
# a=1
# b=2
# # print(a==b)
# a=1
# b=2
# if a==1:
#     print('yes')
#     if b==2:
#         print('yesb')
#     else:
#         print('no')
#
# else:
#     print('no')
# a=1
# s=0
# while a<1000:
#     s+=a
#     a+=1
# # print('最终结果',s)
#     while a>1000:
#         a+=2
# print(a)
# s=0
# for i in range(101):
#     s+=i
# print(s)
# i=1
# while i<=5:
#     print(f'eat {i} apple')
#     if(i==3):
#         print('no eat 3 apple')
#         i+=1
#         continue
#     i+=1
# for i in range(10):
#     if i==3:
#         continue
#     print(i)
# st='this is a string'
# st1=st.encode('utf-8')
# # print(st1)
# print(st1,type(st1))
# st2=st1.decode('utf-8')
# print(st2,type(st2))
# a='hi'
# b='hello'
# c=a+b
# print(c)
# d=a*2
# print(d)
# e=a*2
# print(e)
# name1='hh'
# name2='dd'
# name3=name1 + name2
# name="少年21fdafas和打野"

# print('h' not in name1)
# print('少年' not in name4)
# print(name4[0])
# print(name4[-1])
# print(name4[:])
# print(name4[0:6:2])
# print(name.find('1'))
# print(name.index('打',2))
# print(name.replace("少年","s")
# print(name.split('d'))
#liebiao
# li=[1,2,3,4,5]
#
# # liaobiao.append(6)
# # liaobiao.insert(5,6)
# # print(liaobiao)
# print('b' not    in li)
# while True:
#     name_all=['haha','ddd','sss']
#     name=input('your name:')
#     if name in name_all:
#         print(f"id {name} already exists")
#     else:
#         print("you can use this id")
#         break
#     # print(name not in name_all)
#     name_all.append(name)
#     print(name_all)

# jj=[1,5,7,45,32,75,7,45,234,547,123]
# #
# jj.sort()
# print(jj)

lie=[]
# [lie.append(i) for i in range(1,101)]
# print(lie)

# for i in range(1,101):
#     lie.append(i)
# print(lie)

# for i in range(10):
#     if i%2==1:
#         lie.append(i)
# print(lie)
# [lie.append(i) for i in range(10) if i%2==1]
# print(lie)
#
sex=[4,5,6,7,8]
lie=[1,2,3,sex]
print(lie[3][2])