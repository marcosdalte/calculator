import tkinter as tk
from tkinter import messagebox
import re
import operator

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

    def _avaliar_expressao_segura(self, expressao):
        """
        Avalia uma expressão matemática de forma segura, sem usar eval().
        Suporta apenas operações matemáticas básicas: +, -, *, /, números e decimais.
        """
        # Remove espaços
        expressao = expressao.replace(' ', '')
        
        # Verifica se a expressão contém apenas caracteres permitidos
        if not re.match(r'^[0-9+\-*/.()]+$', expressao):
            raise ValueError("Expressão contém caracteres inválidos")
        
        # Verifica se não há operadores consecutivos
        if re.search(r'[+\-*/]{2,}', expressao):
            raise ValueError("Operadores consecutivos não são permitidos")
        
        # Verifica se não começa ou termina com operador (exceto -)
        if re.match(r'^[+*/]', expressao) or re.search(r'[+\-*/]$', expressao):
            raise ValueError("Expressão não pode começar ou terminar com operador")
        
        # Converte a expressão em uma lista de tokens
        tokens = re.findall(r'\d+\.?\d*|[+\-*/()]', expressao)
        
        # Valida parênteses balanceados
        if tokens.count('(') != tokens.count(')'):
            raise ValueError("Parênteses não balanceados")
        
        try:
            # Usa uma abordagem segura para avaliar a expressão
            resultado = self._calcular_tokens(tokens)
            return resultado
        except ZeroDivisionError:
            raise ValueError("Divisão por zero")
        except Exception as e:
            raise ValueError(f"Erro no cálculo: {str(e)}")
    
    def _calcular_tokens(self, tokens):
        """
        Calcula o resultado dos tokens usando o algoritmo Shunting Yard
        para converter infix para postfix e depois calcular.
        """
        def precedencia(op):
            return {'+': 1, '-': 1, '*': 2, '/': 2}.get(op, 0)
        
        def aplicar_operador(op, b, a):
            ops = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv
            }
            return ops[op](a, b)
        
        # Converte infix para postfix (notação polonesa reversa)
        output = []
        operators = []
        
        i = 0
        while i < len(tokens):
            token = tokens[i]
            
            if re.match(r'\d+\.?\d*', token):
                output.append(float(token))
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove '('
            elif token in '+-*/':
                # Trata números negativos
                if token == '-' and (i == 0 or tokens[i-1] in '(+-*/'):
                    # É um número negativo
                    if i + 1 < len(tokens) and re.match(r'\d+\.?\d*', tokens[i + 1]):
                        output.append(-float(tokens[i + 1]))
                        i += 1  # Pula o próximo token
                    else:
                        raise ValueError("Operador negativo inválido")
                else:
                    while (operators and operators[-1] != '(' and 
                           precedencia(operators[-1]) >= precedencia(token)):
                        output.append(operators.pop())
                    operators.append(token)
            i += 1
        
        while operators:
            output.append(operators.pop())
        
        # Avalia a expressão postfix
        stack = []
        for token in output:
            if isinstance(token, (int, float)):
                stack.append(token)
            else:
                if len(stack) < 2:
                    raise ValueError("Expressão inválida")
                b = stack.pop()
                a = stack.pop()
                stack.append(aplicar_operador(token, b, a))
        
        if len(stack) != 1:
            raise ValueError("Expressão inválida")
        
        return stack[0]

    def calcular(self):
        expressao = self.entrada.get()
        if not expressao:
            return
        
        try:
            resultado = self._avaliar_expressao_segura(expressao)
            self.entrada.delete(0, tk.END)
            
            # Formata o resultado para evitar muitas casas decimais
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            elif isinstance(resultado, float):
                resultado = round(resultado, 10)  # Limita a 10 casas decimais
            
            self.entrada.insert(tk.END, str(resultado))
            
        except ValueError as e:
            messagebox.showerror('Erro', str(e))
            self.limpar()
        except Exception as e:
            messagebox.showerror('Erro', 'Erro inesperado no cálculo')
            self.limpar()

if __name__ == '__main__':
    app = Calculadora()
    app.mainloop()
