database = []
data = {}
total_amount = 0
id = 0

def Get_Enpense():
    while True:
        global total_amount
        global id
        id = id + 1
        date = input('Enter Date(yyyy/mm/dd):  ')
        description = input('Enter Item Purchased:  ')
        try:
            amount = float(input('Enter Amount Spent:  '))
            if amount < 0:
                print('Enter Valid Amount')
            else:
                database.append({'id':id,'date':date, 'description':description, 'amount':amount})
                total_amount = amount + total_amount
                break       
        except:
            print('enter valid amount')


def View_Expense_List():
    if not database:
        print('No Datas Available Here')
    else:    
        print('id\t\tDate\t\tDescription\t\tAmount')
        print('-'*70)
        for datas in database:
            print(f"{datas['id']:<15}{datas['date']:<20}{datas['description']:<20}{datas['amount']}")
        print(f"{total_amount:<50}")




def Delete_Expense():
    pass


def Download_Expense():
    pass
    # we need to ask file name from user 
    # ask extension from user
    # then create file and write
