import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculadora')
        self.geometry('340x420')
        self.resizable(False, False)
        self._criar_widgets()

    def _criar_widgets(self):
        self.entrada = tk.Entry(self, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')
        
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        for (texto, linha, coluna) in botoes:
            if texto == 'C':
                btn = tk.Button(self, text=texto, font=('Arial', 16), height=2, command=self.limpar)
                btn.grid(row=linha, column=coluna, columnspan=4, padx=5, pady=5, sticky='nsew')
            elif texto == '=':
                btn = tk.Button(self, text=texto, font=('Arial', 16), height=2, command=self.calcular)
                btn.grid(row=linha, column=coluna, padx=5, pady=5, sticky='nsew')
            else:
                btn = tk.Button(self, text=texto, font=('Arial', 16), height=2, command=lambda t=texto: self.adicionar(t))
                btn.grid(row=linha, column=coluna, padx=5, pady=5, sticky='nsew')

        # Tornar as colunas e linhas responsivas
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

    def adicionar(self, valor):
        self.entrada.insert(tk.END, valor)

    def limpar(self):
        self.entrada.delete(0, tk.END)

    def calcular(self):
        expressao = self.entrada.get()
        try:
            resultado = eval(expressao)
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(resultado))
        except Exception:
            messagebox.showerror('Erro', 'Expressão inválida')
            self.limpar()

if __name__ == '__main__':
    app = Calculadora()
    app.mainloop()
