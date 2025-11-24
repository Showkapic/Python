from tkinter import Tk, Button, Label, Frame, messagebox, Menu
import random

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

        #Turn Count
        self.compteur = 0

        # Game Mode
        self.mode = "solo"

        self.game_over = False

        # Menu
        menubar = Menu(self)
        mode_menu = Menu(menubar, tearoff=0)
        mode_menu.add_command(label="Solo (contre IA)", command=self.set_mode_solo)
        mode_menu.add_command(label="Multijoueur (2 joueurs)", command=self.set_mode_multi)
        menubar.add_cascade(label="Mode de jeu", menu=mode_menu)

        self.config(menu=menubar)
        
    def reset_board(self):
        for r in range(3):
            for c in range(3):
                self.button[r][c].config(text="", state="normal")
        self.compteur = 0
        self.game_over = False

    def set_mode_solo(self):
        self.mode = "solo"
        self.reset_board()
        messagebox.showinfo("Mode de jeu", "Mode solo (contre IA) activé.")

    def set_mode_multi(self):
        self.mode = "multi"
        self.reset_board()
        messagebox.showinfo("Mode de jeu", "Mode multijoueur activé.")

    def button_click(self, row, col):
        if self.game_over:
            return

        bouton = self.button[row][col]

        if bouton["text"].strip() != "":
            return

        # Mode Solo
        if self.mode == "solo":
            symbole = "X"
            bouton.config(text="X")

            # Victory message
            if self.check_win(symbole):
                messagebox.showinfo("Victoire!", f"Les {symbole} ont gagné")
                self.disable_buttons()
                self.game_over = True
                return

            # Nul Message
            if self.check_board_full():
                messagebox.showinfo("Match nul", "Match Nul!")
                self.disable_buttons()
                self.game_over = True
                return

            self.IA()
            return

        # Mode Multiplayer
        if self.mode == "multi":
            if self.compteur == 0:
                symbole = "X"
                bouton.config(text="X")
                self.compteur = 1
            else:
                symbole = "O"
                bouton.config(text="O")
                self.compteur = 0

            if self.check_win(symbole):
                messagebox.showinfo("Victoire!", f"Les {symbole} ont gagné")
                self.disable_buttons()
                self.game_over = True
                return

            if self.check_board_full():
                messagebox.showinfo("Match nul", "Match Nul!")
                self.disable_buttons()
                self.game_over = True
                return

    def check_board_full(self):
        for r in range(3):
            for c in range(3):
                if self.button[r][c]["text"].strip() == "":
                    return False
        return True
    
    def check_win(self, symbole):
        b = self.button

        # Lignes
        for r in range(3):
            if (b[r][0]["text"] == symbole and
                b[r][1]["text"] == symbole and
                b[r][2]["text"] == symbole):
                return True
            
        # Colonnes
        for c in range(3):
            if (b[0][c]["text"] == symbole and
                b[1][c]["text"] == symbole and
                b[2][c]["text"] == symbole):
                return True
            
        # Diagonale principale
        if (b[0][0]["text"] == symbole and
            b[1][1]["text"] == symbole and
            b[2][2]["text"] == symbole):
            return True

        # Diagonale secondaire
        if (b[0][2]["text"] == symbole and
            b[1][1]["text"] == symbole and
            b[2][0]["text"] == symbole):
            return True

        return False
  
    def disable_buttons(self):
        for r in range(3):
            for c in range(3):
                self.button[r][c]["state"] = "disabled"

    def get_board(self):
        board = []
        for r in range(3):
            row = []
            for c in range(3):
                row.append(self.button[r][c]["text"].strip())
            board.append(row)
        return board

    def gagne_board(self, board, symbole):
        # Lignes
        for r in range(3):
            if board[r][0] == board[r][1] == board[r][2] == symbole:
                return True
        # Colonnes
        for c in range(3):
            if board[0][c] == board[1][c] == board[2][c] == symbole:
                return True
        # Diagonales
        if board[0][0] == board[1][1] == board[2][2] == symbole:
            return True
        if board[0][2] == board[1][1] == board[2][0] == symbole:
            return True
        return False

    def ia_choisir_coup(self, ia="O", joueur="X"):
        board = self.get_board()

        # Liste des cases vides
        vides = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]

        if not vides:
            return None

        for r, c in vides:
            board[r][c] = ia
            if self.gagne_board(board, ia):
                board[r][c] = ""
                return (r, c)
            board[r][c] = ""

        for r, c in vides:
            board[r][c] = joueur
            if self.gagne_board(board, joueur):
                board[r][c] = ""
                return (r, c)
            board[r][c] = ""

        if (1, 1) in vides:
            return (1, 1)

        coins = [(0,0), (0,2), (2,0), (2,2)]
        coups_coins = [pos for pos in coins if pos in vides]
        if coups_coins:
            return random.choice(coups_coins)

        return random.choice(vides)

    def IA(self):
        if self.mode != "solo" or self.game_over:
            return

        coup = self.ia_choisir_coup(ia="O", joueur="X")
        if coup is None:
            return

        row, col = coup
        bouton = self.button[row][col]

        if bouton["text"].strip() != "":
            return

        bouton.config(text="O")

        if self.check_win("O"):
            messagebox.showinfo("Victoire!", "Les O ont gagné")
            self.disable_buttons()
            self.game_over = True
            return

        if self.check_board_full():
            messagebox.showinfo("Match nul", "Match Nul!")
            self.disable_buttons()
            self.game_over = True
            return
            

window = Window()
window.mainloop()