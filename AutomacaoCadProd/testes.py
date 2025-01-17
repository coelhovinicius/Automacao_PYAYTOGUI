import pyautogui
import time
import os

# Abra o Google Chrome
os.startfile("chrome.exe")

# Aguarde alguns segundos para o Chrome abrir
time.sleep(5)

# Maximize a janela do Chrome
pyautogui.hotkey('winleft', 'up')  # Pressiona Win + seta para cima para maximizar a janela
