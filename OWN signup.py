import json
import os

def password(pw):
    len_pw=len(pw)
    if  len_pw >= 8 and len_pw <=18:
        if pw >="A" and pw<="Z" or pw >="a" and pw<="zGoogle" and pw.isdigit() and pw=="@" or pw=="#":
            return ("the password is strong")
        else:
            print("Password should contain atleast one uppercase, lowercase ,one special character and one number.")
            pw=input("enter the password :")
            password(pw)
    else:
        print("minimum at least length of password is 8")   
        pw=input("enter the password :")
        password(pw)


def conformpassword(cnfpw,pw):
    if pw==cnfpw:
        return ("your password is created")
    else:
        b=input("enter the conform password again:")
        if len(b)<=8 and len(b)>=18:
            if b >="A" and b<="Z" or b >="a" and b<="z" and b.isdigit() and b=="@" or b=="#":
                if pw==b:
                     return "your password is created"
                else:
                    print("wrong password")
                    cnfpw=input("enter the conform password :")
                    conformpassword(cnfpw,pw)
            else:
                print("password consists special character,lower case,upper case,digits")
                cnfpw=input("enter the conform password :")
                conformpassword(cnfpw,pw)
        else:
            print(" passwords consits more than 8 ")
            password(pw)
            cnfpw=input("enter the conform password :")
            conformpassword(cnfpw,pw)


userinput=input("enter the login or signup :")
path_exists=os.path.exists("user.json")
l={}   
if userinput=="signup":
    if path_exists==False:
        d={}
        d1={}
        a=input("enter the username :")
        pw=input("enter the password :")
        cnfpw=input("enter the conform password :")
        password(pw)
        if pw==cnfpw:
            d["username"]=a
            d["password"]=pw
            print("congrats",a,"you signed sucessfully")
            w=input("enter the description:")
            x=input("enter the gender:")
            y=input("enter the hobbies:")
            z=input("enter the birthdate:")
            d1["Description"]=w
            d1["Gender"]=x
            d1["Hobbies"]=y
            d1["Birthdate"]=z
            d.update({"profile":d1})
            l.update({a:d})
            conformpassword(cnfpw,pw) 
            with open("user.json","w") as f:
                json.dump(l,f,indent=4)
    elif path_exists==True:
        d={}
        d1={}
        a=input("enter the username :")
        pw=input("enter the password :")
        cnfpw=input("enter the conform password :")
        password(pw)
        if pw==cnfpw:
            d["username"]=a
            d["password"]=pw
            print("congrats",a,"you signed sucessfully")
            w=input("enter the description:")
            x=input("enter the gender:")
            y=input("enter the hobbies:")
            z=input("enter the birthdate:")
            d1["Description"]=w
            d1["Gender"]=x
            d1["Hobbies"]=y
            d1["Birthdate"]=z
            d.update({"profile":d1})
            l.update({a:d})
            conformpassword(cnfpw,pw)
            with open("user.json","w") as f:
                json.dump(l,f,indent=4)
if userinput=="login":
    with open("user.json","r") as f1:
            s=json.load(f1)
            a=input("enter the username :")
            pw=input("enter the password :")
            cnfpw=input("enter the conform password : ")
            for i in s.keys():
                for j in s[i]:
                    if s[i]["username"]==a:
                        if pw==s[i]["password"]:
                                print("your account already exists")
                                password(pw)
                                break
                        else:
                            print("enter the correct password")
                            pw=input("enter the correct  password :")
                            if pw==s[i]["password"]:
                                print("your account already exists")
                                password(pw)
                                break
                            else:
                                print("your password is incorrect")
                                break
                    else:
                        print("your account not created")
                        d={}
                        d1={}
                        if pw==cnfpw:
                                d["username"]=a
                                d["password"]=pw
                                print("congrats",a,"you signed sucessfully")
                                w=input("enter the description:")
                                x=input("enter the gender:")
                                y=input("enter the hobbies:")
                                z=input("enter the birthdate:")
                                d1["Description"]=w
                                d1["Gender"]=x
                                d1["Hobbies"]=y
                                d1["Birthdate"]=z
                                d.update({"profile":d1})
                                l.update({a:d})
                                print("you created account now ")
                                conformpassword(cnfpw,pw)
                                with open("user.json","w") as f:
                                    json.dump(l,f,indent=4)
                                    break
                        else:
                            print("your account is not yet")
                            break
else:
    print("ERROR, You entered wrong input, Try again ")

