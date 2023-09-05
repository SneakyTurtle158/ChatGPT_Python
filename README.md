# ChatGPT_Python
Python script integration with ChatGPT's ChatCompletion.

## Installation
Clone the repository: 
```git clone https://github.com/SneakyTurtle158/ChatGPT_Python.git
```
  
Install the required packages if you don't have them:  
```
pip3 install openai argparse colorama logging
```

## API Key  
Before running the script, you will need to generate an API key and have a valid API subscription plan from openai.com.  
You can do this by:  
- Logging into https://openai.com/
- Select API
- Click on your account at the top right and then _View API Keys_
- Click create new secret key and give it a name.
- Copy the key and store it securely, this gives direct API access to your account.

# Script functionality

There are multiple ways to run the scipt. There are two key things to keep in mind, how you want to supply the API key, and if you want to only ask one question, or many. 
  
```
chatgpt> python3.11.exe .\chatgpt.py -h
usage: chatgpt.py [-h] [-a API] [-q QUESTION] [-l LOG_FILE]
 
This tool can be used for interacting with the ChatGPT API. Default mode is interactive mode. Single questions can be passed using the -q switch.

options:
  -h, --help            show this help message and exit
  -a API, --api API     API key
  -q QUESTION, --question QUESTION
                        Pass a single question.
  -l LOG_FILE, --log_file LOG_FILE
                        File to save log messages (default: script.log)
```

## Supplying the API key:

### Through the command line:

The API key can be passed as a command line arguement:
```
chatgpt> python3.11.exe .\chatgpt.py -a sk-s################################Z
```

### From a file:

With the API key stored in a text file, initiate the script without the -a arguement:
```
chatgpt> python3.11.exe .\chatgpt.py
What is the full path for your API key file (press enter to input key manually): C:\user\..\desktop\api_key
Interactive mode. Type 'exit' to quit.
User Input: 
```

### Write it in the terminal:
Follow the same steps as From a file, however press enter when you are asked for the file path. You will then be prompted to manually enter the API Key.

## Single Question Vs. Interactive Mode:

### Interactive mode:
Interactive mode is the default setting when you initiate the script. To escape from the interactive mode prompt, when you are done, type `exit` in the User input prompt.

### Single Question:
You can pass a single question as a command line arguement (using the `-q` switch) if you only want to ask one question:
```
python3.11.exe .\chatgpt.py -a sk-<redacted> -q "What is the square root of 50?"
Single question mode used. Your question is: What is the square root of 50?
--------------------------------------------------
ChatGPT: The square root of 50 is approximately 7.071.
--------------------------------------------------    
```

## Logging

By default, logging is set to create a script.log file in the directory that you execute the script from. This will also keep a transcript of your questions and ChatGPT's answers in case you need to go back and look at any of your previous queries.  
  
You can manually set the log path/name using the -l option:
```
python3.11.exe .\chatgpt.py -a sk-<redacted> -l new_log_name.log -q "What is the square root of 50?"
Single question mode used. Your question is: What is the square root of 50?
--------------------------------------------------
ChatGPT: The square root of 50 is approximately 7.071.
--------------------------------------------------    
chatgpt> dir
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          9/5/2023  12:05 AM           3678 chatgpt.py
-a----          9/5/2023  12:08 AM            242 new_log_name.log
-a----          9/5/2023  12:04 AM            302 script.log
```
