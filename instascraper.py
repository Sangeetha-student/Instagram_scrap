### Instagram Scrapper Based on Python Tkinter
### Made by Vishal
### Python3
from tkinter import *, Button, Entry, Label, Tk, mainloop
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk

####################################################################################
def printtext(event):
    r = Tk()   
    r.configure(background='white')
    string = e1.get()
    r.title("Instagram of "+string)
    url = "https://www.instagram.com/{}/".format(string)
    x = requests.get(url)
    soup = BeautifulSoup(x.content, "html.parser")  
    Label(r,text="Instagram Scrappy",height=1,width=40,bg="white").grid(row=0,padx=10,pady=10)
    Label(r,text="Username:",height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=1,padx=10,pady=10)
    Label(r,text=e1.get(),height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=1,column=1,padx=20,pady=10)
    lis=''.join(map(str,soup)) #Converted to String
    followc = lis[lis.find('edge_follow')-1:lis.find('edge_follow')+100]  #To find a particular substring from string
    postc=lis[lis.find('edge_owner_to_timeline_media')+39:lis.find('edge_owner_to_timeline_media')+47]
    
    ### Followers 
    Label(r,text="Followers:",height=1,width=40,bg="white",borderwidth=2,relief="solid").grid(row=2,padx=10,pady=10)
    Label(r,text=followc[followc.find("{")+9:followc.find("}")],height=1,width=40,bg="white",borderwidth=2,relief="solid").grid(row=2,column=1,padx=20,pady=10)
    
    ### Following 
    follows = followc[followc.find("}")+52:followc.find(",\"follows")]
    Label(r,text="Following:",height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=3,padx=10,pady=10)
    if (follows.find("}")>1):
        
        Label(r,text=follows[:follows.find("}")],height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=3,column=1,padx=20,pady=10)
    
    else:
        Label(r,text=follows,height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=3,column=1,padx=20,pady=10)
        
    #Total Posts
    Label(r,text="Total Posts:",height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=4,padx=10,pady=10)
    Label(r,text=postc[:postc.find(",")],height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=4,column=1,padx=20,pady=10)
        
    Button(r, text='Exit', width=20, command=r.destroy,bg="white",borderwidth=2,relief="solid").grid(row=5,pady=20)
    mainloop()
##########################################    

master = Tk()
master.title("Instagram")
master.configure(background='white') 
Label(master, text='Enter Username',height=1,width=30,bg="white",borderwidth=2, relief="solid").grid(row=0,padx=10,pady=10) 
e1 = Entry(master) #Input Widget
e1.configure(background='white',width=30,borderwidth=2, relief="solid")
e1.grid(row=0, column=3,padx=30,pady=20)
e1.bind('<Return>',printtext) #Binding Function
button = Button(master, text='Exit', width=20, command=master.destroy,bg="white",borderwidth=2,relief="solid").grid(row=2,pady=20,padx=50)
mainloop()

