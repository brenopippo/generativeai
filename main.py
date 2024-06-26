import tkinter as tk
import google.generativeai as genai
import urllib.request

from tkinter import filedialog
from tkinter import *
from tkinter import ttk

# Define a key
GOOGLE_API_KEY="YOUR_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "temperature": 0.0,
  "top_p": 0.95,
  "top_k": 0
}

# Define a palavra de segurança
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

# Inicia o modelo
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)



def selecionar_arquivo():
  """Abre uma janela para selecionar um arquivo e imprime o caminho."""
  caminho_arquivo = filedialog.askopenfilename(
    initialdir=".", 
    title="Selecione um arquivo",
    filetypes=[("Arquivos de texto", "*.jpg *.jpeg *.png")]
  )
  if caminho_arquivo:
    # Cria um modelo para a IA
    prompt_parts = [
      "Qual é a placa completo do carro nessa foto em formato brasileiro com sete caracteres?",
      "Imagem ",
      genai.upload_file("fotos_modelo/GAE0244.jpg"),
      "A placa desse veículo é GAE0244",
      "Imagem ",
      genai.upload_file("fotos_modelo/POX4G21.jpg"),
      "A placa desse veículo é POX4G21",
      "Imagem ",
      genai.upload_file("fotos_modelo/RHA0A01.jpg"),
      "A placa desse veículo é RHA0A01",
      "Imagem ",
      genai.upload_file(caminho_arquivo),
      "Qual a placa desse veiculo? ",
    ]

    response = model.generate_content(prompt_parts)
    print(response.text)

    ttk.Label(frm, text=response.text).grid(column=0, row=3)
    
  else:
    print("Nenhum arquivo selecionado.")
    
    ttk.Label(frm, text="Nenhum arquivo selecionado.").grid(column=0, row=3)

# Cria a janela principal
janela = tk.Tk()
janela.title("Selecionador de Arquivos")

frm = ttk.Frame(janela, padding=20)
frm.grid()
ttk.Label(frm, text="Primeira tela em Python *.* ").grid(column=0, row=0)
ttk.Label(frm, text="Esse programa serve para analisar a placa do veiculo").grid(column=0, row=1)
ttk.Button(frm, text="Escolha a foto do veiculo", command=selecionar_arquivo).grid(column=5, row=5)


# Inicia o loop principal da janela
janela.mainloop()
