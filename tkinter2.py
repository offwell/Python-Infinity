import tkinter as tk
from tkinter import messagebox

def validar_login():
    email = entry_email.get()
    senha = entry_senha.get()
    
    if len(senha) <= 6:
        messagebox.showerror("Erro", "A senha deve ter mais de 6 caracteres")
    elif '@' not in email:
        messagebox.showerror("Erro", "O email deve conter '@'")
    else:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso")

root = tk.Tk()
root.title("Login")

label_email = tk.Label(root, text="Email:")
label_email.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=5)

label_senha = tk.Label(root, text="Senha:")
label_senha.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_senha = tk.Entry(root, show="*")
entry_senha.grid(row=1, column=1, padx=10, pady=5)

button_login = tk.Button(root, text="Login", command=validar_login)
button_login.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
