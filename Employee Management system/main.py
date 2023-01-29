from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mc
from tkinter import ttk

conn = mc.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "employee")

cursor=conn.cursor()

print(conn)
createTable = [
    """create table employee(
        eid varchar(3) primary key,
        ename varchar(30) ,
        gender varchar(6) not null,
        age int not null,
        salary int,
        addr varchar(20) not null
    );""",

    """create table dept(
        did varchar(3) primary key,
        dname varchar(10) not null,
        location varchar(10),
        no_of_emp int
    )""",

    """create table works_for(
        eid varchar(3) not null,
        did varchar(3) not null,
        primary key(eid, did),
        foreign key (eid) references employee(eid) on delete cascade,
        foreign key (did) references dept(did) on delete cascade
    )""",

    """create table manages(
        eid varchar(3) not null,
        did varchar(3) not null,
        primary key(eid, did),
        foreign key (eid) references employee(eid) on delete cascade,
        foreign key (did) references dept(did) on delete cascade
    )""",

    """create table project(
        pid varchar(3) primary key,
        pname varchar(10) not null,
        description varchar(20) not null
    )""",

    """create table controls(
        did varchar(3) not null,
        pid varchar(3) not null,
        primary key(did, pid),
        foreign key (did) references dept(did) on delete cascade,
        foreign key (pid) references project(pid) on delete cascade 
    )""",
    """create table works_on(
        eid varchar(3) not null,
        pid varchar(3) not null,
        hours int,
        primary key(eid, pid, hours),
        foreign key (eid) references employee(eid) on delete cascade,
        foreign key (pid) references project(pid) on delete cascade 
    )""",
    """create table dependents(
        dependent_name varchar(10) primary key,
        relationship varchar(10) not null
    )""",
    """create table has(
        eid varchar(3) not null,
        dependent_name varchar(10) not null,
        primary key(eid, dependent_name),
        foreign key (eid) references employee(eid) on delete cascade,
        foreign key (dependent_name) references dependents (dependent_name) on delete cascade
    )"""
]
for i in createTable:
    cursor.execute(i)
insert = [
    """insert into employee values('E01','Sumit','male',20,20,'A-50XYZ')""",
    """insert into employee values('E02','Jessica','female',35,25,'JK-23YY')""",
    """insert into employee values('E03','Rohan','male',29,55,'KN-12FGH')""",
    """insert into employee values('E04','Rohit','male',44,42,'HA-20AQ')""",
    """insert into employee values('E05','Kamala','female',35,510,'QW-90SY')""",
    """insert into employee values('E06','Harry','male',55,150,'TYOY-89')""",
    """insert into employee values('E07','Priyanka','female',30,400,'TNA2Y')""",

    """insert into dept values('D01','HR','Delhi',50)""",
    """insert into dept values('D02','CustServ','Delhi',20)""",
    """insert into dept values('D03','SoftDev','Bangalore',100)""",
    """insert into dept values('D04','Finance','Mumbai',150)""",
    """insert into dept values('D05','DevOps','Pune',35)""",

    """insert into works_for values('E01','D04')""",
    """insert into works_for values('E07','D02')""",
    """insert into works_for values('E03','D01')""",
    """insert into works_for values('E02','D05')""",
    """insert into works_for values('E06','D03')""",
    """insert into works_for values('E04','D05')""",
    """insert into works_for values('E05','D04')""",

    """insert into manages values('E03','D01')""",
    """insert into manages values('E07','D02')""",
    """insert into manages values('E06','D03')""",
    """insert into manages values('E05','D04')""",
    """insert into manages values('E05','D05')""",
    """insert into project values('P01','AppImg','Image Creation for D')""",
    """insert into project values('P02','DockApp','kubernetes container')""",
    """insert into project values('P03','APACStrat','SouthEast Asia Markt')""",
    """insert into project values('P04','Hiring','College Hiring')""",
    """insert into project values('P05','ResPlan','Green Energy')""",

    """insert into works_on values('E02','P01',15)""",
    """insert into works_on values('E04','P01',20)""",
    """insert into works_on values('E06','P02',10)""",
    """insert into works_on values('E05','P03',35)""",
    """insert into works_on values('E03','P04',12)""",
    """insert into works_on values('E01','P05',15)""",

    """insert into controls values('D01','P04')""",
    """insert into controls values('D03','P01')""",
    """insert into controls values('D04','P03')""",
    """insert into controls values('D04','P05')""",
    """insert into controls values('D05','P02')""",

    """insert into dependents values('Ramesh','Father')""",
    """insert into dependents values('Meena','Mother')""",
    """insert into dependents values('Anish','Father')""",
    """insert into dependents values('Anupama','Mother')""",
    """insert into dependents values('Anant','Grandfather')""",

    """insert into has values('E02','Ramesh')""",
    """insert into has values('E02','Meena')""",
    """insert into has values('E04','Anant')""",
    """insert into has values('E06','Anish')""",
    """insert into has values('E06','Anupama')"""
]

for i in insert:
    cursor.execute(i)
conn.commit()

def insert():
    id=e_id.get()
    name=e_name.get()
    gender=e_gender.get()
    age=e_age.get()
    salary=e_salary.get()
    address=e_address.get()

    if(id=="" or name=="" or gender=="" or age=="" or salary=="" or address==""  ):
        MessageBox.showinfo("insert Status", "All Fields are required")
    else:
        cursor.execute("insert into employee values('"+id +"','"+name+"','"+gender+"','"+age+"','"+salary+"','"+address+"')")
        
        
        
        cursor.execute("commit");
        MessageBox.showinfo("Insert Status1", "Inserted Successfully");
        

def insert_dept():
    id=e_id.get()
    dept_id=e_dept_id.get()
    dept=e_dept.get()
    location=e_location.get()
    Employee_no=e_Employee_no.get()

    if(dept_id=="" or dept=="" or location=="" or Employee_no=="" or id==""):
        MessageBox.showinfo("insert Status", "All Fields are required")
    else:
        cursor.execute("insert into dept values('"+dept_id +"','"+dept+"','"+location+"','"+Employee_no+"')")
        cursor.execute("insert into works_for values('"+id +"','"+dept_id+"')")
        cursor.execute("insert into manages values('"+id +"','"+dept_id+"')")
        cursor.execute("commit");
        MessageBox.showinfo("Insert Status2", "Inserted Successfully");
        


def insert_project():
    id=e_id.get()
    dept_id=e_dept_id.get()
    p_id=e_p_id.get()
    p_name=e_p_name.get()
    p_description=e_p_description.get()
    hours=e_hours.get()
    dependant=e_dependant.get()
    relation=e_relation.get()

    if(p_id=="" or p_name=="" or p_description=="" or hours=="" or dependant=="" or relation=="" or id=="" or dept_id=="" ):
        MessageBox.showinfo("insert Status", "All Fields are required")
    else:
        cursor.execute("insert into project values('"+p_id +"','"+p_name+"','"+p_description+"')")
        cursor.execute("insert into works_on values('"+id +"','"+p_id+"','"+hours+"')")
        cursor.execute("insert into controls values('"+dept_id+"','"+p_id+"')")
        cursor.execute("insert into dependents values('"+dependant +"','"+relation+"')")
        cursor.execute("insert into has values('"+id +"','"+dependant+"')")
        cursor.execute("commit");
        MessageBox.showinfo("Insert Status3", "Inserted Successfully");
        

root=Tk(className='Python Examples - Window Color')
root.geometry("1010x400")
root.title("Employee Management System")




id=Label(root,text='Enter Employee_Id : ',font=('bold',10))
id.place(x=20,y=30)

name=Label(root,text='Enter Name : ',font=('bold',10))
name.place(x=20,y=60)

gender=Label(root,text='Gender : ',font=('bold',10))
gender.place(x=20,y=90)

age=Label(root,text='Enter Age : ',font=('bold',10))
age.place(x=20,y=120)

salary=Label(root,text='Enter Salary : ',font=('bold',10))
salary.place(x=20,y=150)

address=Label(root,text='Enter Address : ',font=('bold',10))
address.place(x=20,y=180)

dept_id=Label(root,text='Department ID : ',font=('bold',10))
dept_id.place(x=370,y=30)

dept=Label(root,text='Department : ',font=('bold',10))
dept.place(x=370,y=60)

location=Label(root,text='Location : ',font=('bold',10))
location.place(x=370,y=90)

Employee_no=Label(root,text='Number of Employees : ',font=('bold',10))
Employee_no.place(x=370,y=120)

p_id=Label(root,text='Project ID : ',font=('bold',10))
p_id.place(x=720,y=30)

p_name=Label(root,text='Project Name : ',font=('bold',10))
p_name.place(x=720,y=60)

p_description=Label(root,text='Project Description : ',font=('bold',10))
p_description.place(x=720,y=90)

hours=Label(root,text='Number of hours : ',font=('bold',10))
hours.place(x=720,y=120)

dependant=Label(root,text='Depandants : ',font=('bold',10))
dependant.place(x=720,y=150)

relation=Label(root,text='Relationship : ',font=('bold',10))
relation.place(x=720,y=180)

e_id=Entry()
e_id.place(x=150,y=30)

e_name=Entry()
e_name.place(x=150,y=60)

e_gender=Entry()
e_gender.place(x=150,y=90)

e_age=Entry()
e_age.place(x=150,y=120)

e_salary=Entry()
e_salary.place(x=150,y=150)

e_address=Entry()
e_address.place(x=150,y=180)

e_dept_id=Entry()
e_dept_id.place(x=500,y=30)

e_dept=Entry()
e_dept.place(x=500,y=60)

e_location=Entry()
e_location.place(x=500,y=90)

e_Employee_no=Entry()
e_Employee_no.place(x=500,y=120)

e_p_id=Entry()
e_p_id.place(x=850,y=30)

e_p_name=Entry()
e_p_name.place(x=850,y=60)

e_p_description=Entry()
e_p_description.place(x=850,y=90)

e_hours=Entry()
e_hours.place(x=850,y=120)

e_dependant=Entry()
e_dependant.place(x=850,y=150)

e_relation=Entry()
e_relation.place(x=850,y=180)

insert=Button(root,text="Employee Registration",font=("italic",10),bg="white",command=insert)
insert.place(x=20, y=300)

insert_dept=Button(root,text="Department Registration",font=("italic",10),bg="white",command=insert_dept)
insert_dept.place(x=370, y=300)

insert_project=Button(root,text="Insert a Project",font=("italic",10),bg="white",command=insert_project)
insert_project.place(x=720, y=300)

root.mainloop()

cursor.execute("""SELECT distinct employee.eid, 
employee.ename from 
employee JOIN manages ON employee.eid = manages.eid;""")

