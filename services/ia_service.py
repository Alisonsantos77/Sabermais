import os
import time

import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def upload_to_gemini(path, mime_type=None):
    """
    Faz o upload de um vídeo para o serviço da Google Gemini AI.

    :param path: O caminho do arquivo de vídeo.
    :param mime_type: Tipo MIME do arquivo de vídeo.
    :return: A URI do arquivo processado.
    """
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Arquivo '{file.display_name}' enviado como: {file.uri}")
    return file


def wait_for_files_active(files):
    """
    Espera até que os arquivos estejam ativos e prontos para serem usados na IA.

    :param files: Lista de arquivos enviados.
    """
    print("Esperando pelo processamento dos arquivos...")
    for name in (file.name for file in files):
        file = genai.get_file(name)
        while file.state.name == "PROCESSING":
            print(".", end="", flush=True)
            time.sleep(10)
            file = genai.get_file(name)
        if file.state.name != "ACTIVE":
            raise Exception(f"Arquivo {file.name} falhou no processamento")
    print("Todos os arquivos estão prontos")


def gerar_perguntas(video_path):
    """
    Envia o vídeo para o serviço e gera perguntas a partir do conteúdo.

    :param video_path: Caminho para o arquivo de vídeo.
    :return: Perguntas geradas pela IA como texto.
    """
    files = [upload_to_gemini(video_path, mime_type="video/mp4")]
    wait_for_files_active(files)

    chat_session = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 2048,
            "response_mime_type": "text/plain",
        }
    ).start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    files[0],
                ],
            },
            {
                "role": "user",
                "parts": [
                    "Por favor, analise o vídeo fornecido e crie **5 perguntas de múltipla escolha**, cada uma com "
                    "**5 opções**, baseadas no conteúdo do vídeo. As perguntas devem seguir o estilo de exames de "
                    "vestibulares, sendo bem estruturadas e desafiadoras. Certifique-se de que as perguntas cobrem "
                    "diferentes aspectos importantes do vídeo, como personagens, eventos, conceitos discutidos e "
                    "detalhes visuais.\n\n"
                    "**Por favor, siga rigorosamente o seguinte formato para cada pergunta:**\n\n"
                    "**n. Pergunta**\n"
                    "a) Opção A\n"
                    "b) Opção B\n"
                    "c) Opção C\n"
                    "d) Opção D\n"
                    "e) Opção E\n"
                    "**Resposta Correta:** (apenas a letra da opção correta, por exemplo, 'a', 'b', 'c', "
                    "'d' ou 'e')\n\n"
                    "**Não inclua nenhuma informação adicional ou explicações.**"
                ],
            },

        ]
    )

    response = chat_session.send_message("Novamente")

    perguntas_geradas = response.text

    print("Resposta da IA em formato texto:\n", perguntas_geradas)

    return perguntas_geradas
