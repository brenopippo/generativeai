import tkinter as tk
import google.generativeai as genai
import urllib.request

from tkinter import filedialog

# Define a key
GOOGLE_API_KEY="AIzaSyD-RBOn1Gu7BcARyIqDdaGjqO_uBb1_rL8"
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
    filetypes=( ("Arquivos de texto", "*.jpg *.jpeg") , ("Todos os arquivos", "*.*"))
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
    
  else:
    print("Nenhum arquivo selecionado.")

# Cria a janela principal
janela = tk.Tk()
janela.title("Selecionador de Arquivos")

# Cria um botão para abrir o seletor de arquivos
botao = tk.Button(janela, text="Selecionar arquivo", command=selecionar_arquivo)
botao.pack()

# Inicia o loop principal da janela
janela.mainloop()
