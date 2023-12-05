import tkinter as tk
from openai import OpenAI
from creds import CHATGPT_API_KEY

class ChatGPTAPI:
    """
    ChatGPTAPI class manages the interaction with the OpenAI GPT-3.5 Turbo model for chat integration.

    Attributes:
        chat_display (tk.Text): The text widget for displaying chat messages.
        user_input_entry (tk.Entry): The entry widget for user input.
        client (OpenAI): The OpenAI GPT-3.5 Turbo client.
        messages (list): List of chat messages containing user and assistant interactions.
    """

    def __init__(self, chat_display, user_input_entry):
        """
        Initializes the ChatGPTAPI instance.

        Args:
            chat_display (tk.Text): The text widget for displaying chat messages.
            user_input_entry (tk.Entry): The entry widget for user input.
        """
        self.chat_display = chat_display
        self.user_input_entry = user_input_entry
        self.client = OpenAI(api_key=CHATGPT_API_KEY)
        self.messages = [{"role": "assistant", "content": "How can I help?"}]

    def send_message(self, user_input):
        """
        Sends the user input message to the OpenAI GPT-3.5 Turbo model, updates messages, and displays chat history.

        Args:
            user_input (str): The user's input message.
        """
        self.messages.append({"role": "user", "content": user_input})
        assistant_response = self.get_assistant_response()
        self.messages.append({"role": "assistant", "content": assistant_response})
        self.display_chat_history()

    def get_assistant_response(self):
        """
        Retrieves the assistant's response from the OpenAI GPT-3.5 Turbo model.

        Returns:
            str: The assistant's response.
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in self.messages],
        ).choices[0].message.content

        return response

    def display_chat_history(self):
        """
        Displays the chat history in the chat_display widget.
        """
        self.chat_display.config(state="normal")
        self.chat_display.delete(1.0, "end")

        for message in self.messages:
            self.chat_display.insert("end", f"{message['role'].capitalize()}: {message['content']}\n")

        self.chat_display.config(state="disabled")
