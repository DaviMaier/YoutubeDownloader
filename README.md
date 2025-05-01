🎬 YouTube Downloader (Davi Maier)
Um aplicativo simples feito em Python com interface gráfica (Tkinter) para baixar vídeos ou áudios do YouTube com o yt-dlp.

🛠️ Funcionalidades
Baixa vídeos do YouTube como MP4.

Converte e baixa áudios como MP3.

Mostra o progresso do download em tempo real.

Abre automaticamente a pasta de destino após o download.

Interface gráfica amigável feita com Tkinter.

📦 Requisitos
Python 3.7+

yt-dlp

ffmpeg (necessário para conversão de áudio)

📥 Instalação
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/youtube-downloader-gui.git
cd youtube-downloader-gui
Instale as dependências:

bash
Copiar
Editar
pip install yt-dlp
Certifique-se de ter o ffmpeg instalado e acessível pelo terminal:

Windows: Download FFmpeg

Linux (Debian/Ubuntu):

bash
Copiar
Editar
sudo apt install ffmpeg
macOS (Homebrew):

bash
Copiar
Editar
brew install ffmpeg
▶️ Como usar
Execute o script:

bash
Copiar
Editar
python downloader.py
Cole o link do vídeo do YouTube.

Selecione se deseja baixar como áudio (MP3) ou vídeo (MP4).

Clique em "Baixar" e aguarde a finalização.

📁 Downloads
Os arquivos baixados serão salvos na pasta downloads/ organizada por título.
