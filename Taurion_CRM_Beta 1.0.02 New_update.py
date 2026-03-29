import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ==================== JANELA DE LOGIN ====================
root_login = tk.Tk()
root_login.title("TAURION - Login")
root_login.geometry("620x520")
root_login.configure(bg="#0F1620")
root_login.resizable(True, True)

style = ttk.Style()
style.theme_use('clam')

tk.Label(root_login, text="TAURION v1.0.001", font=("Arial", 22, "bold"), fg="#FFD700", bg="#0F1620").pack(pady=30)

tk.Label(root_login, text="Digite seu login:", font=("Arial", 12), fg="white", bg="#0F1620").pack(pady=8)
entrada_nome = tk.Entry(root_login, font=("Arial", 12), width=35, justify="center")
entrada_nome.pack(pady=5)

tk.Label(root_login, text="Digite sua senha:", font=("Arial", 12), fg="white", bg="#0F1620").pack(pady=15)
entrada_senha = tk.Entry(root_login, font=("Arial", 12), width=35, show="*", justify="center")
entrada_senha.pack(pady=5)

tk.Label(root_login, text="Desenvolvido por Maik Willian", font=("Arial", 10), fg="gray", bg="#0F1620").pack(pady=20)

usuarios_validos = ["Maik", "Vendedor_Gomes", "Suporte_Pedro", "CFO_Will", "A"]
senha_correta = "A"
tentativas = 0
max_tentativas = 5


def verificar_login():
    global tentativas
    usuario = entrada_nome.get().strip()
    senha = entrada_senha.get().strip()

    if not usuario:
        messagebox.showwarning("Aviso", "Digite seu nome de usuário.")
        return
    if usuario not in usuarios_validos:
        messagebox.showerror("Erro", "Usuário inválido!")
        return

    if senha == senha_correta:
        messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario}!")
        root_login.destroy()
        criar_janela_Taurion(usuario)
    else:
        tentativas += 1
        if tentativas >= max_tentativas:
            messagebox.showerror("Sistema Bloqueado", "Contate um administrador.")
            root_login.destroy()
        else:
            messagebox.showwarning("Erro", f"Senha incorreta. Tentativa {tentativas}/{max_tentativas}")


# ==================== FUNÇÃO PARA ABRIR JANELA COSMO ====================
def abrir_janela_cosmo():
    Cosmo = tk.Tk()
    Cosmo.title("COSMO - Gerenciamento de Vendedores")
    Cosmo.geometry("1400x900")
    Cosmo.minsize(1000, 600)
    Cosmo.configure(bg="#152843")

    tk.Label(Cosmo, text="COSMO", font=("Arial", 28, "bold"), fg="#FFD700", bg="#152843").pack(pady=30)
    tk.Label(Cosmo, text="Gerenciamento de Vendedores", 
             font=("Arial", 16), fg="white", bg="#152843").pack(pady=5)

    tk.Label(Cosmo, text="Aqui você poderá cadastrar, editar e visualizar vendedores", 
             font=("Arial", 12), fg="#CCCCCC", bg="#152843").pack(pady=20)

    btn_cadastrar = tk.Button(Cosmo, text="Cadastrar Novo Vendedor", 
                              font=("Arial", 12), bg="#FFD700", fg="black", 
                              width=30, height=2)
    btn_cadastrar.pack(pady=30)

    Cosmo.mainloop()


# ==================== JANELA PRINCIPAL TAURION ====================
def criar_janela_Taurion(usuario):
    Taurion = tk.Tk()
    Taurion.title(f"TAURION - {usuario}")
    Taurion.geometry("1920x1080")
    Taurion.minsize(1300, 750)
    Taurion.configure(bg="#0F1620")

    # Cabeçalho
    header = tk.Frame(Taurion, bg="#1A2332", height=100)
    header.pack(fill="x")
    header.pack_propagate(False)
    tk.Label(header, text="TAURION", font=("Arial", 24, "bold"), fg="#FFD700", bg="#1A2332").pack(pady=15)
    tk.Label(header, text=f"Usuário: {usuario}   |   Sistema de Gestão Comercial", 
             font=("Arial", 12), fg="#CCCCCC", bg="#1A2332").pack()

    # Notebook
    abas = ttk.Notebook(Taurion)
    abas.pack(expand=True, fill="both", padx=20, pady=20)

    # Aba PEDIDOS DE VENDA
    aba_taurion = ttk.Frame(abas)
    abas.add(aba_taurion, text="PEDIDOS DE VENDA")
    tk.Label(aba_taurion, text="PEDIDOS DE VENDA", font=("Arial", 20, "bold"), fg="#FFD700").pack(pady=40)

    # ==================== ABA COSMOS ====================
    aba_cosmos = ttk.Frame(abas)
    abas.add(aba_cosmos, text="COSMOS")

    tk.Label(aba_cosmos, text="COSMOS - Gerenciamento de Vendedores", 
             font=("Arial", 18, "bold")).pack(pady=30)

    # ← BOTÃO CORRIGIDO AQUI
    btn_abrir_cosmo = ttk.Button(aba_cosmos, 
                                 text="Abrir Janela Cosmo",
                                 command=abrir_janela_cosmo)
    btn_abrir_cosmo.pack(pady=20)

    # ==================== OUTRAS ABAS ====================
    aba_gemini = ttk.Frame(abas)
    abas.add(aba_gemini, text="CLIENTES X LEADS")
    tk.Label(aba_gemini, text="Clientes Potenciais e Leads", font=("Arial", 18, "bold")).pack(pady=30)

    # ==================== ABA LOGISTICA ====================
    aba_pegasus = ttk.Frame(abas)
    abas.add(aba_pegasus, text="LOGISTICA")

    tk.Label(aba_pegasus, text="LOGISTICA - Logística e Transporte", 
             font=("Arial", 18, "bold")).pack(pady=15)

    # Botão + Tabela (ordem corrigida)
    btn_carregar = ttk.Button(aba_pegasus, text="📂 Carregar arquivo Logística (logistica.txt)", 
                              command=lambda: carregar_logistica(tree))
    btn_carregar.pack(pady=10)

    # Tabela
    colunas = ("motorista", "caminhão", "tipo_caminhão", "transportadora", 
               "cubagem", "preço", "destino", "status")

    tree = ttk.Treeview(aba_pegasus, columns=colunas, show="headings", height=25)

    for col, text in zip(colunas, ["Motorista", "Caminhão", "Tipo Caminhão", "Transportadora", 
                                   "Cubagem (m³)", "Preço (R$)", "Destino", "Status"]):
        tree.heading(col, text=text)
        tree.column(col, width=140 if col != "motorista" else 180)

    tree.pack(expand=True, fill="both", padx=10, pady=10)

    scrollbar = ttk.Scrollbar(aba_pegasus, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Função carregar_logistica (agora definida ANTES de ser usada)
    def carregar_logistica(tree_widget):
        try:
            with open("logistica.txt", "r", encoding="utf-8") as f:
                linhas = f.readlines()

            for item in tree_widget.get_children():
                tree_widget.delete(item)

            for linha in linhas[1:]:
                linha = linha.strip()
                if not linha:
                    continue
                dados = [x.strip() for x in linha.split(",")]
                if len(dados) == 8:
                    tree_widget.insert("", "end", values=dados)

            messagebox.showinfo("Sucesso", "Dados carregados!")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'logistica.txt' não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Outras abas
    for nome, titulo in [("LIBERAÇÃO PEDIDOS", "SAGA - Liberação de Pedidos"), 
                         ("FATURAMENTO", "ARIES - Faturamento")]:
        aba = ttk.Frame(abas)
        abas.add(aba, text=nome)
        tk.Label(aba, text=titulo, font=("Arial", 18, "bold")).pack(pady=30)

    Taurion.mainloop()


# ==================== BOTÃO DE LOGIN ====================
btn_login = tk.Button(root_login, text="ENTRAR NO SISTEMA", font=("Arial", 14, "bold"),
                      fg="white", bg="#C68E03", height=2, width=25,
                      command=verificar_login)
btn_login.pack(pady=50)

root_login.mainloop()