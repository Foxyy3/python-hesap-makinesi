import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hesap Makinesi- Rimes Yazılım")
        self.geometry("400x600")
        self.resizable(0, 0)
        self.configure(bg="#2E2E2E")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self, bd=0, relief=tk.RIDGE, bg="#2E2E2E")
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), fg="#FFFFFF", bg="#2E2E2E", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0, ipadx=8, ipady=25, sticky="nsew")

        btns_frame = tk.Frame(self, bg="#2E2E2E")
        btns_frame.pack(fill=tk.BOTH, expand=True)

        buttons = [
            '7', '8', '9', 'C',
            '4', '5', '6', '/',
            '1', '2', '3', '*',
            '.', '0', '=', '+',
            '(', ')', 'DEL', '-'
        ]

        row = 0
        col = 0

        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(btns_frame, text=button, fg="#FFFFFF", bg="#333333", font=('arial', 18), width=9, height=3, bd=0, command=action).grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(4):
            btns_frame.grid_columnconfigure(i, weight=1)
            btns_frame.grid_rowconfigure(i, weight=1)

    def click_event(self, key):
        if key == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Hata sayı giriniz.")
                self.expression = ""
        elif key == "C":
            self.expression = ""
            self.input_text.set("")
        elif key == "DEL":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        else:
            self.expression += str(key)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()