import subprocess
import sys
import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key

# Função para instalar pacotes
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Inicializa os controladores do mouse e teclado
mouse = MouseController()
keyboard = KeyboardController()
def mov(x,y):
    time.sleep(3)
    mouse.position=(x,y)
    print(f'Posição atual do mouse: {mouse.position}')
    time.sleep(3)

def text(escrever_texto):
    time.sleep(3)  # Pausa para você clicar no campo onde deseja digitar
    keyboard.type(escrever_texto)
    print(f'Texto digitado: {escrever_texto}')
    
    # Pressiona a tecla Enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print('Tecla Enter pressionada')
    time.sleep(3)

#movimentos, escrita e clics para ir até o spotify
def open_spotify():
    #Automatiza a abertura do Spotify na barra de pesquisa.
    mov(900, 890)
    mouse.click(Button.right, 1)
    time.sleep(5)
    mov(900, 690)
    mouse.click(Button.left, 1)
    text("spotify")
    mov(600, 300)
    mouse.click(Button.left, 1)
    time.sleep(5)

def create_spotify_playlist(playlist_name, songs):
    #Cria uma nova playlist no Spotify e adiciona as músicas especificadas.
    time.sleep(2)
    mov(50, 375)  # Coordenadas para o botão "Nova Playlist"
    mouse.click(Button.left, 1)
    mov(900,350) #Coordenadas para mudar o nome da playlist
    mouse.click(Button.left, 1)
    text(playlist_name) # Digita o nome da playlist
    
    for song in songs:
        mov(800, 150)# Posiciona o mouse no campo de busca
        mouse.click(Button.left, 1) #um click para excluir o que já tava escrito na barra de pesquisa
        time.sleep(1)
        mouse.click(Button.left,1) #um click para poder escrever o nome da próxima música 
        text(song) # Digita o nome da música

        # Seleciona a música encontrada
        mov(1175, 350) #vai até os '...' da primeira música que aparece
        mouse.click(Button.left, 1)
        mov(1175,395) #vai até adcionar a playlist
        mov(1130,480) #seleciona a playlist
        mouse.click(Button.left, 1)
        time.sleep(3)
        mov(1030, 150) #o mouse vai até o 'X' da barra de pesquisa
        mouse.click(Button.left,1) #um click para excluir o que já tava escrito na barra de pesquisa

    print(f'Playlist "{playlist_name}" criada com sucesso!')
    mov(50, 375)
    mouse.click(Button.left, 1)

if __name__ == '__main__':
    # Lista de músicas a serem adicionadas
    songs_to_add = [
        "Summer in the City - Now United", 
        "Who Would Think That Love? - Now United", 
        "Come Together - Now United", 
        "Na Na Na - Now United", 
        "Paraná - Now United"]

    # Nome da nova playlist
    playlist_name = "Unidos da Tijuca"

    # Abre o spotify e cria a playlist no Spotify
    open_spotify()
    create_spotify_playlist(playlist_name, songs_to_add)