import flet as ft
import asyncio
from services.ia_service import gerar_perguntas
from services.thumbnail_generator import generate_thumbnail
from services.extract_text_response import extract_questions_from_text
from plyer import notification


def QuestionPage(page: ft.Page):
    wallpaper_container = ft.Ref[ft.Container]()
    text_motivation = ft.Ref[ft.Text]()
    question_container = ft.Ref[ft.Column]()
    tab_rf = ft.Ref[ft.Tabs]()
    select_file_button = ft.Ref[ft.ElevatedButton]()
    submit_button = ft.Ref[ft.ElevatedButton]()

    # Lista para armazenar as instâncias de Answer
    answer_instances = []

    selected_file = ft.Text(
        value="Nenhum arquivo selecionado",
        size=16,
        weight=ft.FontWeight.BOLD,
    )

    class Answer(ft.RadioGroup):
        def __init__(self, pergunta_numero, opcoes: list, letras_opcoes: list, resposta_letra: str):
            radios = [ft.Radio(value=letra, label=opcao) for letra, opcao in zip(letras_opcoes, opcoes)]
            super().__init__(content=ft.Column(radios))
            self.pergunta_numero = pergunta_numero
            self.opcoes = opcoes
            self.letras_opcoes = letras_opcoes
            self.resposta_correta = resposta_letra.lower()
            self.selected_answer = None
            self.on_change = self.store_selected_answer

        def store_selected_answer(self, e):
            self.selected_answer = self.value
            page.session.set(f"resposta_pergunta_{self.pergunta_numero}", self.selected_answer)
            print(f"Pergunta {self.pergunta_numero}: Resposta selecionada: {self.selected_answer}")

    def show_notification_plyer(title, message):
        max_length = 256
        title = (title[:max_length] + '...') if len(title) > max_length else title
        message = (message[:max_length] + '...') if len(message) > max_length else message

        notification.notify(
            title=title,
            message=message,
            timeout=5
        )

    def on_file_picker_result(e: ft.FilePickerResultEvent):
        if e.files:
            file_name = e.files[0].name
            video_path = e.files[0].path
            page.session.set("video_path", video_path)
            page.session.set("last_selected_file", file_name)

            file_size = round(e.files[0].size / (1024 * 1024), 2)

            thumbnail_path = generate_thumbnail(video_path, f"thumbnail_{file_name}.jpg")

            wallpaper_container.current.image_src = thumbnail_path
            wallpaper_container.current.update()

            selected_file.value = f"Arquivo: {file_name}\nTamanho: {file_size} MB\n"
        else:
            selected_file.value = "Nenhum arquivo selecionado"
            wallpaper_container.current.image_src = "https://images8.alphacoders.com/136/1363709.png"
            wallpaper_container.current.update()
        page.update()

    def renderizar_perguntas(perguntas):
        question_container.current.controls.clear()
        answer_instances.clear()

        for idx, pergunta_obj in enumerate(perguntas, start=1):
            pergunta_texto = pergunta_obj['pergunta']
            opcoes_resposta = pergunta_obj['opcoes']
            letras_opcoes = pergunta_obj['letras_opcoes']
            resposta_correta_letra = pergunta_obj['resposta_letra']

            question_container.current.controls.append(
                ft.Text(f"{idx}. {pergunta_texto}", size=20, weight=ft.FontWeight.BOLD)
            )

            answer_group = Answer(
                pergunta_numero=idx,
                opcoes=opcoes_resposta,
                letras_opcoes=letras_opcoes,
                resposta_letra=resposta_correta_letra
            )
            question_container.current.controls.append(answer_group)
            answer_instances.append(answer_group)

        calcular_button = ft.ElevatedButton(
            text="Calcular Pontuação",
            on_click=calcular_perguntas,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN_700,
                color=ft.colors.WHITE,
            )
        )
        question_container.current.controls.append(calcular_button)
        question_container.current.update()

    def calcular_perguntas(e):
        total_perguntas = len(answer_instances)
        respostas_corretas = sum(
            1 for answer in answer_instances if
            answer.selected_answer and answer.selected_answer.strip().lower() == answer.resposta_correta.strip().lower()
        )

        if respostas_corretas == total_perguntas:
            feedback = "🎉 Parabéns, você acertou todas!"
        elif respostas_corretas > total_perguntas / 2:
            feedback = f"👏 Bom trabalho! Você acertou {respostas_corretas} de {total_perguntas}."
        else:
            feedback = f"⚠️ Você acertou {respostas_corretas} de {total_perguntas}. Continue praticando!"

        # Mostra o feedback ao usuário
        show_notification_plyer("Resultado do Quiz", feedback)
        page.session.set("score", {"total_perguntas": total_perguntas, "respostas_corretas": respostas_corretas})
        page.go('/score')

    async def processar_upload():
        video_path = page.session.get("video_path")
        if not video_path:
            selected_file.value = "Nenhum vídeo foi selecionado. Vamos lá, escolha um vídeo para continuar! 🎥"
            page.update()
            return

        show_notification_plyer("Processamento em Andamento", "A IA está analisando o vídeo, por favor aguarde...")

        try:
            loop = asyncio.get_event_loop()
            perguntas_geradas = await loop.run_in_executor(None, gerar_perguntas, video_path)

            perguntas_extraidas = extract_questions_from_text(perguntas_geradas)
            if perguntas_extraidas:
                page.session.set("questions", perguntas_extraidas)
                renderizar_perguntas(perguntas_extraidas)
                tab_rf.current.selected_index = 1
                tab_rf.current.update()
                show_notification_plyer("Sucesso", "A análise do vídeo foi concluída e as perguntas foram geradas!")
            else:
                show_notification_plyer("Erro", "Não foi possível extrair perguntas do vídeo.")

        except Exception as e:
            show_notification_plyer("Erro no Processamento", f"Erro inesperado: {e}")

    async def on_confirm_upload(e):
        video_path = page.session.get("video_path")
        if not video_path:
            selected_file.value = "Nenhum vídeo foi selecionado. Vamos lá, escolha um vídeo para continuar! 🎥"
            selected_file.update()
            return
        print("🟢 Iniciando o upload do vídeo...")
        selected_file.value = "Processando upload... Segura aí que estamos trabalhando! 😉"
        page.update()

        select_file_button.current.disabled = True
        submit_button.current.disabled = True
        select_file_button.current.update()
        submit_button.current.update()

        elapsed_time = 0

        submit_button.current.content = ft.Row(
            controls=[
                ft.ProgressRing(width=16, height=16, stroke_width=2),
                ft.Text(f"Processando... {elapsed_time}s"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        submit_button.current.update()

        async def atualizar_timer():
            nonlocal elapsed_time
            while True:
                await asyncio.sleep(1)
                elapsed_time += 1
                submit_button.current.content.controls[1].value = f"Processando... {elapsed_time}s"
                submit_button.current.update()

        # Inicia a tarefa de atualização do timer
        timer_task = asyncio.create_task(atualizar_timer())

        await processar_upload()

        # Cancela a tarefa do timer
        timer_task.cancel()
        try:
            await timer_task
        except asyncio.CancelledError:
            pass

        select_file_button.current.disabled = False
        submit_button.current.disabled = False
        submit_button.current.content = ft.Text("Executar")
        select_file_button.current.update()
        submit_button.current.update()

        print("🎬 Upload e processamento concluídos com sucesso!")

    file_picker = ft.FilePicker(on_result=on_file_picker_result)
    page.overlay.append(file_picker)

    select_file_button_control = ft.ElevatedButton(
        ref=select_file_button,
        text="Selecionar Arquivo",
        on_click=lambda _: file_picker.pick_files(allow_multiple=False, allowed_extensions=["mp4"]),
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: ft.colors.WHITE,
                ft.ControlState.HOVERED: ft.colors.BLACK
            },
            color={
                ft.ControlState.DEFAULT: ft.colors.BLACK,
                ft.ControlState.HOVERED: ft.colors.WHITE,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            shape=ft.RoundedRectangleBorder(radius=6),
        )
    )

    submit_button_control = ft.ElevatedButton(
        ref=submit_button,
        text="Executar",
        on_click=on_confirm_upload,
        style=ft.ButtonStyle(
            padding=ft.padding.all(10),
            bgcolor={
                ft.ControlState.DEFAULT: ft.colors.WHITE,
                ft.ControlState.HOVERED: ft.colors.BLACK
            },
            color={
                ft.ControlState.DEFAULT: ft.colors.BLACK,
                ft.ControlState.HOVERED: ft.colors.WHITE,
            },
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            shape=ft.RoundedRectangleBorder(radius=6),
        )
    )

    sec_file_upload = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    ref=wallpaper_container,
                    image_src='https://images8.alphacoders.com/136/1363709.png',
                    height=300,
                    expand=True,
                    alignment=ft.alignment.center,
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=select_file_button_control,
                                padding=5,
                            ),
                        ]
                    )
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=selected_file,
                    padding=5,
                    col={"sm": 6, "md": 4, "xl": 12},
                ),
                ft.Container(
                    content=submit_button_control,
                    col={"xs": 6, "md": 3},
                ),
            ],
            spacing=20,
            run_spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    return ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='https://images8.alphacoders.com/136/1363709.png',
                            image_fit=ft.ImageFit.COVER,
                            height=300,
                            expand=True,
                            alignment=ft.alignment.center,
                            content=ft.Text(
                                ref=text_motivation,
                                value="Estude o seu conhecimento com o Quiz!",
                                size=30,
                                weight=ft.FontWeight.BOLD
                            )
                        ),
                    ],
                ),
                ft.Tabs(
                    selected_index=0,
                    animation_duration=300,
                    tab_alignment=ft.TabAlignment.CENTER,
                    ref=tab_rf,
                    tabs=[
                        ft.Tab(
                            text="Selecionar Arquivo",
                            content=sec_file_upload
                        ),
                        ft.Tab(
                            text="Perguntas",
                            content=ft.Container(
                                content=ft.Column(ref=question_container),
                                col=10,
                            )
                        ),
                        ft.Tab(
                            text="Relatório",
                            content=ft.Container(
                                content=ft.Text("Relatório"),
                                col=10,
                            )
                        )
                    ],
                ),
            ]
        )
    )
