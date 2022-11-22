# from cryptography.fernet import Fernet
import sqlite3 
# import pandas as pd

# import re
# key = Fernet.generate_key()
# fernet = Fernet(key)


class User:
    print("WELCOME TO DB BANK")

    def __init__(self):
        self.file = sqlite3.connect("USER.DB")
        self.c = self.file.cursor()
        # sqlquery = "SELECT * FROM USER_TABLE"
        # self.c.execute(sqlquery)
        # data = c.fetchall()
        # for row in data:
        #     df = pd.read_sql_query(sqlquery,self.file)
        #     df.to_csv('output.csv', index = False)

    def CreateAccount(self):
        self.c.execute("""create table if not exists USER_TABLE
            (
                User_ID integer PRIMARY KEY,
                Login_Email text,
                Password text,
                Access_Count integer
            )""")
        email = input("Enter your email address:- ")
        # EMAIL_REGEX = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        letternumb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        key = "TIMEODANSFRBCGHJKLPOUVWXYZ9876543210"
        password = input("Enter your Password:- ")
        self.result = ""
        for letter in password:
            if letter.upper() in letternumb:
                self.result += key[letternumb.find(letter.upper())]
            else:
                self.result += letter
        print(self.result)
        # encPassword = fernet.encrypt(password.encode())
        # if EMAIL_REGEX.match(email)
        self.accessCount = 0
        self.c.execute(
            'INSERT INTO USER_TABLE (Login_Email, Password, Access_Count) values(?,?,?)', (email, self.result, self.accessCount))
        print("Hello there!! Your Login Email address is {}:- ".format(email),
              "and you can now login.")
        # self.c.execute("select * from USER")
        # print(self.c.fetchall())

        # fun.Login()
        self.file.commit()
        self.file.close()

        return self.result
        # else:
        #     print("Invalid email address, Try Again...!")

    def Login(self):
        emailz = input("Enter your email address:- ")
        in_Password = input("Enter your password:- ")
        check = True
        flag = False
        for a, b, c, d in self.c.execute("select* from USER_TABLE"):
            if (b == emailz) & (c == c):
                flag = True
                check = False
                numCounts = d

        if check:
            print("Invalid Email or Password.")

        if flag:
            numCounts += 1
            self.c.execute(
                "update USER_TABLE set Access_Count = ? where Login_Email = ?", (numCounts, emailz))
            self.file.commit()
            print("Hello {}, this is your login number {}.".format(emailz, numCounts))
            print(emailz)
            print(numCounts)


fun = User()
print("(C)-CreateAccount")
print("(L)-Login")
option = input(
    "What would you like to do today? Create an Account(C) / Already a Customer then LOGIN (L):- ")
if option == 'c' or option == 'C':
    fun.CreateAccount()
if option == 'l' or option == 'L':
    fun.Login()
