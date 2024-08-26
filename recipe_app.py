from flask import Flask, request, render_template
import requests

app = Flask(__name__)

SPOONACULAR_API_KEY = 'API'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        recipes = get_recipes(ingredients)
        return render_template('results.html', recipes=recipes)
    return '''
        <form method="POST">
            <label for="ingredients">Enter ingredients (comma separated):</label>
            <input type="text" id="ingredients" name="ingredients">
            <button type="submit">Search</button>
        </form>
    '''

def get_recipes(ingredients):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={SPOONACULAR_API_KEY}"
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
