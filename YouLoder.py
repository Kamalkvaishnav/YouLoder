from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #install pytube in cmd ....pip install pytube3

Folder_Name = ""

#function for detecting the location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose a Folder!!",fg="red")

#donwloading information of the video
def DownloadVideo():
    choice = youloderchoices.get()
    url = youloderEntry.get()

    if(len(url)>1):
        youloderError.config(text="We'll download this for you")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            youloderError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    youloderError.config(text="Your file is now downloded..cheers!!")



gui = Tk()
gui.title("YouLoder")
gui.geometry("500x400") #set window
gui.columnconfigure(0,weight=1) #this will justify all content in center.


#Just a empty text to give a proper Speacing
emptylabel3 = Label(gui,text="YouLoder",fg = "red" ,font=("Ubuntu",60, "bold"))
emptylabel3.grid()

#YouLoder Link Label
youloderLabel = Label(gui,text="Enter the URL of the Video",font=("Ubuntu",15, "bold"))
youloderLabel.grid()

#Entry Box
youloderEntryVar = StringVar()
youloderEntry = Entry(gui,width=50,textvariable=youloderEntryVar)
youloderEntry.grid()

#Error Msg
youloderError = Label(gui,text=" ",fg="red",font=("Ubuntu",10))
youloderError.grid()

#Asking save file label
saveLabel = Label(gui,text="Save the Video File here",font=("Ubuntu",15,"bold"))
saveLabel.grid()

#Just a empty text to give a proper Speacing
emptylabel1 = Label(gui,text="",font=("Ubuntu",5))
emptylabel1.grid()

#btn of save file
saveEntry = Button(gui,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#location of error msg 
locationError = Label(gui,text="",fg="red",font=("Ubuntu",10))
locationError.grid()

#Download Quality options 
youloderQuality = Label(gui,text="Select Quality",font=("Ubuntu",15, "bold"))
youloderQuality.grid()

#combobox (Choice Options)
choices = ["High Quality","Low Quality","Only Audio"]
youloderchoices = ttk.Combobox(gui,values=choices)
youloderchoices.grid()

#Just a empty text to give a proper Speacing
emptylabel2 = Label(gui,text="",font=("Ubuntu",5))
emptylabel2.grid()

#Button to download the files
downloadbtn = Button(gui,text="Donwload",width=10,bg="blue",fg="white",command=DownloadVideo)
downloadbtn.grid()

#Just a empty text to give a proper Speacing
emptylabel3 = Label(gui,text="_________________________________",font=("Ubuntu",10))
emptylabel3.grid()

#Copyrights
developerlabel = Label(gui,text="© Kamal Vaishnav",font=("Ubuntu",13))
developerlabel.grid()

#Loop for the code
gui.mainloop()
