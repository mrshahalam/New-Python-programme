import tkinter as tk
from  tkinter import filedialog,Text
import  os
root  = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps = tempApps.split(',')
        apps = [ x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children(): #delete the first selected directory... from the ui
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/",title="Select File",
                                        filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame,text=app,bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root,height=600,width=600,bg="#263D42")
canvas.pack()

frame = tk.Frame(root,bg="white") # for white area....
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1) #..............
openFile = tk.Button(root,text="Open File",padx=8,pady=4,fg="white",bg="#263042",command=addApp)
openFile.pack()
runApps= tk.Button(root,text="Run Apps",padx=8,pady=4,fg="white",bg="#263042",command=runApps)
runApps.pack()

for app in apps:
    label  = tk.Label(frame,text=app)
    label.pack()

root.mainloop()

with open('save.txt','w') as f:
    for  app in apps:
        f.write(app+',')
