from flask import Flask, request
from gpt4all import GPT4All

app = Flask(__name__)
gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy")

# Define the HTML form for the web application
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Capital Finder</title>
</head>
<body>
    <h1>Capital Finder</h1>
    <form method="POST" action="/get_capital">
        <label for="country">Enter a country:</label>
        <input type="text" id="country" name="country" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

# Generate the capital for a given country using GPT4All
def generate_capital(country):
    messages = [{"role": "user", "content": f"What is the capital of {country}?"}]
    response = gptj.chat_completion(messages)
    generated_content = response['choices'][0]['message']['content']
    capital = generated_content.strip()
    return capital

# Route for the main page
@app.route("/")
def index():
    return HTML_FORM

# Route to handle the form submission
@app.route("/get_capital", methods=["POST"])
def get_capital():
    country = request.form.get("country")
    capital = generate_capital(country)
    return f"The capital of {country} is {capital}"

if __name__ == "__main__":
    app.run()
