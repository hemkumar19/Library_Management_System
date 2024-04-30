import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from datetime import date
from PyQt5.QtCore import QDate
import random
import mysql.connector
class Welcome(QDialog):
    def __init__(self):
        super(Welcome, self).__init__()
        loadUi("welcome.ui",self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = Create()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui",self)
        global num1 
        num1 = int(random.randint(1, 100000))  # Generate a random number for comparison
        self.lineEdit1.setText(str(num1))
        self.create_id_back.clicked.connect(self.create_id)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
        self.verify.clicked.connect(self.verify_btn)
    
    def create_id(self):
        widget.removeWidget(widget.currentWidget())      

    def verify_btn(self):
        try:
            num2 = int(self.lineEdit2.text())  # Get the user's input (second number)
            if num1 == num2:  # Compare the first number with the user's input
                self.label_5.setText("Match! First number equals second number.")
                return True
            else:
                self.label_5.setText("No match! First number doesn't equal second number.")
                return False
        except ValueError:
            self.label_5.setText("Invalid input. Please enter a number.")

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        

        if len(user)==0 or len(password)==0:
            self.error.setText("Please input all fields.")

        else:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="library")
            cursor = connection.cursor()
            query = 'SELECT password FROM login WHERE username = %s'
            cursor.execute(query, (user,))
            result_pass = cursor.fetchone()
            if ( result_pass and result_pass[0] == password) and (True == self.verify_btn()):
                print("Successfully logged in.")

                Home()
            else:
                self.error.setText("Invalid username or password")


class Create(QDialog):  
    def __init__(self):
        super(Create, self).__init__()
        loadUi("create.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)
        self.login_id.clicked.connect(self.login_idf)
    
    def login_idf(self):
        widget.removeWidget(widget.currentWidget())      

    def signupfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error.setText("Please fill in all inputs.")

        elif password!=confirmpassword:
            self.error.setText("Passwords do not match.")
        else:
            try:
                connection = mysql.connector.connect(host="localhost", user="root", password="", database="library")
                cursor = connection.cursor()
                login = (user, password) 
                cursor.execute('INSERT INTO login (username, password) VALUES (%s, %s)', login)

                connection.commit()
                connection.close()
                print("Signup successful.")  
                welcome.gotologin()
            except mysql.connector.Error as err:
                print("Error:", err)


class Logout(QDialog):
    def __init__(self):
        super(Logout, self).__init__()

    def logout(self):
        widget.removeWidget(widget.currentWidget())

class Home(QDialog):
    def __init__(self):
        super(Home, self).__init__()
        loadUi("home.ui", self)
        widget.addWidget(self)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        self.student.clicked.connect(self.gotoAddStudent)
        self.book.clicked.connect(self.gotoAddBook)
        self.issue.clicked.connect(self.gotoIssueBook)
        self.return_2.clicked.connect(self.gotoReturnBook)
        self.statics.clicked.connect(self.gotoStatic)
        self.logout.clicked.connect(self.logout_btn)

    def logout_btn(self):
        # self.close()
        logout = Logout()
        widget.addWidget(logout)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
             

    def gotoAddStudent(self):
        addStudent = AddStudent()
        widget.addWidget(addStudent)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoAddBook(self):
        addBook = AddBook()
        widget.addWidget(addBook)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoIssueBook(self):
        issueBook = IssueBook()
        widget.addWidget(issueBook)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoReturnBook(self):
        returnBook = ReturnBook()
        widget.addWidget(returnBook)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoStatic(self):
        static = Static()
        widget.addWidget(static)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        
    def open_next_page(self):
        pass


class AddStudent(QDialog):  
    def __init__(self):
        super(AddStudent, self).__init__()
        loadUi("student.ui",self)
        self.sback.clicked.connect(self.sback_btn)
        self.sadd.clicked.connect(self.add)
        self.scm1.addItem("MCA")
        self.scm1.addItem("MBA")
        self.scm1.addItem("CS")
        self.scm1.addItem("B.Tech")

        self.scm2.addItem("Computer Applicatin")
        self.scm2.addItem("Computer Scince")
        self.scm2.addItem("Management")
        self.scm2.addItem("Machanical")
        self.scm2.addItem("Electrical")
        self.scm2.addItem("Civil")

        self.scm3.addItem("First Year")
        self.scm3.addItem("Second Year")
        self.scm3.addItem("Third Year")
        self.scm3.addItem("Fourth Year")

        self.scm4.addItem("First Semester")
        self.scm4.addItem("Second Semester")
        self.scm4.addItem("Third Semester")
        self.scm4.addItem("Fourth Semester")
        self.scm4.addItem("Fifth Semester")
        self.scm4.addItem("Six Semester")
        self.scm4.addItem("Seven Semester")
        self.scm4.addItem("Eighth Semester")


    def sback_btn(self):
        Home()


    def add(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="",database="library")
        try:
            if connection.is_connected():
                print("Connected successfully") 
                cursor = connection.cursor()
                id = self.st1.text()
                name = self.st2.text()
                fathername = self.st3.text()
                course = self.scm1.currentText()
                branch = self.scm2.currentText()
                year = self.scm3.currentText()
                semester = self.scm4.currentText()

                query = " INSERT INTO user(id,name,fathername,course,branch,year,semester)VALUE(%s,%s,%s,%s,%s,%s,%s)"
                value = (id,name,fathername,course,branch,year,semester)
                cursor.execute(query, value)
                connection.commit()
                cursor.close()
            else:
                print("Failed to connect")

        except mysql.connector.Error as error:
            print("Error:", error)
        finally:    
            connection.close()    

class AddBook(QDialog):  
    def __init__(self):
        super(AddBook, self).__init__()
        loadUi("book.ui",self) 
        self.badd.clicked.connect(self.add_btn)
        self.bback.clicked.connect(self.bback_btn)

        self.bcm1.addItem("New Edition")
        self.bcm1.addItem("Frist Edition")
        self.bcm1.addItem("Second Edition")
        self.bcm1.addItem("Third Edition")
        self.bcm1.addItem("Forth Edition")
        self.bcm1.addItem("Fifth Edition")
        self.bcm1.addItem("Six Edition")
        self.bcm1.addItem("Seventh Edition")
        self.bcm1.addItem("Eighth Edition")       

    def bback_btn(self):
        Home()

    def add_btn(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="",database="library")
        try:
            if connection.is_connected():
                print("Connected successfully") 
                cursor = connection.cursor()
                id = self.bt1.text()
                title = self.bt2.text()
                edition = self.bcm1.currentText()
                author = self.bt3.text()
                publish = self.bt4.text()
                price = self.bt5.text()
                page = self.bt6.text()
                query = " INSERT INTO book(id,title,edition,author,publish,price,page)VALUE(%s,%s,%s,%s,%s,%s,%s)"
                value = (id,title,edition,author,publish,price,page)
                cursor.execute(query, value)
                connection.commit()
                cursor.close()
            else:
                print("Failed to connect")

        except mysql.connector.Error as error:
            print("Error:", error)
        finally:    
            connection.close()


class IssueBook(QDialog):
    def __init__(self):
        super(IssueBook, self).__init__()
        loadUi("issue.ui", self)
        global current_date 
        current_date = QDate.currentDate()  # Get the current date
        self.idate.setDate(current_date)    # Set the date in the QDateEdit widget
        self.issue_book_search.clicked.connect(self.issuebook_search)
        self.issue_student_search.clicked.connect(self.issuestudent_search)
        self.issuebook_btn.clicked.connect(self.issue_btn)
        self.issue_back_btn.clicked.connect(self.issueback)

    def issueback(self):
        Home()

    def issuebook_search(self):
        book = self.bt1.text()
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="library")
            if connection.is_connected():
                print("Connected successfully")
                cursor = connection.cursor()
                query = "SELECT * FROM `book` WHERE id = "+ book
                cursor.execute(query)
                results = cursor.fetchall()
                for row in results:
                    print(row) 
                    id = row[0] 
                    title = row[1]
                    edition = row[2]
                    author = row[3]
                    publisher = row[4]
                    price = row[5]
                    page = row[6]
                    self.bt1.setText(str(id))
                    self.bt2.setText(title)
                    self.bt3.setText(edition)
                    self.bt4.setText(author)
                    self.bt5.setText(publisher)
                    self.bt6.setText(str(price))
                    self.bt7.setText(str(page))
            else:
                print("Failed to connect")  
        except mysql.connector.Error as error:
            print("Error:", error)
        finally:
            if 'connection' in locals():
                connection.close()
    def issuestudent_search(self):
        user = self.st1.text()
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="library")
            if connection.is_connected():
                print("Connected successfully")
                cursor = connection.cursor()
                query = "SELECT * FROM `user` WHERE id = "+ user
                cursor.execute(query)
                results = cursor.fetchall()
                if results:
                        # If a record is found, populate the text fields with its details
                        id, name, fathername, course, branch, year, semester = results[0]
                        self.st1.setText(str(id))
                        self.st2.setText(name)
                        self.st3.setText(fathername)
                        self.st4.setText(course)
                        self.st5.setText(branch)
                        self.st6.setText(year)
                        self.st7.setText(semester)
                else:
                        self.st1.clear()
                        self.st2.clear()
                        self.st3.clear()
                        self.st4.clear()
                        self.st5.clear()
                        self.st6.clear()
                        self.st7.clear()
            else:
                print("Failed to connect")  
        except mysql.connector.Error as error:
            print("Error:", error)
        finally:
            if 'connection' in locals():
                connection.close()


    def issue_btn(self):
        ######################
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="library")
        print("Connected successfully")
        cursor = connection.cursor()
        query = "SELECT * FROM `issue` WHERE stdid = "+ self.st1.text()
        cursor.execute(query)
        result = len(cursor.fetchall())
        print(result)

        if(result <= 4):   
        ######################
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="library")
            try:
                if connection.is_connected():
                    print("Connected successfully") 
                    cursor = connection.cursor()
                    bookid = self.bt1.text()
                    title = self.bt2.text()
                    edition = self.bt3.text()
                    author = self.bt4.text()
                    publish = self.bt5.text()
                    price = self.bt6.text()
                    page = self.bt7.text()
                    stdid = self.st1.text()
                    name = self.st2.text()
                    fathername = self.st3.text()
                    course = self.st4.text()
                    branch = self.st5.text()
                    year = self.st6.text()
                    semester = self.st7.text()
                    date = self.idate.date().toString("yyyy-MM-dd")
                    #    idate = self.idate.date().toString("yyyy-MM-dd")
                    query = "INSERT INTO `issue` (bookid,title,edition,author,publish,price,page,stdid,name,fathername,course,branch,year,semester,date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    value = (bookid,title,edition,author,publish,price,page,stdid,name,fathername,course,branch,year,semester,date)
                    cursor.execute(query, value)
                    connection.commit()
                    cursor.close()
                else:
                    print("Failed to connect")

            except mysql.connector.Error as error:
                print("Error:", error)
            finally:    
                connection.close()
        else:
            self.msg_l.setText("More than 5 book not issued Plese return some book !")


class ReturnBook(QDialog):
    def __init__(self):
        super(ReturnBook, self).__init__()
        loadUi("return.ui", self)
        global current_date 
        # global current_date
        global a, b, c, d, e,bookids,stdids ,day , date

        # Initialize global variables (you can replace these with actual values)
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.bookids = 0
        self.stdids = 0 
        self.day = 0
        self.date = 0
        current_date = QDate.currentDate()  # Get the current date
        self.rdate.setDate(current_date)    # Set the date in the QDateEdit widget
        self.static_search.clicked.connect(self.std_search)
        self.return_back.clicked.connect(self.returnback)
        self.returnbook_btn_2.clicked.connect(self.return_btn)
        self.pay_btn.clicked.connect(self.pay)
        price = self.day * 5 ;
        self.latefess.setText(str(price)) 
       #Create checkboxes and connect their stateChanged signals
        self.create_checkboxes()
    def return_btn(self):
        if ((self.bookids != 0 and self.stdids != 0 )and(self.day >= 0 and self.day <= 30)):
             # Assuming self.pay is a QLineEdit
            ######################
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="library")
            try:
                if connection.is_connected():
                    print("Connected successfully") 
                    cursor = connection.cursor()
                    #UPDATE `issue` SET `pdate`='date' WHERE `bookid` ='bookid' and `stdid` = 'stdid'
                    #    idate = self.idate.date().toString("yyyy-MM-dd")
                    query = "DELETE FROM `issue` WHERE  `date` = %s AND `bookid` = %s AND `stdid` = %s"
                    value = (self.date, self.bookids, self.stdids)
                    cursor.execute(query, value)
                    connection.commit()
                    cursor.close()
                    print("return successfully")
                    self.std_search()
                else:
                    print("Failed to connect")
                self.bookids = 0
                self.stdids = 0 
            except mysql.connector.Error as error:
                print("Error:", error)
            finally:    
                connection.close()

        else:
            price = 0 ;
            print(price)
            self.latefess.setText(str(price))  # Assuming self.pay is a QLineEdit


    def create_checkboxes(self):
        checkbox_positions = [
            (45, 530),  # Checkbox 1
            (45, 570),  # Checkbox 2
            (45, 610),  # Checkbox 3
            (45, 650),  # Checkbox 4
            (45, 690),  # Checkbox 5
        ]

        self.checkboxes = []  # Store checkboxes in a list

        for i, (x, y) in enumerate(checkbox_positions):
            checkbox = QCheckBox(f"Check {i + 1}", self)
            checkbox.setGeometry(x, y, 21, 31)
            checkbox.stateChanged.connect(lambda state, num=i + 1: self.on_checkbox_changed(num))
            self.checkboxes.append(checkbox)
   
    def day_calculator(self,birthdate,current_date):
        total_days = (current_date.toJulianDay() - birthdate.toJulianDay())
        if(total_days > 30):
            total_days -= 30
            return total_days
        else:
            return 0
        
    def on_checkbox_changed(self, num):
        if((num == 1)):
            if(num == 1 and (self.a == 0)):
                print(self.bt1.text())
                print(self.bt8.text())
                self.a = num
                birthdate = QDate.fromString(self.bt8.text(), "yyyy-MM-dd")
                self.date = str(self.bt8.text())
                current_date = QDate.currentDate()
                totalday = self.day_calculator(birthdate,current_date)
                self.day = totalday
                ##########Copy bellow rest 4 ###### 
                bt1_text = self.bt1.text()
                if bt1_text:
                    try:
                        self.bookids = int(bt1_text)
                        # Rest of your logic...
                        self.stdids = int(self.st1.text())                
                        price = self.day * 5 ;
                        print(price)
                        self.latefess.setText(str(price)) 
                    except ValueError:
                        print("Invalid input for bookid:", bt1_text)
                else:
                    print("Empty input for bookid")
                # self.bookids = int(self.bt1.text())

                # self.pay(num,totalday,int(self.bt1.text()),int(self.st1.text()))
            else:
                self.a = 0
                self.day = 0
                self.bookids = 0
                self.stdids = 0
                # self.pay(num,0,int(self.bt1.text()),int(self.st1.text()))
        elif(num == 2):
            if(num == 2 and (self.b == 0)):
                print(self.bt1_2.text())
                print(self.bt8_2.text())
                self.b = num
                birthdate = QDate.fromString(self.bt8_2.text(), "yyyy-MM-dd")
                self.date = str(self.bt8_2.text())
                current_date = QDate.currentDate()
                totalday =self.day_calculator(birthdate,current_date)
                self.day = totalday

                bt1_text = self.bt1_2.text()
                if bt1_text:
                    try:
                        self.bookids = int(bt1_text)
                        # Rest of your logic...
                        self.stdids = int(self.st1.text())                
                        price = self.day * 5 ;
                        print(price)
                        self.latefess.setText(str(price)) 
                    except ValueError:
                        print("Invalid input for bookid:", bt1_text)
                else:
                    print("Empty input for bookid")
            else:
                self.b = 0
                self.day = 0
                self.bookids = 0
                self.stdids = 0
        elif(num == 3):
            if(num == 3 and (self.c == 0)):
                print(self.bt1_3.text())
                self.c = num
                birthdate = QDate.fromString(self.bt8_3.text(), "yyyy-MM-dd")
                self.date = str(self.bt8_3.text())
                current_date = QDate.currentDate()
                totalday =self.day_calculator(birthdate,current_date)
                self.day = totalday
                bt1_text = self.bt1_3.text()
                if bt1_text:
                    try:
                        self.bookids = int(bt1_text)
                        # Rest of your logic...
                        self.stdids = int(self.st1.text())                
                        price = self.day * 5 ;
                        print(price)
                        self.latefess.setText(str(price)) 
                    except ValueError:
                        print("Invalid input for bookid:", bt1_text)
                else:
                    print("Empty input for bookid")
            else:
                self.c = 0
                self.day = 0
                self.bookids = 0
                self.stdids = 0
        elif(num == 4):
            if(num == 4 and (self.d == 0)):
                print(self.bt1_4.text())
                self.d = num
                birthdate = QDate.fromString(self.bt8.text(), "yyyy-MM-dd")
                self.date = str(self.bt8_4.text())
                current_date = QDate.currentDate()
                totalday =self.day_calculator(birthdate,current_date)
                self.day = totalday
                bt1_text = self.bt1_4.text()
                if bt1_text:
                    try:
                        self.bookids = int(bt1_text)
                        # Rest of your logic...
                        self.stdids = int(self.st1.text())                
                        price = self.day * 5 ;
                        print(price)
                        self.latefess.setText(str(price)) 
                    except ValueError:
                        print("Invalid input for bookid:", bt1_text)
                else:
                    print("Empty input for bookid")
            else:
                self.d = 0
                self.day = 0
                self.bookids = 0
                self.stdids = 0
        elif(num == 5):
            if(num == 5 and (self.e == 0)):
                print(self.bt1.text())
                self.e = num
                birthdate = QDate.fromString(self.bt8.text(), "yyyy-MM-dd")
                self.date = str(self.bt8_5.text())
                current_date = QDate.currentDate()
                totalday =self.day_calculator(birthdate,current_date)
                self.day = totalday
                bt1_text = self.bt1_5.text()
                if bt1_text:
                    try:
                        self.bookids = int(bt1_text)
                        # Rest of your logic...
                        self.stdids = int(self.st1.text())                
                        price = self.day * 5 ;
                        print(price)
                        self.latefess.setText(str(price)) 
                    except ValueError:
                        print("Invalid input for bookid:", bt1_text)
                else:
                    print("Empty input for bookid")
            else:
                self.e = 0
                self.day = 0
                self.bookids = 0
                self.stdids = 0
        else:
            print("error")

    def returnback(self):
         Home()

    def pay(self):
        if (self.bookids != 0 and self.stdids != 0 and self.day != 0):
             # Assuming self.pay is a QLineEdit
            ######################
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="library")
            try:
                if connection.is_connected():
                    print("Connected successfully") 
                    cursor = connection.cursor()
                    date = self.rdate.date().toString("yyyy-MM-dd")
                    #UPDATE `issue` SET `pdate`='date' WHERE `bookid` ='bookid' and `stdid` = 'stdid'
                    #    idate = self.idate.date().toString("yyyy-MM-dd")
                    query = "UPDATE `issue` SET `date` = %s WHERE `bookid` = %s AND `stdid` = %s"
                    value = (date, self.bookids, self.stdids)
                    cursor.execute(query, value)
                    connection.commit()
                    cursor.close()
                    self.std_search()
                else:
                    print("Failed to connect")
                self.bookids = 0
                self.stdids = 0 
            except mysql.connector.Error as error:
                print("Error:", error)
            finally:    
                connection.close()

        else:
            price = 0 ;
            print(price)
            self.latefess.setText(str(price))  # Assuming self.pay is a QLineEdit

    def std_search(self):
        issue = self.st1.text()

    def std_search(self):
        issue = self.st1.text()
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="library")
            if connection.is_connected():
                print("Connected successfully")
                cursor = connection.cursor()
                #query = "SELECT * FROM `issue`"
                query = "SELECT * FROM `issue` WHERE stdid = "+ issue
                cursor.execute(query)
                results = cursor.fetchall()
                for row in results:
                    print(row) 
                    stdid = row[0] 
                    name = row[1]
                    fathername = row[2]
                    course = row[3]
                    branch = row[4]
                    year = row[5]
                    semester = row[6]
                    self.st1.setText(str(stdid))
                    self.st2.setText(name)
                    self.st3.setText(fathername)
                    self.st4.setText(course)
                    self.st5.setText(branch)
                    self.st6.setText(year)
                    self.st7.setText(semester)

                for i in range(len(results)):
                    res = results
                    for row in res:
                        bookid = row[7] 
                        title = row[8]
                        edition = row[9]
                        author = row[10]
                        publisher = row[11]
                        price = row[12]
                        page = row[13]
                        date = row[14]
                        if(i == 0): 
                            self.bookid1 = bookid
                            self.stdid1 = stdid
                            # self.create_checkboxes(bookid , stdid ,date ,45 ,530)        
                            self.bt1.setText(str(bookid))
                            self.bt2.setText(title)
                            self.bt3.setText(edition)
                            self.bt4.setText(author)
                            self.bt5.setText(publisher)
                            self.bt6.setText(str(price))
                            self.bt7.setText(str(page))
                            self.bt8.setText(date)
                            res.pop(0)
                            break
                        elif(i == 1):
                            self.bt1_2.setText(str(bookid))
                            self.bt2_2.setText(title)
                            self.bt3_2.setText(edition)
                            self.bt4_2.setText(author)
                            self.bt5_2.setText(publisher)
                            self.bt6_2.setText(str(price))
                            self.bt7_2.setText(str(page))
                            self.bt8_2.setText(date) 
                            res.pop(0)
                            break                       
                        elif(i == 2):
                            self.bt1_3.setText(str(bookid))
                            self.bt2_3.setText(title)
                            self.bt3_3.setText(edition)
                            self.bt4_3.setText(author)
                            self.bt5_3.setText(publisher)
                            self.bt6_3.setText(str(price))
                            self.bt7_3.setText(str(page))
                            self.bt8_3.setText(date)   
                            res.pop(0) 
                            break                     
                        elif(i == 3):
                            self.bt1_4.setText(str(bookid))
                            self.bt2_4.setText(title)
                            self.bt3_4.setText(edition)
                            self.bt4_4.setText(author)
                            self.bt5_4.setText(publisher)
                            self.bt6_4.setText(str(price))
                            self.bt7_4.setText(str(page))
                            self.bt8_4.setText(date)   
                            res.pop(0)
                            break                         
                        else:
                            self.bt1_5.setText(str(bookid))
                            self.bt2_5.setText(title)
                            self.bt3_5.setText(edition)
                            self.bt4_5.setText(author)
                            self.bt5_5.setText(publisher)
                            self.bt6_5.setText(str(price))
                            self.bt7_5.setText(str(page))
                            self.bt8_5.setText(date)   
                            res.pop(0)
                            break                     
            else:
                print("Failed to connect")  
        except mysql.connector.Error as error:
            print("Error:", error)
        finally:
            if 'connection' in locals():
                connection.close()

class Static(QDialog):
    def __init__(self):
        super(Static, self).__init__()
        loadUi("static.ui", self)

        self.static_search.clicked.connect(self.search_st)
        self.static_back.clicked.connect(self.slogout)

    def slogout(self):
         Home()
    def search_st(self):
        issue = self.st1.text()
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="", database="library")
            if connection.is_connected():
                print("Connected successfully")
                cursor = connection.cursor()
                query = "SELECT * FROM `issue` WHERE stdid = "+ issue
                cursor.execute(query)
                results = cursor.fetchall()
                for row in results:
                    print(row) 
                    stdid = row[0] 
                    name = row[1]
                    fathername = row[2]
                    course = row[3]
                    # branch = row[4]
                    # year = row[5]
                    # semester = row[6]
                    self.st1.setText(str(stdid))
                    self.st2.setText(name)
                    self.st3.setText(fathername)
                    self.st4.setText(course)
                    # self.st5.setText(branch)
                    # self.st6.setText(year)
                    # self.st7.setText(semester)

                for i in range(len(results)):
                    res = results
                    for row in res:
                        bookid = row[7] 
                        title = row[8]
                        edition = row[9]
                        author = row[10]
                        publisher = row[11]
                        price = row[12]
                        page = row[13]
                        date = row[14]
                        if(i == 0): 
                            self.bookid1 = bookid
                            self.stdid1 = stdid
                            # self.create_checkboxes(bookid , stdid ,date ,45 ,530)        
                            self.bt1.setText(str(bookid))
                            self.bt2.setText(title)
                            self.bt3.setText(edition)
                            self.bt4.setText(author)
                            self.bt5.setText(publisher)
                            self.bt6.setText(str(price))
                            self.bt7.setText(str(page))
                            self.bt8.setText(date)
                            res.pop(0)
                            break
                        elif(i == 1):
                            self.bt1_2.setText(str(bookid))
                            self.bt2_2.setText(title)
                            self.bt3_2.setText(edition)
                            self.bt4_2.setText(author)
                            self.bt5_2.setText(publisher)
                            self.bt6_2.setText(str(price))
                            self.bt7_2.setText(str(page))
                            self.bt8_2.setText(date) 
                            res.pop(0)
                            break                       
                        elif(i == 2):
                            self.bt1_3.setText(str(bookid))
                            self.bt2_3.setText(title)
                            self.bt3_3.setText(edition)
                            self.bt4_3.setText(author)
                            self.bt5_3.setText(publisher)
                            self.bt6_3.setText(str(price))
                            self.bt7_3.setText(str(page))
                            self.bt8_3.setText(date)   
                            res.pop(0) 
                            break                     
                        elif(i == 3):
                            self.bt1_4.setText(str(bookid))
                            self.bt2_4.setText(title)
                            self.bt3_4.setText(edition)
                            self.bt4_4.setText(author)
                            self.bt5_4.setText(publisher)
                            self.bt6_4.setText(str(price))
                            self.bt7_4.setText(str(page))
                            self.bt8_4.setText(date)   
                            res.pop(0)
                            break                         
                        else:
                            self.bt1_5.setText(str(bookid))
                            self.bt2_5.setText(title)
                            self.bt3_5.setText(edition)
                            self.bt4_5.setText(author)
                            self.bt5_5.setText(publisher)
                            self.bt6_5.setText(str(price))
                            self.bt7_5.setText(str(page))
                            self.bt8_5.setText(date)   
                            res.pop(0)
                            break 
                
            else:
                print("Failed to connect")  
        except mysql.connector.Error as error:
            print("Error:", error)
        finally:
            if 'connection' in locals():
                connection.close()


app = QApplication(sys.argv)
welcome = Welcome()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
# a = b = c = d = e =0
login = Login()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")