SYSTEM_PROMPT = """
You are Anuvaad AI, a multilingual assistant for Indian users.
Be polite, clear, and helpful.
"""

def build_prompt(user_text):
    return SYSTEM_PROMPT + "\nUser: " + user_text
