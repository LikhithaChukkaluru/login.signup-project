# 1.
# import json 
# ab='{"name":"likhitha","name1":"usharani","n":"thrishna","man":"manasa"}'
# ab='["56",23,90,78,"k"]'
# ab="89"
# ab='true'
# ab='false'
# ab="null"
# ab="90.89"
# b=json.loads(ab)
# print(type(ab))
# print(type(b))
# print(b)

# import json
# print(json.loads('{"name": "John", "age": 30}'))
# print(json.loads('["apple", "bananas"]'))
# print(json.loads('42'))
# print(json.loads('31.76'))
# print(json.loads("true"))
# print(json.loads("false"))
# print(json.loads('null')) 


# 2.
# import json
# a={'name':"likhitha","name1":'usharani',"n":"thrishna","man":"manasa"}
# a=["56",23,90,78,"k"]s
# a=89
# a=True
# a=False
# a=None
# a=90.89
# b=json.dumps(a)
# print(type(b))
# print(b)
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None)) 

# import json
# t={"name": "David", "class": "I", "age": 6}
# b=json.dumps(t)
# print(b)


# 3.
# import json
# y ={"name" : "likki","phonenumber" : "9976770500"}
# x={"likki":23,"krishna":"lord"}
# with open("text.json", "w") as f:
#     json.dump((y,x),f)

# import json
# with open('sample.json', 'r') as f:
#     js = json.load(f) 
# print(js)
# print(type(js))


# 4.
# import json
# d={'4': 5, '6': 7, '1': 3, '2': 4}
# c=json.dumps(d,sort_keys=True)
# print(c)


# 6.
# import json
# a = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
# b=json.loads(a)
# print(b)
# c=json.dumps(b)
# print(c)
# print(type(a))
# print(type(b))
# print(type(c))


# 7.
# f=open("text.txt","w")
# f.write("Name Abhishek\n")
# f.write("Designation CEO of navgurukul\n")
# f.write("Gender male\n")
# f.write("Age 29\n")
# print(f)
# f.close()

# import json
# file="text.txt"
# d={}
# with open("text.txt")as f:
#     for s in f:
#         key,value=s.strip().split(None,1)
#         d[key]=value.strip()
# sf=open("text3.json","w")
# json.dump(d,sf,indent=4)
# sf.close()

# import json
# filename = "text.txt"
# dict1 = {}
# with open(filename) as fh:
#     for line in fh:
#         command, description = line.strip().split(None, 1) 
#         dict1[command] = description.strip()
# out_file = open("test1.json", "w")
# json.dump(dict1, out_file, indent = 4, sort_keys = False)
# out_file.close()

# import json
# filename = 'text.txt'
# dict1 = {}
# fields =['name', 'designation', 'age'] 
# with open(filename) as fh:
#     l = 1 
#     for line in fh:
#         description = list( line.strip().split(None, 4))
#         print(description)
#         sno ='emp'+str(l)
#         i = 0
#         dict2 = {}
#         while i<len(fields):
#                 dict2[fields[i]]= description[i]
#                 i = i + 1
#         dict1[sno]= dict2
#         l = l + 1        
# out_file = open("test2.json", "w")
# json.dump(dict1, out_file, indent = 4)
# out_file.close()


#  8
# a=["neelam","programer","24","24000",]
# b=["komal","trainer","24","20000"]
# c=["anuradha","HR","25","40000"]
# e=["Abhishek","manager","29","63000"]
# d={}
# w={}
# for i in a:
#     w.update({"name":a[0],"Destignation":a[1],"Age":a[2],"Salary":a[-1]})
# d.update({"emp1":w})
# x={}
# for i in d:
#     x.update({"Name":b[0],"Destignation":b[1],"Age":b[2],"Salary":b[-1]})
# d.update({"emp2":x})
# y={}
# for i in c:
#     y.update({"Name":c[0],"Destignatiom":c[1],"Age":c[2],"Salary":c[-1]})
# d.update({"emp3":y})
# z={}
# for i in e:
#     z.update({"Name":e[0],"Destignatiom":e[1],"Age":e[2],"Salary":e[-1]})
# d.update({"emp4":z})
# # print(d)

# import json
# with open("text2.json","w") as f:
#     json.dump(d,f,indent=3)

# with open("text2.json","r") as f: 
#     s=json.load(f)
# print(s)


# PASSWORD

# def password(pw):
#     len_pw=len(pw)
#     if len_pw<=8:
#         print("password has minimum as length of 8")
#         if pw >="A" and pw<="Z" or pw >="a" and pw<="z" and pw.isdigit() and pw=="@" or pw=="#":
#              return True
#         if pw==True:
#             pw2=input("enter the conform password:")
#             if pw==pw2:
#                 return True
#             else:
#                 return "both passwords are not same"
#         else:
#             return "not in minium length"
#     else:
#         print("Password should contain atleast one uppercase, lowercase ,one special character and one number.")
# a=input("enter the password")
# print(password(a))


# CONFORM PASSWORD :

# def cmpassword():
#     a=input("enter the password:")
#     b=input("enter the conform password:")
#     if a==b:
#         print("you password is created")
#     else:
#         if len(a)<=8:
#             if a>="A" and a<="Z" or  a>="a" and a<="z" and a.isdigit() and a=="@" or a=="#": 
#                 print("password consists special character,lower case,upper case,digits")
#             else:
#                 print("wrong password")
#         else:
#             print(" passwords consits more than 8 ")
# cmpassword()      

    
             


