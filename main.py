import pyautogui
import time

def spam_message(message, repetitions):
    print(f"Aguardando 5 segundos para focar o campo de texto...")
    time.sleep(5)
    for i in range(repetitions):
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')  # Pressiona Enter


spam_message("Me Avisa Quando Voltar!!!!!!", repetitions=300)
