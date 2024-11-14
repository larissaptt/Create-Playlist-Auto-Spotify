from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key
import time

# Inicializa o controlador do mouse
mouse = MouseController()

print("Pressione Ctrl+C para interromper.")

try:
    while True:
        # Obtém a posição do mouse
        x, y = mouse.position
        print(f"Posição atual do mouse: X={x}, Y={y}")
        time.sleep(1)  # Aguarda 1 segundos antes de verificar novamente
except KeyboardInterrupt:
    print("\nPrograma interrompido.")