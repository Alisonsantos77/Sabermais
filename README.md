# Saber+ 🎓

**Saber+** é uma aplicação desenvolvida em **Flet Python** para ajudar estudantes a otimizar seus estudos para o vestibular e outras avaliações. A aplicação analisa videoaulas e gera questionários completos no estilo vestibular, incluindo perguntas desafiadoras, opções de resposta, explicações e dicas.

![Saber+](https://github.com/Alisonsantos77/Sabermais/blob/main/sabermais_capa.PNG)


## 🚀 Funcionalidades

1. **Upload de Videoaulas**
   - Permite selecionar e enviar videoaulas para análise.
   - Gera automaticamente um conjunto de perguntas baseadas no conteúdo do vídeo.

2. **Questionários Dinâmicos**
   - Gera perguntas de múltipla escolha com explicações detalhadas e dicas úteis.
   - Feedback em tempo real sobre respostas corretas e incorretas.

3. **Interface Intuitiva**
   - Design responsivo e amigável.
   - Alterne entre temas claros e escuros conforme sua preferência.

4. **Histórico de Resultados**
   - Salva o histórico de pontuações e permite acompanhar o progresso ao longo do tempo.

5. **Notificações**
   - Integra notificações de sistema e áudio para melhorar a experiência do usuário.

## 🖥️ Tecnologias Utilizadas

- **[Flet](https://flet.dev/)**: Framework de desenvolvimento para criar aplicações Python com interfaces modernas.
- **Python**: Linguagem de programação principal.
- **Google Gemini AI**: Análise de vídeos e geração de perguntas.
- **FFmpeg**: Geração de thumbnails a partir de vídeos.
- **Loguru**: Log eficiente para depuração e rastreamento.
- **Win10Toast**: Exibição de notificações no sistema operacional Windows.

## 🔧 Configuração do Ambiente

### Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/Alisonsantos77/Sabermais.git
   cd Sabermais
   ```

2. Instale as dependências com os comandos abaixo:

   ```bash
   pip install -q -U flet
   pip install -q -U google-generativeai
   pip install -q -U loguru
   pip install -q -U win10toast
   pip install -q -U pillow
   ```

3. Configure a chave de API para a **Google Gemini AI**:
   - Crie um arquivo `.env` e adicione a chave:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. Instale o **FFmpeg** para gerar thumbnails de vídeos:

### ⚙️ Instalação do FFmpeg no Windows

1. Baixe o executável do FFmpeg no site oficial:
   [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).

2. Escolha a opção para sistemas Windows (Build oficial ou gyan.dev).

3. Após o download:
   - Extraia o arquivo `.zip` para um local como `C:\ffmpeg`.
   - Adicione o caminho da pasta `bin` do FFmpeg às Variáveis de Ambiente do sistema:
     - Pressione `Win + S` e procure por **"Editar variáveis de ambiente do sistema"**.
     - Na seção "Variáveis de Sistema", encontre e edite a variável `Path`.
     - Adicione o caminho `C:\ffmpeg\bin`.

4. Verifique a instalação executando:
   ```bash
   ffmpeg -version
   ```

5. Execute a aplicação:
   ```bash
   flet run main.py
   ```

## 🎨 Temas Disponíveis

- **Dark Mode**: Ideal para estudo em ambientes com pouca luz.
- **Light Mode**: Perfeito para ambientes claros.

A troca de tema pode ser feita pressionando a tecla `T` ou chacoalhando o dispositivo (em dispositivos móveis).

## 🚧 Limitações Conhecidas

- O processamento de vídeos pode levar algum tempo, dependendo do tamanho do arquivo.
- Compatível apenas com os formatos de vídeo: `.mp4`, `.mov`, `.avi`, `.mkv`.

## 📚 Créditos e Autor

**Desenvolvido por:** Alison Santos  
Perfil do LinkedIn: [Alison Santos](https://www.linkedin.com/in/alisonsantosdev/)  
GitHub: [Alisonsantos77](https://github.com/Alisonsantos77)

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
