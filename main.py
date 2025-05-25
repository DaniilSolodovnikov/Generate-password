from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def generate_password(length=12, use_digits=True, use_specials=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_digits = 'digits' in request.form
        use_specials = 'specials' in request.form
        password = generate_password(length, use_digits, use_specials)
    return render_template('index.html', password=password)


if __name__ == '__main__':
    app.run(debug=True)