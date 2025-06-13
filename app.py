from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'flashcard-secret'

flashcards = []
scores = []

@app.route('/')
def home():
    return render_template('index.html', flashcards=flashcards)

@app.route('/add', methods=['POST'])
def add_flashcard():
    question = request.form['question']
    answer = request.form['answer']
    flashcards.append({'question': question, 'answer': answer})
    return redirect(url_for('home'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answers = request.form
        score = sum(1 for i, card in enumerate(flashcards) if user_answers.get(str(i)) == card['answer'])
        scores.append(score)
        return render_template('score.html', score=score, total=len(flashcards))

    return render_template('quiz.html', flashcards=flashcards)

@app.route('/scores')
def view_scores():
    return render_template('scores.html', scores=scores)

if __name__ == '__main__':
    app.run(debug=True)
