import os
import csv
from tkinter import filedialog
from tkinter import Tk
import shutil
import time
import sys
# import mysql.connector

# DESKTOP_LOCATION = os.path.join(os.environ['USERPROFILE'],'Desktop')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CREATE_PATH = os.path.join(ROOT_DIR,'Source')
UPLOAD_PATH = os.path.join(ROOT_DIR, 'destination')
DELETE_PATH = os.path.join(ROOT_DIR, 'deleteContribution')
root = Tk()
root.withdraw()

#This Function is for Connect DB
# def dbConnect(host=None, user=None, password=None, port=None):
#     try:
#         mydb = mysql.connector.connect(
#             host = str(host),
#             user = str(user),
#             password = str(password),
#             port = str(port),
#             database = 'shivamdb',
#         )
#         return mydb
#     except:
#         return 'Something went wrong'

# This Function is For Create CSV

def createCsv(headlist, valuelist, filename=None):
    if filename is None or filename == '':
        filename = 'newcsv'
    if not os.path.exists(CREATE_PATH):
        os.makedirs(CREATE_PATH)
    with open(str(os.path.join(CREATE_PATH,filename))+'.csv', mode='w', newline='\n', encoding='cp1252') as file:
        writer = csv.writer(file)
        writer.writerow(headlist)
        writer.writerow(valuelist)
    print("Your file has been created successfully:\n\n")
    uploadOrNot = input('Do you want to upload file ?\n1.Yes 2.No\n')
    if uploadOrNot == 'YES' or uploadOrNot == '1' or uploadOrNot == 'yes' or uploadOrNot == 'Yes' or uploadOrNot == 1:
        uploadCsv()
    file.close()

# This Function is for Upload Function
def uploadCsv():
    print("Please choose the file")
    time.sleep(1)
    try:
        filepath = filedialog.askopenfilename(parent=root)
        file_name = str(filepath).split('/')
        if file_name[0] =='':
            sys.exit('Error:Source Not Found')
        yesOrNo = input(f'You selected this file "{file_name[-1]}"\n1.Confirm and 2.Cancel\n')
        if not yesOrNo == '1' or  yesOrNo=='Confirm' or yesOrNo == 'confirm':
            sys.exit('Thanx For Using')
    except:
        sys.exit('Error:Source Not Found')
    fileName = input('Please Enter the Folder Name\n')
    if '/' in fileName:
        print("\n'/' is not allowed use '-' instead")
        fileName = input('Please Enter the Folder Name\n')
    actualUploadPath = os.path.join(UPLOAD_PATH,fileName)
    if not os.path.exists(actualUploadPath):
        os.makedirs(actualUploadPath)
    shutil.move(filepath, actualUploadPath)
    print(f"Your file has been placed to this folder 'destination/{fileName}':\n\n")

#This Function is For Delete Contribution
def deleteCsv():
    head = ['Contribution Id', 'Email Id']
    finalList = []
    id = []
    writeRow = ['Delete Contribution']
    removeContrId = 'remove contr ID     '
    first = True
    for headName in head:
        value = input(f'Please enter {headName} value\n')
        finalList.append(value)
        if first:
            first = False
            removeContrId += value
            id.append(value)
            writeRow.append(removeContrId)
        else:
            writeRow.append(value)     
    filename = input('\n\n\nPlease Enter the CSV File name\n')
    if filename is None or filename == '':
        filename = 'newcsv'
    if not os.path.exists(DELETE_PATH):
        os.makedirs(DELETE_PATH)
    with open(str(os.path.join(DELETE_PATH, filename))+'.csv', mode='w', newline='\n', encoding='cp1252') as file:
        writer = csv.writer(file)
        writer.writerow(writeRow)
        writer.writerow(id)
    print("Your file has been placed to the 'deleteContribution' folder:\n\n")
    file.close()

def mainCode(var_opt):
    if var_opt == 1 or var_opt == '1':
        is_confirm = input(
            "You choose for Add Missing Transaction opration?\nYes or No\n")
        if is_confirm == 'Yes' or is_confirm == 'yes' or is_confirm == 'YES' or is_confirm == 1 or is_confirm == '1':
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
                uploadCsv()

        elif is_confirm == 'No' or is_confirm == 'no' or is_confirm == 2 or is_confirm == '2':
            print('Thank you For Using')
        else:
            print('Please Try Again')
    
    # Delete CSV
    elif var_opt == 2 or var_opt == '2':
        is_confirm = input("You choose for Delete Contribution opration?\nYes or No\n")
        if is_confirm == 'Yes' or is_confirm == 'yes' or is_confirm == 1 or is_confirm == '1':
            deleteCsv()
        else:
            print('Please Try Again')

if __name__ == '__main__':
    while True:
        print("Choose any one number for oprations")
        var_opt = input(
            '0.Exit\n1.Add Missing Transaction \n2.Delete Contribution\n')
        if var_opt == 0 or var_opt == '0' or var_opt == 'Exit' or var_opt == 'exit':
            break
        mainCode(var_opt=var_opt)
        
        '''
        # This is for database works
        print("Please Enter the db details for connection\n\n\n")
        host = input("Please Enter the Host\n")
        user = input('Please Enter the User\n')
        password = input('Please Enter the password\n')
        port = input('Please Enter the port\n')
        mydb = dbConnect(host=host,user=user,password=password,port=port)
        print(mydb)
        mycursor  = mydb.cursor()
        mycursor.execute("CREATE TABle newtable (name VARCHAR(300), age VARCHAR(200));")
        
        mycursor.close()
        mydb.close()
        '''