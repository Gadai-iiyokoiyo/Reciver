import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb

import requests
import json
import sys
import os
toggle_warn = True

if len(sys.argv) >= 2:
    serverlist = sys.argv[1]
else:
    serverlist = "https://gadaireciverserverlist.gadaidev.repl.co/"
serverroute = requests.get(serverlist).content.decode()
serverroute_json = json.loads(serverroute)
channellist = "\n".join(list(serverroute_json.keys()))

def infodialog(name,text):
    msb.showinfo(name,text)
def warndialog(name,text):
    msb.showwarning(name,text)
def errordialog(name,text):
    msb.showerror(name,text)
def questiondialog(name,text):
    msb.askquestion(name,text)
def cmdcommand(command):
    yesorno = msb.askquestion("confirmation","Do you want to execute this command?\n"+command)
    if yesorno == "yes":
        os.system(command)

def recive():
    s_id = e2.get()
    getstr = requests.get(serverroute_json[s_id]).content.decode()
    exec(getstr)

app = tk.Tk()
app.title("DataReciver")
app.geometry("700x500")
app.resizable(False,False)

e1 = ttk.Label(text = "DataReciver", font = ("Aliel", 40)).pack(side = tk.TOP)
e2 = ttk.Entry(); e2.pack(side = tk.TOP)
e3 = ttk.Button(text = "Recive", command = recive).pack(side = tk.TOP)
e4 = ttk.Label(text = channellist, font = ("Aliel", 10)).pack(side = tk.TOP)

app.mainloop()