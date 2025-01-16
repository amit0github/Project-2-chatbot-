import json
import random
import logging

# Set up logging
logging.basicConfig(filename='chat_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Load responses from JSON file
def load_responses(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Generate a random agent name
def generate_agent_name():
    names = ["Ram","Shyam","Amit","Aarin","Gopi","Ishan","Himanshu"]
    return random.choice(names)

# Get a response based on user input
def get_response(user_input, responses):
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])
    return random.choice(responses["default"])

def main():
    print("Welcome to the University of Poppleton's chat system!")
    
    # Prompt for user name
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}! I'm your virtual agent today.")
    
    # Display agent name
    agent_name = generate_agent_name()
    print(f"Your agent today is {agent_name}.")

    # Load responses
    responses = load_responses('responses.json')

    while True:
        user_question = input(f"{user_name}: ")
        
        # Check for exit commands
        if user_question.lower() in ["bye", "quit", "exit"]:
            print(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            print("--Created By: Amit Chaudhary")
            break
        
        # Log the question
        logging.info(f"{user_name}: {user_question}")
        
        # Get response
        response = get_response(user_question, responses)
        print(f"{agent_name}: {response}")
        
        # Log the response
        logging.info(f"{agent_name}: {response}")

if __name__ == "__main__":
    main()