#import libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

#function to define database
def Database():
    global conn, cursor
    #creating student database
    conn = sqlite3.connect("stdmng.db")
    cursor = conn.cursor()
    #creating STUD_REGISTRATION table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, STU_PRNNO TEXT ,STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_BRANCH TEXT, STU_BLOODGROUP TEXT,STU_ADDRESS TEXT)")

#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("1250x500")
    #setting title for window
    display_screen.title("Student Database Management System")
    global tree
    global SEARCH
    global prnno,name,contact,email,rollno,branch,address,bloodgroup
    SEARCH = StringVar()
    prnno = StringVar()
    name = StringVar()
    contact = StringVar()
    email = StringVar()
    rollno = StringVar()
    branch = StringVar()
    bloodgroup = StringVar()
    address = StringVar()

    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=GROOVE)
    TopViewForm.pack(side=TOP, fill=X)
    #first left frame for registration from
    LFrom = Frame(display_screen, width="350",bg="lightcyan3")
    LFrom.pack(side=LEFT, fill=Y)
    #seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="gray80")
    LeftViewForm.pack(side=LEFT, fill=Y)
    #mid frame for displaying students record
    MidViewForm = Frame(display_screen, width=600,bg="rosybrown1")
    MidViewForm.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(TopViewForm, text="Student Data Management System", font=('times new roman', 18) , width=600,bg="midnightblue",fg="white")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="PRN no. ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=prnno).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Name  ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=name).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Rollno ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=rollno).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Email ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=email).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Branch ", font=("Arial", 12)).pack(side=TOP)
    branch_list = ['Computer Engineering', 'Information Technology', 'Electronics and Telecommunication']
    branch = ttk.Combobox(LFrom, values=branch_list, font=("Arial", 10, "bold"), textvariable=branch)
    branch.set("Select")
    branch.pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Blood group ", font=("Arial", 12)).pack(side=TOP)
    bloodgroup_list = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    bloodgroup = ttk.Combobox(LFrom, values=bloodgroup_list, font=("Arial", 10, "bold"), textvariable=bloodgroup)
    bloodgroup.set("Select")
    bloodgroup.pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Address ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=address).pack(side=TOP, padx=20, fill=BOTH)
    Button(LFrom,text="Submit",font=("Arial", 10, "bold"),command=register).pack(side=TOP, padx=10,pady=5, fill=X)

    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter PRN no. to Search", font=('verdana', 10),bg="black",fg="white")
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating view button
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData)
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete button
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
   #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Student Id", "PRN no.","Name","Rollno" ,"Contact","Branch", "Email","Address","Blood group"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    #setting headings for the columns
    tree.heading('PRN no.',text="PRN no.",anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Rollno', text="Rollno", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Branch', text="Branch", anchor=W)
    tree.heading('Blood group', text="Blood group",anchor=W)
    tree.heading('Address', text="Address", anchor=W)

    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0) 
    tree.column('#2', stretch=NO, minwidth=0, width=100) 
    tree.column('#3', stretch=NO, minwidth=0, width=100) 
    tree.column('#4', stretch=NO, minwidth=0, width=80)
    tree.column('#5', stretch=NO, minwidth=0, width=90)
    tree.column('#6', stretch=NO, minwidth=0, width=160)
    tree.column('#7', stretch=NO, minwidth=0, width=150)
    tree.column('#8', stretch=NO, minwidth=0, width=100)
    tree.pack()
    DisplayData()
#function to insert data into database
def register():
    Database()
    #getting form data
    name1=name.get()
    prnno1=prnno.get()
    con1=contact.get()
    email1=email.get()
    rol1=rollno.get()
    branch1=branch.get()
    address1=address.get()
    bldgrp=bloodgroup.get()

    #applying empty validation
    cursor.execute("SELECT * FROM STUD_REGISTRATION WHERE STU_PRNNO=?", (prnno1,))
    if cursor.fetchone() is not None:
        tkMessageBox.showinfo("Error", "PRN no. already exists in database")
        return
    elif prnno1=='':
        tkMessageBox.showinfo("Warning","fill the prnno field!!!")
    elif name1=='':
        tkMessageBox.showinfo("Warning","fill the name field!!!")
    elif con1=='':
        tkMessageBox.showinfo("Warning","fill the contact field!!!")
    elif email1=='':
        tkMessageBox.showinfo("Warning","fill the email field!!!")
    elif rol1=='':
        tkMessageBox.showinfo("Warning","fill the rollno. field!!!")
    elif branch1=='':
        tkMessageBox.showinfo("Warning","fill the branch field!!!")
    elif address1=='':
        tkMessageBox.showinfo("Warning","fill the address field!!!")
    elif bldgrp=='' :
        tkMessageBox.showinfo("Warning","fill the bloodgroup field!!!")
    elif '@' not in email1:
        tkMessageBox.showinfo("Error","Invalid email address")
    elif not con1.isdigit() or len(con1) != 10:
        tkMessageBox.showinfo("Warning","Contact number should contain only 10 digits!")
    elif len(prnno1)!=9:
        tkMessageBox.showinfo("Warning","PRN number should contain only 9 digits!")
    else:
        #execute query
        conn.execute('INSERT INTO STUD_REGISTRATION (STU_PRNNO,STU_NAME,STU_CONTACT,STU_EMAIL,STU_ROLLNO,STU_BRANCH,STU_BLOODGROUP,STU_ADDRESS) \
              VALUES (?,?,?,?,?,?,?,?)',(prnno1,name1,rol1,con1,branch1,email1,address1,bldgrp));
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
        DisplayData()
        conn.close()

def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    prnno.set("")
    name.set("")
    contact.set("")
    email.set("")
    rollno.set("")
    branch.set("")
    address.set("")
    bloodgroup.set("")

def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM STUD_REGISTRATION WHERE STU_ID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM STUD_REGISTRATION WHERE STU_PRNNO LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
#defining function to access data from SQLite database
def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM STUD_REGISTRATION")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

#calling function
DisplayForm()
if __name__=='__main__':
#Running Application
 mainloop()