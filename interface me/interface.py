import customtkinter as ctk

#aparencia

ctk.set_appearance_mode("dark")

#validar informacoes

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    #info a ser validada
    if usuario == "pedro" and senha == "3535":
        resultado_login.configure(text="login bem sucedido!", text_color="green")
    else:        resultado_login.configure(text="usuario ou senha incorretos", text_color="red")

    # variável global
senha_visivel = False

    # função mostrar/esconder senha
def toggle_senha():
    global senha_visivel
    if senha_visivel:
        campo_senha.configure(show="*")
        botao_ver.configure(text="ver")
        senha_visivel = False
    else:
        campo_senha.configure(show="")
        botao_ver.configure(text="esconder")
        senha_visivel = True

#tela principal

app =ctk.CTk()
app.title("tela de login")
app.geometry("1000x1000")

#label

label_usuario = ctk.CTkLabel(app, text="usuario")
label_usuario.pack(pady=10)

#entry

campo_usuario = ctk.CTkEntry(app, placeholder_text="informe seu usuario")
campo_usuario.pack(pady=10)

#label

label_senha = ctk.CTkLabel(app, text="senha")
label_senha.pack(pady=10)

#entry

campo_senha = ctk.CTkEntry(app, placeholder_text="digite sua senha", show="*")
campo_senha.pack(pady=10)

# botão mostrar/esconder
botao_ver = ctk.CTkButton(app, text="ver", command=toggle_senha)
botao_ver.pack(pady=5)

#button

button_login = ctk.CTkButton(app, text="entrar",command=validar_login)
button_login.pack(pady=10)

#feedback login

resultado_login = ctk.CTkLabel(app, text="")
resultado_login.pack(pady=10)

#iniciar aplicativo

app.mainloop()