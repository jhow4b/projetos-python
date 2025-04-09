import pandas as pd
from docx import Document
import os

df = pd.read_excel("cacau_show_canecas.xlsx")

df.fillna("", inplace=True)
df = df.astype(str)

template_path = "template.docx"
output_dir = "arquivos_gerados"
os.makedirs(output_dir, exist_ok=True)

for idx, row in df.iterrows():
    doc = Document(template_path)

    for shape in doc.inline_shapes:
        pass

    for para in doc.paragraphs:
        if "{{nome}}" in para.text or "{{preco_normal}}" in para.text or "{{preco_lovers}}" in para.text:
            inline = para.runs
            for i in inline:
                i.text = i.text.replace("{{nome}}", row["Produto"])
                i.text = i.text.replace("{{preco_normal}}", row["Preço Normal"]).replace(".", ",")
                i.text = i.text.replace("{{preco_lovers}}", row["Preço Cacau Lovers"]).replace(".", ",")

    for shape in doc._element.xpath("//w:txbxContent//w:t"):
        text = shape.text
        if text:
            text = text.replace("{{nome}}", row["Produto"])
            text = text.replace("{{preco_normal}}", row["Preço Normal"].replace(".", ","))
            text = text.replace("{{preco_lovers}}", row["Preço Cacau Lovers"].replace(".", ","))
            shape.text = text
    
    nome_produto = "".join(c for c in row["Produto"] if c.isalnum() or c in (" ", "-", "_")).strip()
    nome_arquivo = f"{output_dir}/{nome_produto}.docx"
    doc.save(nome_arquivo)
    print(f"Gerado: {nome_arquivo}")


print("Arquivos gerados com sucesso!")
    