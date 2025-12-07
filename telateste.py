import pyautogui

# encontra na tela um botão salvo como "botao.png"
button_location = pyautogui.locateOnScreen("botao.png")
if button_location:
    x, y = pyautogui.center(button_location)
    pyautogui.click(x, y)
