import random
import os
import re


def get_random_question(questions_amount=5, foldername='quiz-questions'):
    pattern = r"Вопрос (\d+):(.*?)(Ответ:\s*.*?)(?:\n\n|\Z)"
    proceeded = 0
    questions = []  

    for root, subfolders, filenames in os.walk(foldername):
        for filename in filenames:
            if proceeded >= questions_amount:
                break

            file_path = os.path.join(root, filename)
            
            with open(file_path, encoding='koi8-r') as f:
                file_contents = f.read()

            matches = re.findall(pattern, file_contents, re.DOTALL)

            for match in matches:
                if proceeded >= questions_amount:
                    break
                n, question, answer = match 

                questions.append({
                    'question': question.strip(), 
                    'answer': answer.strip().replace('Ответ:\n', '').replace('"', '').replace('.', '')})
                proceeded += 1

    return random.choice(questions)


if __name__ == '__main__':
    print(get_random_question())
