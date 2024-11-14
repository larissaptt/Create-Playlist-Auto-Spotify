# Spotify Playlist Automator

Este projeto automatiza a criação de playlists no Spotify utilizando Python. O script usa coordenadas do mouse e comandos de teclado para interagir com o Spotify e adicionar músicas a uma nova playlist automaticamente. 

⚠️ **Importante**: Antes de executar o script, ajuste as coordenadas do mouse para que correspondam ao layout de tela do seu dispositivo, pois diferenças de resolução e tamanho de tela podem causar erros.

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

## Uso

1. **Pré-requisito**: Certifique-se de que o Spotify está instalado e configurado para abrir através da barra de pesquisa do Windows.

2. **Ajuste das Coordenadas**: Abra o script e ajuste as coordenadas do mouse para que correspondam à sua resolução de tela e layout.

3. **Execução do Script**:

    ```bash
    python criar_playlist_auto.py
    ```

4. **Processo Automático**: O script abrirá o Spotify, criará uma nova playlist com o nome especificado e adicionará automaticamente as músicas listadas.

## Fluxo de Ações do Script

O script segue as etapas abaixo para automatizar a criação de uma playlist no Spotify:

1. **Abrir o Spotify**:
   - O script move o mouse até a barra de tarefas do Windows, clica com o botão direito no ícone do navegador e seleciona "Nova Janela".
   - No navegador, o script digita `open.spotify.com` no campo de busca para acessar a versão web do Spotify.

2. **Criar Nova Playlist**:
   - Localiza o botão "Nova Playlist" e clica para iniciar uma nova lista de reprodução.
   - Posiciona o mouse no campo de nome e insere o título especificado para a playlist.

3. **Adicionar Músicas à Playlist**:
   - Para cada música na lista fornecida:
      - Move o mouse até o campo de busca do Spotify, limpa o texto existente, e digita o nome da música desejada.
      - Posiciona o mouse sobre a música nos resultados, clica com o botão direito para abrir o menu de opções e seleciona "Adicionar à playlist".
      - Fecha a barra de pesquisa para facilitar a busca da próxima música.

4. **Finalização**:
   - O script finaliza movendo o mouse para a área de controle de reprodução para iniciar a playlist.

Ao final, a playlist estará criada com as músicas especificadas, pronta para ser ouvida.

## Contribuição

Se você deseja contribuir com melhorias, fique à vontade para enviar pull requests ou abrir issues com sugestões e correções.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
