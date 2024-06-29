from flask import render_template, request, session
from app import app
import openai
from openai import Image, ChatCompletion
import re

openai.api_key = open("key.txt", "r").read().strip("\n")


def generate_image(prompt):
    try:
        response = Image.create(prompt=prompt, n=1, size="512x512")
        img_url = response.data[0].url
    except Exception as e:
        img_url = "https://pythonprogramming.net/static/images/imgfailure.png"
    return img_url


def chat_interaction(input_text, message_history, role="user"):
    message_history.append({"role": role, "content": f"{input_text}"})

    completion = ChatCompletion.create(model="gpt-3.5-turbo", messages=message_history)

    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": f"{reply_content}"})

    return reply_content, message_history


@app.route("/", methods=["GET", "POST"])
def home():
    title = "TaleTinkerer"
    button_messages = {}
    button_states = {}

    if request.method == "GET":
        session["message_history"] = [
            {
                "role": "user",
                "content": """You are a story telling expert with short interesting & funny stories, also possess experience explroing all across the globe. One day, you come across a mysterious door in the middle of a bustling city street. Curiosity overtakes you, and you decide to open it. As you step through, you find yourself in a vibrant forest with talking animals.
                If you understand, say, OK, and begin when I say "begin." When you present the story and options, present just the story and start immediately with the story, no further commentary, and then options like "Option 1:" "Option 2:" ...etc where as the option 4 will remain as the custom prompt from the user.""",
            },
            {
                "role": "assistant",
                "content": f"""Understood. Ready to begin when you are.""",
            },
        ]

        message_history = session["message_history"]
        reply_content, message_history = chat_interaction("Begin", message_history)

        text = reply_content.split("Option 1")[0]

        options = re.findall(r"Option \d:.*", reply_content)

        for i, option in enumerate(options):
            button_messages[f"button{i+1}"] = option

        for button_name in button_messages.keys():
            button_states[button_name] = False

    message = None
    button_name = None

    if request.method == "POST":
        message_history = session["message_history"]
        button_messages = session
        

        button_name = request.form.get("button_name")
        button_states[button_name] = True
        message = button_messages.get(button_name)

        if button_name == "button4":
            custom_prompt = request.form.get("custom_prompt")
            reply_content, message_history = chat_interaction(
                custom_prompt, message_history
                
            )
        else:
            reply_content, message_history = chat_interaction(message, message_history)

        text = reply_content.split("Option 1")[0]
        options = re.findall(r"Option \d:.*", reply_content)

        button_messages = {}
        for i, option in enumerate(options):
            button_messages[f"button{i+1}"] = option
        for button_name in button_messages.keys():
            button_states[button_name] = False

    session["message_history"] = message_history
    session["button_messages"] = button_messages

    image_url = generate_image(text)

    return render_template(
        "home.html",
        title=title,
        text=text,
        image_url=image_url,
        button_messages=button_messages,
        button_states=button_states,
        message=message,
    )
