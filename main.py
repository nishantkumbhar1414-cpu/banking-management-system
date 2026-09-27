import random
import pandas as pd
import numpy as np
class account:
        def __init__(self,name,mo_no,password,account_no):
            self.name=name
            self.mo_no=mo_no
            self.password=password
            self.account_no=account_no



        
acc_lis=[]
obj_lis=[]
def create_acc():
    name=input("enter the name : ")
    mobile_no=(input("enter the mobile no :"))
    password=(input("enter the pass :"))
    dipo=100
    

    
    account_no=random.randint(1,1000)
    while account_no in acc_lis:
        account_no=random.randint(1,1000)
    acc_lis.append(account_no)
    obj=account(name,mobile_no,password,account_no)

    print("ACCOUNT CREATED SUCCESSFULLY !!!")
    print("name is :",obj.name)
    print("mobile no :",obj.mo_no)
    print("password is :",obj.password)
    print(" your acc  number :",obj.account_no)

    deta=open("data.csv","+a")
    deta.write(f"{obj.name},{obj.mo_no},{obj.password},{obj.account_no}\n")
    print()
    deta.close()
    return obj








def logain():
    
    l_acc_no=int(input("Enter the acc number : "))
    l_inf=pd.read_csv("data.csv")
    if l_acc_no not in l_inf["Acc_no"].values:
        print("INCORRECT ACC NO !!!!!!")
            

    
    else :
        acc_imp=l_acc_no
        count=1
        while count<=3:
            l_pass=input("Enter the password : ")
            if l_inf.loc[l_inf["Acc_no"]==l_acc_no,"Password"].iloc[0]==l_pass:
                print(" YOU ARE SUCCESSFULLY LOGIN ....")
                temp_log=True
                break

            

            else:
                if count==3:
                    print("TOO MANY ATTEMPTS TRY AGAIN AFTER 30 SEC ")
                    return

                else:

                    print("encorrect password . try again !!!!!!")
                    count+=1 

    if temp_log==True:
        while True:
            print("1) DEPOSIT")
            print("2) WITHDRAWL")
            print("3) CHECK")
            print("4) TRANSFER")
            print("5) TRANSITIN")
            print("6) ACC_DETAILS")
            print("7) BREAK")

            logain_choice=int(input("ENTER YOUR CHOICE: "))


            if logain_choice==1:
                deposit(l_acc_no,l_pass)

            elif logain_choice==2:
                withdrawal(l_acc_no,l_pass)

            elif logain_choice==3:
                check(l_acc_no,l_pass)

            elif logain_choice==4:
                transfer(l_acc_no,l_pass)

            elif logain_choice==5:
                transition()

            elif logain_choice==6:
                acc_details(l_acc_no,l_pass)

            elif logain_choice==7:
                break

        return









def deposit(dep_acc_n,password):
    print("hello deposit")
    d_deposit=int(input("enter the amount how you want to deposit : "))
    data=pd.read_csv("data.csv")
    temp_dep=data.loc[data["Acc_no"]==dep_acc_n,"Deposit"][0]
    temp_dep+=d_deposit
    data.loc[data["Acc_no"]==dep_acc_n,"Deposit"]=temp_dep
    data.to_csv("data.csv", index=False)
    print("SUCESS$$$$$")
    print("your current balence is now : ",temp_dep)
    return








def withdrawal(dep_acc_n,password):
    print("HELLO WITHDRAWL.")
    w_withdrawl=int(input("ENTER THE AMMOUNT HOW MUCH DO YOU WANT: "))
    data=pd.read_csv("data.csv")
    ans=data.loc[data["Acc_no"]==dep_acc_n,"Deposit"][0]
    if w_withdrawl<=ans:
        ans-=w_withdrawl
        data.loc[data["Acc_no"]==dep_acc_n,"Deposit"]=ans
        print(w_withdrawl," ammount withdrawal successfully $$$$")
        print("your current balence is ",ans)

    else:
        print("in sufficient balence!!!!!!!!")

    data.to_csv("data.csv",index=False)
    return






def check(bank_acc,bank_pass):
    print("hello check balence.")
    data=pd.read_csv("data.csv")
    balence=data.loc[data["Acc_no"]==bank_acc,"Deposit"][0]
    print("YOUR BANK BALENCE IS : ",balence)
    return





def transfer(bank_acc,bank_pass):
    print("hello transfer")
    count=0
    data=pd.read_csv("data.csv")
    acc_no=int(input("ENTER RECEIVERS ACC NO: "))
    t_temp=False
    while count<3:
        if acc_no in data["Acc_no"].to_list():
            amount=int(input("ENTER THE AMMOUNT : "))
            if amount > data.loc[data["Acc_no"]==bank_acc,"Deposit"].iloc[0]:
                print("In sufficient balence !!!!!!")

            else:
                if bank_acc==acc_no:
                    print("CANT TRANSFER ENTER VALID ACC NO!!!!")
                    break
                else:

                    f_amount=data.loc[data["Acc_no"]==bank_acc,"Deposit"].iloc[0]
                    s_amount=data.loc[data["Acc_no"]==acc_no,"Deposit"].iloc[0]
                    s_amount+=amount
                    f_amount-=amount
                    data.loc[data["Acc_no"]==bank_acc,"Deposit"]=f_amount
                    data.loc[data["Acc_no"]==acc_no,"Deposit"]=s_amount
                    print(amount," sent successifully$$$")
                    print("your current balence is : ",f_amount)
                    data.to_csv("data.csv",index=False)
                    break
        else:
            print("incorrect acc no try again")
                

        count+=1
    return
    
                



def transition():
    print("hello transition")
    print("SORRY FOR INCONVENENCE HISTRY IS NOT AVAILABLE ATE!!!!!")

def acc_details(bank_acc,bank_pass):
    print("hello acc_details")
    information=data.loc[data["Acc_no"]==bank_acc]
    print("ACCOUNT HOLDERS NAME IS : ",information["Name"][0])
    print("Mo_number IS :",information["Mo_number"][0])
    print("ACCOUNT NUMBER IS: ",information["Acc_no"][0])
    print(" WALET BALENCE IS: ",information["Deposit"][0])
    return






while True:

    print("1. Create Account")
    print("2. Login")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Transfer Money")
    print("7. Transaction History")
    print("8. Account Details")
    print("9. Exit")

    # enter the choice
    choice=int(input("enter your choice: "))

    if choice==1:
        print("CREATE AN ACC: ")
        create_acc()


    elif choice==2:
        print("LOGAIN :")
        logain()

    elif choice==3:

        print("DEPOSIT MONEY :")
        temp=False
        ct=0
        while True:
            ct+=1
            bank_acc=int(input(" enter the acc no: "))
            data=pd.read_csv("data.csv")
            if bank_acc in data["Acc_no"].to_list():
                bank_pass=(input(" enter the password: "))
                ans=data.loc[data["Acc_no"]==bank_acc,"Password"].iloc[0]
                count=0
                while count<3:
                    if ans==bank_pass:
                        deposit(bank_acc,bank_pass)
                        temp=True
                        break

                    elif(count==2):
                        print("TRY AFTER THE 30 SEC.!!!!")
                        temp=True
                        break

                    else:
                        print("RE ENTER THE PASS")

                    count+=1

            else:
                print(" RE ENTER THE ACC NO")
            if temp==True:
                break
            if ct==3:
                print(" try again after 30 sec!!!!")
                break




            

    elif choice==4:
        temp=False
        ct=0
        while True:
            ct+=1
            bank_acc=int(input(" enter the acc no: "))
            data=pd.read_csv("data.csv")
            if bank_acc in data["Acc_no"].to_list():
                bank_pass=(input(" enter the password: "))
                ans=data.loc[data["Acc_no"]==bank_acc,"Password"].iloc[0]
                count=0
                while count<3:
                    if ans==bank_pass:
                        withdrawal(bank_acc,bank_pass)
                        temp=True
                        break
        
                    elif(count==2):
                        print("TRY AFTER THE 30 SEC.!!!!")
                        temp=True
                        break
        
                    else:
                        print("RE ENTER THE PASS")
        
                    count+=1
        
            else:
                print(" RE ENTER THE ACC NO")
            if temp==True:
                break
            if ct==3:
                print(" try again after 30 sec!!!!")
                break

    

    elif choice==5:
        print("CHECK BALENCE :")
        temp=False
        ct=0
        while True:
            ct+=1
            bank_acc=int(input(" enter the acc no: "))
            data=pd.read_csv("data.csv")
            if bank_acc in data["Acc_no"].to_list():
                bank_pass=(input(" enter the password: "))
                ans=data.loc[data["Acc_no"]==bank_acc,"Password"].iloc[0]
                count=0
                while count<3:
                    if ans==bank_pass:
                        check(bank_acc,bank_pass)
                        temp=True
                        break
                
                    elif(count==2):
                        print("TRY AFTER THE 30 SEC.!!!!")
                        temp=True
                        break
                
                    else:
                        print("RE ENTER THE PASS")
                
                    count+=1
                
            else:
                print(" RE ENTER THE ACC NO")
            if temp==True:
                break
            if ct==3:
                print(" try again after 30 sec!!!!")
                break

        

    elif choice==6:
        print("TRANSFER MONEY :")
        print("ACC DETAILS :")
        temp=False
        ct=0
        while True:
            ct+=1
            bank_acc=int(input(" enter YOUR  the acc no: "))
            data=pd.read_csv("data.csv")
            if bank_acc in data["Acc_no"].to_list():
                
                ans=data.loc[data["Acc_no"]==bank_acc,"Password"].iloc[0]
                count=0
                while count<3:
                    bank_pass=(input(" enter the password: "))
                    if ans==bank_pass:
                        transfer(bank_acc,bank_pass)
                        temp=True
                        break
                                
                    elif(count==2):
                        print("TRY AFTER THE 30 SEC.!!!!")
                        temp=True
                        break
                                
                    else:
                        print("RE ENTER THE PASS")
                                
                    count+=1
                                
            else:
                print(" RE ENTER THE ACC NO")
            if temp==True:
                break
            if ct==3:
                print(" try again after 30 sec!!!!")
                break

    elif choice==7:
        print("TRANSITION HISTRY :")
        transition()

    elif choice==8:
        print("ACC DETAILS :")
        temp=False
        ct=0
        while True:
            ct+=1
            bank_acc=int(input(" enter the acc no: "))
            data=pd.read_csv("data.csv")
            if bank_acc in data["Acc_no"].to_list():
                bank_pass=(input(" enter the password: "))
                ans=data.loc[data["Acc_no"]==bank_acc,"Password"].iloc[0]
                count=0
                while count<3:
                    if ans==bank_pass:
                        acc_details(bank_acc,bank_pass)
                        temp=True
                        break
                        
                    elif(count==2):
                        print("TRY AFTER THE 30 SEC.!!!!")
                        temp=True
                        break
                        
                    else:
                        print("RE ENTER THE PASS")
                        
                    count+=1
                        
            else:
                print(" RE ENTER THE ACC NO")
            if temp==True:
                break
            if ct==3:
                print(" try again after 30 sec!!!!")
                break

    elif choice==9:
        print("EXIT :")
        break

    else:
        print("INVALID CHOICE PLEASE TRY AGAIN .")

