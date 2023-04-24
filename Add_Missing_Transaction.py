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


# This Function is For Create CSV --------------------
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

# This Function is for Upload File -----------------------
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

#This Function is For Delete Contribution ------------------------
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


# Create csv File recursivelly when file uploaded
def createCSV_recurssively(filename,header,data,requestId,recursiveCounter):
        filename = filename + str(recursiveCounter)
        with open(str(os.path.join(CREATE_PATH,filename))+'.csv', mode='w', newline='', encoding='cp1252') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            counter = 0
            requestId = requestId
            for row in data:
                if any(row) and counter > 0:  #Check here if row is blank or not and skip the first row
                    if row[1] == requestId:
                        writer.writerow(row)
                counter += 1

#This Funtion is for Create Csv file from existing File ---------------------
def createCSVFromFile():
    contrId  = input('Please Enter contr ID\n')
    nameOfRep = input('Please Enter the name of REP\n')
    email = input('Please Enter the email\n')
    header = ['Add Missing Transcation',f'update contr ID {contrId}',nameOfRep,email]
    print('Please Upload CSV File\n')
    time.sleep(1)
    try:
        filepath = filedialog.askopenfilename(parent=root)
        file_name = str(filepath).split('/')
        if len(file_name[-1]) == 2 or len(file_name[-1]) == '2': #Check if file selected or not
            raise 'File Not Selected'
        yesOrNo = input(f'You selected this file "{file_name[-1]}"\n1.Confirm and 2.Cancel\n')
        if not yesOrNo == '1' or  yesOrNo=='Confirm' or yesOrNo == 'confirm':
            sys.exit('Thank You For Using')
    except:
        sys.exit('Error:Source Not Found')

    #read_csv Here
    try:
        with open(filepath,'r') as file:
            reader = csv.reader(file)
            data = list(reader)
    except:
        sys.exit('Error:Please Select Correct CSV File Formate')
    
    #write_csv here
    filename = input('Please Enter The new CSV File Name\n')
    try:
        with open(str(os.path.join(CREATE_PATH,filename))+'.csv', mode='w', newline='', encoding='cp1252') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            counter = 0
            recursiveCounter = 1
            # requestId = None
            requestId = contrId 
            uniqueRequestIds = []
            for row in data:
                if counter > 0 and requestId is None:
                    requestId = row[1]
                if any(row) and counter > 0:  #Check here if row is blank or not and skip the first row
                    if row[1] == requestId:
                        writer.writerow(row)
                    else:
                        if row[1] not in uniqueRequestIds:
                            header = ['Add Missing Transcation',f'update contr ID {row[1]}',nameOfRep,email]
                            createCSV_recurssively(filename=filename, header=header,data=data,requestId=row[1],recursiveCounter = recursiveCounter)
                        uniqueRequestIds.append(row[1])
                        recursiveCounter += 1
                counter += 1
        print("Your file has been created successfully:\n\n")
    except:
        sys.exit("Error:Something Went Wrong,Can't write new csv file\n\n")

    #**************************  Main Code started from here ******************   

def mainCode(var_opt):
    if var_opt == 1 or var_opt == '1':
        is_confirm = input(
            "You choose for Add Missing Transaction opration?\nYes or No\n")
        if is_confirm == 'Yes' or is_confirm == 'yes' or is_confirm == 'YES' or is_confirm == 1 or is_confirm == '1':
            createOrupdate = input("1.Create CSV and   2.Upload CSV   3.Create CSV From REP provided file\n")

            #Create_Csv
            if createOrupdate == 1 or createOrupdate == '1' or createOrupdate == 'create' or createOrupdate == 'Create':
                head = ['Account Id', 'Request Id', 'Request Date', 'From Account',
                        'Asset Source', 'Symbol', 'Quantity', 'Approx Value']
                value = [input(f'Please enter {item} value\n')
                         for item in head]
                filename = input('\n\nPlease Enter the CSV File name\n')
                createCsv(headlist=head, valuelist=value, filename=filename)
                
            #Upload_Csv
            elif createOrupdate == 2 or createOrupdate == '2' or createOrupdate == 'Upload Csv' or createOrupdate == 'upload':
                uploadCsv()

            #Create_Csv_with_New_File
            elif createOrupdate == 3 or createOrupdate == '3':
                createCSVFromFile()

            else:
                print('Something went wrong,Please try again.')
        elif is_confirm == 'No' or is_confirm == 'no' or is_confirm == 2 or is_confirm == '2':
            print('Thank you For Using')
        else:
            print('Something went wrong,Please try again.')
    
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