import tkinter as tk
import json 
import requests

#The username and webhook url are set here
username = "Ampachi"
webhook_url = "http://IP OF RECIVER/webhook"

#This is the main send function
def idk():
    name = label_a.get()
    #Stops no name
    if name != "":
        #Makes the json
        data = {'username': username, 'message': name}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        #Sends the json to the webhook
        r = requests.post(webhook_url, data=json.dumps(data), headers=headers)

#Updates the main window with the new msg
def update_text(root, label, x2,):
    r = requests.get('http://IP OF RECIVER:5000/sender')
    x = r.text
    if x != x2:
        label_c.insert("1.0", x + '\n')
        x2 = x
    else:
        pass
    window.after(1000, update_text, root, label_c, x2)

#The main window
window = tk.Tk()
window.title("Welcome to Faceblock Logged in as: " + username)


label_a = tk.Entry(master=window)
label_b = tk.Button(master=window, text="Send", command=idk, width=5, height=0)
label_c = tk.Text(master=window)

label_c.pack(side=tk.TOP)
label_b.pack(side=tk.LEFT)
label_a.pack(side=tk.LEFT)

window.after(1, update_text, window, label_c, '')

window.mainloop()
