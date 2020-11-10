from flask import Flask, redirect, request, render_template
from surveys import satisfaction_survey

app = Flask(__name__)
responses = []


@app.route('/')
def Home():
    return render_template('survey_start.html')

@app.route('/questions/<int:number>')
def quest_input(number):
    return render_template('question.html', question=satisfaction_survey.questions[number])

@app.route('/thankyou')
def thank_you():
    return render_template('/completion.html')

@app.route('/answer', methods=['POST'])
def survey_responses():
    question_index = len(responses)
    num_ans = int(request.form['answer'])
    ans_val = satisfaction_survey.questions[question_index].choices[num_ans]
    responses.append(ans_val)
    if question_index + 1 < len(satisfaction_survey.questions):
        return redirect(f'/questions/{question_index + 1}')
    else:
        return redirect('/thankyou')