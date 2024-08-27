from flask import Flask, request, redirect, render_template_string
import string
import random

app = Flask(__name__)

# Dictionary to store the mappings of short URLs to original URLs
url_map = {}

# Characters to use for generating short URLs
characters = string.ascii_letters + string.digits


def generate_short_url():
    return ''.join(random.choice(characters) for _ in range(6))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = generate_short_url()

        # Ensure the generated short URL is unique
        while short_url in url_map:
            short_url = generate_short_url()

        url_map[short_url] = original_url
        return render_template_string('''
            <p>Short URL: <a href="/{{short_url}}">{{short_url}}</a></p>
            <p>Original URL: {{original_url}}</p>
            <a href="/">Shorten another URL</a>
        ''', short_url=short_url, original_url=original_url)

    return '''
        <form method="post">
            Original URL: <input type="text" name="original_url">
            <input type="submit" value="Shorten">
        </form>
    '''


@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_map.get(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return 'URL not found', 404


if __name__ == '__main__':
    app.run(debug=True)
