import flet as ft


class Answer(ft.RadioGroup):
    def __init__(self, page, pergunta_numero, opcoes: list, letras_opcoes: list, resposta_letra: str):
        radios = [ft.Radio(value=letra, label=opcao)
                  for letra, opcao in zip(letras_opcoes, opcoes)]
        super().__init__(content=ft.Column(radios))
        self.pergunta_numero = pergunta_numero
        self.opcoes = opcoes
        self.letras_opcoes = letras_opcoes
        self.resposta_correta = resposta_letra.lower()
        self.selected_answer = None
        self.on_change = self.store_selected_answer
        self.page = page

    def store_selected_answer(self, e):
        self.selected_answer = self.value
        self.page.session.set(f"resposta_pergunta_{
                              self.pergunta_numero}", self.selected_answer)
        print(f"Pergunta {self.pergunta_numero}: Resposta selecionada: {
              self.selected_answer}")
