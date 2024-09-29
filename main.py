import openai
from flask import Flask, render_template, request

openai.api_key = "Your API key"

app = Flask(__name__)

# List to store generated recipes
recipe_history = []

def generate_tutorial(components):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant."
        }, {
            "role": "user",
            "content": f"Suggest an Italian recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {components}, Olive Oil, Garlic, Tomatoes, Basil, Parmesan Cheese."
        }]
    )
    return response.choices[0].message.content

@app.route('/', methods=['GET', 'POST'])

def hello():
    output = ""
    if request.method == 'POST':
        components = request.form['components']
        output = generate_tutorial(components)
        # Store the generated recipe in history
        recipe_history.append(output)
    
    return render_template('index.html', output=output, history=recipe_history)

@app.route('/generate', methods=['POST'])

@app.route('/generate', methods=['POST'])

def generate():
    components = request.form['components']
    output = generate_tutorial(components)
    # Store the generated recipe in history
    recipe_history.append(output)
    return {
        'output': output,
        'history': recipe_history
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
