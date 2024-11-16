import tkinter as tk
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to send the user's input to ChatGPT and display the response in a new window
def send_to_chatgpt():
    user_input = text_box.get("1.0", tk.END).strip()  # Get text from text box
    if not user_input:
        response_label.config(text="Please enter some text!")
        return
    
    try:
        # Send the prompt to ChatGPT
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the model
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        
        # Access the response content
        reply = response.choices[0].message.content  # Use dot notation to access fields
        
        # Open a new window to display the response
        show_response_in_new_window(reply)
    except Exception as e:
        # Handle and display the error message in the main window
        response_label.config(text=f"Error: {e}")


# Function to create a new window for displaying the response
def show_response_in_new_window(response):
    # Create a new Toplevel window
    response_window = tk.Toplevel(root)
    response_window.title("ChatGPT Response")
    response_window.geometry("500x300")  # Set size for the response window
    
    # Add a text widget to display the response
    response_text = tk.Text(response_window, wrap="word", font=("Arial", 12))
    response_text.pack(expand=True, fill="both", padx=10, pady=10)
    
    # Insert the response and disable editing
    response_text.insert("1.0", response)
    response_text.config(state="disabled")


# Create the main application window
root = tk.Tk()
root.title("ChatGPT Text Submission")
root.geometry("500x400")  # Set the window size

# Label
label = tk.Label(root, text="Enter your prompt for ChatGPT below:")
label.pack(pady=10)

# Text box
text_box = tk.Text(root, height=5, width=50)
text_box.pack(pady=10)

# Submit Button
button = tk.Button(root, text="Submit", command=send_to_chatgpt)
button.pack(pady=10)

# Response Label (to show brief errors or confirmations)
response_label = tk.Label(root, text="", wraplength=450, justify="left")
response_label.pack(pady=20)

# Run the application
root.mainloop()
