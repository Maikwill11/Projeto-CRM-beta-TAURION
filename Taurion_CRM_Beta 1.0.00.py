#importações
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# login NOTE: Futura atualização de melhoria de aparência 
root_login = tk.Tk()
root_login.title("Taurion") #nome sistema
root_login.geometry("620x520")
root_login.configure(bg="#0F1620") # cor preto azulado
root_login.resizable(True, True)

style = ttk.Style()
style.theme_use('clam') #temas: clam, alt, default, classic

# Título do Login
tk.Label(root_login, text= "TAURION v1.0.001" , font=("Arial", 22, "bold"), fg="#FFD700", bg="#0F1620").pack(pady=30)

tk.Label(root_login, text="Digite seu login:", font=("Arial", 12), fg="white", bg="#0F1620").pack(pady=8)
entrada_nome = tk.Entry(root_login, font=("Arial", 12), width=35, justify="center")
entrada_nome.pack(pady=5)

tk.Label(root_login, text="Digite sua senha:", font=("Arial", 12), fg="white", bg="#0F1620").pack(pady=15)
entrada_senha = tk.Entry(root_login, font=("Arial", 12), width=35, show="*", justify="center")
entrada_senha.pack(pady=5)

tk.Label(root_login, text="Desenvolvido por Maik Willian", font=("Arial", 12), fg="white", bg="#0F1620").pack(pady=9)


#Regras de Login
usuarios_validos = ["Maik", "Vendedor_Gomes", "Suporte_Pedro", "CFO_Will"] #Usuarios permitidos
senha_correta = "AB"
tentativas = 0
max_tentativas = 5

#verficação de login
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
        root_login.destroy()                    # Fecha login
        criar_janela_Taurion(usuario)           # Abre a janela principal e chama a janela Taurion
    else:
        tentativas += 1
        if tentativas >= max_tentativas:
            messagebox.showerror("Sistema Bloqueado", "Contate um adminstrador.") # NOTE: Atualização futura pensada no admin
            root_login.destroy()                                                  # para desbloquear o sistema travado
        else:
            messagebox.showwarning("Erro", f"Senha incorreta. Tentativa {tentativas}/{max_tentativas}")


def criar_janela_Taurion(usuario):
    
    
    Taurion = tk.Tk()
    Taurion.title(f"Taurion - {usuario}")
    Taurion.geometry("1920x1080")
    Taurion.minsize(1300, 750)
    Taurion.configure(bg="#0F1620")

    # Cabeçalho
    header = tk.Frame(Taurion, bg="#1A2332", height=100)
    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(header, text="TAURION", 
             font=("Arial", 24, "bold"), fg="#FFD700", bg="#1A2332").pack(pady=15)
    
    tk.Label(header, text=f"Usuário: {usuario}   |   Sistema de Gestão Comercial", 
             font=("Arial", 12), fg="#CCCCCC", bg="#1A2332").pack()

    # NOTE modulo de notebook com abas 
    abas = ttk.Notebook(Taurion)
    abas.pack(expand=True, fill="both", padx=20, pady=20)

    # ==================== TAURION - ABA PRINCIPAL PEDIDOS DE VENDA  ====================
    aba_taurion = ttk.Frame(abas)
    abas.add(aba_taurion, text="            PEDIDOS DE VENDA         ")

    tk.Label(aba_taurion, text="PEDIDOS DE VENDA", 
             font=("Arial", 20, "bold"), fg="#FFD700").pack(pady=40)
    tk.Label(aba_taurion, text="Visão Geral do CRM • Indicadores • Resumo do Dia", 
             font=("Arial", 13)).pack(pady=10)
    
    colunas = ("Pedido", "Cliente", "Produto", "Quantidade", "Unidade_Med", "Transporte", "ICMS")




    # ==================== COSMOS - Vendedores ====================
    aba_cosmos = ttk.Frame(abas)
    abas.add(aba_cosmos, text="         COSMOS          ")

    tk.Label(aba_cosmos, text="COSMOS - Gerenciamento de Vendedores", 
             font=("Arial", 18, "bold")).pack(pady=30)
    tk.Label(aba_cosmos, text="Consulta, cadastro e desempenho dos vendedores", 
             font=("Arial", 12)).pack()

    # ====================  Clientes ====================
    aba_gemini = ttk.Frame(abas)
    abas.add(aba_gemini, text="         CLIENTES X LEADS         ") #criar uma janela, não fzer parte do Tarurion mas sim do Cosmos
    # NOTE:Implementação de particularidades de clientes criar arquivo beta (criar nova janela pensando na 
    # modularidade de janelas com o cliente com vário monitores)

    tk.Label(aba_gemini, text=" Clientes Potenciais  e Leads", 
             font=("Arial", 18, "bold")).pack(pady=30)

    # ==================== LOGISTICA DE PEDIDOS - Pedidos ====================
    #Implementar aqui os calculos de cubagem, transportadoras, tipo caminhão, dados losgisticos gerais : carga, carga avalida, entrega, destino, status,

    aba_pegasus = ttk.Frame(abas)
    abas.add(aba_pegasus, text="            LOGISTICA           ") 
# incluir aba de lead_time ou fazer uma planilha para tal e se guiar pela planilha formalizada

    tk.Label(aba_pegasus, text="LOGISTICA - Logística e Transporte", 
             font=("Arial", 18, "bold")).pack(pady=15)

    # Botão para carregar o arquivo
    btn_carregar = ttk.Button(aba_pegasus, text="📂 Carregar arquivo Logística (logistica.txt)", 
                              command=lambda: carregar_logistica(tree))
    btn_carregar.pack(pady=10)

    # ==================== TABELA (Treeview) ====================
    # Definir colunas
    colunas = ("motorista", "caminhão", "tipo_caminhão", "transportadora", 
               "cubagem", "preço", "destino", "status")

    tree = ttk.Treeview(aba_pegasus, columns=colunas, show="headings", height=25)

    # Cabeçalhos
    tree.heading("motorista", text="Motorista")
    tree.heading("caminhão", text="Caminhão")
    tree.heading("tipo_caminhão", text="Tipo Caminhão")
    tree.heading("transportadora", text="Transportadora")
    tree.heading("cubagem", text="Cubagem (m³)")
    tree.heading("preço", text="Preço (R$)")
    tree.heading("destino", text="Destino")
    tree.heading("status", text="Status")

    # Largura das colunas
    tree.column("motorista", width=180)
    tree.column("caminhão", width=120)
    tree.column("tipo_caminhão", width=140)
    tree.column("transportadora", width=160)
    tree.column("cubagem", width=100)
    tree.column("preço", width=100)
    tree.column("destino", width=160)
    tree.column("status", width=130)

    tree.pack(expand=True, fill="both", padx=10, pady=10)

    # Scrollbar vertical
    scrollbar = ttk.Scrollbar(aba_pegasus, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Função para carregar o arquivo TXT
    def carregar_logistica(tree_widget):
        try:
            with open("logistica.txt", "r", encoding="utf-8") as f:
                linhas = f.readlines()

            # Limpa a tabela antes de carregar
            for item in tree_widget.get_children():
                tree_widget.delete(item)

            for linha in linhas[1:]:  # pula o cabeçalho
                if linha.strip() == "":
                    continue
                dados = linha.strip().split(",")
                if len(dados) == 8:
                    tree_widget.insert("", "end", values=dados)

            messagebox.showinfo("Sucesso", "Dados de logística carregados com sucesso!")

        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'logistica.txt' não encontrado!\nCrie o arquivo na mesma pasta do programa.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler o arquivo:\n{str(e)}")
    










    tk.Label(aba_pegasus, text="PEGASUS - Gerenciamento de Pedidos", 
             font=("Arial", 18, "bold")).pack(pady=30)

    # ====================  - Liberação de Pedidos ====================
    aba_saga = ttk.Frame(abas)
    abas.add(aba_saga, text="           LIBERAÇÃO PEDIDOS           ")

    tk.Label(aba_saga, text="SAGA - Liberação e Aprovação de Pedidos", 
             font=("Arial", 18, "bold")).pack(pady=30)

    # ==================== - Faturamento ====================
    aba_aries = ttk.Frame(abas)
    abas.add(aba_aries, text="          FATURAMENTO         ")

    tk.Label(aba_aries, text="ARIES - Faturamento e Financeiro", 
             font=("Arial", 18, "bold")).pack(pady=30)

    Taurion.mainloop()


# ==================== BOTÃO DE LOGIN ====================
btn_login = tk.Button(root_login, text="ENTRAR NO SISTEMA", font=("Arial", 14, "bold"),
                      fg="white", bg="#C68E03", height=2, width=25,
                      command=verificar_login)
btn_login.pack(pady=50)

root_login.mainloop()