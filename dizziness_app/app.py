from flask import Flask, request, jsonify, render_template
import openai
import os

openai.api_key = os.getenv("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")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.json
    prompt = f"""A patient submitted the following dizziness and imbalance questionnaire. Provide a differential diagnosis and a management plan based on this information:

{data}

Include possible vestibular, neurological, cardiovascular, and systemic causes."""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        diagnosis = response.choices[0].message.content
        return jsonify({"result": diagnosis})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
