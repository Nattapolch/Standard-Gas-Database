from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk


def Database():
    global conn, cursor
    conn = sqlite3.connect("dbtest2.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `invendb-test2` (Parts_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Parts_Name TEXT,Parts_Manufacturer TEXT,Parts_Model TEXT,Parts_Price INTERGER,Parts_Qty INTERGER)")
    conn.commit()


def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add New Part")
    addnewform.geometry("800x600")
    addnewform.config(bg="#B9D4DB")
    AddNewForm()


def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    label_text = Label(TopAddNew, text="Add New Part", font=('arial', 18), width=600, bg="#478BA2", fg="#F2A490")
    label_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600, bg="#B9D4DB")
    MidAddNew.pack(side=TOP, pady=50)
    label_partname = Label(MidAddNew, text="Part Name:", font=('arial', 25), bd=10, bg="#B9D4DB")
    label_partname.grid(row=0, sticky=W)

    label_partmanufacturer = Label(MidAddNew, text="Part Manufacturer:", font=('arial', 25), bd=10, bg="#B9D4DB")
    label_partmanufacturer.grid(row=1, sticky=W)

    label_partmodel = Label(MidAddNew, text="Part Model:", font=('arial', 25), bd=10, bg="#B9D4DB")
    label_partmodel.grid(row=2, sticky=W)

    label_partprice = Label(MidAddNew, text="Part Price:", font=('arial', 25), bd=10, bg="#B9D4DB")
    label_partprice.grid(row=3, sticky=W)

    label_partqty = Label(MidAddNew, text="Part Quantity:", font=('arial', 25), bd=10, bg="#B9D4DB")
    label_partqty.grid(row=4, sticky=W)

    partname = Entry(MidAddNew, textvariable=Parts_Name, font=('arial', 25), width=15, bg="#D4CFC9")
    partname.grid(row=0, column=1)

    partnmanufacturer = Entry(MidAddNew, textvariable=Parts_Manufacturer, font=('arial', 25), width=15, bg="#D4CFC9")
    partnmanufacturer.grid(row=1, column=1)

    partmodel = Entry(MidAddNew, textvariable=Parts_Model, font=('arial', 25), width=15, bg="#D4CFC9")
    partmodel.grid(row=2, column=1)

    partprice = Entry(MidAddNew, textvariable=Parts_Price, font=('arial', 25), width=15, bg="#D4CFC9")
    partprice.grid(row=3, column=1)

    partqty = Entry(MidAddNew, textvariable=Parts_Qty, font=('arial', 25), width=15, bg="#D4CFC9")
    partqty.grid(row=4, column=1)

    button_save = Button(MidAddNew, text="Save", font=('arial', 18), width=30, command=AddNew, bg="#c3aed6",
                         activeforeground="#f0a500", activebackground="#290001")
    button_save.grid(row=6, columnspan=2, pady=20)


def AddNew():
    Database()
    cursor.execute(
        "INSERT INTO `invendb-test2` (Parts_Name,Parts_Manufacturer,Parts_Model,Parts_Price,Parts_Qty) VALUES(?, ?, ?, ?, ?)",
        (str(Parts_Name.get()), str(Parts_Manufacturer.get()), str(Parts_Model.get()), int(Parts_Price.get()),
         int(Parts_Qty.get())))
    conn.commit()
    Parts_Name.set("")
    Parts_Manufacturer.set("")
    Parts_Model.set("")
    Parts_Price.set("")
    Parts_Qty.set("")
    cursor.close()
    conn.close()


def Exit():
    ResultExit = tkMessageBox.askquestion('Simple Inventory System', 'Do you want to exit program?', icon="warning")
    if ResultExit == 'yes':
        root.destroy()
        exit()


################################ Test view ###########################################
def ViewForm():
    global tree
    global edit
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)

    label_text = Label(TopViewForm, text="Consumable Parts List", font=('arial', 18), width=600)
    label_text.pack(fill=X)
    label_search = Label(LeftViewForm, text="Search (Enter Part name)", font=('arial', 15))
    label_search.pack(side=TOP, anchor=W)

    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)

    button_search = Button(LeftViewForm, text="Search", command=Search)
    button_search.pack(side=TOP, padx=10, pady=10, fill=X)
    button_reset = Button(LeftViewForm, text="Reset", command=Reset)
    button_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    button_delete = Button(LeftViewForm, text="Delete", command=Delete)
    button_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    label_Edit = Label(LeftViewForm, text="Edit (Enter Part id)", font=('arial', 15))
    label_Edit.pack(side=TOP, anchor=W)

    edit = Entry(LeftViewForm, textvariable=EDIT, font=('arial', 15), width=10)
    edit.pack(side=TOP, padx=10, fill=X)

    button_edit = Button(LeftViewForm, text="Edit", command=ShowEdit)
    button_edit.pack(side=TOP, padx=10, pady=10, fill=X)

    scrollbar_x = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbar_y = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=(
    "Parts id", "Parts Name", "Parts Manufacturer", "Parts Model", "Product Price", "Product Quantity"),
                        selectmode="extended", height=100, yscrollcommand=scrollbar_y.set,
                        xscrollcommand=scrollbar_x.set)
    scrollbar_y.config(command=tree.yview)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    scrollbar_x.config(command=tree.xview)
    scrollbar_x.pack(side=BOTTOM, fill=X)

    tree.heading('Parts id', text="Parts id", anchor=W)
    tree.heading('Parts Name', text="Parts Name", anchor=W)
    tree.heading('Parts Manufacturer', text="Parts Manufacturer", anchor=W)
    tree.heading('Parts Model', text="Parts Model", anchor=W)
    tree.heading('Product Price', text="Product Price", anchor=W)
    tree.heading('Product Quantity', text="Product Quantity", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=50)
    tree.column('#2', stretch=NO, minwidth=0, width=180)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)

    tree.pack()
    DisplayData()


def ShowEdit():
    global editform
    editform = Toplevel()
    editform.title("Edit data")
    editform.geometry("800x600")
    EditForm()


def ShowAbout():
    global aboutform
    aboutform = Toplevel()
    aboutform.title("About")
    aboutform.geometry("400x300")
    aboutform.config(bg="#8db596")
    AboutForm()


def AboutForm():
    TopAbout = Frame(aboutform, width=300, height=100, bd=1, relief=SOLID)
    TopAbout.pack(side=TOP, pady=20)
    label_text = Label(TopAbout, text="About this program 😎", font=('arial', 18), width=300, bg="#b8de6f")
    label_text.pack()
    MidAbout = Frame(aboutform, width=300, bg="#8db596")
    MidAbout.pack(side=TOP, pady=30)
    label_version = Label(MidAbout, text="Version : 1.00", font=('arial', 10), bd=10, bg="#8db596")
    label_version.grid(row=0, sticky=W)
    label_devname = Label(MidAbout, text="Developed by : Nattapol Charuthamrrong", font=('arial', 10), bd=10,
                          bg="#8db596")
    label_devname.grid(row=1, sticky=W)


def EditForm():
    global partname
    global partnmanufacturer
    global partmodel
    global partprice
    global partqty
    TopEdit = Frame(editform, width=600, height=100, bd=1, relief=SOLID)
    TopEdit.pack(side=TOP, pady=20)
    label_text = Label(TopEdit, text="Edit part data", font=('arial', 18), width=600)
    label_text.pack(fill=X)
    MidEdit = Frame(editform, width=600)
    MidEdit.pack(side=TOP, pady=50)
    label_partname = Label(MidEdit, text="Part Name:", font=('arial', 25), bd=10)
    label_partname.grid(row=0, sticky=W)

    label_partmanufacturer = Label(MidEdit, text="Part Manufacturer:", font=('arial', 25), bd=10)
    label_partmanufacturer.grid(row=1, sticky=W)

    label_partmodel = Label(MidEdit, text="Part Model:", font=('arial', 25), bd=10)
    label_partmodel.grid(row=2, sticky=W)

    label_partprice = Label(MidEdit, text="Part Price:", font=('arial', 25), bd=10)
    label_partprice.grid(row=3, sticky=W)

    label_partqty = Label(MidEdit, text="Part Quantity:", font=('arial', 25), bd=10)
    label_partqty.grid(row=4, sticky=W)

    partname = Entry(MidEdit, font=('arial', 25), width=15)
    partname.grid(row=0, column=1)

    partnmanufacturer = Entry(MidEdit, font=('arial', 25), width=15)
    partnmanufacturer.grid(row=1, column=1)

    partmodel = Entry(MidEdit, font=('arial', 25), width=15)
    partmodel.grid(row=2, column=1)

    partprice = Entry(MidEdit, font=('arial', 25), width=15)
    partprice.grid(row=3, column=1)

    partqty = Entry(MidEdit, font=('arial', 25), width=15)
    partqty.grid(row=4, column=1)

    button_save = Button(MidEdit, text="Save edit", font=('arial', 18), width=30, bg="#009ACD", command=Edit)
    button_save.grid(row=6, columnspan=2, pady=20)
    DisplayEditData()


def DisplayEditData():
    Database()
    record_id = edit.get()
    cursor.execute("SELECT * FROM 'invendb-test2' WHERE oid = " + record_id)
    # cursor.execute("SELECT * FROM 'invendb-test2' WHERE Parts_id = " + record_id)

    records = cursor.fetchall()
    """for data in records:
        partname.delete(0,END)
        partnmanufacturer.delete(0,END)
        partmodel.delete(0,END)
        partprice.delete(0,END)
        partqty.delete(0,END)"""

    for data in records:
        partname.insert(0, data[1])
        partnmanufacturer.insert(0, data[2])
        partmodel.insert(0, data[3])
        partprice.insert(0, data[4])
        partqty.insert(0, data[5])

    cursor.close()
    conn.close()


def Edit():
    Database()
    record_id = edit.get()
    cursor.execute("""UPDATE 'invendb-test2' SET
    Parts_Name = :name,
    Parts_Manufacturer = :manufacturer,
    Parts_Model = :model,
    Parts_Price = :price,
    Parts_Qty = :qty

    WHERE oid = :oid""",
                   {
                       'name': partname.get(),
                       'manufacturer': partnmanufacturer.get(),
                       'model': partmodel.get(),
                       'price': partprice.get(),
                       'qty': partqty.get(),
                       'oid': record_id
                   })
    conn.commit()
    cursor.close()
    conn.close()


def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `invendb-test2`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `invendb-test2` WHERE `Parts_Name` LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
    EDIT.set("")


def Delete():
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('Consumable Parts Inventory System', 'Do you want to delete this item?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `invendb-test2` WHERE `Parts_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Consumable Parts List")
    viewform.geometry("1000x600")
    ViewForm()


######################################################################################
### GUI ###
root = Tk()
root.title("Consumable Parts Inventory System")
root.geometry('900x300')
root.config(bg="#fae0df")

### Variables ###
Parts_Name = StringVar()
Parts_Manufacturer = StringVar()
Parts_Model = StringVar()
Parts_Price = IntVar()
Parts_Qty = IntVar()
SEARCH = StringVar()
EDIT = StringVar()

### Label ###
label_head = Label(root, text="Consumable Parts Inventory System", font=('arial', 25), bg="#ff9a8c")
label_head.pack()
label_devname = Label(root, text="Nattapol Charuthamrong", font=('arial', 8), fg="white", bg="#fae0df")
label_devname.place(x=770, y=280)

### Button in GUI ###
button_Additem = Button(root, command=ShowAddNew, text="Add new item", height="3", width="13", bg="#51adcf",
                        activeforeground="#f0a500", activebackground="#290001")
button_Additem.place(x=100, y=150)

button_viewlist = Button(root, command=ShowView, text="View Parts List", height="3", width="13", bg="#de4463",
                         activeforeground="#f0a500", activebackground="#290001")
button_viewlist.place(x=300, y=150)

button_exit = Button(root, command=Exit, text="Exit", height="3", width="13", bg="#8db596",
                     activeforeground="#f0a500", activebackground="#290001")
button_exit.place(x=500, y=150)

button_about = Button(root, command=ShowAbout, text="About", height="3", width="13", bg="#b8de6f",
                      activeforeground="#f0a500", activebackground="#290001")
button_about.place(x=700, y=150)

Database()
root.mainloop()