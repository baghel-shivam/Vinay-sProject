import os
import csv
from tkinter import filedialog
from tkinter import Tk
import shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'source')
UPLOAD_PATH = os.path.join(ROOT_DIR, 'destination')
root = Tk()
root.withdraw()

# This Function is For Create CSV
def createCsv(headlist, valuelist, filename=None):
    if filename is None:
        filename = 'Csv'
    selectPath = filedialog.askdirectory(parent=root)
    with open(str(os.path.join(selectPath, filename))+'.csv', mode='w', newline='\n', encoding='cp1252') as file:
        writer = csv.writer(file)
        writer.writerow(headlist)
        writer.writerow(valuelist)
    print("Success:")
    file.close()

# This Function is for Upload Function
def uploadCsv(sourcePath):
    try:
        source = sourcePath
    except:
        print('Error:Source Not Found')
    input('Press Enter for choose destination')
    try:
        destination = filedialog.askdirectory(parent=root)
    except:
        destination = UPLOAD_PATH
    shutil.move(source, destination)
    print("Success:")


def mainCode(var_opt):
    if var_opt == 1 or var_opt == '1':
        is_confirm = input(
            "You choose for Add Missing Transaction opration?\nYes or No\n")
        if is_confirm == 'Yes' or is_confirm == 'yes' or is_confirm == 1 or is_confirm == '1':
            createOrupdate = input("1.Create CSV and 2.Upload CSV\n")
            # Create Csv
            if createOrupdate == 1 or createOrupdate == '1' or createOrupdate == 'create' or createOrupdate == 'Create':
                head = ['Account Id', 'Request Id', 'Request Date', 'From Account',
                        'Asset Source', 'Symbol', 'Quantity', 'Approx Value']
                value = [input(f'Please enter {item} value\n')
                         for item in head]
                filename = input('\n\n\nPlease Enter the CSV File name\n')
                createCsv(headlist=head, valuelist=value, filename=filename)
            # Upload Csv
            elif createOrupdate == 2 or createOrupdate == '2' or createOrupdate == 'Upload Csv' or createOrupdate == 'upload':
                filepath = filedialog.askopenfilename(parent=root)
                uploadCsv(sourcePath=filepath)

        elif is_confirm == 'No' or is_confirm == 'no' or is_confirm == 2 or is_confirm == '2':
            print('Thank you For Using')
        else:
            print('Please Try Again')

    elif var_opt == 2 or var_opt == '2':
        is_confirm = input(
            "You choose for Delete Contribution opration?\nYes or No\n")
        if is_confirm == 'Yes' or is_confirm == 'yes' or is_confirm == 1 or is_confirm == '1':
            head = ['Contribution Id', 'Email Id']
            value = [input(f'Please enter {item} value\n') for item in head]
            filename = input('\n\n\nPlease Enter the CSV File name\n')
            createCsv(headlist=head, valuelist=value, filename=filename)

        else:
            print('Thank you For Using')


if __name__ == '__main__':
    while True:
        print("Choose any one number for oprations")
        var_opt = input(
            '1.Add Missing Transaction \n2.Delete Contribution\n3.Exit\n')
        if var_opt == 3 or var_opt == '3' or var_opt == 'Exit' or var_opt == 'exit':
            break
        mainCode(var_opt=var_opt)
