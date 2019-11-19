import tkinter as tk
from PIL import Image, ImageTk


class soraGui():
    """interface graphique pour soraphone"""

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SoraPhone")
        self.window.geometry("400x600")
        self.window.iconbitmap("image/im.ico")
        self.window.config(background='#7383B1')
        self.window.resizable(width=False, height=False)
        self.numero = ""
        #self.numero.set('count = 0')
        self.clavier = tk.Frame(self.window, bg='#7383B1', bd=1)
        self.clavier.pack(expand=tk.YES)
        self.label = tk.Label(self.window, text="0", font=("Helvetica", 30), bg='#7383B1', fg='white')
        self.label.place(x=10, y=10)
        self.creerWid()


        self.window.mainloop()

    def creerWid(self):
        """creer les widget pour l'interface"""
        self.appel = self.configImage('image/im1.png')
        self.message = self.configImage('image/im2.png')
        self.endCall = self.configImage('image/im3.png')
        self.barreMenu = tk.Menu(self.window)
        self.creerMenu(self.barreMenu)
        self.creerBouton()

    def creerMenu(self, barre_menu):
        """tous les command a changer"""
        file_menu = tk.Menu(barre_menu, tearoff=0)
        file_menu.add_command(label="connexion", command=self.window.quit)
        file_menu.add_command(label="Quitter", command=self.window.quit)
        call_menu = tk.Menu(barre_menu, tearoff=0)
        call_menu.add_command(label="Repertoire", command=self.window.quit)
        call_menu.add_command(label="Journal", command=self.window.quit)
        call_menu.add_command(label="Groupes", command=self.window.quit)
        help_menu = tk.Menu(barre_menu, tearoff=0)
        help_menu.add_command(label="Outils", command=self.window.quit)
        help_menu.add_command(label="Aide", command=self.window.quit)
        barre_menu.add_cascade(label="Fichier", menu=file_menu)
        barre_menu.add_cascade(label="Appel", menu=call_menu)
        barre_menu.add_cascade(label="Aide", menu=help_menu)
        # configurer fenetre pour ajouter cette menu
        self.window.config(menu=barre_menu)

    def configImage(self, path):
        self.image = Image.open(path)
        self.image = self.image.resize((120, 80))
        self.image = ImageTk.PhotoImage(self.image)
        return self.image

    def creerBouton(self):
        self.btn=[]
        iter = 9
        for i in range(3):
           for j in range(3):
               self.btn.append(tk.Button(self.clavier,width = 5,text=str(iter),font=("Courrier", 30), bg='white',
                                         fg='#7383B1', command=lambda iter=iter :self.num(iter)).grid(row=i+1,column=j+1))
               iter -= 1

        self.btnC = tk.Button(self.clavier, text='C', width=5, font=("Courrier", 30), bg='white', fg='#7383B1', command=self.clear).grid(
            row=4, column=1)
        self.call= self.configImage('image/im1.png')
        self.btnCall = tk.Button(self.clavier, text="appeler", image=self.call, font=("Courrier", 30), bg='white', fg='#7383B1',
                         command=self.clear).grid(row=5, column=1)
        self.endCall = self.configImage('image/im3.png')
        self.btnE = tk.Button(self.clavier, text="racrocher", image=self.endCall, font=("Courrier", 30), bg='white', fg='#7383B1',
                      command=self.clear).grid(row=5, column=3)
        self.message = self.configImage('image/im2.png')
        self.btnM = tk.Button(self.clavier, text="message", image=self.message, font=("Courrier", 30), bg='white', fg='#7383B1',
                      command=self.clear).grid(row=5, column=2)
        self.btnD = tk.Button(self.clavier, text='#', width=5, font=("Courrier", 30), bg='white', fg='#7383B1',
                              command=self.clear).grid(row=4, column=3)
        self.btn0 = tk.Button(self.clavier, text='0', width=5, font=("Courrier", 30), bg='white', fg='#7383B1',
                              command=lambda :self.num(0)).grid(
            row=4, column=2)

    def num(self,i):
        self.numero += str(i)
        self.label["text"] = self.numero

    def clear(self):
        self.numero = ""
        self.label["text"] = self.numero

if __name__ == "__main__":
    camGUI = soraGui()