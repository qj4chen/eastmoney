import re

with open('./data.txt') as file:
    html = file.read()

# method 1: not safe
questions = re.findall(string=html, pattern=r'<div class="qa_question_text">([\s\S]*?)<\/div>')
questions = [ques.strip() for ques in questions]
answers = re.findall(string=html, pattern=r'<div class="qa_answer_text">[\s\S]*?<p>([\s\S]*?)<\/p>')
answers = [ans.strip() for ans in answers]

# method 2: better
question_answer_pairs = re.findall(string=html,
                                   pattern=r'<div class="qa_question_text">([\s\S]*?)<\/div>[\s\S]*?<div class="qa_answer_text">[\s\S]*?<p>([\s\S]*?)<\/p>')
question_answer_pairs = [(q.strip(), a.strip()) for q, a in question_answer_pairs]
