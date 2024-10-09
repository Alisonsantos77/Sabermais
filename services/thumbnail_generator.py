import os
import subprocess
from PIL import Image


def generate_thumbnail_with_pillow(video_path, thumbnail_path, time="00:00:02"):
    """
    Gera uma thumbnail do vídeo no tempo especificado usando Pillow.
    
    Se o arquivo de thumbnail já existir, ele é reutilizado. Caso contrário, uma nova
    thumbnail é gerada a partir do vídeo.

    :param video_path: Caminho do arquivo de vídeo.
    :param thumbnail_path: Caminho onde a thumbnail será salva.
    :param time: Tempo em que a thumbnail será capturada, no formato HH:MM:SS.
    :return: Caminho para a thumbnail gerada ou None em caso de erro.
    """
    try:
        if os.path.exists(thumbnail_path):
            print(
                f"Arquivo {thumbnail_path} já existe. Utilizando o existente.")
            return thumbnail_path

        print(f"Gerando thumbnail para: {video_path}")
        result = subprocess.run([
            'ffmpeg',
            '-ss', time,
            '-i', video_path,
            '-frames:v', '1',
            '-q:v', '2',
            '-vf', 'scale=320:-1',
            thumbnail_path
        ], check=True, capture_output=True, text=True)

        print(f"Thumbnail gerada em: {thumbnail_path}")
        return thumbnail_path
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar thumbnail com Pillow: {str(e)}")
        print(f"Detalhes do erro: {e.stderr}")
        return None
