import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import threading
import time
import os
import shutil
import json
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw

# Diretorio a ser monitorado
config_path = "config.json"
rodando = False

def carregar_config():
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            return json.load(file)
    return {"diretorio": "", "intervalo": 300, "arquivos_bloqueados": [], "extensoes_bloqueadas": []}

def salvar_config(config):
    with open(config_path, "w") as file:
        json.dump(config, file)

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entry_diretorio.delete(0, tk.END)
        entry_diretorio.insert(0, pasta )

def iniciar_organizacao():
    global rodando
    if rodando:
        messagebox.showwarning("Aviso", "A organização já está em execução!")
        return
    
    diretorio = entry_diretorio.get()
    intervalo = int(entry_intervalo.get())

    if not diretorio or not os.path.exists(diretorio):
        messagebox.showerror("Erro", "Diretorio invalido")
        return
    
    config["diretorio"] = diretorio
    config["intervalo"] = intervalo
    salvar_config(config)

    rodando = True
    thread = threading.Thread(target=executar_organizacao, args=(diretorio, intervalo), daemon=True).start()
    messagebox.showinfo("Iniciando", "A organização foi iniciada!")

def parar_organizacao():
    global rodando
    rodando = False
    messagebox.showinfo("Parado", "A organização foi interrompida.")

def executar_organizacao(diretorio, intervalo):
    global rodando
    while rodando:
        organizar_pasta(diretorio)
        time.sleep(intervalo)

def organizar_pasta(diretorio):
    categorias = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
        "Áudios": [".mp3", ".wav", ".aac", ".flac"],
        "Vídeos": [".mp4", ".avi", ".mkv", ".mov"],
        "Compactados": [".zip", ".rar", ".7z", ".tar.gz"],
        "Executaveis": [".exe"],
        "Outros": []
    }
    for item in os.listdir(diretorio):
        item_path = os.path.join(diretorio, item)
        
        if os.path.isdir(item_path) or item in config["arquivos_bloqueados"]:
            continue

        _, ext = os.path.splitext(item)
        ext = ext.lower()

        if ext in config["extensoes_bloqueadas"]:
            continue

        categoria = "Outros"
        for key, extensoes in categorias.items():
            if ext in extensoes:
                categoria = key
                break

        pasta_destino = os.path.join(diretorio, categoria)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        try:
            shutil.move(item_path, os.path.join(pasta_destino, item))
        except Exception as e:
            print(f"Erro ao mover {item}: {e}")

def adicionar_arquivo_bloqueado():
    arquivo = simpledialog.askstring("Adicionar", "Digite o nome do arquivo a ser bloqueado:")
    if arquivo and arquivo not in config["arquivos_bloqueados"]:
        config["arquivos_bloqueados"].append(arquivo)
        salvar_config(config)
        messagebox.showinfo("Sucesso", "Arquivo bloqueado adiocionado!")

def remover_arquivo_bloqueado():
    arquivo = simpledialog.askstring("Remover", f"Arquivos bloqueados: \n{config['arquivos_bloqueados']}\n\nDigite o nome do arquivo a remover:")
    if arquivo in config["arquivos_bloqueados"]:
        config["arquivos_bloqueados"].remove(arquivo)
        salvar_config(config)
        messagebox.showinfo("Sucesso", f"Arquivo '{arquivo}' removido!")

def editar_arquivo_bloqueado():
    antigo = simpledialog.askstring("Editar", f"Arquivos bloqueados: \n{config['arquivos_bloqueados']}\n\nDigite o nome do arquivo a editar:")
    if antigo in config["arquivos_bloqueados"]:
        novo = simpledialog.askstring("Editar", f"Digite o nome para '{antigo}'")
        if novo:
            index = config["arquivos_bloqueados"].index(antigo)
            config["arquivos_bloqueados"][index] = novo
            salvar_config(config)
            messagebox.showinfo("Sucesso", f"Arquivo '{antigo}' alterado para '{novo}'!")


def adicionar_extensao_bloqueada():
    extensao = simpledialog.askstring("Adicionar", "Digite a extensão do arquivo a ser bloqueado:")
    if extensao and extensao not in config["extensoes_bloqueadas"]:
        config["extensoes_bloqueadas"].append(extensao)
        salvar_config(config)
        messagebox.showinfo("Sucesso", "Extensão bloqueada adicionada!")

def remover_extensao_bloqueada():
    extensao = simpledialog.askstring("Remover", f"Arquivos bloqueados: \n{config['extensoes_bloqueadas']}\n\nDigite o nome do arquivo a remover:")
    if extensao in config["extensoes_bloqueadas"]:
        config["extensoes_bloqueadas"].remove(extensao)
        salvar_config(config)
        messagebox.showinfo("Sucesso", f"Arquivo '{extensao}' removido!")

def editar_extensao_bloqueada():
    antigo = simpledialog.askstring("Editar", f"Arquivos bloqueados: \n{config['extensoes_bloqueadas']}\n\nDigite o nome do arquivo a editar:")
    if antigo in config["extensoes_bloqueadas"]:
        novo = simpledialog.askstring("Editar", f"Digite o nome para '{antigo}'")
        if novo:
            index = config["extensoes_bloqueadas"].index(antigo)
            config["extensoes_bloqueadas"][index] = novo
            salvar_config(config)
            messagebox.showinfo("Sucesso", f"Arquivo '{antigo}' alterado para '{novo}'!")

def criar_icone():
    image = Image.new("RGB", (64, 64), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.rectangle((10, 10, 54, 54), fill="blue")

    menu = (
        item("Iniciar", iniciar_organizacao),
        item("Parar", parar_organizacao),
        item("Abrir Janela", mostrar_janela),
        item("Sair", sair_programa),
    )
    
    icone = pystray.Icon("desktop_cleaner", image, "Desktop Cleaner", menu)
    icone.run()

def mostrar_janela():
    root.deiconify()

def minimizar():
    root.withdraw()
    threading.Thread(target=criar_icone, daemon=True).start()

def sair_programa(icon, _):
    global rodando
    rodando = False
    icon.stop()
    root.destroy()

config = carregar_config()
rodando = False
root = tk.Tk()
root.title("Desktop Cleaner")
root.geometry("400x300")

tk.Label(root, text="Diretorio Monitorado:").pack(pady=5)
entry_diretorio = tk.Entry(root, width=40)
entry_diretorio.pack(pady=5)
entry_diretorio.insert(0, config["diretorio"])
btn_selecionar = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta)
btn_selecionar.pack(pady=5)

tk.Label(root, text="Intervalo (segundos):").pack(pady=5)
entry_intervalo = tk.Entry(root, width=10)
entry_intervalo.pack(pady=5)
entry_intervalo.insert(0, str(config["intervalo"]))

tk.Button(root, text="Iniciar", command=iniciar_organizacao, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Parar", command=parar_organizacao, bg="red", fg="white").pack(pady=5)

tk.Button(root, text="Adicionar Arquivo", command=adicionar_arquivo_bloqueado).pack(pady=5)
tk.Button(root, text="Editar Arquivo", command=editar_arquivo_bloqueado).pack(pady=5)
tk.Button(root, text="Remover Arquivo", command=remover_arquivo_bloqueado).pack(pady=5)


tk.Button(root, text="Adicionar Extensão", command=adicionar_extensao_bloqueada).pack(pady=5)
tk.Button(root, text="Editar Extensão", command=editar_extensao_bloqueada).pack(pady=5)
tk.Button(root, text="Remover Extensão", command=remover_extensao_bloqueada).pack(pady=5)



tk.Button(root, text="Minimizar", command=minimizar).pack(pady=5)

root.mainloop()