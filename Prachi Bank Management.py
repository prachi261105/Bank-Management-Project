from tkinter import *
from tkinter import messagebox
from tkinter import IntVar
from tkinter import StringVar
from tkinter import ttk
import mysql.connector
import smtplib


convar=mysql.connector.connect(
   host='localhost',
   user='root',
   passwd='',
   database='bankmanagement'
    )
mycur=convar.cursor()

welwin=None 
loginwin=None
mainwin=None
formwin=None
nomineewiny=None
cashbookwin=None



usertxt= None
passtxt = None
nominee = None
optin=None

accno=None
fname=None
lname=None
email=None
phoneno=None
aadhar=None
bal=None

trv=None
csearch=None
cacc=None
cname=None
cbal=None
cphno=None
cmail=None
cwdwl=None
cdeposit=None
fbal=None

    


def loginwinopener():
    welwin.destroy()
    loginwinf()

def mainwinopener():
    username=usertxt.get()
    password=passtxt.get()
    if (username=='rajbankofficial' and password=='rajbank@123'):
        loginwin.destroy()
        mainwinf()
    else:
        root=Tk()
        root.withdraw()
        messagebox.showinfo("RAJ BANk","username and password error")

def formwinopener():
    mainwin.destroy()
    formwinf()

def formwincloser():
    root=Tk()
    root.withdraw()
    if messagebox.askyesno('confirm please','Are you sure you want to exit'):
        formwin.destroy()
        loginwinf()
    else:
        return True
    
    

def formwincloser2():
    formwin.destroy()
    mainwinf()
    
def mainwincloser():
    root=Tk()
    root.withdraw()
    if messagebox.askyesno('confirm please','Are you sure you want to logout'):
            mainwin.destroy()
            loginwinf()
    else:
        return True
    

def loginwincloser():
    loginwin.destroy()
    welwinf()

def nomineewinopenery():
    formwin.destroy()
    nomineewinyf()

def nomineewinopenern():
    nomineewinnf()

def nomineewinycloser():
    nomineewiny.destroy()
    formwinf()

def nomineewinycloser2():
    nomineewiny.destroy()
    root=Tk()
    root.withdraw()
    messagebox.showinfo("RAJ BANk","Account created successfully")
    mainwinf()

def nomineewincloser2():
    formwin.destroy()
    root=Tk()
    root.withdraw()
    messagebox.showinfo("RAJ BANk","Account created successfully")
    mainwinf()

def cashwinopener():
    mainwin.destroy()
    cashbookwinf()
    

def cashbookwincloser():
    root=Tk()
    root.withdraw()
    if messagebox.askyesno('confirm please','Are you sure you want to exit'):
            cashbookwin.destroy()
            mainwinf()
    else:
        return True

def cashbookwincloser2():
    root=Tk()
    root.withdraw()
    if messagebox.askyesno('confirm please','Are you sure you want to logout'):
            cashbookwin.destroy()
            loginwinf()
    else:
        return True
    
    



def database1():
    global mycur
    global convar
    mycur.execute("insert into account values('"+accno.get()+"','"+fname.get()+"','"+lname.get()+"','"+email.get()+"','"+phoneno.get()+"','"+aadhar.get()+"','"+str(bal.get())+"')")
    convar.commit()
    nomineewinycloser2()

def database2():
    global mycur
    global convar
    mycur.execute("insert into account values('"+accno.get()+"','"+fname.get()+"','"+lname.get()+"','"+email.get()+"','"+phoneno.get()+"','"+aadhar.get()+"','"+str(bal.get())+"')")
    convar.commit()
    nomineewincloser2()



    
def welwinf():
    global welwin
    welwin=Tk()
    welwin.geometry('500x300+475+245')
    welwin.title('RAJ Bank')
    welwin.configure(background='light blue')
    wellbl=Label(welwin,text='WELCOME \nTo \nRAJ BANK',bd=2,font=("Monotype Corsiva",50),bg='light blue',fg='brown')
    wellbl.pack()
    logbttn=Button(welwin,text='login page',activebackground='violet',command=loginwinopener,bd=1,bg='pink')
    logbttn.place(x=400,y=250,height=25,width=100)


def loginwinf():
    global usertxt
    global passtxt
    global loginwin
    loginwin=Tk()
    loginwin.geometry('600x450+400+150')
    loginwin.title('RAJ bank')
    loginwin.configure(background='light blue')
    
    loginlbl=Label(loginwin,text='Login page',bd=2,font=("Monotype Corsiva",40),bg='light blue',fg='brown')
    loginlbl.pack()

    usertxt=StringVar(loginwin)
    passtxt=StringVar(loginwin)

    userlbl=Label(loginwin,text='Username',bg='light blue',font=("Monotype Corsiva",20))
    userlbl.place(x=50,y=150,height=25,width=100)

    userentry=Entry(loginwin,textvariable=usertxt)
    userentry.place(x=220,y=150,height=25,width=110)

    passlbl=Label(loginwin,text='Password',bg='light blue', font=("Monotype Corsiva",20))
    passlbl.place(x=50,y=250,height=25,width=100)

    
    passentry=Entry(loginwin,textvariable=passtxt,show='*')
    passentry.place(x=220,y=250,height=25,width=110)

    logbttn=Button(loginwin,text='login',activebackground='violet',command=mainwinopener,bd=2,bg='pink')
    logbttn.place(x=400,y=350,height=25,width=100)

    backbttn=Button(loginwin,text='Back',activebackground='violet',command=loginwincloser,bd=2,bg='pink')
    backbttn.place(x=100,y=350,height=25,width=100)


def mainwinf():
    global option
    global mainwin
    mainwin=Tk()
    mainwin.geometry('700x450+350+150')
    mainwin.title('RAJ bank')
    mainwin.configure(background='light blue')
    option=IntVar(mainwin)

    mainlbl=Label(mainwin,text='Choose what to perform',bd=2,font=("Monotype Corsiva",50),bg='light blue',fg='brown')
    mainlbl.pack()

    o1=Radiobutton(mainwin,text='Create new account',value=1,variable=option,font=('Monotype Corsiva',20),bg='light blue',activeforeground='violet',command=formwinopener)
    o1.place(x=100,y=150)

    o2=Radiobutton(mainwin,text='View account details ,update or delete ',value=2,variable=option,font=('Monotype Corsiva',20),bg='light blue',activeforeground='violet',command=cashwinopener)
    o2.place(x=100,y=250)

    logoutbttn=Button(mainwin,text='logout',activebackground='violet',command=mainwincloser,bd=2,bg='pink')
    logoutbttn.place(x=500,y=350,height=25,width=100)


def formwinf():
    global accno
    global fname
    global lname
    global email
    global phoneno
    global aadhar
    global bal
    
    global formwin
    formwin=Tk()
    formwin.geometry('650x750+375+25')
    formwin.title('RAJ Bank')
    formwin.configure(background='light blue')

    accno=StringVar(formwin)
    fname=StringVar(formwin)
    lname=StringVar(formwin)    
    email=StringVar(formwin)
    phoneno=StringVar(formwin)
    aadhar=StringVar(formwin)
    bal=IntVar(formwin)

    global nominee
    nominee = IntVar(formwin)
    
    formlbl=Label(formwin,text='FORM',bd=2,font=("Monotype Corsiva",50),bg='light blue',fg='brown')
    formlbl.pack()

    fnamelbl=Label(formwin,text='First Name:',bg='light blue',font=("Monotype Corsiva",20))
    fnamelbl.place(x=50,y=150,height=25,width=150)

    fnameentry=Entry(formwin,textvariable=fname)
    fnameentry.place(x=220,y=150,height=25,width=150)

    lnamelbl=Label(formwin,text='Last Name:',bg='light blue', font=("Monotype Corsiva",20))
    lnamelbl.place(x=50,y=200,height=25,width=150)

    lnameentry=Entry(formwin,textvariable=lname)
    lnameentry.place(x=220,y=200,height=25,width=150)

    doblbl=Label(formwin,text='Date of Birth:',bg='light blue', font=("Monotype Corsiva",20))
    doblbl.place(x=50,y=250,height=25,width=150)

    dobentry=Entry(formwin)
    dobentry.place(x=220,y=250,height=25,width=150)

    addlbl=Label(formwin,text='Address:',bg='light blue', font=("Monotype Corsiva",20))
    addlbl.place(x=50,y=300,height=25,width=150)

    addentry=Entry(formwin)
    addentry.place(x=220,y=300,height=25,width=400)

    emaillbl=Label(formwin,text='Email:',bg='light blue', font=("Monotype Corsiva",20))
    emaillbl.place(x=50,y=350,height=25,width=150)

    emailentry=Entry(formwin,textvariable=email)
    emailentry.place(x=220,y=350,height=25,width=400)

    pnolbl=Label(formwin,text='Phone No:',bg='light blue', font=("Monotype Corsiva",20))
    pnolbl.place(x=50,y=400,height=25,width=150)

    pnoentry=Entry(formwin,textvariable=phoneno)
    pnoentry.place(x=220,y=400,height=25,width=150)

    adharlbl=Label(formwin,text='Aadhar No:',bg='light blue', font=("Monotype Corsiva",20))
    adharlbl.place(x=50,y=450,height=25,width=150)

    adharentry=Entry(formwin,textvariable=aadhar)
    adharentry.place(x=220,y=450,height=25,width=150)

    acclbl=Label(formwin,text='New Acc. No.',bg='light blue', font=("Monotype Corsiva",20))
    acclbl.place(x=50,y=500,height=25,width=150)

    accentry=Entry(formwin,textvariable=accno)
    accentry.place(x=220,y=500,height=25,width=150)
    
    openballbl=Label(formwin,text='Opening balance',bd=2,font=("Monotype Corsiva",20),bg='light blue')
    openballbl.place(x=50,y=550)

    openbalentry=Entry(formwin,textvariable=bal)
    openbalentry.place(x=220,y=550,height=25,width=150)

    nomineelbl=Label(formwin,text='Nominee required:',bd=2,font=("Monotype Corsiva",20),bg='light blue')
    nomineelbl.place(x=50,y=600)

    nomineeyes=Radiobutton(formwin,text="yes",value=1,variable=nominee,font=('Monotype Corsiva',20),bg='light blue',activeforeground='violet',command=nomineewinopenery)
    nomineeyes.place(x=220,y=650,)

    nomineeno=Radiobutton(formwin,text='no',value=2,variable=nominee,font=('Monotype Corsiva',20),bg='light blue',activeforeground='violet',command=database2)
    nomineeno.place(x=350,y=650)
       
    logbttn=Button(formwin,text='Logout',activebackground='violet',command=formwincloser,bd=2,bg='pink')
    logbttn.place(x=450,y=700,height=25,width=100)
    
    backbttn=Button(formwin,text='Back',activebackground='violet',command=formwincloser2,bd=2,bg='pink')
    backbttn.place(x=100,y=700,height=25,width=100)







def nomineewinyf():
    global nomineewiny
    nomineewiny=Tk()
    nomineewiny.geometry('650x650+400+70')
    nomineewiny.title('RAJ Bank')
    nomineewiny.configure(background='light blue')

    formlbl=Label(nomineewiny,text=' Nominee form',bd=2,font=("Monotype Corsiva",50),bg='light blue',fg='brown')
    formlbl.pack()

    fnamelbl=Label(nomineewiny,text='First Name:',bg='light blue',font=("Monotype Corsiva",20))
    fnamelbl.place(x=50,y=150,height=25,width=150)

    fnameentry=Entry(nomineewiny)
    fnameentry.place(x=220,y=150,height=25,width=150)

    lnamelbl=Label(nomineewiny,text='Last Name:',bg='light blue', font=("Monotype Corsiva",20))
    lnamelbl.place(x=50,y=200,height=25,width=150)

    lnameentry=Entry(nomineewiny)
    lnameentry.place(x=220,y=200,height=25,width=150)

    doblbl=Label(nomineewiny,text='Date of Birth:',bg='light blue', font=("Monotype Corsiva",20))
    doblbl.place(x=50,y=250,height=25,width=150)

    dobentry=Entry(nomineewiny)
    dobentry.place(x=220,y=250,height=25,width=150)

    emaillbl=Label(nomineewiny,text='Email:',bg='light blue', font=("Monotype Corsiva",20))
    emaillbl.place(x=50,y=300,height=25,width=150)

    emailentry=Entry(nomineewiny)
    emailentry.place(x=220,y=300,height=25,width=400)

    relationlbl=Label(nomineewiny,text='Relation:',bg='light blue', font=("Monotype Corsiva",20))
    relationlbl.place(x=50,y=350,height=25,width=150)

    relationentry=Entry(nomineewiny)
    relationentry.place(x=220,y=350,height=25,width=150)

    pnolbl=Label(nomineewiny,text='Phone No:',bg='light blue', font=("Monotype Corsiva",20))
    pnolbl.place(x=50,y=400,height=25,width=150)

    pnoentry=Entry(nomineewiny)
    pnoentry.place(x=220,y=400,height=25,width=150)

    adharlbl=Label(nomineewiny,text='Adhar No:',bg='light blue', font=("Monotype Corsiva",20))
    adharlbl.place(x=50,y=450,height=25,width=150)

    adharentry=Entry(nomineewiny)
    adharentry.place(x=220,y=450,height=25,width=150)
    
    submitbttn=Button(nomineewiny,text='Submit',activebackground='violet',command=database1,bd=2,bg='pink')
    submitbttn.place(x=450,y=550,height=25,width=100)
    
    backbttn=Button(nomineewiny,text='Back',activebackground='violet',command=nomineewinycloser,bd=2,bg='pink')
    backbttn.place(x=100,y=550,height=25,width=100)

    


def clear():
    query='SELECT accountno,firstname,lastname,email,phoneno,closingbalance from account'
    mycur.execute(query)
    rows=mycur.fetchall()
    update(rows)

    
def delete():
    global cacc
    if messagebox.askyesno('confirm delete?','Are you sure you want to delete this account'):
        query='DELETE FROM account WHERE accountno="'+cacc.get()+'"'
        mycur.execute(query)
        convar.commit()
        clear()
    else:
        return True

def search():
    global csearch
    query='SELECT accountno,firstname,lastname,email,phoneno,closingbalance from account WHERE firstname LIKE "'+csearch.get()+'" or lastname LIKE "'+csearch.get()+'" or accountno LIKE "'+csearch.get()+'"'
    mycur.execute(query)
    rows=mycur.fetchall()
    update(rows)

    
def update(rows):
    global trv
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)

def viewall():
    query='SELECT accountno,firstname,lastname,email,phoneno,closingbalance from account'
    mycur.execute(query)
    rows=mycur.fetchall()
    update(rows)
    

    
def getrow(event):
    global cacc
    global cname
    global cbal
    global cphno
    global cmail
    rowid=trv.identify_row(event.y)
    item=trv.item(trv.focus())
    cacc.set(item['values'][0])
    cname.set(item['values'][1])
    cbal.set(item['values'][5])
    cphno.set(item['values'][4])
    cmail.set(item['values'][3])

def update2():
    global cwdwl
    global cdeposit
    global fbal
    global cbal
    global cacc
    global cmail
    try:
        if(cwdwl.get()!=0):  
            totalsub =cbal.get()-cwdwl.get()
            if(totalsub<0):
                messagebox.showinfo("RAJ bank","Not enough amount in account ")
            else:
                query='UPDATE account SET closingbalance="'+str(totalsub)+'" WHERE accountno="'+cacc.get()+'"'
                mycur.execute(query)
                cbal.set(totalsub)
                fbal.set(totalsub)
                
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login('rajbankofficial@gmail.com','rajbank@123')
                message='your account debited with Rs. '+str(cwdwl.get())+' current balance is Rs. '+str(cbal.get())
                s.sendmail('rajbankofficial@gmail.com','"'+cmail.get()+'"',message)
                s.quit()
                messagebox.showinfo("RAJ bank","email sent")
                
                convar.commit()
                clear()
        else:
            totalsum =cbal.get()+cdeposit.get()
            query1='UPDATE account SET closingbalance="'+str(totalsum)+'" WHERE accountno="'+cacc.get()+'"'
            mycur.execute(query1)
            convar.commit()
            cbal.set(totalsum)
            fbal.set(totalsum)
            
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login('rajbankofficial@gmail.com','rajbank@123')
            message='your account credited with Rs. '+str(cdeposit.get())+' current balance is Rs. '+str(cbal.get())
            s.sendmail('rajbankofficial@gmail.com','"'+cmail.get()+'"',message)
            s.quit()
            messagebox.showinfo("RAJ bank","email is sent")
            
            convar.commit()
            convar
            clear()
    except:
        root=Tk()
        root.withdraw()
        messagebox.showinfo("RAJ bank","check your email or connection!")
        
            
def cashbookwinf():
    global mycur
    global cashbookwin
    
    global csearch
    global cacc
    global cname
    global cbal
    global cphno
    global cmail
    global cwdwl
    global cdeposit
    global fbal
    global trv
    
    cashbookwin=Tk()
    cashbookwin.geometry('1400x700+50+50')
    cashbookwin.configure(background='maroon')
    cashbookwin.title('RAJ bank',)

    csearch=StringVar(cashbookwin)
    cacc=StringVar(cashbookwin)
    cname=StringVar(cashbookwin)
    cbal=IntVar(cashbookwin)
    cphno=StringVar(cashbookwin)
    cmail=StringVar(cashbookwin)
    cwdwl=IntVar(cashbookwin)
    cdeposit=IntVar(cashbookwin)
    fbal=IntVar(cashbookwin)
    
    cashbookw=LabelFrame(cashbookwin,text='Cashbook',bg='light pink',font=('Monotype Corsiva',20))
    cashbookw.pack(fill='both',expand='yes',padx='20',pady='10')
    
    updatew=LabelFrame(cashbookwin,text='Update',bg='light pink',font=('Monotype Corsiva',20))
    updatew.pack(fill='both',expand='yes',padx='20',pady='10')
    
    trv=ttk.Treeview(cashbookw,columns=(1,2,3,4,5,6),show='headings')
    trv.pack()
    
    trv.heading(1,text='accountno')
    trv.heading(2,text='firstname')
    trv.heading(3,text='lastname')
    trv.heading(4,text='email')
    trv.heading(5,text='phoneno')
    trv.heading(6,text='Closing Balance')
    
    trv.bind('<Double 1>',getrow)
    
    searchlbl=Label(updatew,text='Search :',font=('Gabriola',15),bg='light pink',fg='black')
    searchlbl.grid(row=1,column=1,padx='5',pady='3')
    
    searchentry=Entry(updatew,bd=4,textvariable=csearch)
    searchentry.grid(row=1,column=2,padx='5',pady='3')
    
    searchbttn=Button(updatew,text="   SEARCH   ",activebackground='violet',command=search)
    searchbttn.grid(row=1,column=3)
    
    clearbttn=Button(updatew,text="     CLEAR     ",activebackground='violet',command=clear)
    clearbttn.grid(row=1,column=4,padx='6',pady='3')
    
    acclbl=Label(updatew,text='Account no:',font=('Gabriola',15),bg='light pink')
    acclbl.grid(row=2,column=1,padx='5',pady='3')
    
    accentry=Entry(updatew,bd=4,textvariable=cacc)
    accentry.grid(row=2,column=2,padx='5',pady='3')
    
    namelbl=Label(updatew,text='Name :',font=('Gabriola',15),bg='light pink')
    namelbl.grid(row=3,column=1,padx='5',pady='3')
    
    nameentry=Entry(updatew,bd=4,textvariable=cname)
    nameentry.grid(row=3,column=2,padx='5',pady='3')
    
    ballbl=Label(updatew,text='Balance :',font=('Gabriola',15),bg='light pink')
    ballbl.grid(row=4,column=1,padx='5',pady='3')
    
    balentry=Entry(updatew,bd=4,textvariable=cbal)
    balentry.grid(row=4,column=2,padx='5',pady='3')

    phlbl=Label(updatew,text='Phone no. :',font=('Gabriola',15),bg='light pink')
    phlbl.grid(row=5,column=1,padx='5',pady='3')
    
    phentry=Entry(updatew,bd=4,textvariable=cphno)
    phentry.grid(row=5,column=2,padx='5',pady='3')

    maillbl=Label(updatew,text='Email :',font=('Gabriola',15),bg='light pink')
    maillbl.grid(row=6,column=1,padx='5',pady='3')
    
    mailentry=Entry(updatew,bd=4,textvariable=cmail)
    mailentry.grid(row=6,column=2,padx='10',pady='3')
    
    withdrawllbl=Label(updatew,text='Withdrawl :',font=('Gabriola'),bg='light pink')
    withdrawllbl.grid(row=2,column=5,padx='50',pady='3')
    
    withdrawlentry=Entry(updatew,bd=4,textvariable=cwdwl)
    withdrawlentry.grid(row=2,column=6,padx='0',pady='3')

    depositlbl=Label(updatew,text='Deposit :',font=('Gabriola'),bg='light pink')
    depositlbl.grid(row=3,column=5,padx='50',pady='3')
    
    depositentry=Entry(updatew,bd=4,textvariable=cdeposit)
    depositentry.grid(row=3,column=6,padx='0',pady='3')

    fballbl=Label(updatew,text='final balance :',font=('Gabriola'),bg='light pink')
    fballbl.grid(row=4,column=5,padx='50',pady='3')

    fbalentry=Entry(updatew,bd=4,textvariable=fbal)
    fbalentry.grid(row=4,column=6,padx='0',pady='3')
   
    delbttn=Button(updatew,text="   DELETE   ",activebackground='violet',command=delete)
    delbttn.grid(row=3,column=7,padx='50',pady='3')

    updatebttn=Button(updatew,text="   UPDATE   ",activebackground='violet',command=update2)
    updatebttn.grid(row=3,column=8,padx='50',pady='3')

    exitbttn=Button(updatew,text="      EXIT      ",activebackground='violet',fg='maroon',command=cashbookwincloser)
    exitbttn.grid(row=3,column=9,padx='50',pady='3')

    logoutbttn=Button(updatew,text="      Logout      ",activebackground='violet',fg='maroon',command=cashbookwincloser2)
    logoutbttn.grid(row=5,column=9,padx='50',pady='3')

    viewallbttn=Button(updatew,text="      view all      ",activebackground='violet',command=viewall)
    viewallbttn.grid(row=5,column=8,padx='50',pady='3')
    
    
welwinf()
   
    
    
