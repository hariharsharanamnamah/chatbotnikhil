from tkinter import *
import time
import os
import pyttsx3


import tkinter.messagebox as tmsg
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
wind = Tk()
wind.title('ChatBot')
wind.geometry('1020x1020')
wind.configure(bg='#0084ff')
entry_bg = Frame(height=200,width=500,bg='white')
entry_bg.place(x=10,y=520)
xi = 0
yi = 0

def clear_message():
    global yi
    yi -= yi
    for widget in chat_bg.winfo_children():
        widget.destroy()
    yi -= 50
def send_message():
    global yi
    u = user_entry.get()
    timestamp = time.strftime('%I:%M %p')
    if u=='AMERICA' or u=='LONDON' or u=='SAUDI':
        user = Label(chat_bg,height=1,width=80,bg='#a6a6a6',fg='black',text=u+' <You  -:'+timestamp,font=12,anchor='e')
        user.place(x=xi,y=yi+80)
    elif u=='ICICI' or u=='IDBD' or u=='SBI':
        user = Label(chat_bg, height=1, width=80, bg='#a6a6a6', fg='black', text=u + ' <You  -:' + timestamp, font=12,
                     anchor='e')
        user.place(x=xi, y=yi + 140)
    elif u=='ok':
        user = Label(chat_bg, height=1, width=80, bg='#a6a6a6', fg='black', text=u + ' <You  -:' + timestamp, font=12,
                     anchor='e')
        user.place(x=xi, y=yi + 50)

    else:
        user = Label(chat_bg, height=1, width=80, bg='#a6a6a6', fg='black', text=u + ' <You  -:' + timestamp, font=12,
                     anchor='e')
        user.place(x=xi, y=yi)
    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    if 'hello' in u:
        timestamp1 = time.strftime('%I:%M %p')
        v=''
        t=int(timestamp1[0:1])
        if timestamp1.endswith("AM"):
            v="GOOD MORNING"
        elif timestamp1.endswith("PM") and t<=4 and t<=12:
            v="GOOD AFTERNOON"
        elif timestamp1.endswith("PM") and t>4 and t<=7:
            v="GOOD EVENING"
        else:
            v="GOOD NIGHT"
        bot = Label(chat_bg, height=1, width=80, bg='white', fg='black',text=' Bot>'+v+',How may i help you?       -:'+timestamp1, font=12, anchor='w')
        bot.place(x=xi, y=yi+25)
        t=v+',How may i help you?'
        engine.say(t)
        engine.runAndWait()
    elif 'how are you?' in u:
        timestamp1 = time.strftime('%I:%M %p')
        bot = Label(chat_bg, height=1, width=80, bg='white', fg='black', text=' Bot> Im fine     -:'+timestamp1, font=12, anchor='w')
        bot.place(x=xi, y=yi + 25)
        t='Im fine'
        engine.say(t)
        engine.runAndWait()
    elif u=='ICIC' or u=='IDBD' or u=='SBI':
        timestamp1 = time.strftime('%I:%M %p')
        bot = Label(chat_bg, height=1, width=80, bg='white', fg='black', text=' Bot> Your bill will be updated     -:' + timestamp1,
                    font=12, anchor='w')
        bot.place(x=xi, y=yi + 170)
        t='Your bill will be updated'
        engine.say(t)
        engine.runAndWait()
        

    elif 'what is your name?' in u:
        timestamp1 = time.strftime('%I:%M %p')
        bot = Label(chat_bg, height=1, width=80, bg='white', fg='black', text=' Bot> my name is NIKHIL    -:'+timestamp1, font=12, anchor='w')
        bot.place(x=xi, y=yi + 25)
        t='my name is NIKHIL'
        engine.say(t)
        engine.runAndWait()
    elif 'i want to book ticket' in u:
        timestamp1 = time.strftime('%I:%M %p')
        bot = Label(chat_bg, height=4, width=80, bg='white', fg='black', text=' Bot>enter your destination:WE offer travelling to:\nAMERICA,\nSAUDI,\nLONDON;-:'+timestamp1, font=8, anchor='w')
        bot.place(x=xi, y=yi + 25)
        t='enter your destination:WE offer travelling to:\nAMERICA,\nSAUDI,\nLONDON;'
        engine.say(t)
        engine.runAndWait()
        u = user_entry.get()
        user = Label(chat_bg, height=1, width=80, bg='#a6a6a6', fg='black', text=u + ' <You  ' + timestamp, font=12,anchor='e')
        user.place(x=xi, y=yi)


    elif u == 'clear':
        clear_message()
    elif u=='AMERICA' or u=='LONDON' or u=='SAUDI':
        rote=Tk()
        rote.geometry("644x467")
        Label(rote, text="WELCOME TO NIKHIL TRAVELS", font="Comicsansms 15 bold").grid(column=3)
        t='WELCOME TO NIKHIL TRAVELS'
        engine.say(t)
        engine.runAndWait()

        name = Label(rote, text="NAME")
        email = Label(rote, text="EMAIL")
        age = Label(rote, text="AGE")
        phone = Label(rote, text="PHONE")
        gender = Label(rote, text="GENDER")
        travellingfrom = Label(rote, text="TRAVELLING FROM")
        paymentmethod = Label(rote, text="PAYMENT METHOD")

        name.grid(row=1, column=2)
        email.grid(row=2, column=2)
        age.grid(row=3, column=2)
        phone.grid(row=4, column=2)
        gender.grid(row=5, column=2)
        travellingfrom.grid(row=6, column=2)
        paymentmethod.grid(row=7, column=2)

        namevalue = StringVar()
        emailvalue = StringVar()
        agevalue = StringVar()
        phonevalue = StringVar()
        gendervalue = StringVar()
        travellingfromvalue = StringVar()
        paymentmethodvalue = StringVar()
        foodservice = IntVar()

        nameentry = Entry(rote, textvariable=namevalue)
        emailentry = Entry(rote, textvariable=emailvalue)
        ageentry = Entry(rote, textvariable=agevalue)
        phoneentry = Entry(rote, textvariable=phonevalue)
        genderentry = Entry(rote, textvariable=gendervalue)
        travellingfromentry = Entry(rote, textvariable=travellingfromvalue)
        paymentmethodentry = Entry(rote, textvariable=paymentmethodvalue)

        nameentry.grid(row=1, column=3)
        emailentry.grid(row=2, column=3)
        ageentry.grid(row=3, column=3)
        phoneentry.grid(row=4, column=3)
        genderentry.grid(row=5, column=3)
        travellingfromentry.grid(row=6, column=3)
        paymentmethodentry.grid(row=7, column=3)

        def getvals1():

            with open("kl.txt", "a+") as f:
                f.write(f'''NAME:{namevalue.get()} \nEMAIL:{emailvalue.get()} \nAGE:{agevalue.get()} \nPHONE:{phonevalue.get()} \nGENDER:{gendervalue.get()} \nTRAVELLING FROM:{travellingfromvalue.get()}\n''')
                f.write(f"\n")
                print(f"our team will respond within 24hrs ")
                print(f'''NAME:{namevalue.get()} \nEMAIL:{emailvalue.get()} \nAGE:{agevalue.get()} \nPHONE:{phonevalue.get()} \nGENDER:{gendervalue.get()} \nTRAVELLING FROM:{travellingfromvalue.get()}''')

        Button(rote, text="SUBMIT TO NIKHIL TRAVELS", command=getvals1).grid(row=8, column=3)
        rote.mainloop()

    elif 'THANKS' in u:
        timestamp1 = time.strftime('%I:%M %p')
        bot = Label(chat_bg, height=1, width=80, bg='white', fg='black', text=' Bot> YOUR WELCOME        -:'+timestamp1, font=12, anchor='w')
        bot.place(x=xi, y=yi + 25)
        t='YOUR WELCOME '
        engine.say(t)
        engine.runAndWait()
        
    elif 'Do we get discount or any offer' in u:
        timestamp1 = time.strftime('%I:%M %p')
        bot = Label(chat_bg, height=7, width=80, bg='white', fg='black', text=' Bot> yes,offcourse you are our customer and our aim is to provide best offers\nyou will be getting:\n15% discount on IDBD credit card\n10% discount on ICICI credit card\n18% discount on SBI credit card\nchoose your option  '+timestamp1, font=9, anchor='w')
        bot.place(x=xi, y=yi + 25)
        u = user_entry.get()
        user = Label(chat_bg, height=1, width=80, bg='#a6a6a6', fg='black', text=u + ' <You  -:' + timestamp, font=12,anchor='e')
        user.place(x=xi, y=yi)
        t='yes,offcourse you are our customer and our aim is to provide best offers\nyou will be getting:\n15% discount on IDBD credit card\n10% discount on ICICI credit card\n18% discount on SBI credit card\nchoose your option '
        engine.say(t)
        engine.runAndWait()
    elif 'When will i get my ticket' in u:
        timestamp1 = time.strftime('%I:%M %p')
        bot = Label(chat_bg, height=3, width=80, bg='white', fg='black', text=' Bot> Our team will respond to you within 12 hours,\nif you have a good experience please rate us -:'+timestamp1, font=12, anchor='w')
        bot.place(x=xi, y=yi + 25)
        t='Our team will respond to you within 12 hours,\nif you have a good experience please rate us -:'
        engine.say(t)
        engine.runAndWait()
        u = user_entry.get()
        user = Label(chat_bg, height=1, width=80, bg='#a6a6a6', fg='black', text=u + ' <You  ' + timestamp, font=12,anchor='e')
        user.place(x=xi, y=yi)
        

    elif 'ok' in u:
        root=Tk()
        root.geometry('500x500')
        root.title('Slider scroll bar')
        def rateus():
            print(f"we have recieved your experince rating")
            tmsg.showinfo('rate us ', f"successfully submitted")

        Label(root, text="RATE US").pack()
        slider = Scale(root, from_=0, to=5, orient=HORIZONTAL, tickinterval=2.5)
        slider.pack()
        Button(root, text="RATINGS", pady=10, command=rateus).pack()
        t='we have recieved your experince rating'
        engine.say(t)
        engine.runAndWait()
        root.mainloop()
    else:
        timestamp1 = time.strftime('%I:%M %p')
        bot = Label(chat_bg, height=1, width=80, bg='white', fg='black', text=' Bot> SORRY!,I can not understand you     -:'+timestamp1, font=12, anchor='w')
        bot.place(x=xi, y=yi + 25)
        t='SORRY!,I can not understand you '
        engine.say(t)
        engine.runAndWait()
        root.mainloop()

    yi+=50
    user_entry.delete(0,'end')


hcb_text = Label(height=2,width=14, bg='#0084ff',text='NIKHIL TRAVELS',font=('Impact',20),fg='white')
hcb_text.place(x=200,y=5)
chat_bg = Frame(height=1050, width=1000, bg='#f5f5f5')
chat_bg.place(x=10,y=80)
entry_bg = Frame(height=200,width=500,bg='white')
entry_bg.place(x=10,y=520)
sendbtn_bg = Frame(height=60, width=65,bg='white')
sendbtn_bg.place(x=520,y=520)
def on_enter(e):
    user_entry.delete(0,'end')
    user_entry.config(fg='black')
def on_leave(e):
    n = user_entry.get()
    user_entry.config(fg='#5c5a5a')
    if n == '' or n == ' ':
        user_entry.insert(0,'Enter message...')
        user_entry.config(fg='#5c5a5a')
user_entry = Entry(entry_bg, width=32, bg='white',font=('Helvectica',20),relief=FLAT,border=0)
user_entry.place(x=10,y=13)
user_entry.insert(0,'Enter message...')
user_entry.config(fg='#5c5a5a')
user_entry.bind("<FocusIn>",on_enter)
user_entry.bind("<FocusOut>", on_leave)
send_button = Button(sendbtn_bg,height=1,width=3,bg='#0084ff',text='➤',font=('helvectica',20),
                     activeforeground='white',fg='white',relief=FLAT,border=0,
                     activebackground='#0084ff',command=send_message)
send_button.place(x=5,y=4)


wind.mainloop()