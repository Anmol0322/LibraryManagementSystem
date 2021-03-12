import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", password="root", database="lms")

mycursor = mydb.cursor()

class create:
    def __init__(self,std_name,clg,br,yr,lib,ph):
        self.std_name=std_name
        self.clg=clg
        self.br=br
        self.yr=yr
        self.lib=lib
        self.ph=ph

    def create_acc(self):
        mycursor.execute(f"insert into student(std_name,college,branch,year,library,ph_no)"
                         f"values('{self.std_name}','{self.clg}','{self.br}',"
                         f"{self.yr},'{self.lib}',{self.ph})")
        mydb.commit()
        print("\nAccount Created!!!")
        id=mycursor.lastrowid
        print(f"\nYour id: {id}\nYour name: {self.std_name}")

class select:
    def __init__(self,std_id,ph_no):
        self.std_id=std_id
        self.ph_no=ph_no

    def show_details(self):
        mycursor.execute(f"select * from student where std_id={self.std_id} and ph_no={self.ph_no}")
        record=mycursor.fetchone()
        print("\nStudent Id:",record[0])
        print("Student Name:", record[1])
        print("College:", record[2])
        print("Branch:",record[3])
        print("Year:", record[4])
        print("Library:", record[5])
        print("Phone number:",record[6])

class delete:
    def __init__(self,std_id,ph_no):
        self.std_id=std_id
        self.ph_no=ph_no

    def del_acc(self):
        mycursor.execute(f"delete from student where std_id={self.std_id}")
        mydb.commit()

class update:
    def __init__(self,std_id,ph_no):
        self.std_id=std_id
        self.ph_no=ph_no

    def sname(self, name):
        mycursor.execute(f"update student set std_name='{name}' where std_id={self.std_id} and ph_no={self.ph_no}")
        mydb.commit()

    def college(self,clg):
        mycursor.execute(f"update student set college='{clg}' where std_id={self.std_id} and ph_no={self.ph_no}")
        mydb.commit()

    def branch(self, br):
        mycursor.execute(f"update student set branch='{br}' where std_id={self.std_id} and ph_no={self.ph_no}")
        mydb.commit()

    def year(self, yr):
        mycursor.execute(f"update student set year={yr} where std_id={self.std_id} and ph_no={self.ph_no}")
        mydb.commit()

    def library(self, lib):
        mycursor.execute(f"update student set library='{lib}' where std_id={self.std_id} and ph_no={self.ph_no}")
        mydb.commit()

    def phno(self, ph):
        mycursor.execute(f"update student set ph_no={ph} where std_id={self.std_id}")
        mydb.commit()

class book_i:
    def __init__(self,std_id,ph_no):
        self.std_id=std_id
        self.ph_no=ph_no

    def issue(self,st_id,bk_name,author,isbn):
        mycursor.execute(f"insert into book(std_id,book_name,author,isbn)"
                         f"values({st_id},'{bk_name}','{author}','{isbn}')")
        mydb.commit()
        mycursor.execute(f"select * from book where std_id={self.std_id}")
        record = mycursor.fetchone()
        print("\nStudent Id:", record[0])
        print("Book Name:", record[1])
        print("Author:", record[2])
        print("ISBN:", record[3])

    def up_book(self,std_id):
        mycursor.execute(f"delete from book where std_id={std_id}")
        mydb.commit()

    def sel_book(self):
        mycursor.execute(f"select * from book where std_id={self.std_id}")
        record = mycursor.fetchone()
        print("\nBook Name:", record[1])
        print("Author:", record[2])
        print("ISBN:", record[3])
