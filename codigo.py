#Passo a passo do projeto
#Passo 1: Entrar no sistema da empresa
#Passo 2: Fazer login
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Passo 3: Importar base de dados de produtos
#Passo 4: Cadastrar um produto
#Passo 5: Repetir o processo para todos os produtos

import pyautogui #para instalar: pip install pyautogui
import time
#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar uma tecla
#pyautogui.hotkey -> atalho (combinação de teclas)

#tempo de espera entre as tarefas
pyautogui.PAUSE = 0.3

#Passo1
#abrir o chrome
pyautogui.press ("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
#pyautogui.click(x=546, y=438) (perfil lara)
pyautogui.click(x=690, y=436, button="left", clicks=3)

#entrar no link
#link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.click(x=326, y=67, button="left", clicks=3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#esperar o site carregar
time.sleep(3)

#Passo 2
#fazer login
pyautogui.click(x=557, y=390)
pyautogui.write("teste.python@hashtag.com")
#número de cliques: clicks=2
#botão do mouse: button="right"
pyautogui.click(x=486, y=489)
pyautogui.write("senha123")
pyautogui.press("enter")

time.sleep(3)

#Passo 3
#Importar base de dados de produtos
#pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

#estrutura de repetição
for linha in tabela.index: 

    #Passo 4
    #cadastrar um produto
    pyautogui.click(x=605, y=283, button="left", clicks=2)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]
    #tabela do pandas: colchetes
    #preencher os campos

    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #condição
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")

    #enviar os dados cadastrados
    pyautogui.press("enter")

    #scroll
    pyautogui.scroll(50000)

 



#Passo 5
#repetir o processo para todos os produtos