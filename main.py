import os
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from tkinter import ttk
import csv


class LibraryFunctions:
    def __init__(self):
        pass

    def addsession(self):
        book = str(self.book.get())
        writer = str(self.writer.get())
        subject = str(self.subject.get())
        year = str(self.year.get())
        if not all([book, writer, subject, year]):
            self.notFound.config(text='Fill all the fields*', fg='red')
            return
        with open('books.csv', 'r') as booksLi:
            csv_reader = csv.reader(booksLi)
            if any(row[0] == book for row in csv_reader):
                self.notFound.config(
                    text='Book already exists in the list!', fg='green')
                return
        with open('books.csv', 'a') as file:
            file.write(f"{book},{writer},{subject},{year}\n")
        self.notFound.config(text='Book Added!', fg='green')
        li = [
            f"{book}  By   {writer} :: subject : [ {subject} ]  , Edition :({year})"]
        for widgets in self.added.winfo_children():
            widgets.destroy()
        scrollbarY = Scrollbar(self.added)
        scrollbarY.pack(side=RIGHT, fill=Y)
        for i, item in enumerate(li):
            self.added.insert(i, item)

    def clearFieldsofSearchBooks(self):
        self.book_en.delete(0, 'end')
        self.author_en.delete(0, 'end')
        self.subject_en.delete(0, 'end')
        self.ed_en.delete(0, 'end')
        self.Returned.delete(0,"end")
        self.error.config(text='')

    def clearFieldsofAddBooks(self):
        self.book.delete(0, 'end')
        self.writer.delete(0, 'end')
        self.subject.delete(0, 'end')
        self.year.delete(0, 'end')
        self.notFound.config(text='')

    def clearFieldsofDelBooks(self):
        self.booktoDel.delete(0, 'end')
        self.notDel.config(text='')

    def clearFieldsofModifyBooks(self):

        self.mod_book.delete(0, 'end')
        self.mod_author.delete(0, "end")
        self.mod_subject.delete(0, "end")
        self.mod_ed.delete(0, "end")
        self.notModify.config(text='')

    def SearchSession(self):
        book = str(self.book_en.get()).lower()
        author = str(self.author_en.get()).lower()
        subject = str(self.subject_en.get()).lower()
        edition = str(self.ed_en.get())

        if book == "" and author == "" and subject == "" and edition == "":
            self.error.config(text=r'Fill at least one Field*')
            return
        with open("books.csv", "r") as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            count = 1
            for row in rows:
                if book == "" and subject == "" and edition == "":
                    if (row[1].lower().startswith(author)) :
                        self.Returned.insert("end",
                                             f"{count} :: Book Name   [ {row[0]} ]  By   [ {row[1]}  ] :: subject : [ {row[2]} ]  , Edition :({row[3]})  ::"
                                             )
                        count += 1
                elif author == "" and subject == "" and edition == "":
                    if (row[0].lower().startswith(book)) :
                        self.Returned.insert("end",
                                             f"{count} :: Book Name   [ {row[0]} ]  By   [ {row[1]}  ] :: subject : [ {row[2]} ]  , Edition :({row[3]})  ::"
                                             )
                        count += 1
                elif book =="" and subject == "" and author == "":
                    if  (row[3].lower().startswith(edition)):
                        self.Returned.insert("end",
                                             f"{count} :: Book Name   [ {row[0]} ]  By   [ {row[1]}  ] :: subject : [ {row[2]} ]  , Edition :({row[3]})  ::"
                                             )
                        count += 1
                elif book ==""  and author == "" and edition == "":
                    if  (row[2].lower().startswith(subject)):
                        self.Returned.insert("end",
                                             f"{count} :: Book Name   [ {row[0]} ]  By   [ {row[1]}  ] :: subject : [ {row[2]} ]  , Edition :({row[3]})  ::"
                                             )
                        count += 1
                
    
    def sortSessionByTitle(self):
        file_path = "books.csv"
        with open(file_path, 'r') as file:
          csv_reader = csv.reader(file)
          header = next(csv_reader)  
          sorted_rows = sorted(csv_reader, key=lambda row: row[0]) 

        with open(file_path, 'w', newline='') as file:
          csv_writer = csv.writer(file)
          csv_writer.writerow(header) 
          csv_writer.writerows(sorted_rows) 
          
        self.sorted.config(fg='Yellow', text='Books are sorted by Book Title')
          
    def sortSessionByAuthor(self):
        file_path = "books.csv"
        with open(file_path, 'r') as file:
          csv_reader = csv.reader(file)
          header = next(csv_reader)  
          sorted_rows = sorted(csv_reader, key=lambda row: row[1])  
        with open(file_path, 'w', newline='') as file:
          csv_writer = csv.writer(file)
          csv_writer.writerow(header)  
          csv_writer.writerows(sorted_rows)  
        
        self.sorted.config(fg='white', text='Books are sorted by Author Name')

    
    
    def delsession(self):
        count = 1
        book = str(self.booktoDel.get())
        date = datetime.now()

        if book == '':
            self.notDel.config(text='Please Enter the book name!', fg='red')

        else:
            with open("books.csv", 'r') as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)

            with open("books.csv", 'w', newline='') as file:
                csv_writer = csv.writer(file)
                deleted = False
                for row in rows:
                    if row[0] == book:
                        deleted = True
                        self.deleted.insert(
                            'end', f"{count}.The Book :: {book}  is Deleted  on {date.strftime('%d/ %m/ %y : %I : %M %p')}\n")
                        count += 1
                        continue
                    csv_writer.writerow(row)

            if deleted:
                self.notDel.config(text='Book Deleted!', fg='green')
            else:
                self.notDel.config(text=r"Book donot Exist!", fg='red')

    def ModifySession(self):
        count = 1
        book = str(self.mod_book.get())
        author = str(self.mod_author.get())
        subject = str(self.mod_subject.get())
        edition = str(self.mod_ed.get())

        if book == '' or author == '' or subject == '' or edition == '':
            self.notModify.config(
                text='Please Enter the one thing previous to modify!', fg='red')

        else:
            with open("books.csv", 'r') as file:
                csv_reader = csv.reader(file)
                rows = list(csv_reader)

            with open("books.csv", 'w', newline='') as file:
                csv_writer = csv.writer(file)
                deleted = False
                for row in rows:
                    if row[0] == book or row[1] == author or row[2] == subject or row[3] == edition:
                        deleted = True
                        row[0] = book
                        row[1] = author
                        row[2] = subject
                        row[3] = edition
                        self.Returned.insert(
                            'end', f"{count}.The Book :: {book}  is Modified \n")
                        count += 1
                    #   continue
                    csv_writer.writerow(row)

            if deleted:
                self.notModify.config(text='Book Modify!', fg='green')
            else:
                self.notModify.config(text=r"Book donot Exist!", fg='red')


class BackEnd:

    def __init__(self):
        pass

    def register(self):

        f_name = self.first_name.get()
        l_name = self.last_name.get()
        age_ = self.age.get()
        u_name = self.user.get()
        email_ = self.email.get()
        cpwd = self.passwConf.get()
        pwd = self.password.get()

        allAccounts = os.listdir(f'{os.getcwd()}/Accounts')

        if f_name == "" or age_ == "" or email_ == "" or pwd == "":
            self.notif.config(
                fg="red", text="Fill All Fields*", font='hack 10')
            return

        if cpwd == pwd:
            for i in allAccounts:
                if i == u_name:
                    self.notif.config(fg="red", text="Name Taken")
                    return
                else:
                    newFile = open(f"{os.getcwd()}/Accounts/{u_name}", "w")
                    newFile.write(f_name+"\n")
                    newFile.write(l_name+"\n")
                    newFile.write(u_name+"\n")
                    newFile.write(age_+"\n")
                    newFile.write(email_+"\n")
                    newFile.write(pwd+"\n")
                    newFile.close()
                    self.notif.config(
                        fg="green", text="Account has successfully been created!", font='hack 10')

        else:
            self.notif.config(
                fg="red", text="Password doesnt matched!", font='hack 10')

    def login(self):

        p = self.passw.get()
        u = self.user_name.get()
        allAcc = os.listdir(f'{os.getcwd()}/Accounts')

        if p == "":
            self.error.config(fg='red', text='Fill Password!')
        if u == "":
            self.error.config(fg='red', text='Fill Username!')

        try:

            for names in allAcc:
                if names != u:
                    self.error.config(fg='red', text='Invalid Account')
                if names == u:
                    acc = open(f"{os.getcwd()}/Accounts/{names}", 'r').read()
                    pwd = acc.split('\n')
                    pwd_from_list = pwd[5]

                    if pwd_from_list == p:
                        self.LibraryScreen()

        except:
            pass


class LoginSys(BackEnd):

    def loginSession(self):
        self.loginwin = Toplevel(self.mainWin)
        self.loginwin.title('LMS - Login')
        self.loginwin.geometry('400x220')
        self.loginwin.config(bg='#FFF7F1')
        self.loginwin.resizable(width=False, height=False)
        self.loginwin.wm_iconbitmap("2.ico")

        Label(self.loginwin, text="Login", font="hack 20").grid(
            row=0, column=2, pady=10, padx=10)
        Label(self.loginwin, text='User Name ', font="hack 10").grid(
            row=1, column=1, pady=10, padx=10)
        self.user_name = Entry(self.loginwin, borderwidth=3)
        self.user_name.grid(row=1, column=2, pady=10, padx=10, sticky=E)
        Label(self.loginwin, text='Password ', font="hack 10").grid(
            row=2, column=1, pady=10, padx=10)
        self.passw = Entry(self.loginwin, show='*', borderwidth=3)
        self.passw.grid(row=2, column=2, pady=10, padx=10, sticky=E)

        Button(self.loginwin, text="Login", bg='black', fg='white', font='hack 10',
               command=self.login).grid(row=3, column=2, pady=10, padx=10)
        self.error = Label(self.loginwin, font="hack 10", fg='red', bg='black')
        self.error.grid(row=4, column=2)
        self.loginwin.mainloop()


class RegisterSys(BackEnd):

    def registerSession(self):

        self.registerwin = Toplevel(self.mainWin)
        self.registerwin.title('New Registeration')
        self.registerwin.geometry('650x450')
        self.registerwin.config(bg='#FF7864')
        self.registerwin.resizable(width=False, height=False)
        self.registerwin.wm_iconbitmap("2.ico")

        Label(self.registerwin, text="Register", font="Stencil 20 italic").grid(
            row=0, column=5, pady=10, padx=10)
        Label(self.registerwin, text='First Name ', font="hack 10").grid(
            row=1, column=0, pady=10, padx=10, sticky=E)
        self.first_name = Entry(self.registerwin, borderwidth=3)
        self.first_name.grid(row=1, column=1, pady=10, padx=10)
        Label(self.registerwin, text='Last Name ', font="hack 10").grid(
            row=2, column=0, pady=10, padx=10, sticky=E)
        self.last_name = Entry(self.registerwin, borderwidth=3)
        self.last_name.grid(row=2, column=1, pady=10, padx=10)
        Label(self.registerwin, text='Username ', font="hack 10").grid(
            row=3, column=0, pady=10, padx=10, sticky=E)
        self.user = Entry(self.registerwin, borderwidth=3)
        self.user.grid(row=3, column=1, pady=10, padx=10)
        Label(self.registerwin, text='Age ', font="hack 10").grid(
            row=4, column=0, pady=10, padx=10, sticky=E)
        self.age = Entry(self.registerwin, borderwidth=3)
        self.age.grid(row=4, column=1, pady=10, padx=10)
        Label(self.registerwin, text='Email ', font="hack 10").grid(
            row=5, column=0, pady=10, padx=10, sticky=E)
        self.email = Entry(self.registerwin, borderwidth=3)
        self.email.grid(row=5, column=1, pady=10, padx=10)
        Label(self.registerwin, text='Password ', font="hack 10").grid(
            row=6, column=0, pady=10, padx=10, sticky=E)
        self.password = Entry(self.registerwin, show='*', borderwidth=3)
        self.password.grid(row=6, column=1, pady=10, padx=10)
        Label(self.registerwin, text='Confirm Password ', font="hack 10").grid(
            row=7, column=0, pady=10, padx=10, sticky=E)
        self.passwConf = Entry(self.registerwin, show='*', borderwidth=3)
        self.passwConf.grid(row=7, column=1, pady=10, padx=10)

        Button(self.registerwin, text="Register", fg='white', bg='black',
               font='hack 10', command=self.register).grid(row=9, column=1, pady=10, padx=10)
        self.notif = Label(self.registerwin, font='hack 10', bg='black')
        self.notif.grid(row=3, column=5, pady=10, padx=10)

        self.registerwin.mainloop()


class LibraryModels(LibraryFunctions, LoginSys, RegisterSys):

    def __init__(self, win, img):

        super().__init__()

        self.mainWin = win
        self.mainWin.geometry('650x550')
        self.mainWin.title('Library Management System')
        self.mainWin.config(bg='grey')
        self.mainWin.resizable(width=False, height=False)
        self.mainWin.wm_iconbitmap("2.ico")

        Label(self.mainWin, text='WELCOME  TO  NAMAL  LIBRARY',
              font="Algerian 20 italic", pady=5).pack(pady=50)
        Label(self.mainWin, image=img).pack(pady=30)

        Button(self.mainWin, text="Login", width=15, fg='white', bg='black',
               font="hack 10 ", command=self.loginSession).pack(pady=5)

        Button(self.mainWin, text="Register", width=15, fg='white',
               bg='black', font="hack 10", command=self.registerSession).pack()

        Label(self.mainWin, text='Fahim Ur Rehman Shah',
              font="Algerian 12 italic", bg='black', fg='yellow').pack(pady=25)

        self.loginwin = None
        self.registerwin = None
        self.lib = None
        self.error = None
        self.notif = None

        self.user_name = None
        self.passw = None
        self.passwConf = None
        self.password = None
        self.last_name = None
        self.first_name = None
        self.user = None
        self.age = None
        self.email = None

    def LibraryScreen(self):

        self.mainWin.withdraw()
        self.loginwin.withdraw()
        un = self.user_name.get()

        self.lib = Tk()
        self.lib.title('LMS - Dashborad')
        self.lib.config(bg='#474747')
        self.lib.geometry('800x500')
        self.lib.wm_iconbitmap("2.ico")

        winHead = Label(self.lib, text="Library - Dashborad",
                        fg='black', font="Algerian 28 italic")
        winHead.pack(side=TOP, padx=5, pady=80)

        Button(self.lib, text=f"Log Out", fg='white', bg='#0E0E0E', font='hack 8', command=lambda: [
               self.mainWin.deiconify(), self.lib.destroy()]).pack(pady=5, side=BOTTOM)

        Label(self.lib, text=f"Logged in as {un}", fg='green', bg='black', font='hack 10').pack(
            pady=10, side=BOTTOM)
        if un == "admin":
            btn1 = Button(self.lib, text="View Books", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.ViewBooks)
            btn1.place(relx=0.37, rely=0.3, relwidth=0.25, relheight=0.1)

            btn2 = Button(self.lib, text="Search Book", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.Search_book)
            btn2.place(relx=0.37, rely=0.4, relwidth=0.25, relheight=0.1)
            
            btn_sort_t = Button(self.lib, text="Sort By Title", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.sortSessionByTitle)
            btn_sort_t.place(relx=0.65, rely=0.4, relwidth=0.1, relheight=0.1)
            
            btn_sort_a = Button(self.lib, text="Sort By Author", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.sortSessionByAuthor)
            btn_sort_a.place(relx=0.80, rely=0.4, relwidth=0.1, relheight=0.1)
            
            self.sorted = Label(self.lib, font='Callibri 14 italic ', bg='#474747')
            self.sorted.place(relx=0.65, rely=0.5, anchor=NW)
            
            btn3 = Button(self.lib, text="Add Book", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.AddBook)
            btn3.place(relx=0.37, rely=0.5, relwidth=0.25, relheight=0.1)

            btn4 = Button(self.lib, text="Delete Book", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.DeleteBooks)
            btn4.place(relx=0.37, rely=0.6, relwidth=0.25, relheight=0.1)

            btn5 = Button(self.lib, text="Modify Book", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.ModifyBooks)
            btn5.place(relx=0.37, rely=0.7, relwidth=0.25, relheight=0.1)
        else:
            btn1 = Button(self.lib, text="View Books", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.ViewBooks)
            btn1.place(relx=0.37, rely=0.3, relwidth=0.25, relheight=0.1)

            btn2 = Button(self.lib, text="Search Book", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.Search_book)
            btn2.place(relx=0.37, rely=0.4, relwidth=0.25, relheight=0.1)
            
            btn_sort_t = Button(self.lib, text="Sort By Title", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.sortSessionByTitle)
            btn_sort_t.place(relx=0.65, rely=0.4, relwidth=0.1, relheight=0.1)
            
            btn_sort_a = Button(self.lib, text="Sort By Author", bg='#dfd3c3',
                          fg='#0E0E0E', font="hack 9", command=self.sortSessionByAuthor)
            btn_sort_a.place(relx=0.80, rely=0.4, relwidth=0.1, relheight=0.1)
            
            self.sorted = Label(self.lib, font='Callibri 14 italic', bg='#474747')
            self.sorted.place(relx=0.65, rely=0.5, anchor=NW)

        self.lib.mainloop()

    def AddBook(self):

        self.addbook = Tk()
        self.addbook.title('LMS - Add Books')
        self.addbook.geometry('900x600')
        self.addbook.config(bg='#a99ec3')
        self.addbook.wm_iconbitmap("2.ico")

        Label(self.addbook, text="Add Books", font='hack 20').place(
            relheight=0.05, relwidth=0.5, relx=0.26, rely=0.02)
        self.bookFrame = Frame(self.addbook, borderwidth=2,
                               bg='#CBB2DA', height=400, width=500)
        self.bookFrame.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.1)

        name = Label(self.addbook, text='Book Name', font='hack 10')
        name.place(rely=0.75, relx=0.35, anchor=NE)
        book = Label(self.addbook, text='Writer', font='hack 10')
        book.place(rely=0.80, relx=0.35, anchor=NE)
        subject = Label(self.addbook, text='Subject', font='hack 10')
        subject.place(rely=0.85, relx=0.35, anchor=NE)
        year = Label(self.addbook, text='Year', font='hack 10')
        year.place(rely=0.90, relx=0.35, anchor=NE)

        self.book = Entry(self.addbook, borderwidth=3)
        self.book.place(rely=0.75, relx=0.56, anchor=NE, relwidth=0.2)

        self.writer = Entry(self.addbook, borderwidth=3)
        self.writer.place(rely=0.80, relx=0.56, anchor=NE, relwidth=0.2)

        self.subject = Entry(self.addbook, borderwidth=3)
        self.subject.place(rely=0.85, relx=0.56, anchor=NE, relwidth=0.2)

        self.year = Entry(self.addbook, borderwidth=3)
        self.year.place(rely=0.90, relx=0.56, anchor=NE, relwidth=0.2)

        submit = Button(self.addbook, text='Submit', fg='white',
                        bg='black', font="hack 8 ", command=self.addsession)
        submit.place(rely=0.96, relx=0.44)
        clear = Button(self.addbook, text='Clear', fg='white', bg='black',
                       font="hack 8 ", command=self.clearFieldsofAddBooks)
        clear.place(rely=0.96, relx=0.38)

        self.notFound = Label(self.addbook, font='hack 10', bg='#B7C5C0')
        self.notFound.place(rely=0.80, relx=0.6, anchor=NW)

        self.added = Listbox(self.addbook, fg='green',
                             bg='#B7C5C0', font='hack 12')

        scrollbarY = Scrollbar(self.added)
        scrollbarY.pack(side=RIGHT, fill=Y)

        self.added.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.1)

        self.addbook.mainloop()

    def Search_book(self):

        self.search_bk = Tk()
        self.search_bk.title('LMS - Search Books')
        self.search_bk.geometry('900x600')
        self.search_bk.config(bg='#C3B98B')
        # self.search_bk.resizable(width=False, height=False)
        self.search_bk.wm_iconbitmap("2.ico")

        Label(self.search_bk, text="Searched Books", font='hack 15').place(
            relheight=0.05, relwidth=0.5, relx=0.26, rely=0.02)

        self.issuedBooks = Frame(
            self.search_bk, background='black', borderwidth=2, height=400, width=500)
        self.issuedBooks.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.1)

        book = Label(self.search_bk, text='Book Name for search', font='hack 10')
        book.place(rely=0.75, relx=0.35, anchor=NE)

        author = Label(self.search_bk, text='Author Name for search', font='hack 10')
        author.place(rely=0.80, relx=0.35, anchor=NE)

        Subject = Label(self.search_bk, text="Subject for search", font='hack 10')
        Subject.place(rely=0.85, relx=0.35, anchor=NE)

        edition = Label(self.search_bk, text="Edition for search", font='hack 10')
        edition.place(rely=0.90, relx=0.35, anchor=NE)

        self.book_en = Entry(self.search_bk, borderwidth=3)
        self.book_en.place(rely=0.75, relx=0.56, anchor=NE, relwidth=0.2)

        self.author_en = Entry(self.search_bk, borderwidth=3)
        self.author_en.place(rely=0.80, relx=0.56, anchor=NE, relwidth=0.2)

        self.subject_en = Entry(self.search_bk, borderwidth=3)
        self.subject_en.place(rely=0.85, relx=0.56, anchor=NE, relwidth=0.2)

        self.ed_en = Entry(self.search_bk, borderwidth=3)
        self.ed_en.place(rely=0.90, relx=0.56, anchor=NE, relwidth=0.2)

        submit = Button(self.search_bk, text='Submit', fg="white",
                        bg="black", font="hack 8 ", command=self.SearchSession)
        submit.place(rely=0.95, relx=0.40)
        clear = Button(self.search_bk, text='Clear', fg="white", bg="black",
                       font="hack 8 ", command=self.clearFieldsofSearchBooks)
        clear.place(rely=0.95, relx=0.46)

        self.error = Label(self.search_bk, font='hack 10', bg='white')
        self.error.place(rely=0.95, relx=0.6, anchor=NW)

        self.Returned = Listbox(
            self.search_bk, fg='white', bg='grey', font='hack 12')
        self.Returned.place(relheight=0.6, relwidth=0.89, relx=0.05, rely=0.1)
        scrollbarY = Scrollbar(self.Returned)
        scrollbarY.pack(side=RIGHT, fill=Y)
        scrollbarX = Scrollbar(self.Returned, orient=HORIZONTAL)
        scrollbarX.pack(side=BOTTOM , fill=X)

        self.Returned.config(yscrollcommand=scrollbarY.set)
        self.Returned.config(yscrollcommand=scrollbarX.set)
        scrollbarY.config(command=self.Returned.yview())
        scrollbarX.config(command=self.Returned.xview())

        self.search_bk.mainloop()

 
    def ViewBooks(self):
        viewBooks = Tk()
        viewBooks.title('LMS - View Books')
        viewBooks.geometry('850x600')
        viewBooks.config(bg='#CE7FD0')
        viewBooks.wm_iconbitmap("2.ico")

        Label(viewBooks, text="All Available Books",
              font='hack 25').pack(side=TOP, pady=25)

        li = ttk.Treeview(viewBooks)
        li["columns"] = ("Book Name", "Author", "Subject","Edition")

        li.heading("#0", text="S.No")
        li.heading("Book Name", text="Book Name")
        li.heading("Author", text="Author")
        li.heading("Subject", text="Subject")
        li.heading("Edition", text="Edition")

        li.column("#0", width=50)
        li.column("Book Name", width=200)
        li.column("Author", width=200)
        li.column("Subject", width=200)
        li.column("Edition", width=200)

        with open("books.csv", 'r') as file:
            j = 1
            for i in file:
                bk_dt = i.split(",")  
                li.insert(parent="", index="end", iid=j, text=str(j),
                          values=(bk_dt[0], bk_dt[1], bk_dt[2],bk_dt[3]))
                j += 1

        scrollbar = ttk.Scrollbar(
            viewBooks, orient="vertical", command=li.yview)
        li.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        li.pack(expand=True, fill="both")
        viewBooks.mainloop()

    def ModifyBooks(self):

        modifyBook = Tk()
        modifyBook.title('LMS - Modify Books')
        modifyBook.config(bg='#34C85B')
        modifyBook.geometry('750x600')
        modifyBook.wm_iconbitmap("2.ico")

        Label(modifyBook, text="Modify Books", font='hack 15').place(
            relheight=0.05, relwidth=0.5, relx=0.26, rely=0.05)
        self.returnFrame = Frame(
            modifyBook, background='cyan', borderwidth=.5, height=400, width=500)
        self.returnFrame.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.1)

        book = Label(modifyBook, text='Book ', font='hack 10')
        book.place(rely=0.70, relx=0.35, anchor=NE)
        author = Label(modifyBook, text="Author", font="hack 10")
        author.place(rely=0.75, relx=0.35, anchor=NE)
        subject = Label(modifyBook, text="Subject", font="hack 10")
        subject.place(rely=0.80, relx=0.35, anchor=NE)
        edition = Label(modifyBook, text="Edition", font="hack 10")
        edition.place(rely=0.85, relx=0.35, anchor=NE)

        self.mod_book = Entry(modifyBook, borderwidth=3)
        self.mod_book.place(rely=0.70, relx=0.56, anchor=NE, relwidth=0.2)
        self.mod_author = Entry(modifyBook, borderwidth=3)
        self.mod_author.place(rely=0.75, relx=0.56, anchor=NE, relwidth=0.2)
        self.mod_subject = Entry(modifyBook, borderwidth=3)
        self.mod_subject.place(rely=0.80, relx=0.56, anchor=NE, relwidth=0.2)
        self.mod_ed = Entry(modifyBook, borderwidth=3)
        self.mod_ed.place(rely=0.85, relx=0.56, anchor=NE, relwidth=0.2)

        clear = Button(modifyBook, text='Clear', fg='white', bg='black',
                       font="hack 8 ", command=self.clearFieldsofModifyBooks)
        clear.place(rely=0.90, relx=0.33)

        modify = Button(modifyBook, text='Modify', fg='white', bg='black',
                        font="hack 8 ", command=self.ModifySession)
        modify.place(rely=0.90, relx=0.39)

        self.notModify = Label(modifyBook, font='hack 10', bg='black')
        self.notModify.place(rely=.95, relx=0.3, anchor=NW)

        self.Returned = Listbox(
            self.returnFrame, fg='white', bg='grey', font='hack 12')
        self.Returned.place(relheight=0.9, relwidth=0.89, relx=0.05, rely=0.1)

        scrollbarY = Scrollbar(self.Returned)
        scrollbarY.pack(side=RIGHT, fill=Y)
        scrollbarX = Scrollbar(self.Returned, orient=HORIZONTAL)
        scrollbarX.pack(side=BOTTOM, fill=X)

        self.Returned.config(yscrollcommand=scrollbarY.set)
        self.Returned.config(yscrollcommand=scrollbarX.set)
        scrollbarY.config(command=self.Returned.yview())
        scrollbarX.config(command=self.Returned.xview())

        modifyBook.mainloop()

    def DeleteBooks(self):

        deleteBook = Tk()
        deleteBook.title('LMS - Delete Books')
        deleteBook.geometry('700x600')
        deleteBook.config(bg='#97B7CE')
        deleteBook.wm_iconbitmap("2.ico")
        Label(deleteBook, text="Delete Books", font='hack 15').place(
            relheight=0.05, relwidth=0.5, relx=0.26, rely=0.02)
        self.delFrame = Frame(deleteBook, background='#EEC9A2',
                              borderwidth=2, height=400, width=500)
        self.delFrame.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.1)

        name = Label(deleteBook, text='Book Name', font='hack 10')
        name.place(rely=0.75, relx=0.35, anchor=NE)

        self.booktoDel = Entry(deleteBook, borderwidth=3)
        self.booktoDel.place(rely=0.75, relx=0.56, anchor=NE, relwidth=0.2)

        submit = Button(deleteBook, text='Delete', fg='white',
                        bg='black', font="hack 8 ", command=self.delsession)
        submit.place(rely=0.81, relx=0.45)
        clear = Button(deleteBook, text='Clear', fg='white', bg='black',
                       font="hack 8 ", command=self.clearFieldsofDelBooks)
        clear.place(rely=0.81, relx=0.38)

        self.notDel = Label(deleteBook, font='hack 10', bg='black')
        self.notDel.place(rely=0.88, relx=0.3, anchor=NW)

        self.deleted = Listbox(deleteBook, fg='green',
                               bg='#B7C5C0', font='hack 12')
        self.deleted.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.1)

        scrollbarY = Scrollbar(self.deleted)
        scrollbarY.pack(side=RIGHT, fill=Y)

        self.deleted.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.1)

        deleteBook.mainloop()


Win = Tk()
img = Image.open("OIP.jpg")
img = img.resize((200, 180))
img = ImageTk.PhotoImage(img)


library = LibraryModels(Win, img)

Win.mainloop()
