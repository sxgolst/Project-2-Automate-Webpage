def generate_concept_HTML(question_title, question_answer):
    html_text_1 = '''
    <div class="question">
       <div class="question-title">
           ''' + question_title
    html_text_2 = '''
       </div>
       <div class="question-answer">
           ''' + question_answer
    html_text_3 = '''
       </div>
    </div>'''

    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('ANSWER:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_answer(concept):
    start_location = concept.find('ANSWER:')
    answer = concept[start_location+8 :]
    return answer

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept   

text = '''TITLE: What is a function  
ANSWER: A function takes input, processes it and the outputs. Are the mapping of inputs and outputs! 
TITLE: What is the difference between making and using a function?
ANSWER: Functions starts with the line with the keyword <b>def</b> followed by the name of the function followed by the values 
TITLE: How do functions help programmers avoid repetition?
ANSWER: Functions can be reused over and over again once they have been defined.'''

def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        answer = get_answer(concept)
        concept_html = generate_concept_HTML(title, answer)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html

concept1 = get_concept_by_number(text, 1)
title1 = get_title(concept1)
answer1 = get_answer(concept1)
html1 = generate_concept_HTML(title1, answer1)
print html1


def make_NTML(concept):
    concept_title = concept[0]
    concept_answer = concept[1]
    return generate_concept_HTML(concept_title, concept_answer)

print generate_all_html(text)