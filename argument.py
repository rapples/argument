import concurrent.futures
import openai
import string
import time


# Set OpenAI API key
openai.api_key = "your_api_key_here"


# Function to process OpenAI request
def process_request(name):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="I'd like you to assume the Argument clinic side of a conversation about '" + s + "' Can you help me out? Please respond using the script from the Argument Clinic skit by Monty Python. Don't print the Me: side of the conversation.",
            temperature=0,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            timeout=15,
            presence_penalty=0
        )
        return response.choices[0].text
    except:
        return None


# Use a thread pool executor to process requests
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    while True:
        try:
            # Get user input and clean it
            s = input("Please enter your argument: ")
            s = s.translate(str.maketrans("", "", string.punctuation))


            # Start timer and submit request
            start_time = time.time()
            future = executor.submit(process_request, s)
            response = future.result(timeout=15)


            # End timer and check response time
            end_time = time.time()
            if end_time - start_time > 15:
                print("Sorry, the response took too long. Please try again.")
                continue


            # Print response
            print(response)


            # Exit loop if user input is "quit"
            if s == "quit":
                break


        except KeyboardInterrupt:
            print("\nKeyboardInterrupt received. Exiting.")
            break


        except Exception as e:
            print("Time is up! Sorry, I can't argue unless you pay.", str(e))
            continue


