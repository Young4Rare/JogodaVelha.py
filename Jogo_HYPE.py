import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        self.jogador = 'X'
        self.tabuleiro = [' '] * 9

        self.botoes = [tk.Button(root, text=' ', font=('normal', 24), width=6, height=3, command=lambda i=i: self.clique(i)) for i in range(9)]

        for i, botao in enumerate(self.botoes):
            row, col = divmod(i, 3)
            botao.grid(row=row, column=col)

    def reiniciar_jogo(self):
        self.jogador = 'X'
        self.tabuleiro = [' '] * 9
        for botao in self.botoes:
            botao['text'] = ' '
            botao['state'] = tk.NORMAL

    def clique(self, indice):
        if self.tabuleiro[indice] == ' ':
            self.tabuleiro[indice] = self.jogador
            self.botoes[indice]['text'] = self.jogador

            if self.verificar_vitoria():
                messagebox.showinfo("Fim do Jogo", f"O jogador {self.jogador} venceu!")
                self.reiniciar_jogo()
            elif ' ' not in self.tabuleiro:
                messagebox.showinfo("Fim do Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.jogador = 'O' if self.jogador == 'X' else 'X'

    def verificar_vitoria(self):
        # Verifica linhas, colunas e diagonais
        for i in range(3):
            if self.tabuleiro[i] == self.tabuleiro[i + 3] == self.tabuleiro[i + 6] != ' ':
                self.bloquear_botoes()
                return True
            if self.tabuleiro[i * 3] == self.tabuleiro[i * 3 + 1] == self.tabuleiro[i * 3 + 2] != ' ':
                self.bloquear_botoes()
                return True
        if self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] != ' ' or \
           self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] != ' ':
            self.bloquear_botoes()
            return True
        return False

    def bloquear_botoes(self):
        for botao in self.botoes:
            botao['state'] = tk.DISABLED

if __name__ == "__main__":
    root = tk.Tk()
    jogo_da_velha = JogoDaVelha(root)
    root.mainloop()
