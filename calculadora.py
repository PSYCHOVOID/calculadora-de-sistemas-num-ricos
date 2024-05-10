import tkinter as tk

# Funções de conversão de sistemas numéricos
def decimal_para_binario(decimal):
    return bin(decimal)[2:]

def decimal_para_octal(decimal):
    return oct(decimal)[2:]

def decimal_para_hexadecimal(decimal):
    return hex(decimal)[2:]

def binario_para_decimal(binario):
    return int(binario, 2)

def binario_para_octal(binario):
    return oct(int(binario, 2))[2:]

def binario_para_hexadecimal(binario):
    return hex(int(binario, 2))[2:]

def octal_para_decimal(octal):
    return int(octal, 8)

def octal_para_binario(octal):
    return bin(int(octal, 8))[2:]

def octal_para_hexadecimal(octal):
    return hex(int(octal, 8))[2:]

def hexadecimal_para_decimal(hexadecimal):
    return int(hexadecimal, 16)

def hexadecimal_para_binario(hexadecimal):
    return bin(int(hexadecimal, 16))[2:]

def hexadecimal_para_octal(hexadecimal):
    return oct(int(hexadecimal, 16))[2:]

# Classe da calculadora Tkinter
class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.display = tk.Entry(root, font=('Arial', 18), borderwidth=2, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=7, padx=10, pady=10, sticky="ew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('DB', 1, 4), ('DO', 2, 4), ('DH', 3, 4), ('BD', 4, 4),
            ('BO', 1, 5), ('BDH', 2, 5), ('OB', 3, 5), ('OH', 4, 5),
            ('HB', 1, 6), ('HO', 2, 6), ('HBD', 3, 6), ('HOB', 4, 6)
        ]

        for (text, row, column) in buttons:
            btn = tk.Button(root, text=text, font=('Arial', 18), command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=column, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

        for i in range(7):
            root.grid_columnconfigure(i, weight=1)
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)

    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        elif value in ['DB', 'DO', 'DH', 'BD', 'BO', 'BDH', 'OB', 'OH', 'HB', 'HO', 'HBD', 'HOB']:
            try:
                entrada = self.display.get()
                if value == 'DB':
                    resultado = decimal_para_binario(int(entrada))
                elif value == 'DO':
                    resultado = decimal_para_octal(int(entrada))
                elif value == 'DH':
                    resultado = decimal_para_hexadecimal(int(entrada))
                elif value == 'BD':
                    resultado = binario_para_decimal(entrada)
                elif value == 'BO':
                    resultado = binario_para_octal(entrada)
                elif value == 'BDH':
                    resultado = binario_para_hexadecimal(entrada)
                elif value == 'OB':
                    resultado = octal_para_binario(entrada)
                elif value == 'OH':
                    resultado = octal_para_hexadecimal(entrada)
                elif value == 'HB':
                    resultado = hexadecimal_para_binario(entrada)
                elif value == 'HO':
                    resultado = hexadecimal_para_octal(entrada)
                elif value == 'HBD':
                    resultado = hexadecimal_para_decimal(entrada)
                elif value == 'HOB':
                    resultado = hexadecimal_para_binario(entrada)

                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(resultado))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        else:
            self.display.insert(tk.END, value)

# Função principal do programa
def main():
    root = tk.Tk()
    root.resizable(False, False)  # Desabilita redimensionamento da janela
    calc = Calculadora(root)
    root.mainloop()

# Executar função principal
if __name__ == "__main__":
    main()





