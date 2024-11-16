# FridayProject9

ChatGPT Text Submission Application

This is a simple Tkinter-based GUI application that allows users to interact with OpenAI's ChatGPT API. Users can enter prompts, submit them to ChatGPT, and view the responses in a separate window

# Getting Started
1. Prerequisites
Before running this application, make sure you have the following installed on your system:

Python 3.7 or later
pip (Python's package installer)

2. Install Required Python Libraries
Run the following command to install the required dependencies:

pip install openai python-dotenv

# Setting Up the API Key
1. Obtain an API Key
Sign up or log in to OpenAI.
Ensure you have purchased credits for your APIs.
Navigate to the API Keys page.
Generate a new API key and copy it.

2. Create a .env File
In the project directory, create a file named API.env.
Add the following line to the .env file, replacing your_api_key_here with your actual API key. Do not surround the key with quotation marks:

OPENAI_API_KEY=your_api_key_here

# Code Breakdown
1. Importing Libraries
tkinter: The standard Python library used for creating graphical user interfaces (GUIs).
openai: The library used to interact with the OpenAI API.
dotenv: Used to load environment variables from the .env file into the application.
os: Used to access environment variables such as the API key.

2. Loading the API Key
load_dotenv(): Loads the environment variables from the .env file, which contains the OpenAI API key.
openai.api_key: The API key is set using os.getenv("OPENAI_API_KEY"), which retrieves the key stored in the .env file.

3. Sending User Input to ChatGPT
send_to_chatgpt(): This function retrieves the text input from the main window, sends it to the OpenAI API, and handles the response.
The user input is fetched using text_box.get("1.0", tk.END) which grabs all text from the Tkinter Text widget.
The input is passed to the openai.chat.completions.create() method, which sends it to the GPT model and returns a response.
If successful, the response is displayed in a new window; if there is an error, the error message is shown in the main window.

4. Displaying the Response in a New Window
show_response_in_new_window(): This function creates a new window (Toplevel) to display the response from ChatGPT.
response_text: A Text widget is used to display the response in a scrollable, readable format.
The text is inserted into the widget using response_text.insert("1.0", response), and editing is disabled using response_text.config(state="disabled")

5. The Main Application Window
The main window is created using Tk() and is configured with a title and size.
The layout includes:
A Label widget prompting the user to enter their input.
A Text widget for user input (with height and width defined).
A Button widget that triggers the send_to_chatgpt() function when clicked.
A Label widget to display errors or success messages briefly.
root.mainloop() keeps the application running until the user closes the window.
