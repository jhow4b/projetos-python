import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import datetime

historicoMovimentos = {}

categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Áudios": [".mp3", ".wav", ".aac", ".flac"],
    "Vídeos": [".mp4", ".avi", ".mkv", ".mov"],
    "Compactados": [".zip", ".rar", ".7z", ".tar.gz"],
    "Executaveis": [".exe"],
    "Outros": []
}

def registrarLog(msg):
    with open("desktop_cleaner_log.txt", "a", encoding="utf-8") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {msg}\n")

def organizarPasta(caminho):
    global historicoMovimentos
    historicoMovimentos = {} #Limpa historico anterior

    for item in os.listdir(caminho):
        item_path = os.path.join(caminho, item)


        if os.path.isdir(item_path):
            continue #Ignora pastas
    
        
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        categoria = "Outros"
        for key, extensoes in categorias.items():
            if ext in extensoes:
                categoria = key
                break

        pasta_destino = os.path.join(caminho, categoria)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)        

        novoCaminho = os.path.join(pasta_destino, item)
        shutil.move(item_path, os.path.join(pasta_destino, item))

        historicoMovimentos[item] = item_path #Registra historico

        registrarLog(f"Arquivo movido: {item_path} -> {novoCaminho}")

    messagebox.showinfo("Sucesso", "Arquivos organizados com sucesso!")

def desazerOrganizacao():
    global historicoMovimentos

    if not historicoMovimentos:
        messagebox.showwarning("Aviso", "Nenhuma ação para desfazer.")
        return
    
    for arquivo, caminhoOriginal in historicoMovimentos.items():
        categoria = os.path.basename(os.path.dirname(caminhoOriginal)) #Pega a pasta destino
        pastaCategoria = os.path.join(os.path.dirname(caminhoOriginal), categoria)

        arquivoMovido = os.path.join(pastaCategoria, arquivo)

        if os.path.exists(arquivoMovido):
            shutil.move(arquivoMovido, caminhoOriginal)
            registrarLog(f"Desfeito: {arquivoMovido} -> {caminhoOriginal}")
    
    messagebox.showinfo("Sucesso", "Desfazer concluído!")
    historicoMovimentos = {}


def selecionarPasta():
    caminho = filedialog.askdirectory()
    if caminho:
        try:
            organizarPasta(caminho)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao organizar arquivos: {e}")

    else:
        messagebox.showwarning("Atenção!", "Nenhuma pasta selecionada.")

def editarCategoria():
    def adicionarCategoria():
        novaCategoria = simpledialog.askstring("Adicionar Categoria", "Digite o nome da nova categoria:")
        if novaCategoria and novaCategoria.strip():
            if novaCategoria in categorias:
                messagebox.showwarning("Atenção", "Essa categoria já existe")
            else:
                categorias[novaCategoria] = []
                atualizarLista()
                messagebox.showinfo("Sucesso", f"Categoria {novaCategoria} adicionada!")

    def removerCategoria():
        selecionada = Listbox.curselection()
        if selecionada:
            categoriaExibida = Listbox.get(selecionada)
            categoria = categoriaExibida.split(" (")[0]
            
            if categoria == "Outros":
                messagebox.showwarning("Atenção", "A categoria 'Outros' não pode ser removida.")
            else:
                del categorias[categoria]
                atualizarLista()
                messagebox.showinfo("Sucesso", f"Categoria '{categoria}' removida!")

    def adicionarExtensao():
        selecionada = Listbox.curselection()
        if selecionada:
            categoria = Listbox.get(selecionada)
            novaExtensao = simpledialog.askstring("Adicionar Extensão", f"Digite a extensão para a categoria '{categoria}'")
            if novaExtensao and novaExtensao.strip():
                novaExtensao = novaExtensao.lower()
                if novaExtensao in categorias[categoria]:
                    messagebox.showwarning("Atenção", "Essa extensão já está na categoria.")
                else:
                    categorias[categoria].append(novaExtensao)
                    atualizarLista()
                    messagebox.showinfo("Sucesso", f"Extensão '{novaExtensao}' adicionada à categoria '{categoria}'")

    def atualizarLista():
        Listbox.delete(0, tk.END)
        for cat, exts in categorias.items():
            Listbox.insert(tk.END, f"{cat} ({', '.join(exts)})" if exts else f"{cat}")

    editWindow = tk.Toplevel()
    editWindow.title("Editar Categorias")
    editWindow.geometry("500x400")

    Listbox = tk.Listbox(editWindow, font=("Arial", 12), width=50, height=15)
    Listbox.pack(pady=10)
    atualizarLista()

    btnFrame = tk.Frame(editWindow)
    btnFrame.pack(pady=10)

    btnAddCat = tk.Button(btnFrame, text="Adicionar Categoria", command=adicionarCategoria)
    btnAddCat.grid(row=0, column=0, padx=5)

    btnAddCat = tk.Button(btnFrame, text="Remover Categoria", command=removerCategoria)
    btnAddCat.grid(row=0, column=1, padx=5)

    btnAddCat = tk.Button(btnFrame, text="Adicionar Extensão", command=adicionarExtensao    )
    btnAddCat.grid(row=0, column=2, padx=5)

def simularOrganizacao(caminho):
    simulacao = []
    for item in os.listdir(caminho):
        itemPath = os.path.join(caminho, item)
        if os.path.isdir(itemPath):
            continue
        
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        categoria = "Outros"
        for key, extensoes in categorias.items():
            if ext in extensoes:
                categoria = key
                break
        
        pastaDestino = os.path.join(caminho, categoria)
        simulacao.append(f"{item} -> {pastaDestino}")

    if not simulacao:
        messagebox.showinfo("Simulação", "Nenhum arquivo será movido.")
        return

    simulacaoJanela = tk.Toplevel()
    simulacaoJanela.title("Prévia de Organização")
    simulacaoJanela.geometry("500x400")

    textArea = tk.Text(simulacaoJanela, wrap=tk.WORD, font=("Arial", 10))
    textArea.pack(expand=True, fill=tk.BOTH)

    textArea.insert(tk.END, "\n".join(simulacao))

    btnConfirmar = tk.Button(simulacaoJanela, text="Confirmar e Organizar", command=lambda: organizarPasta(caminho))
    btnConfirmar.pack(pady=5)

def criarInterface():
    root = tk.Tk()
    root.title("Desktop Cleaner")
    root.geometry("500x300")
    root.resizable(False, False)

    label = tk.Label(root, text="Organizador de arquivos", font=("Arial", 16))
    label.pack(pady=10)

    btnSelecionar = tk.Button(
        root,
        text="Selecionar Pasta",
        command=selecionarPasta,
        font=("Arial", 12),
        bg="#4CAF50",
        fg="white",
        width=20,
        height=2
    )
    btnSelecionar.pack(pady=5)

    btnDesfazer = tk.Button(
        root,
        text="Desfazer Última Organização",
        command=desazerOrganizacao,
        font=("Arial", 12),
        bg="#FF5733",
        fg="white",
        width=25,
        height=2
    )
    btnDesfazer.pack(pady=5)

    btnEditar = tk.Button(
        root,
        text="Editar Categorias",   
        command=editarCategoria,
        font=("Arial", 12),
        bg="#FFA500",
        fg="white",
        width=20,
        height=2
    )
    btnEditar.pack(pady=10) 

    btnSimular = tk.Button(
        root,
        text="Simular Organização",
        command=lambda: simularOrganizacao(filedialog.askdirectory()),
        font=("Arial", 12),
        bg="#3498DB",
        fg="white",
        width=20,
        height=2
    )
    btnSimular.pack(pady=5)

    footer = tk.Label(root, text="Desenvolvido em Python", font=("Arial", 10), fg="gray")
    footer.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()


    
if __name__ == "__main__":
    criarInterface()