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

# Classe da calculadora Tkinter
class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.display = tk.Entry(root, font=('Arial', 18), borderwidth=2, relief="ridge")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('DB', 1, 4), ('DO', 2, 4), ('DH', 3, 4), ('BD', 4, 4)
        ]

        for (text, row, column) in buttons:
            btn = tk.Button(root, text=text, font=('Arial', 18), command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=column, padx=5, pady=5, ipadx=10, ipady=10)

    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        elif value == 'DB':
            try:
                decimal = int(self.display.get())
                resultado = decimal_para_binario(decimal)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(resultado))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        elif value == 'DO':
            try:
                decimal = int(self.display.get())
                resultado = decimal_para_octal(decimal)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(resultado))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        elif value == 'DH':
            try:
                decimal = int(self.display.get())
                resultado = decimal_para_hexadecimal(decimal)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(resultado))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        elif value == 'BD':
            binario = self.display.get()
            if not all(bit in '01' for bit in binario):
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
            else:
                decimal = binario_para_decimal(binario)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(decimal))
        else:
            self.display.insert(tk.END, value)

# Função principal do programa
def main():
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()

# Executar função principal
if __name__ == "__main__":
    main()
