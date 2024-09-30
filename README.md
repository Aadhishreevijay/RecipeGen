# Recipe Generator

## Overview
The Recipe Generator is a web application that utilizes OpenAI's GPT-3.5-turbo model to create Italian recipes based on user-provided ingredients. Users can enter available ingredients, and the application generates a fun and unique recipe, including a humorous twist on the recipe name, step-by-step instructions, and a fun fact about the dish.

## Features
- **Recipe Generation**: Input your available ingredients and receive a unique Italian recipe.
- **Recipe History**: View a list of previously generated recipes.
- **User-Friendly Interface**: Simple and clean design for easy interaction.
- **Copy to Clipboard**: Easily copy the generated recipe to share or save.

## Technologies Used
- **Python**: For the backend, utilizing Flask as the web framework.
- **HTML/CSS**: For the frontend, including Bootstrap for responsive design.
- **JavaScript**: For handling asynchronous requests and dynamic updates to the recipe history.
- **OpenAI API**: To generate recipes based on user input.

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- OpenAI Python client library

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Aadhishreevijay/Recipe-Generator.git
   cd Recipe-Generator
   ```
   
2. Install the required packages:
   ```bash
   pip install flask openai
   ```

3. Set your OpenAI API key:
   Replace `"Your API key"` in `main.py` with your actual OpenAI API key.

### Running the Application
To start the application, run:
```bash
python main.py
```
Visit `http://127.0.0.1:8080` in your web browser to access the Recipe Generator.

## How to Use
1. Enter a list of ingredients you have available in the input field.
2. Click on "Create a Recipe" to generate your recipe.
3. The generated recipe will appear below along with any previously generated recipes in the history section.
4. Use the "Copy" button to copy the recipe to your clipboard.

## File Structure
- **main.py**: The main Flask application code.
- **templates/index.html**: The HTML template for the web application.
- **static/style.css**: The CSS file for styling the application.
- **static/script.js**: The JavaScript file for handling frontend functionality.

## Output Example
![Output Example](https://github.com/user-attachments/assets/f4d8ab6c-0602-4f4a-a38a-5c9f71e106be)
