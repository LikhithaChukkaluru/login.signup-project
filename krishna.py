# import json
# import os
# path_exists=os.path.exists("userdetails.json")
# print(path_exists)
# d={}
# def loginsingnup():
#     a=input("enter the login or signup")
#     if a=="signup":
#         if path_exists==True:
#             d1={}
#             d2={}
#             b=input("enter the username:")
#             c=input("enter the password:")
#             t=input("enter the conform password")
#             if t==c:
#                 d1["username"]=b
#                 d1["password"]=c
#                 print("congrats",b,"you are signed successfully")
#                 w=input("enter the description:")
#                 x=input("enter the gender:")
#                 y=input("enter the hobbies:")
#                 z=input("enter the birthdate:")
#                 d2["Description"]=w
#                 d2["Gender"]=x
#                 d2["Hobbies"]=y
#                 d2["Birthdate"]=z
#                 d1["profile"]=d2
#                 d[b]=d1
#                 with open("userdetails.json","w") as f:
#                     json.dump(d,f,indent=4)
#         elif path_exists==False:
#             d1={}
#             d2={}
#             b=input("enter the username:")
#             c=input("enter the password:")
#             t=input("enter the conform password")
#             if t==c:
#                 d1["username"]=b
#                 d1["password"]=c
#                 print("congrats",b,"you are signed successfully")
#                 w=input("enter the description:")
#                 x=input("enter the gender:")
#                 y=input("enter the hobbies:")
#                 z=input("enter the birthdate:")
#                 d2["Description"]=w
#                 d2["Gender"]=x
#                 d2["Hobbies"]=y
#                 d2["Birthdate"]=z
#                 d1["profile"]=d2
#                 d[b]=d1
#                 with open("userdetails.json","w") as f:
#                     json.dump(d,f,indent=4)
#     elif a=="login":
#         b=input("enter the username:")
#         c=input("enter the password:")
#         t=input("enter the conform password")
#         if t==c:
#             with open("userdetails.json","r") as f1:
#                 s=json.load(f1)
#             for i in s.keys():
#                 if b==i:
#                     for j in s[i]:
#                         if s[i]["username"]==b:
#                                 print("congrats",b,"you are login in  successfully")
#                                 break
#                         else:
#                                 print("The username is not registrated,you have to signup newly to regristartion")
#                                 loginsingnup()
#                                 break
#                     else:
#                         print("you have to signup for new registration")
#                         loginsingnup()
#     else:
#         print("ERROR, You entered wrong input, Try again")
#         loginsingnup()
# loginsingnup()

