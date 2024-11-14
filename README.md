Sim! Vou ajustar o README para que o arquivo auxiliar seja apresentado como um link relativo, o que facilita o acesso diretamente pelo GitHub:

---

# Spotify Playlist Automator

Este projeto automatiza a criação de playlists no Spotify utilizando Python. O script usa coordenadas do mouse e comandos de teclado para interagir com o Spotify e adicionar músicas a uma nova playlist automaticamente. 

⚠️ **Importante**: Antes de executar o script principal, ajuste as coordenadas do mouse para que correspondam ao layout de tela do seu dispositivo, pois diferenças de resolução e tamanho de tela podem causar erros. Um arquivo auxiliar está incluído para facilitar a obtenção dessas coordenadas.

## Requisitos

- Python 3.x
- [pynput](https://pypi.org/project/pynput/) (instalado automaticamente via `requirements.txt`)

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/larissptt/Criar-Playlist-Auto-Spotify.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd Criar-Playlist-Auto-Spotify
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Encontrando as Coordenadas do Mouse

Para ajustar o script à sua resolução de tela, você pode utilizar o [arquivo auxiliar de coordenadas do mouse](cordenada.py) incluído no projeto. Esse script exibe as coordenadas do mouse em tempo real, facilitando a identificação dos pontos corretos para ajuste.

Execute o seguinte comando para iniciar o arquivo auxiliar:

```bash
python cordenada.py
```

Com ele, você poderá mover o cursor para os pontos desejados e anotar as coordenadas exatas para usá-las no script principal.

## Uso do Script Principal

1. **Pré-requisito**: Certifique-se de que o Spotify está instalado e configurado para abrir através da barra de pesquisa do Windows.

2. **Ajuste das Coordenadas**: Após identificar as coordenadas corretas, ajuste-as no script principal para corresponder à sua configuração de tela.

3. **Execução do Script**:

    ```bash
    python criar_playlist_auto.py
    ```

4. **Processo Automático**: O script abrirá o Spotify, criará uma nova playlist com o nome especificado e adicionará automaticamente as músicas listadas.

## Fluxo de Ações do Script

O script segue as etapas abaixo para automatizar a criação de uma playlist no Spotify:

1. **Abrir o Spotify**:  
    - Move o mouse até a barra de tarefas do Windows, clica com o botão direito no ícone do navegador e seleciona "Nova Janela".
    - No navegador, digita `open.spotify.com` no campo de busca para acessar a versão web do Spotify.

2. **Criar Nova Playlist**:  
    - Localiza o botão "Nova Playlist" e clica para iniciar uma nova lista de reprodução.
    - Posiciona o mouse no campo de nome e insere o título especificado para a playlist.

3. **Adicionar Músicas à Playlist**:  
    - Para cada música na lista:
        - Move o mouse até o campo de busca do Spotify, limpa o texto existente e digita o nome da música.
        - Posiciona o mouse sobre a música nos resultados, clica com o botão direito para abrir o menu de opções e seleciona "Adicionar à playlist".
        - Fecha a barra de pesquisa para a próxima música.

4. **Finalização**:  
    - O script move o mouse para a área de controle de reprodução para iniciar a playlist.

Ao final, a playlist estará criada com as músicas especificadas, pronta para ser ouvida.

## Contribuição

Se você deseja contribuir com melhorias, fique à vontade para enviar pull requests ou abrir issues com sugestões e correções.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

--- 

Agora o arquivo `coordenadas_mouse.py` é apresentado como um link interno, facilitando o acesso direto pelo GitHub.
