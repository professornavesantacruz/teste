import tkinter as tk

def submit_form():
    name = name_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    
    # Você pode adicionar aqui a lógica para processar os dados do formulário
    # Por exemplo, salvar os dados em um arquivo ou enviar para um banco de dados
    
    # Exibindo os dados na saída
    print("Nome:", name)
    print("Login:", login)
    print("Senha:", password)
    name_entry.delete(0,tk.END)
    login_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)


# Criar a janela principal
window = tk.Tk()
window.title("Formulário")
window.geometry("300x200")

# Criar os rótulos e campos de entrada
name_label = tk.Label(window, text="Nome:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

login_label = tk.Label(window, text="Login:")
login_label.pack()
login_entry = tk.Entry(window)
login_entry.pack()

password_label = tk.Label(window, text="Senha:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Criar o botão de envio
submit_button = tk.Button(window, text="Enviar", command=submit_form)
submit_button.pack()

# Iniciar o loop principal da janela
window.mainloop()
