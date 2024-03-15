import os
import random
import string
import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

app = Flask(__name__)

# Define welcome message with keywords
def welcome_message():
    welcome_msg = (
        "Hello! Welcome to our service. Please choose from the following options:\n"
        "1. Generate Random Password\n"
        "2. Generate Random Image\n"
        "3. Generate Fake User Data\n"
        "4. Generate Random Jokes\n"
    )
    return welcome_msg

#Generate Random Password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

#Generate Random Image
def generate_image():
    image_url = os.getenv("IMAGE_URL")
    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            return response.url
        else:
            print("Failed to fetch image from the URL.")
    else:
        print("IMAGE_URL environment variable is not set.")

#Generate Fake User Data
def get_random_user():
    api_url = os.getenv("RANDOM_USER_API_URL")
    if api_url:
        response = requests.get(api_url)
        if response.status_code == 200:
            user_data = response.json()
            user = user_data['results'][0]
            formatted_user = {
                'name': f"{user['name']['first']} {user['name']['last']}",
                'gender': user['gender'],
                'email': user['email'],
                'dob': user['dob']['date'],
                'address': f"{user['location']['street']['number']} {user['location']['street']['name']}, "
                           f"{user['location']['city']}, {user['location']['state']}, {user['location']['country']}",
                'phone': user['phone'],
                'picture': user['picture']['large']
            }
            return formatted_user
        else:
            print("Failed to fetch data from the API.")
            return None
    else:
        print("RANDOM_USER_API_URL environment variable is not set.")
        return None

    
#Generate Random Jokes
def get_jokes():
    api_url = os.getenv("JOKES_API_URL")
    if api_url:
        response = requests.get(api_url)
        if response.status_code == 200:
            jokes_data = response.json()
            setup = jokes_data.get('setup', '')
            punchline = jokes_data.get('punchline', '')
            if setup and punchline:
                formatted_joke = {
                    'setup': setup,
                    'punchline': punchline
                }
                return formatted_joke
            else:
                return {"error": "Failed to fetch data from the API."}
        else:
            return {"error": "Failed to fetch data from the API."}
    else:
        return {"error": "JOKES_API_URL environment variable is not set."}

@app.route("/", methods=["POST"])
def reply():
    text = request.form.get("Body", "").lower()
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")
    response = MessagingResponse()
    
    if "1" in text:
       # generate_password
        random_password = generate_password()  
        msg = response.message(f"Your random password is: {random_password}")

    elif "2" in text:
        #generate_image
        msg = response.message("This is your random image")
        msg.media(generate_image())
       
    elif "3" in text:
         # Generate_fake_user_data
        random_user = get_random_user()
        if random_user:
            message = (
            f"Fake User Data:\n"
            f"Name: {random_user['name']}\n"
            f"Gender: {random_user['gender']}\n"
            f"Email: {random_user['email']}\n"
            f"Date of Birth: {random_user['dob']}\n"
            f"Address: {random_user['address']}\n"
            f"Phone: {random_user['phone']}"
        )
            msg = response.message(message)
            msg.media(random_user['picture'])
        else:
             msg = response.message("Failed to fetch a data from the API.")

    elif "4" in text:
        #generate_jokes
        random_jokes = get_jokes()
        if random_jokes:
            message =(
                 f"jokes: {random_jokes['setup']}\n"
                 f"Punchline: {random_jokes['punchline']}"
            )
            msg = response.message(message)
        else:
            msg = response.message("Failed to fetch a joke from the API.")
                    
    else:
        #welcome_message
        msg = response.message(welcome_message())
        msg.media("https://i.pinimg.com/564x/fa/a3/70/faa370512683c0810a9bbd126550f76d.jpg")
    
    return str(response)

if __name__ == "__main__":
    app.run(port=5000)
