import PyPDF2
import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename

pdf_selecionados = []


def openDraw():
    tkinter.Tk().withdraw()
    filename = askopenfilename()
    pdf_selecionados.append(filename)
    nome_pdf_text = "\n".join(pdf_selecionados)
    nome_pdf['text'] = nome_pdf_text


def generatePdfs():
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_selecionados:
        merger.append(pdf)

    output_filename = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

    if not output_filename.lower().endswith(".pdf"):
        output_filename += ".pdf"

    if output_filename:
        merger.write(output_filename)
        merger.close()
        result_label['text'] = f"PDF mesclado gerado: {output_filename}"


janela = tkinter.Tk()
janela.geometry("500x400")

titulo = tkinter.Label(janela, text="Quais PDF's você gostaria de juntar?", font=("Arial", 17))
titulo.pack()

botao = tkinter.Button(janela, text="Escolher PDF's", command=openDraw)
botao.pack()

pdfs_escolhidos = tkinter.Label(janela, text="PDF's escolhidos:")
pdfs_escolhidos.pack()

nome_pdf = tkinter.Label(janela, text="")
nome_pdf.pack()

botao_pdf_final = tkinter.Button(janela, text="Gerar junção dos PDF's", command=generatePdfs)
botao_pdf_final.pack()

result_label = tkinter.Label(janela, text="")
result_label.pack()

janela.mainloop()
