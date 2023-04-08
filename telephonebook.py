#telephone book
phonebook={}
while True:
    menu=["S]Show Contact","A]Add Contact","M]Modify","D]Delete Contact","E]Exit"]
    for row in menu:
        print(row)
    ch=input("Enter Your Choice [s,a,d and e]:")
    if ch in "Ss":
        print("------------Contact List---------------")
        sr=1
        for row in phonebook:
            print ("SR:",sr,"\nName:",row,"\nPhone Number:",phonebook[row])
            print("-"*50)
            sr+=1
    elif ch in 'Aa':
        print("------------------Add new------------------")
        n=input("Enter Person name: ")
        c=input("Enter Mobile number: ")
        phonebook[n]=c
    elif ch in "Dd":
        print("----------- Delete Contact----------------")
        n=input("Enter Person name: ")
        count=0
        for row in phonebook:
            if row==n:
                count=1
                del(phonebook[row])
                break
        if count==1:
            print("Contact deleted successfully")
        else:
            print("No Contact found...")
    elif ch in "Ee":
        print("------------------Exit-------------------")
        break
    elif ch in "Mm":
        print("------------------Modify Contact-------------------")
        n=input("Enter Person name: ")
        count=0
        d,c="",""
        for row in phonebook:
            if row==n:
                count=1
                c=input("Enter New Contact: ")
                d=phonebook[row]
                phonebook[row]=c
                break
        if count==1:
            print(n," Modified old No:",d,"With new No:",c,"successfully")
        else:
            print("No Contact found...")
