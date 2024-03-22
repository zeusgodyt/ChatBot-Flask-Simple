from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def generate_response(user_message):
    if "hello" in user_message.lower():
        return "Hello! How can I assist you today?"
    elif "help" in user_message.lower():
        return "Sure, I'm here to help. What do you need assistance with?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    bot_response = generate_response(user_message)
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
