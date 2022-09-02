import mysql.connector
import pyttsx3
import pickle
import datetime

mydb=mysql.connector.connect(user='root',passwd='9415',host='localhost',auth_plugin='mysql_native_password',database="BankDB")

mycursor=mydb.cursor (buffered=True)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

hour=int(datetime.datetime.now().hour)

def wishMe(hour):
    if hour<12:
        speak("good morning Sir")
        print("Good Morning Sir")

    elif hour>=12 and hour<17:
        speak("good Afternoon sir")
        print("Good Afternoon Sir")

    else:
        speak("good evening sir")
        print("Good Evening Sir")

wishMe(hour)

speak("enter your Username to login")
userName = input("Username: ") 
speak("enter your password to login")
password = input("Password: ")

count = 0 
count += 1 

while userName == userName and password == password: 
    if count == 5: 
        print("user does not exist") 
        speak("user does not exist")
        speak("goodbye")
        quit()

    elif userName == 'trigun' and password == '9415': 
        print("Welcome trigun ") 
        speak("welcome tregoon")
        break 
    
    elif userName == 'trigun' and password != '9415': 
        print("Your  Password is wrong!") 
        speak("Your  Password is wrong!") 
        speak("enter your Username again")
        userName = input("\n\nUsername: ") 
        speak("enter your password to login")
        password = input("Password: ") 
        count += 1 
        continue 

    elif userName == 'privanshu' and password == 'mprivanshu': 
        print("Welcome privanshu ") 
        speak("welcome privanshu")
        break
    
    elif userName == 'privanshu' and password != 'mprivanshu': 
        print("Your Password is wrong!") 
        speak("Your  Password is wrong!") 
        speak("enter your Username again")
        userName = input("\n\nUsername: ")
        speak("enter your password to login") 
        password = input("Password: ") 
        count += 1 
        continue 
  
    elif userName == 'shashwat' and password == 'shashwat': 
        print("Welcome shashwat ") 
        speak("welcome shashwat")
        break

    elif userName == 'shashwat' and password != 'shashwat':
        print("Your Password is wrong!")
        speak("Your  Password is wrong!")  
        speak("enter your Username again")
        userName = input("\n\nUsername: ")
        speak("enter your password to login") 
        password = input("Password: ") 
        count += 1
        continue 

    elif userName !=[ 'shashwat' , 'privanshu' , 'trigun' ]:
        print("Your Username is wrong!")
        speak("Your  Username is wrong!")  
        speak("enter your Username again")
        userName = input("\n\nUsername: ")
        speak("enter your password to login") 
        password = input("Password: ") 
        count += 1
        continue 


def Menu():
    print("*"*155) 
    print("MAIN MENU".center(140))
    speak("welcome to main menu")
    print("1. Insert Record/Records".center(140))
    speak("first Insert Record")
    print("2. Display Records as per Account Number".center(140))
    speak("second Display Records as per Account Number ")
    print("   a. Sorted as per Account Number".center(140))
    speak(" a Sorted as per Account Number")
    print("   b. Sorted as per Customer Name".center(140)) 
    speak("b  Sorted as per Customer Name")
    print("   c. Sorted as per Customer Balance".center(140))
    speak("c  Sorted as per Customer Balance")  
    print("3. Search Record Details as per the account number".center(140))
    speak(" third Search Record Details as per the account number")
    print("4. Update Record".center (140))
    speak("fourth Update Record")
    print("5. Delete Record".center (140))
    speak("fifth Delete Record")
    print("6. Transactions Debit/Withdraw from the account".center(140))
    speak("sixth Transactions Debit or Withdraw from the account")
    print("   a.Debit/Withdraw from the account".center (140))
    speak(" a debit")
    print("   b.Credit into the account".center(140))
    speak(" b credit")
    print("7. Exit".center(140))
    speak("seventh exit")
    print("*"*155)


def MenuSort():
    print("   a. Sorted as per Account Number".center(140))
    speak(" a Sorted as per Account Number")
    print("   b. Sorted as per Customer Name".center(140)) 
    speak("b  Sorted as per Customer Name")
    print("   c. Sorted as per Customer Balance".center(140))
    speak("c  Sorted as per Customer Balance")
    print("   d. Back".center (140))
    speak(" d back")


def MenuTransaction():
    print("   a.Debit/Withdraw from the account".center (140))
    speak(" a debit")
    print("   b.Credit into the account".center(140))
    speak(" b credit")
    print("   c. Back".center (140))
    speak(" c back")


def Create():
    try:
        mycursor.execute('create table bank_2(ACC_NO bigint(15) primary key, NAME varchar(20),MOBILE bigint(15),EMAIL varchar(40),ADDRESS varchar(30),CITY varchar(20),COUNTRY varchar(20),BALANCE bigint(15)')
        print("Table Created")
        speak("Table Created")
        Insert()

    except:
        Insert()


def Insert():
            while True:        
                speak("Enter account number")
                ACC_NO=int(input("Enter account no:"))   
                speak("Enter Name")        
                NAME=input("Enter Name:")
                speak("Enter Mobile Number")
                MOBILE=int(input("Enter Mobile Number:"))
                speak("Enter Email")
                EMAIL=input("Enter Email:")
                speak("Enter Address")
                ADDRESS=input("Enter Address:")
                speak("Enter City")
                CITY=input("Enter City:")
                speak("Enter Country")
                COUNTRY=input("Enter Country:")
                speak("Enter Balance")
                BALANCE=int(input("Enter Balance:"))             
                Rec=[ACC_NO,NAME,MOBILE,EMAIL,ADDRESS,CITY,COUNTRY,BALANCE]
                Cmd="insert into bank_2 values (%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(Cmd, Rec)
                mydb.commit()
                speak("Do you want to enter more records")
                ch=input("Do you want to enter more records(n/y): ")
                if ch=='N' or ch=='n':
                    break


def DispSortAcc():      
    try:                                 
        cmd="select*from bank_2 order by ACC_NO"
        mycursor.execute(cmd)
        F="%10s %17s %15s %22s %25s %14s %11s %15s"
        print(F % ("ACC_NO", "NAME", "MOBILE", "EMAIL "," ADDRESS", "CITY", "COUNTRY", "BALANCE"))
        print("="*155)
        for i in mycursor:
            G="%13s %15s %15s %30s %20s %10s %10s %15s"
            print(G%i)
        print("="*155)

    except:
         print("Table doesn't exist")
         speak("Table doesn't exist")


def DispSortName():                                                                    
    try:
       cmd="select * from bank_2 order by NAME"
       mycursor.execute(cmd)
       F="%10s %17s %15s %22s %25s %14s %11s %15s"
       print(F % ("ACC_NO", "NAME", "MOBILE","EMAIL", " ADDRESS", "CITY", "COUNTRY", "BALANCE"))
       print("="*155)
       for i in mycursor:
           G="%13s %15s %15s %30s %20s %10s %10s %15s"
           print(G%i)
       print("="*155)

    except:
        print("Table doesn't exist")
        speak("Table doesn't exist")


def DispSortBal():
    try:
       cmd="select * from bank_2 order by BALANCE"
       mycursor.execute(cmd)
       F="%10s %17s %15s %22s %25s %14s %11s %15s"
       print(F % ("ACC_NO","NAME","MOBILE","EMAIL","ADDRESSS","CITY","COUNTRY","BALANCE"))
       print("="*155)
       for i in mycursor:
           G="%13s %15s %15s %30s %20s %10s %10s %15s"
           print(G%i)
       print("="*155)

    except:
        print("Table dosen't exist")
        speak("Table doesn't exist")


def DispSearchAcc():
    try:
        cmd="select*from bank_2"
        mycursor.execute(cmd)
        ch=int(input("Enter the account_no to be searched: "))
        for i in mycursor:
            if  i[0]==ch:
                print("="*155)
                F="%10s %17s %15s %22s %25s %14s %11s %15s"
                print(F % ("ACC_NO", "NAME", "MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
                print("="*125)
                G="%13s %15s %15s %30s %20s %10s %10s %15s"
                print(G%i)
                break
        else :
            print("Record Not found")
            speak("Record Not found")

    except :
        print ("Table doesn't exist")
        speak("Table doesn't exist")


def Update():                                                                           
    try:
        cmd="select * from bank_2"
        mycursor.execute(cmd)
        speak("Enter the account number whose details to be changed")
        A=int(input("Enter the account_no whose details to be changed: "))
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                speak("do you want to Change Name yes or no ")
                ch=input("Change Name (Y/N) : ")
                if ch=='y' or ch=='Y':
                    speak("enter name")
                    i[1]=input("Enter Name: ")
                    i[1]=i[1].upper()

                speak("do you want to Change Mobile yes or no")
                ch=input("Change Mobile(Y/N): ")                
                if ch=='y' or ch=='Y':
                    speak("enter mobile number")
                    i[2]=int(input("Enter Mobile: "))

                speak("do you want to Change email yes or no")
                ch=input("Change Email(Y/N): ")
                if ch=='y' or ch=='Y':
                    speak("enter email address")
                    i[3]=input("Enter email: ")
                    i[3]=i[3].upper()

                speak("do you want to Change address yes or no")
                ch=input("Change Address (Y/N): " )
                if ch=='y' or ch=='Y':
                    speak("enter address")
                    i[4]=input("Enter Address:  ")
                    i[4]=i[4].upper()
                    
                speak("do you want to Change email yes or no")
                ch=input("Change city(Y/N): ")
                if ch=='y' or ch=='Y':
                    speak("enter city")
                    i[5]=input("Enter City: ")
                    i[5]=i[5].upper()
                    
                speak("do you want to Change country yes or no")
                ch=input("Change Country (Y/N): ")
                if ch=='y' or ch=='Y':
                    speak("enter country")
                    i[6]=input("Enter country: ")
                    i[6]=i[6]. upper()
                    
                speak("do you want to Change balance yes or no")
                ch=input("Change Balance(Y/N): ")
                if ch=='y' or ch=='Y':
                    speak("enter balance")
                    i[7]=int(input("Enter Balance: "))
                cmd="UPDATE bank_2 SET NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s WHERE ACC_NO=%s"
                val=(i[1], i[2],i[3], i[4], i[5],i[6], i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Updated")
                speak("Account Updated")
                break

        else:
            print("Record not found")
            speak("Record Not found")

    except:
        print("No such table")
        speak("No such Table")


def Delete():                                                                           
    try:
        cmd="select * from bank_2"
        mycursor.execute(cmd)
        speak("Enter the account number whose details to be changed")
        A=int(input("Enter the account_no whose details to be changed:"))
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                cmd="delete from bank_2 where ACC_NO=%s"
                val=(i[0],)
                mycursor.execute(cmd, val)
                mydb.commit()
                print ("Account Deleted")
                speak("Account Deleted")
                break

        else:
            print( "Record not found")
            speak("Record Not found")

    except:
        print("No such Table")
        speak("No such Table")


def Debit():                                                                            
    try:
        cmd="select * from bank_2"
        mycursor.execute(cmd)
        print("Please Note that the money can only be debited if min balance of Rs 5000 exists")
        speak("Please Note that the money can only be debited if min balance of Rs 5000 exists")
        acc=int(input("Enter the account no from which the money is to be debited: "))
        
        for i in mycursor:
            i=list(i)
            if i[0]==acc:
                speak("Enter the amount to be withdrawn")
                Amt=int(input("Enter the amount to be withdrawn: " ) )                  
                if  (i[7]-Amt)>=5000:
                    i[7]-=Amt
                    cmd="UPDATE bank_2 SET BALANCE=%s WHERE ACC_NO=%s"
                    val=(i[7],i[0])
                    mycursor.execute(cmd,val)
                    mydb.commit()
                    print("Amount Debited") 
                    speak("Amount Debited")
                    break
                else:
                    print("There must be min balance of Rs 5000")
                    speak("There must be min balance of Rs 5000")
                    break
        else:
            print("Record Not found")
            speak("Record Not found")

    except:
        print("Table Doesn't exist")
        speak("Table doesn't exist")


def Credit():                                                                           
    try:
        cmd="select * from bank_2"
        mycursor.execute(cmd)
        speak("Enter the account number from which the money is to be debited")   
        ACC_NO=int(input("Enter the account no from which the money is to be debited: "))
        
        for i in mycursor:
            i=list(i)
            if  i[0]==ACC_NO:
                speak("Enter the amount to be credited")
                Amt=int(input("Enter the amount to be credited: "))
                i[7]+=Amt
                cmd="UPDATE bank_2 SET BALANCE=%s WHERE ACC_NO=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd, val)
                mydb.commit()
                print ("Amount Credited")
                speak("Amount Credited")
                break        
        else:
            print("Record Not found")
            speak("Record Not found")
    
    except:
        print("Table Doesn't exist")
        speak("Table doesn't exist")

while True:
    Menu()
    speak("Enter your Choice")
    ch=input("Enter your Choice: ")
    
    if ch=="1":
        Create()
    
    elif ch=="2":
        while True:
            MenuSort()
            speak("Enter choice ")
            ch1=input("Enter choice a/b/c/d: ")
            if ch1 in ['a', 'A']:
                DispSortAcc()
            elif  ch1 in ['b' , 'B' ]:
                DispSortName()
            elif ch1 in ['c', 'C']:
                DispSortBal()
            elif ch1 in ['d', 'D']:
               print("Back to the main menu : ")
               speak("Back to the main menu")
               break
            else:
                print("invalid choice")
                speak("invalid choice")
    
    elif ch=="3":
        DispSearchAcc()
    
    elif ch=="4":
        Update()
    
    elif ch=="5":
        Delete()
    
    elif ch=="6":
        while True:
            MenuTransaction()
            speak("Enter choice")
            ch1=input("Enter choice a/b/c: ")
            if ch1 in ['a','A']:
                Debit()
            elif ch1 in ['b', 'B']:
                Credit ()
            elif ch1 in ['c', 'C']:
                print("Back to the main menu")
                speak("Back to the main menu")
                break
            else:
                print("Invalid choice")
                speak("Invalid choice")
    
    elif ch=="7":
        print("Exiting...")
        speak("Exiting")
        break
    
    else:
        print("Wrong Choice Entered")
        speak("Wrong Choice Entered")
