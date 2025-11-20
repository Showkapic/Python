from tkinter import Tk, Button, Label, Frame
class Window(Tk):

    def __init__(self):
        
        super().__init__()

        #Grid Definition
        for i in range (3):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        #Settings Buttons
        button_dict = {"fg": "black", "font": ("Arial", 20, "bold")}
        grid_dict = {"sticky": "nswe", "padx":10, "pady":10}

        #Buttons Grid Creation
        self.button = []
        for r in range(3):
            row = []
            for c in range(3):
                button = Button(self,
                                text = "",
                                command=lambda col=c,row=r: self.button_click(row,col),
                                **button_dict
                                )
                button.grid(row=r,column=c, **grid_dict)
                row.append(button)
            self.button.append(row)

        #Background
        self.configure(bg="#333333")

        #Window Dimension
        self.geometry("400x400")

        #Window Title
        self.title("Tic Tac Toe")
        self.compteur=0
        
    def button_click(self, row, col):
        bouton = self.button[row][col]
        if bouton["text"].strip() == "" and self.compteur==0:
            symbole="X"
            bouton.config(text="X")
            self.compteur=1

        if bouton["text"].strip() == "" and self.compteur==1:
            symbole="O"
            bouton.config(text="O")
            self.compteur=0

        if self.check_win(symbole):
            print("Les",symbole,"ont gagné")
            self.disable_buttons()


    def check_win(self,symbole):
        b = self.button

        for r in range(3):
            if (b[r][0]["text"]==symbole and
                b[r][1]["text"]==symbole and
                b[r][2]["text"]==symbole):
                return True
            
        for c in range(3):
            if (b[c][0]["text"]==symbole and
                b[c][1]["text"]==symbole and
                b[c][2]["text"]==symbole):
                return True
            
        if (b[0][0]["text"]==symbole and
            b[1][1]["text"]==symbole and
            b[2][2]["text"]==symbole):
            return True

        if (b[0][2]["text"]==symbole and
            b[1][1]["text"]==symbole and
            b[2][0]["text"]==symbole):
            return True
    
    def disable_buttons(self):
        for r in range(3):
            for c in range(3):
                self.button[r][c]["state"] = "disabled"
    
    def IA(self,grid,signe):
        if self.compteur == 1:
            

        
window = Window()
window.mainloop()
