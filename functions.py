database = []
data = {}
total_amount = 0
id = 0

def Get_Enpense():
    while True:
        global total_amount,id
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
                print('your expense added succussfully')
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
        print(f"Total : {total_amount:<50}")




def Delete_Expense():
    global total_amount
    if not database:
        print('no items here to delete')
    else:
        del_id = int(input('enter a id to be delete:  '))
        for items in database:
            if del_id == items['id']:
                database.remove(items)
                total_amount -= items['amount']
                print('items deleted successfully')
            else:
                print('no such data available here')



