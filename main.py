import functions
import filehandling as fi #this is file handling module


print('Monthly Expense Tracker')
while True:
    print('1.Enter Expense\n2.View Expense List\n3.Delete Expense\n4.Download Expense List\n5.Exit')
    userinput = input('Enter Your Choice:  ')
    if userinput == '1':
        functions.Get_Enpense()
    elif userinput == '2':
        functions.View_Expense_List()
    elif userinput == '3':
        functions.Delete_Expense()
    elif userinput == '4':
        fi.Download_Expense()
    elif userinput == '5':
        print('you are logged out..thank you')
        quit()
    else:
        print('invalid input')



