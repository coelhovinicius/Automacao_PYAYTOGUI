# pip install pyautogui: Instalar a biblioteca de automação
# pip install pandas: Instalar a biblioteca de manipulação de dados
# pip install openpyxl: Instalar a biblioteca de leitura de arquivos excel

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.3 # inclui uma pausa entre os comandos

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey('ctrl', 'c') -> combinação de teclas (exemplo de um crlt+c)

# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
link_da_pagina = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.press('win') # pressiona a tecla win
pyautogui.write('chrome') # digita o nome do navegador
pyautogui.press('enter') # pressiona enter
time.sleep(1) # aguarda 3 segundos para carregar o navegador
pyautogui.write(link_da_pagina) # digita o endereço do site
pyautogui.press('enter') # pressiona enter


# Passo 2: Fazer login
usuario = 'vinicius@vinicius.com'
senha = 'Vinicius123'

time.sleep(1) # aguarda 3 segundos para carregar a página
pyautogui.click(x=421, y=409) # clica no campo de email
pyautogui.write(usuario) # preenche o campo com o email
pyautogui.press('tab') # pressiona a tecla tab
pyautogui.write(senha) # preenche o campo com a senha
pyautogui.press('tab') # pressiona a tecla tab
pyautogui.press('enter') # pressiona a tecla enter

# Passo 3: Importar a base de dados
tabela = pandas.read_csv('produtos.csv')
#print(tabela)

# Passo 4: Cadastrar produtos da base de dados (# Passo 5: Repetir o processo de cadastro para todos os produtos)
time.sleep(1)

for linha in tabela.index:
    pyautogui.click(x=416, y=295) # clica no primeiro campo (código)

    # campo código
    codigo = tabela.loc[linha, 'codigo'] 
    pyautogui.write(str(codigo)) # transforma em string e preenche
    pyautogui.press('tab')

    # campo marca
    marca = tabela.loc[linha, 'marca'] 
    pyautogui.write(str(marca)) # transforma em string e preenche
    pyautogui.press('tab')

    # campo tipo
    tipo = tabela.loc[linha, 'tipo'] 
    pyautogui.write(str(tipo)) # transforma em string e preenche
    pyautogui.press('tab')

    # campo categoria
    categoria = tabela.loc[linha, 'categoria'] 
    pyautogui.write(str(categoria)) # transforma em string e preenche
    pyautogui.press('tab')

    # campo preco unitario
    preco_unitario = tabela.loc[linha, 'preco_unitario'] 
    pyautogui.write(str(preco_unitario)) # transforma em string e preenche
    pyautogui.press('tab')

    # campo custo do produto
    custo = tabela.loc[linha, 'custo'] 
    pyautogui.write(str(custo)) # transforma em string e preenche
    pyautogui.press('tab')

    # campo observações
    obs = str(tabela.loc[linha, 'obs'])

    if obs != 'nan':
        pyautogui.write(obs) # transforma em string e preenche

    pyautogui.press('tab')
    pyautogui.press('enter')

    # dar scroll de tudo pra cima
    pyautogui.press('home')
    #pyautogui.scroll(10000)