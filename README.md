Argument Clinic AI

This is a Python program that uses OpenAI's GPT-3 language model to generate arguments based on user input. It creates a conversation where the program takes on the Argument Clinic side of the conversation from the Monty Python sketch.

Dependencies
This program requires the following dependencies:

concurrent.futures

openai

string

time

Usage
Set your OpenAI API key by replacing "your_api_key_here" with your actual API key in the openai.api_key line.
Run the program in your terminal or Python environment.

Enter your argument when prompted by the program. It will respond using the script from the Argument Clinic skit.

The program will continue prompting you for arguments until you enter "quit" or you interrupt it using Ctrl+C.


Notes
The program uses a thread pool executor to process OpenAI requests, allowing for multiple requests to be made concurrently.

The program has a timeout of 15 seconds for each request. If the response takes longer than that, the program will prompt the user to try again.

If an exception occurs, the program will prompt the user with an error message.

The program cleans the user input by removing all punctuation from it.

