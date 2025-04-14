import tkinter as tk
import secrets
import string
from difflib import SequenceMatcher

class PasswordGenerator:
    def __init__(self):
        self.previous_password = ""
        
    def generate(self):
        length = int(self.spinbox.get())
        numbers = self.var1.get()
        special = self.var2.get()
        spaces = self.var3.get()
        
        characters = string.ascii_letters
        required_categories = [string.ascii_letters]
        
        if special:
            characters += string.punctuation
            required_categories.append(string.punctuation)
        if spaces:
            characters += ' '
            required_categories.append(' ')
        if numbers:
            characters += string.digits
            required_categories.append(string.digits)
        

        for _ in range(10):
            password = []
            for category in required_categories:
                password.append(secrets.choice(category))
            
            while len(password) < length:
                password.append(secrets.choice(characters))
            
            secrets.SystemRandom().shuffle(password)
            password = ''.join(password)
            
            if not self.previous_password or self.similarity(self.previous_password, password) < 0.5:
                self.previous_password = password
                self.textbox.delete(0, tk.END)
                self.textbox.insert(0, password)
                return

        self.textbox.delete(0, tk.END)
        self.textbox.insert(0, password)
    
    def similarity(self, a, b):
        return SequenceMatcher(None, a, b).ratio()
    
    def setup_ui(self, root):
        root.geometry("500x250")
        root.title("Генератор паролей")

        tk.Label(root, text="Длина пароля:").pack(pady=5)
        
        self.spinbox_var = tk.StringVar(value=12)
        self.spinbox = tk.Spinbox(root, from_=12, to=100, textvariable=self.spinbox_var)
        self.spinbox.pack(pady=5)

        self.var1 = tk.IntVar(value=1)
        self.var2 = tk.IntVar(value=1)
        self.var3 = tk.IntVar()

        tk.Checkbutton(root, text='Цифры', variable=self.var1).pack(anchor='w', padx=100)
        tk.Checkbutton(root, text='Спецсимволы', variable=self.var2).pack(anchor='w', padx=100)
        tk.Checkbutton(root, text='Пробелы', variable=self.var3).pack(anchor='w', padx=100)

        tk.Button(root, text="Сгенерировать", command=self.generate).pack(pady=15)

        self.textbox = tk.Entry(root, font=("Arial", 14), width=30)
        self.textbox.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator()
    app.setup_ui(root)
    root.mainloop()