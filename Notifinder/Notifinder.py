import tkinter as tk
from tkinter import messagebox
from notifypy import Notify
from datetime import datetime
from twilio.rest import Client
import time
from datetime import datetime

def clear():
    title.delete(0, 'end')
    message.delete(0, 'end')
    Time.delete(0, 'end')

def submit():
    messagebox.showinfo("Notifinder", "Successfully saved")
    time.sleep(2)
    root.iconify()
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    userTime = varTime.get()

    stringTime = str(current_time)

    hour= int(userTime[0]+userTime[1])-int(stringTime[0]+stringTime[1])
    minute = int(userTime[3]+userTime[4])-int(stringTime[3]+stringTime[4])
    second = int(userTime[6]+userTime[7])-int(stringTime[6]+stringTime[7])

    totalTime = (hour*60*60)+(minute*60)+second

    time.sleep(totalTime)
    notification = Notify()
    notification.title = varTitle.get()
    notification.message = varMessage.get()
    notification._notification_application_name = "Notifinder"
    notification.icon = "<Enter here>"                                                          #Here enter the directory of icon which is attached with it
    notification.audio = "<Enter here>"                                                         #Here enter the directory of audio for notification which is attached with it
    notification.send()
    title.delete(0, 'end')
    message.delete(0, 'end')
    Time.delete(0, 'end')

    # Your Account Sid and Auth Token from twilio.com / console 
    account_sid = '<Enter here>'                                                                #Here enter the account sid from twilio
    auth_token = '<Enter here>'                                                                 #Here enter the authentication token from twilio
    
    client = Client(account_sid, auth_token) 
    
    ''' Change the value of 'from' with the number  
    received from Twilio and the value of 'to' 
    with the number in which you want to send message.'''
    msg = client.messages.create(
                                from_='+<Enter here>',                                          #Here enter the sender's Mobile Number...You can get it from Twilio
                                body = "Notifinder, Did you forgot something?...",              #Can customise your message
                                to ='+<Enter here>'                                             #here enter receiver's Mobile Number
                                ) 
    
    print(msg.sid)

    root.state('zoomed')

root = tk.Tk()
root.title("Notifinder")
root.geometry("1200x700")
root.configure(background="#89ABE3")

varTitle = tk.StringVar()
varMessage = tk.StringVar()
varTime = tk.StringVar()
varDate = tk.StringVar()

tk.Label(bg="#89ABE3").grid(row=0,pady=(25))
tk.Label(root, text='NOTIFINDER', bg="#89ABE3", fg="#89e3c1", font="system 25 bold").grid(row=1, column=1, pady=(30))
tk.Label(root, text='TITLE', bg="#89ABE3", fg="#FCF6F5", font="Times 18 bold").grid(row=2, padx=(100), pady=(25))
tk.Label(root, text='MESSAGE', bg="#89ABE3", fg="#FCF6F5", font="Times 18 bold").grid(row=3, padx=(100), pady=(25))

title = tk.Entry(root, bg="#89ABE3", fg="#152e58", borderwidth=2, relief="sunken", width=40, font="Arial 20 normal", textvariable = varTitle)
message = tk.Entry(root, bg="#89ABE3", fg="#152e58", borderwidth=2, relief="sunken", width=40, font="Arial 20 normal", textvariable= varMessage)

title.grid(row=2, column=1,padx=(0))
message.grid(row=3, column=1,padx=(0))

tk.Label(root, text='TIME', bg="#89ABE3", fg="#FCF6F5", font="Times 18 bold").grid(row=4, padx=(100))
Time = tk.Entry(root, bg="#89ABE3", fg="#152e58", borderwidth=2, relief="sunken", width=20, font="Arial 20 normal", textvariable = varTime)
Time.grid(row=4, column=1,padx=(0))

tk.Label(root, text='(HH:MM:SS)', bg="#89ABE3", fg="#FCF6F5", font="Times 10 bold").grid(row=5, padx=(100))

tk.Button(root, text="SUBMIT", bg="#89ABE3", fg="#152e58", borderwidth=2, relief="sunken", width=10, font="Arial 20 bold", command= submit).grid(row=6,column=1,pady=(25))
tk.Button(root, text="CLEAR", bg="#89ABE3", fg="#152e58", borderwidth=2, relief="sunken", width=10, font="Arial 20 bold", command= clear).grid(row=7,column=1)

root.mainloop()
