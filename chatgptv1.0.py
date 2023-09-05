import openai
import argparse
from colorama import Fore, Back, Style
import logging

messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

# Pull API key from file
def api_key(key):
    f = open(key, "r")
    return f.readline()

# Get API key from user input
def api_key_cmd():
    f = input("Please input your ChatGPT API key: ")
    return f

# Create interactive mode to talk back and forth with ChatGPT
def interactive_mode():
    print("Interactive mode. Type 'exit' to quit.")
    while True:
        print(Fore.GREEN + "User Input: ", end='')
        message = input()
        if message == "exit":
            logging.info("Interactive mode exited gracefully.")
            break
        elif message:
            logging.info(f"User input: {message}")
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-4", messages=messages
            )
        reply = chat.choices[0].message.content
        logging.info(f"ChatGPT Reply: {reply}")
        print(Fore.RED + "-"*50)
        print(Fore.BLUE + f"ChatGPT: {reply}")
        print(Fore.RED + "-"*50)
        messages.append({"role": "assistant", "content": reply})

def single_question(question):
    print(Fore.GREEN + f"Single question mode used. Your question is: {question}")
    logging.info(f"User Question: {question}")
    message = question
    messages.append(
    {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
    model="gpt-4", messages=messages
    )
    reply = chat.choices[0].message.content
    logging.info(f"ChatGPT Reply: {reply}")
    print(Fore.RED + "-"*50)
    print(Fore.BLUE + f"ChatGPT: {reply}")
    print(Fore.RED + "-"*50)
    messages.append({"role": "assistant", "content": reply})


# Main function
def main():
    parser = argparse.ArgumentParser(description="This tool can be used for interacting with the ChatGPT API. Default mode is interactive mode. Single questions can be passed using the -q switch.")
    parser.add_argument("-a", "--api", help="API key")
    parser.add_argument("-q", "--question", help="Pass a single question.")
    parser.add_argument("-l", "--log_file", help="File to save log messages (default: script.log)")
    args = parser.parse_args()

    log_file = args.log_file if args.log_file else "script.log"
    logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Check if key is passed with -a 
    if args.api:
        openai.api_key = args.api
    #If not, get the API key from a file or direct input
    elif args.api == None:
        apiKey = input("What is the full path for your API key file (press enter to input key manually): ")
        if apiKey:
            openai.api_key = api_key(apiKey)
        else: 
            openai.api_key = api_key_cmd()       
    else:
        print("A valid API key must be used.")
        logging.error("API key not supplied")
        exit
    try:
        if args.question:
            logging.info("Single Question user input used.")
            single_question(args.question)
        else:
            logging.info("Interactive mode enabled.")
            interactive_mode()
    except openai.error.RateLimitError:
        print("You have exceeded your rate limit or your plan does not support API integration.")
        logging.error("You have exceeded your rate limit or your plan does not support API integration.")


if __name__ == "__main__":
    main()
