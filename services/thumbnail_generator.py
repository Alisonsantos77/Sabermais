import ffmpeg


def generate_thumbnail(video_path, thumbnail_path, time="00:00:02"):
    """
    Gera uma thumbnail do vídeo no tempo especificado.

    :param video_path: Caminho do arquivo de vídeo.
    :param thumbnail_path: Caminho onde a thumbnail será salva.
    :param time: Tempo em que a thumbnail será capturada, no formato HH:MM:SS.
    :return: Caminho para a thumbnail gerada ou None em caso de erro.
    """
    try:
        (
            ffmpeg
            .input(video_path, ss=time)  # Captura a thumbnail no tempo especificado
            .output(thumbnail_path, vframes=1, update=1, pix_fmt="yuvj420p")
            .run(overwrite_output=True, quiet=True)
        )
        return thumbnail_path
    except ffmpeg.Error as e:
        print(f"Erro ao gerar thumbnail: {str(e)}")
        return None
