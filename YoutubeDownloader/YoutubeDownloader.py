import yt_dlp
import os
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import platform
import threading
import re

def limpar_nome(nome):
    return re.sub(r'[\\/*?:"<>|]', '', nome)

def abrir_pasta(pasta):
    if platform.system() == "Windows":
        os.startfile(pasta)
    elif platform.system() == "Darwin":
        subprocess.call(["open", pasta])
    else:
        subprocess.call(["xdg-open", pasta])

def log_mensagem(msg):
    texto_saida.insert(tk.END, msg + "\n")
    texto_saida.see(tk.END)
    janela.update()

def baixar():
    url = entrada_url.get()
    tipo = var_tipo.get()

    if not url:
        messagebox.showwarning("Aviso", "Cole o link do vídeo.")
        return

    def executar_download():
        try:
            log_mensagem("Obtendo informações do vídeo...")
            with yt_dlp.YoutubeDL({}) as ydl:
                info = ydl.extract_info(url, download=False)
                titulo = ydl.prepare_filename(info).split('.')[0]
                titulo_limpo = limpar_nome(titulo)

            # Criar pasta exclusiva para o vídeo
            base_pasta = os.path.join("downloads", titulo_limpo)
            pasta_destino = base_pasta
            contador = 1
            while os.path.exists(pasta_destino):
                pasta_destino = f"{base_pasta}_{contador}"
                contador += 1
            os.makedirs(pasta_destino)

            def hook(d):
                if d['status'] == 'downloading':
                    porcent = d.get('_percent_str', '0.0%').strip().replace('%', '')
                    try:
                        barra['value'] = float(porcent)
                        janela.update_idletasks()
                    except:
                        pass
                    log_mensagem(f"Baixando... {porcent}%")
                elif d['status'] == 'finished':
                    barra['value'] = 100
                    log_mensagem("Download finalizado. Convertendo se necessário...")

            if tipo == "audio":
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'progress_hooks': [hook],
                }
            else:
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
                    'progress_hooks': [hook],
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            log_mensagem("Concluído com sucesso!")
            abrir_pasta(pasta_destino)

        except Exception as e:
            log_mensagem(f"Erro: {e}")
            messagebox.showerror("Erro", str(e))

    barra['value'] = 0
    texto_saida.delete("1.0", tk.END)
    threading.Thread(target=executar_download).start()

# Interface Gráfica
janela = tk.Tk()
janela.title("YouTube Downloader")
janela.geometry("500x340")

tk.Label(janela, text="Cole o link do vídeo do YouTube:").pack(pady=5)
entrada_url = tk.Entry(janela, width=60)
entrada_url.pack(pady=5)

var_tipo = tk.StringVar(value="audio")
tk.Radiobutton(janela, text="Áudio (MP3)", variable=var_tipo, value="audio").pack()
tk.Radiobutton(janela, text="Vídeo (MP4)", variable=var_tipo, value="video").pack()

tk.Button(janela, text="Baixar", command=baixar).pack(pady=10)

barra = ttk.Progressbar(janela, length=400, mode='determinate')
barra.pack(pady=5)

texto_saida = tk.Text(janela, height=8, width=60)
texto_saida.pack(pady=5)

janela.mainloop()