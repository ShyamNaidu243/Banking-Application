import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='root',database='userdetails')
cursor = mydb.cursor()

class Reg:
    #INIT FUNCTION
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.user_name = ""
        self.email_id = ""
        self.phone_number = ""
        self.pass_word = ""
        userName = self.user_name
        passWord = self.pass_word
    #REGISTRATION FUNCTION
    def registration(self):
        #USER INPUTS
        self.first_name = input("Enter your first name : ")
        self.last_name = input("Enter your last name : ")
        self.user_name = input("Enter a user name : ")
        self.email_id = input('Enter your Email id : ')
        self.phone_number = input('Enter your phone number : ')
        self.pass_word = input('Enter your password : ')

        
        #block of code for storing index position of @
        x = 0
        for i in range(len(self.email_id)):
            if self.email_id[i] == '@':
                x = i
                break
        #Variables for storing booleans whether the usera-name and email-id are valid or not
        y = False
        z = False
        #list of all capital letters
        l = [chr(i) for i in range(65, 91)]
        #list of all small letters
        m = [chr(i) for i in range(97, 123)]
        #list of alphanumeric and special characters

        #loops for stating of illegal characters
        for i in range(len(l)):
            if self.user_name[0] in l:
                y = True
            elif self.user_name[0] in m:
                y = True
            else:
                y = False

        for i in range(len(l)):
            if self.email_id[0] in l:
                z = True
            elif self.email_id[0] in m:
                z = True
            else:
                z = False
        #====================================================

        # Password checking
        psn = [chr(i) for i in range(32, 48)]
        psn1 = [chr(i) for i in range(58,65)]
        psn.append('{')
        psn.append('}')
        psn.append('|')
        psn.append('~')
        psn = psn + psn1
        pn = [chr(i) for i in range(48,58)]
        pswd_check = ""
        num = False
        upper = False
        lower = False
        special = False

        for i in self.pass_word:
            if i  in psn:
                special  = True
            elif i  in l:
                upper = True
            elif i  in m :
                lower = True
            elif i  in pn:
                num = True
        if num and upper and lower and special:
            pswd_check =True
        else:
            pswd_check = False
        if self.email_id[0] == '@':
            print('Email should not start with @')
        elif self.user_name[0] == '@':
            print('User Name should not start with @')
        elif "@" not in self.email_id:
            print('email should contain "@"')
        elif '@' not in self.user_name:
            print('User name should contain @')
        elif self.user_name[0] == '@':
            print('User name should not starts with @')
        elif self.email_id[0] == '@':
            print('Email id should not starts with @')
        elif '.' in self.user_name:
            print('User Name  should not contain "."')
        elif '.' not in self.email_id:
            print('Email  should contain "."')
        elif self.user_name[-1] == '@':
            print('User name should not end with @')
        elif self.email_id[-1] == '@':
            print('Email id  should not end with @')
        elif self.email_id[x + 1] == ".":
            print('"." should not appear immediatley after "@"')
        elif (y == False):
            return "User Name should not start with numbers or special characters"
        elif (z == False):
            return 'Email ID should not start with numbers or special characters'
        elif (len(self.pass_word) > 5) and (len(self.pass_word) < 16) == False:
            return 'Password length should be between 6 and 15'
        elif pswd_check != True :
            print("Password Should be combination of Small Letters, Capital Letters, Numbers and Special Characters")
        elif len(self.phone_number) != 10:
            print("Phone number should be 10 digits")
        else:
            ins = 'INSERT INTO registration (first_name , last_name,user_name,email_id,phone_number,pass_word) values(%s,%s,%s,%s,%s,%s)'
            val = (r1.first_name, r1.last_name, r1.user_name, r1.email_id, r1.phone_number, r1.pass_word)
            cursor.execute(ins, val)
            mydb.commit()
            print("================================================================================\n \n")
            print("Registration is Successful. Please proceed to Login")
            print('\n \n================================================================================')
        # print(f"your email is : {email_id} and your phone number is : {phone_number}")

    def login(self ):
        self.username = input("Enter your login user name: ")
        self.password = input("Enter your Password: ")

        login_check = 'select * from registration where user_name = %s and pass_word = %s'
        user_check  = (self.username,self.password)
        cursor.execute(login_check,user_check)
        result = cursor.fetchone()
        if result:
            print("================================================================================\n \n")
            print(f"Login is Successful, Welcome {self.username} !")
            print('\n \n================================================================================')
        else:
            print("================================================================================\n \n")
            print("Username or password is incorrect")
            print('\n \n================================================================================')

    def fpass(self):
        self.users = input("Enter your Username : ")
        u_check = 'select user_name from registration where user_name = %s'
        user_checks = (self.users)
        cursor.execute(u_check, (self.users,))
        res = cursor.fetchone()
        if res:
            self.update_pass = input("Enter your new password : ")
            self.confirm_update_pass = input("Confirm your new password : ")
            if self.update_pass == self.confirm_update_pass :
                update_pass_query = 'update  registration set pass_word = %s where user_name = %s'
                cursor.execute(update_pass_query, (self.update_pass, self.users))
                mydb.commit()
                # pass_word_check = (self.update_pass,self.users)
                # cursor.execute(update_pass_query,pass_word_check)
                print("================================================================================\n \n")
                print("Password is Updated Successfully, please try to login once again")
                print('\n \n================================================================================')
            else:
                print("================================================================================\n \n")
                print("Password Do not match")
                print('\n \n================================================================================')
        else:
            print("================================================================================\n \n")
            print("No such Username exists")
            print('\n \n================================================================================')


r1 = Reg()
cases = int(input("Choose Your action : \n 1)Register \n 2)Login \n 3)Forgot Password \n 4) Exit \n"))

if cases == 1:
    r1.registration()
elif cases == 2:
    r1.login()
elif cases == 3:
    r1.fpass()
else:
    exit()

cursor.close()
mydb.close()