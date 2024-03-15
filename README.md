# Simple WhatsApp Bot
This WhatsApp bot is created using the Python programming language and interacts with users through the WhatsApp application using the WhatsApp Twilio API service. This bot has four simple features that allow users to generate random data instantly. These features include generating passwords, generating random images, generating fake user data, and generating random jokes.

# Table of Contents

- [Simple WhatsApp Bot](#simple-whatsapp-bot)
- [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Documentation API WhatsApp Bot](#documentation-api-whatsapp-bot)
    - [Miscellaneous](#miscellaneous)
      - [Root](#root)
  - [Running the Application](#running-the-application)
## Prerequisites

Before running the WhatsApp Bot, make sure you have the following installed:

- **twilio**
- **nodemon**
- **localtunnel**
- **flask**
- **node.Js**

## Installation

1. Clone the repository from GitHub:

   ```shell
   git clone https://github.com/haqi111/WaBot.git
   ```

2. Change into the project directory:

   ```shell
   cd WaBot
   ```

3. Install the required dependencies using npm and pip

   ```shell
   npm install -g nodemon localtunnel
   ```
   ```shell
   pip install flask twilio
   ```

## Configuration

Before running the application, you need to configure the following settings in the `.env` file:

- URL configuration:
  - `.env['IMAGE_URL']`: link for generate random image.
  - `.env['RANDOM_USER_API_URL']`: link for generate random data user.
  - `.env['JOKES_API_URL']`: link for generate random jokes.
- Twilio configuration:
     - link tutorial for twilio sandbox activation.
       ```shell
        https://youtu.be/UVez2UyjpFk?si=ZkLlQtGIvKPp9XcC
       ```
- localtunnel configuration 
     - Run this command on the terminal .
       ```shell
        nodemon --watch "main.py" --exec "lt --subdomain YOURSUBDOMAIN --port 5000" --delay 3
       ```
     - Replace YOURSUBDOMAIN with your subdomain.  
     - After that enter the output to twilio sandbox setting

## Documentation API WhatsApp Bot

### Miscellaneous
#### Root

- **Endpoint:** /
- **Method:** POST
- **Response:**  
    - Hello! Welcome to our service. Please choose from the following options :
        - 1.Generate Random Password
        - 2.Generate Random Image
        - 3.Generate Fake User Data
        - 4.Generate Random Jokes

## Running the Application

To run the WhatsApp Bot application, execute the following command:

```shell
nodemon main.py
```

The application will start running on `http://localhost:5000/`.

Make sure you have the required dependencies installed and the necessary configurations set before running the application.

That's it! You have successfully set up and documented the WhatsApp Bot application.