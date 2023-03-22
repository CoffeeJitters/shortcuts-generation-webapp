from flask import Flask, render_template, request, jsonify
import openai

app = Flask("myapp")


# Replace 'your_openai_api_key' with your actual OpenAI API key
openai.api_key = "your_openai_api_key"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = generate_shortcut(user_input)
        return jsonify(response)
    return render_template("index.html")

def generate_shortcut(user_input):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Design an iOS shortcut for: {user_input}",
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":

    app.run(debug=True)
