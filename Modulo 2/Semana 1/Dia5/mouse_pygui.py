import pyautogui

#1 Tamanho da tela

print(pyautogui.size())

# Posicao atual do mouse
print(pyautogui.position())

# App para ver a posicao do mouse em tempo real
#python
#from pyautogui import mouseInfo
#mouseInfo()

# Mover o cursor do mouse
pyautogui.moveTo(200, 500, duration=0.5)
pyautogui.click()
pyautogui.scroll(900)
