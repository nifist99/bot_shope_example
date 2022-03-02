import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from login import id_user
import requests
import os

root = Tk()

def api_server():
        api_url='https://tanlalana.com/api/get_data'
        api_data={'id':id_user}
        r = requests.post(api_url, data=api_data)
        global json_response
        json_response = r.json()       

class WindowDraggable():

        def __init__(self, label):
                self.label = label
                label.bind('<ButtonPress-1>', self.StartMove)
                label.bind('<ButtonRelease-1>', self.StopMove)
                label.bind('<B1-Motion>', self.OnMotion)

        def StartMove(self, event):
                self.x = event.x
                self.y = event.y

        def StopMove(self, event):
                self.x = None
                self.y = None

        def OnMotion(self,event):
                x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
                y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
                root.geometry("+%s+%s" % (x, y))
                
class boot:
        def __init__(self, parent):
                self.parent = parent
                self.parent.protocol("WM_DELETE_WINDOWS", self.keluar)
                lebar=650
                tinggi=600
                setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
                setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
                self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi,setTengahX, setTengahY))
                self.parent.overrideredirect(1)
                self.parent.configure(bg="#fff")
                self.aturKomponen()
                self.auto()

        def auto(self):
            api_server()
            if(json_response['api_status']==1):
                self.entPinshope.insert(0,json_response['data']['pin_shope'])
                self.entNama.insert(0,json_response['data']['name'])
                self.entNama.config(state='disabled')
                self.entCookie.insert(END,json_response['data']['cookie'])
                self.entUrl.insert(END,json_response['data']['url'])
                self.entItemid.insert(END,json_response['data']['itemid'])
                self.entShopeid.insert(END,json_response['data']['shopeid'])
                if(json_response['data']['varian'] is None):
                        self.entVarian.insert(0,'')
                else:
                        self.entVarian.insert(0,str(json_response['data']['varian']))

                if(json_response['data']['ukuran'] is None ):
                        self.entUkuran.insert(0,'')
                else:
                        self.entUkuran.insert(0,str(json_response['data']['ukuran']))
            else:
                messagebox.showinfo(title="Peringatan", \
                                    message="HIDUPIN INTERNETNYA WOI")  


            self.showStatus.insert(END,"Selamat Datang Ngab.....\n")
            self.showStatus.insert(END,"Boot Shope Versi 1...... \n\n")
            self.showStatus.insert(END,"INI ADALAH MENU CONFIGURASI PRODUK YANG AKAN DI BELI NGAB,\nPASTIKAN TERISI SESUAI DESKRIPSI PRODUK")
            if(json_response['api_status']==1):
                self.showStatus.insert(END,"\n\nDATA DIRI")
                self.showStatus.insert(END,"\n"+"===============================================")
                self.showStatus.insert(END,'\nEMAIL :'+json_response['data']['email'])
                self.showStatus.insert(END,'\nSTATUS :'+json_response['data']['status'])

                
        def keluar(self,event=None):
                self.parent.destroy()
                
        def aturKomponen(self):
                frameWin = Frame(self.parent, bg="#3DB2FF")
                frameWin.pack(fill=X,side=TOP)
                WindowDraggable(frameWin)
                Label(frameWin, text='Tanlalana Boot Shopee Versi 1',bg="#3DB2FF",fg="white").pack(side=LEFT,padx=20)
                buttonx = Button(frameWin, text="X",fg="white", bg="#FA8072", width=6, height=2,bd=0,\
                                 activebackground="#FB8072",activeforeground="white", command=self.onClose, relief=FLAT)
                buttonx.pack(side=RIGHT)
                mainFrame = Frame(self.parent)
                mainFrame.pack(side=TOP,fill=X)
                btnFrame = Frame(self.parent)
                btnFrame.pack(side=TOP, fill=X)
                tabelFrame = Frame(self.parent)
                tabelFrame.pack(side=TOP,fill=Y)

                Label(mainFrame, text='PIN SHOPE').grid(row=1, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=1, column=1, sticky=W,pady=5,padx=10)
                self.entPinshope = Entry(mainFrame, width=30)
                self.entPinshope.grid(row=1, column=2,sticky=W)


                Label(mainFrame, text="NAMA").grid(row=2, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=2, column=1, sticky=W,pady=5,padx=10)
                self.entNama = Entry(mainFrame, width=30)
                self.entNama.grid(row=2, column=2,sticky=W)
                

                Label(mainFrame, text="COOKIE SPEC").grid(row=3, column=0, sticky=NW,padx=20)
                Label(mainFrame, text=':').grid(row=3, column=1, sticky=NW,padx=10,pady=20)
                self.entCookie = ScrolledText(mainFrame,height=4,width=45)
                self.entCookie.grid(row=3, column=2,sticky=W)

                Label(mainFrame, text="URL PRODUK ").grid(row=4, column=0, sticky=NW,padx=20)
                Label(mainFrame, text=':').grid(row=4, column=1, sticky=NW,padx=10,pady=30)
                self.entUrl = ScrolledText(mainFrame,height=4,width=45)
                self.entUrl.grid(row=4, column=2,sticky=W)

                Label(mainFrame, text="SHOPE ID").grid(row=5, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=5, column=1, sticky=W,pady=5,padx=10)
                self.entShopeid = Entry(mainFrame, width=30)
                self.entShopeid.grid(row=5, column=2,sticky=W)

                Label(mainFrame, text="ITEM ID").grid(row=6, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=6, column=1, sticky=W,pady=5,padx=10)
                self.entItemid = Entry(mainFrame, width=30)
                self.entItemid.grid(row=6, column=2,sticky=W)

                Label(mainFrame, text="VARIAN PRODUK",fg="#3DB2FF").grid(row=7, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=7, column=1, sticky=W,pady=5,padx=10)
                self.entVarian = Entry(mainFrame, width=30)
                self.entVarian.grid(row=7, column=2,sticky=W)

                Label(mainFrame, text="UKURAN PRODUK",fg="#3DB2FF").grid(row=8, column=0, sticky=W,padx=20)
                Label(mainFrame, text=':').grid(row=8, column=1, sticky=W,pady=5,padx=10)
                self.entUkuran = Entry(mainFrame, width=30)
                self.entUkuran.grid(row=8, column=2,sticky=W)


                self.btnSave = Button(btnFrame, text='Save',\
                                        command=self.onSave, width=10,\
                                        relief=FLAT, bd=2, bg="#50CB93", fg="white",activebackground="#444",activeforeground="white" )
                self.btnSave.grid(row=0, column=1,padx=20,pady=10,sticky=W)

                self.btnBotApi = Button(btnFrame, text='Click To Run Api Bot',\
                                        command=self.open_bot_1, width=20,\
                                        relief=FLAT, bd=2, bg="#297F87", fg="white",activebackground="#444",activeforeground="white" )
                self.btnBotApi.grid(row=0, column=2,padx=20,pady=10,sticky=W)

                self.btnBotTime = Button(btnFrame, text='Click To Run Time Bot',\
                                        command=self.open_bot_2, width=20,\
                                        relief=FLAT, bd=2, bg="#F6D167", fg="white",activebackground="#444",activeforeground="white" )
                self.btnBotTime.grid(row=0, column=3,padx=20,pady=10,sticky=W)

                self.showStatus = ScrolledText(tabelFrame, width=78,  height=10)
                self.showStatus.grid(row=0,column=0,padx=10,pady=1,sticky=N)
                self.showStatus.configure(bg='black',fg='green')
                self.showStatus.focus_set()
        def onClose(self, event=None):
                response=messagebox.askyesno('Exit','Are you sure you want to exit?')
                if response:
                                self.parent.destroy()
        
        def open_bot_1(self):
             v1="C:\chromedriver_win32\Api_bot.exe"
             os.system('"%s"' % v1)  
        
        def open_bot_2(self):
             v2="C:\chromedriver_win32\Time_bot.exe"
             os.system('"%s"' % v2)

        def onSave(self):
                pin = self.entPinshope.get()
                nama = self.entNama.get()
                cookie= self.entCookie.get('1.0','end')
                url=self.entUrl.get('1.0','end')
                itemid=self.entItemid.get()
                shopeid=self.entShopeid.get()
                varian=self.entVarian.get()
                ukuran=self.entUkuran.get()
                if( pin != None and cookie != None and url != None and itemid != None and shopeid != None):
                        api_url='https://tanlalana.com/api/simpan'
                        api_data={'id':id_user,'pin_shope':pin,'name':nama,'cookie':cookie,'url':url,'itemid':itemid,'shopeid':shopeid,'varian':varian,'ukuran':ukuran}
                        r = requests.post(api_url, data=api_data) 
                        print(r)
                        respon=r.json()
                        if(respon['api_status']==1):
                                txt="PIN SHOPE :"+pin+"\nNAME :"+nama+"\nCOOKIE :"+cookie+"\nURL :"+url+"\nITEMID :"+itemid+"\nSHOPEID :"+shopeid+"\nVARIAN :"+varian+"\nUKURAN :"+ukuran
                                self.showStatus.insert(END,'\n\nSuccess Save Data \n=======================================\n')
                                self.showStatus.insert(END,txt)
                                messagebox.showinfo(title="SELAMAT", \
                                    message="ACCOUNT ANDA BERHASIL DISIMPAN")
                        else:   
                                self.showStatus.insert(END,'\n\nGagal Save Data \n=======================================\n')
                                self.showStatus.insert(END,str(respon))
                                messagebox.showinfo(title="GAGAL MENYIMPAN DATA", \
                                    message="CEK LAGI DATANYA NGAB, PIN, COOKIE, URL, ITEMID, SHOPEID , JANGAN SAMPAI KOSONG")


                
def main():
    api_server()
    if(json_response['data']['status']=='notactive'):
           messagebox.showinfo(title="Peringatan", \
                                    message="ACCOUNT ANDA SUDAH DI NONACTIVEKAN SILAHKAN HUBUNGI ADMIN")
           root.destroy()

    boot(root)
    root.mainloop()

main()