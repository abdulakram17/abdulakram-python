master_pwd=input("Enter the Master__Password::")

def view():
    with open('abdul.txt','r')as f:
        for line in f.readlines():
            data=line.rstrip()
            name,pwd=data.split("|")
            print("usename",name,"Password",pwd)
              
def add():
    acctype=input("Enter the Acctype::")
    name=input("Enter the AccountName::")
    pwd=input("Enter the passsword::")

    with open('password.txt','a')as f:
        f.write(name+"|"+pwd+"\n")

while True:
    mode=input("Would you like to add or view or quit? add|view|q::")
    if mode=='q':
        break
    elif mode=='add':
        add()
    elif mode=='view':
        view()
    else:
        print('Invalid Input from any one of the Type add|view|q::')
