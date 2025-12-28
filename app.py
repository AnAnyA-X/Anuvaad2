from flask import Flask, request, jsonify
from flask_cors import CORS

from translation import translate_to_english, translate_back
from prompt import build_prompt
from llm import llm_response   # dummy or real

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    # Step 1: Translate to English
    english_text, user_lang = translate_to_english(user_input)

    # Step 2: Prompt Engineering
    prompt = build_prompt(english_text)

    # Step 3: Generative AI
    ai_english_reply = llm_response(prompt)

    # Step 4: Translate back
    final_reply = translate_back(ai_english_reply, user_lang)

    return jsonify({
        "reply": final_reply,
        "detected_language": user_lang
    })

if __name__ == "__main__":
    app.run(debug=True)
