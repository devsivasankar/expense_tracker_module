import functions as fun



def Download_Expense():
    if not fun.database:
        print('no data availabe here you cant download')
    else:
        filename = input('enter file name whaterver you want:  ')
        extension = input('enter extension whaterver you want: ')
        fullname = f'{filename}.{extension}'
        try:
            with open(fullname,mode='x+') as file:
                file.write('mohtly expense tracker\n')
                file.write('id\t\tDate\t\tDescription\t\tAmount\n')
                file.write('-'*70)
                for datas in fun.database:
                    file.write(f"\n{datas['id']:<25}{datas['date']:<25}{datas['description']:<25}{datas['amount']}\n")
                file.write(f"Total : {fun.total_amount:<50}")
        except FileExistsError:
            print('this filename is already exist give other name.')




