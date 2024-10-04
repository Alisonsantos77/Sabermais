import re


def extract_questions_from_text(text):
    questions = []
    lines = text.strip().split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Procura por perguntas no formato **n. Pergunta**
        question_match = re.match(r'\*\*(\d+)\.\s+(.*?)\*\*', line)
        if question_match:
            question_text = question_match.group(2).strip()
            i += 1
            options = []
            option_letters = []
            # Coleta as opções
            while i < len(lines):
                option_line = lines[i].strip()
                option_match = re.match(r'([a-e])\)\s+(.*)', option_line)
                if option_match:
                    option_letter = option_match.group(1)
                    option_text = option_match.group(2).strip()
                    options.append(f"{option_letter}) {option_text}")
                    option_letters.append(option_letter)
                    i += 1
                elif '**Resposta Correta:**' in option_line:
                    correct_answer_match = re.match(r'\*\*Resposta Correta:\*\*\s*(.*)', option_line)
                    if correct_answer_match:
                        correct_answer_letter = correct_answer_match.group(1).strip().lower()
                        questions.append({
                            'pergunta': question_text,
                            'opcoes': options,
                            'letras_opcoes': option_letters,
                            'resposta_letra': correct_answer_letter
                        })
                    i += 1
                    break
                else:
                    i += 1
        else:
            i += 1
    return questions
