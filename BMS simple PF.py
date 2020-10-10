import os
import time

"""
CREDENTIALS
"""
user = "USERNAME"
submitto = "PROFESSOR"

# CREDENTIALS ENDS HERE

# GLOBAL VARIABLES
# LIST VARIABLES
index = 0
NAME = []
F_NAME = []
ACC_TYPE = []
ACC_NO = []
BALANCE = []
ADDRESS = []

# GLOBAL VARIABLES ENDS HERE

# FUNCTIONS


def create(val):
    n = input("\n enter name : ")
    f = input("\n enter father/husband name : ")
    a_type = input("\n enter account type c/s : ")
    cred = input("\n enter amount min 2000 : ")
    if not cred.isdigit():
        print("\ninvalid entery accoutn creatiion failed ")
        return
    elif(cred < "2000"):
        print("\ninvalid entery account creatiion failed, low amount ")
        return

    address = input("\n enter address : ")
    NAME.insert(index, n)
    F_NAME.insert(index, f)
    ACC_NO.insert(index, val)
    ACC_TYPE.insert(index, a_type)
    BALANCE.insert(index, cred)
    ADDRESS.insert(index, address)
    print("\n\t\tACCOUNT CREATED.....")
    input()



def display(val):
    local_index = ACC_NO.index(val)
    print(F"\n\tNAME           : {NAME[local_index]}")
    print(F"\n\tFATHER NAME    : {F_NAME[local_index]}")
    print(F"\n\tACCOUNT NO     : {ACC_NO[local_index]}")
    print(F"\n\tACCOUNT TYPE   : {ACC_TYPE[local_index]}")
    print(F"\n\tBALANCE        : {BALANCE[local_index]}")
    print(F"\n\tADDRESS        : {BALANCE[local_index]}")
    input()


def deposit(account_no):
    cred = int(input("\nEnter amount to deposit : "))
    if(cred < 100):
        print("\ninvalid entery account creatiion failed, low amount ")
        return
    else:
        ind = ACC_NO.index(account_no)
        sum = int(BALANCE[ind]) + cred
        BALANCE[ind] = sum
        input("\n\tAMOUNT DEPOSITED....")


def widraw(account_no):
    cred = int(input("\nEnter amount to widraw \n min amount could be 500 \n remaining account balance should be more than 1000 : "))
    if (cred < 500):
        print("\ninvalid entery account creatiion failed, low amount ")
        return
    else:
        ind = ACC_NO.index(account_no)
        if(int(BALANCE[ind]) - cred > 1000):
            diff = int(BALANCE[ind]) - cred
            BALANCE[ind] = diff
            input("\n\tAMOUNT WIDRAWED....")
        else:
            print("\naccount balance is low")


def remove(account_no):
    local_index = ACC_NO.index(account_no)
    name = NAME[local_index]
    f = F_NAME[local_index]
    accno = ACC_NO[local_index]
    acct = ACC_TYPE[local_index]
    add = ADDRESS[local_index]
    bal = BALANCE[local_index]
    NAME.remove(name)
    F_NAME.remove(f)
    ACC_NO.remove(accno)
    ACC_TYPE.remove(acct)
    ADDRESS.remove(add)
    BALANCE.remove(bal)
    print("\nACCOUNT REMOVED.....")
    input()
    


def list_accounts():
    i = 0
    for local_account in ACC_NO:
        print(F"\nNAME           : {NAME[i]}\t\t {BALANCE[i]}")
        i = i + 1

def check_for_index(val):                #checks if account no is already existed or not
    for account_no in ACC_NO:
        if(account_no == val):
            return True
    else:
        return False


def welcome():
    print(F"\n\nTHIS PROJECT IS CREATED BY : {user}")   #change username
    print(F"SUBMITTED TO : {submitto}")             #submitted to
    time.sleep(5)                                   #waiting command
    os.system('cls')                                #clear WELCOME SCREEN

# FUNCTIONS ENDS HERE




if __name__ == '__main__':                          #MAIN PROGRAM
 welcome()
 i = True
 while (i):
     print ("\n\n1 : Create an account")
     print ("2 : Display an account")
     print ("3 : Depsoit ")
     print ("4 : Widraw ")
     print ("5 : Remove Account ")
     print ("6 : List of Accounts ")
     print ("7 : Exit ")
     choice = int(input("Enter Your Choice : "))
     if(choice == 1):
         account_no = int(input("enter account no : "))
         BOOL = bool(check_for_index(account_no))
         if (BOOL == False):
             create(account_no)
         else:
             print("ACCOUNT ALREADY CREATED ")
         index = index + 1
     elif (choice == 2):
         account_no = int(input("enter account no : "))
         BOOL = bool(check_for_index(account_no))
         if (BOOL == True):
             display(account_no)

     elif (choice == 3):
         account_no = int(input("enter account no : "))
         BOOL = bool(check_for_index(account_no))
         if (BOOL == True):
             deposit(account_no)
     elif (choice == 4):
         account_no = int(input("enter account no : "))
         BOOL = bool(check_for_index(account_no))
         if (BOOL == True):
             widraw(account_no)
     elif (choice == 5):
         account_no = int(input("enter account no : "))
         BOOL = bool(check_for_index(account_no))
         if (BOOL == True):
             remove(account_no)

     elif (choice == 6):
         list_accounts()
     elif(choice == 7):
        exit(0)
     else:
         print("\n\ninvalid option\n please select from 1-6")
         input()