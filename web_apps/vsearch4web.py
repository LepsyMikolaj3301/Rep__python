from asyncore import write
from flask import Flask, render_template, request, escape
from vsearch import search4letters
from cgitb import html


app = Flask(__name__)

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Oto Twoje wyniki'
    def log_request(req: 'flask_request', res: str) -> None:
        with open('vsearch.log', 'a') as log:
            print(req.form, req.remote_addr, req.user_agent, res, file=log, sep=' | ')
            
    results = str(search4letters(phrase,letters))
    log_request(request, results)
    return render_template('results.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_tittle=title,
                            the_results=results,)
@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Witamy na stronie internetowej search4letters!')
if __name__ == '__main__':
    app.run(debug=True)