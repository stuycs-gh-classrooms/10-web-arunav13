#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

def make_html(title, body):
    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="utf-8">
    """
    html+= '<title>' + title + '</title></head>'
    html+= '<body>' + body + '</body>'
    html+= '</body></html>'
    return html


def make_question(question):
    html = '<h3>'
    html += question
    html += '</h3>'
    return html


def make_form(question_num, radio_options):
    # html = """
    radio = ''
    html = '<form action="dynaform.py" method="GET">'
    html += '<input type="hidden" name="question" value="' + question_num + '">'

    for option in radio_options:
        x = radio_options.index(option)
        if x == 0:
            name = 'a'
        elif x == 1:
            name = 'b'
        else:
            name = 'c'
        iput = '<div>'
        iput += '<input type="radio" name="choice" value="' + name + '">'
        iput += option + '</div>'
        radio += iput

    html += radio
    html += '<input type="submit" value="Submit!">'
    return html


body = '<h1> Pick your own adventure! </h2>'
question_bank = {
    '1': ["It’s midnight on a Saturday night. The sound of the wind whistling echoes through your ears. Suddenly, you hear a knock on the door. You’re unsure of whether to answer it. What do you do?", 'Definitely answer it', 'Run away'],
    '1a': ['The door opens and you see a policeman. “We will need you to come with us,” he says. Suddenly, you remember you have a bottle of pepper spray in your hand. What do you do?', 'Use it', 'Save it for later'],
    '1b': ['You run away and race down the block. Suddenly, you receive a call from a colleague. “Are the police there? Look, you need to escape. They realized you are responsible for the theft of the diamond. But, remember, we still need to steal the crimson diamond from the Museum of Sciences. Go to the location as quickly as possible and return to the headquarters.','Use the subway station a mile away', 'Use the loud helicopter a block away'],
    '1aa': ['You aim the pepper spray at the policeman. The policeman struggles to see, but uses his walkie-talkie to dial his colleague. What do you do?', 'Panic, sprint and run away' , 'Wait to see if you receive important info'],
    '1ab': ['As you wait cautiously, you receive a call from your phone. “Sorry, got to take this,” you say to the policemen. The phone answers: “Are the police there? Look, you need to escape. They realized you are responsible for the theft of the diamond. But, remember, we still need to steal the crimson diamond from the Museum of Sciences. Go to the location as quickly as possible and return to the headquarters.', 'Use the subway station a mile away', 'Use the loud helicopter a block away'],
    '1aba': ['The train station is a mile away and you sprint to the station. A few blocks away, you hear sirens in the background. The police are behind you and you’ve been caught. Game over' , 'Play Again'],
    '1aab': ['As you wait cautiously, you receive a call from your phone. “Sorry, got to take this,” you say to the policemen. The phone answers: “Are the police there? Look, you need to escape. They realized you are responsible for the theft of the diamond. But, remember, we still need to steal the crimson diamond from the Museum of Sciences. Go to the location as quickly as possible and return to the headquarters.', 'Use the subway station a mile away', 'Use the loud helicopter a block away'],
    '1aaa': ['You run several blocks until you hear sirens from the police cars in the distance. You have been caught. Game over.' , 'Play Again'],
    '1abb' : ['The helicopter is a block away and you can hear sirens in the background. Just in the nick of time, you enter the helicopter. You know the police are onto you, but you’re relieved you’re safe. You keep traveling until you reach and enter the Museum. The diamond is right in front of you. You reach out. Then, you hear “STOP. Stand where you are!” What do you do next?', 'Surrender and accept defeat' , 'Use the pepper spray' , 'Sprint into the darkness'],
    '1ba': ['The train station is a mile away and you sprint to the station. A few blocks away, you hear sirens in the background. The police are behind you and you’ve been caught. Game over' , 'Play Again'],
    '1aaba': ['The train station is a mile away and you sprint to the station. A few blocks away, you hear sirens in the background. The police are behind you and you’ve been caught. Game over' , 'Play Again'],
    '1bb': ['The helicopter is a block away and you can hear sirens in the background. Just in the nick of time, you enter the helicopter. You know the police are onto you, but you’re relieved you’re safe. You keep traveling until you reach and enter the Museum. The diamond is right in front of you. You reach out. Then, you hear “STOP. Stand where you are!” What do you do next?', 'Surrender and accept defeat' , 'Use the pepper spray' , 'Sprint into the darkness'],
    '1aabb': ['The helicopter is a block away and you can hear sirens in the background. Just in the nick of time, you enter the helicopter. You know the police are onto you, but you’re relieved you’re safe. You keep traveling until you reach and enter the Museum. The diamond is right in front of you. You reach out. Then, you hear “STOP. Stand where you are!” What do you do next?', 'Surrender and accept defeat' , 'Use the pepper spray' , 'Sprint into the darkness'],
    '1bbb': ['You use the pepper spray to delay the intruder, grab the diamond, and leave. You enter the helicopter and you are safe with the retrieved diamond. You have won' , 'Play Again'],
    '1aabbb': ['You use the pepper spray to delay the intruder, grab the diamond, and leave. You enter the helicopter and you are safe with the retrieved diamond. You have won' , 'Play Again'],
    '1bba': ['Game Over' , 'Play Again'],
    '1aabba': ['Game Over' , 'Play Again'],
    '1bbc': ['You manage to escape safely, but you have not retrieved the diamond. The End.' , 'Play Again'],
    '1aabbc': ['You manage to escape safely, but you have not retrieved the diamond. The End.' , 'Play Again'],
    '1abba' : ['Game Over' , 'Play Again']
}


data = cgi.FieldStorage()
html = make_html('Pick your adventure', 'Pick your adventure')
if (len(data) == 0):
    question_num = '1'
else:
    question_num = data['question'].value
    choice_num = data['choice'].value
    if question_num in ['1bba' , '1aabba' ,  '1aabbc', '1aabbb' , '1bbb' , '1ba' ,'1aaa' , '1aba' , '1aaba' , '1bbc'] and choice_num == 'a':
        question_num = '1'
    else:
        question_num += choice_num


list = question_bank[question_num]
question = list[0]
choices = list[1:]

html += make_question(question)
if choices != []:
    html += make_form(question_num, choices)
print(html)

# name = 'batman'
# if ('name' in data):
#     name = data['name'].value
#     bgcolor = 'DarkSeaGreen'
#     if ('bgcolor' in data):
#         bgcolor = data['bgcolor'].value
#     body = '<body style="background-color: '
#     body+= bgcolor + ';">'
#     body+= '<h1>Hello ' + name + '</h1>'
#     body+= '<br><a href="dynaform.py">Try Again</a>'
#     html = make_html('Form Result', body)
#     print(html)
# #if no form data, return the form html instead of result
