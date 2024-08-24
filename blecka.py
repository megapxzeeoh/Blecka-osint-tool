import sys
import time
import random
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Basic color options
basic_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]

def get_basic_text(text):
    colored_text = ""
    color_index = 0
    for char in text:
        if char == '\n':
            colored_text += char
        else:
            colored_text += basic_colors[color_index] + char
            color_index = (color_index + 1) % len(basic_colors)
    return colored_text

def print_ascii_art():
    art = r'''
 _   _            _    _ 
| | | |          | |  | |
| |_| | ___  _ __| | _| | ___ 
|  _  |/ _ \| '__| |/ / |/ _ \
| | | | (_) | |  |   <| |  __/
\_| |_/\___/|_|  |_|\_\_|\___|
    '''
    print(get_basic_text(art))

def simulate_search_effect():
    search_messages = [
        "Searching...",
        "Looking for matches...",
        "Checking databases...",
        "Scanning social media...",
        "Analyzing data..."
    ]
    for _ in range(5):
        message = random.choice(search_messages)
        sys.stdout.write("\r" + get_basic_text(message))
        sys.stdout.flush()
        time.sleep(1)
    print("\rSearch completed!        ", end="")

def search_email(email):
    api_key = 'your-email-api-key'
    url = 'https://api.email-validator.net/api/verify'
    params = {
        'EmailAddress': email,
        'APIKey': api_key
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get('status') == 'success':
            return {"Email": email, "Valid": data.get('info', 'Unknown')}
        else:
            return {"Email": email, "Valid": "Not valid"}
    except requests.RequestException as e:
        print(get_basic_text(f"Search error: {e}"))
        return {}

def display_results(results):
    if not results:
        print(get_basic_text("No data to display."))
    else:
        print(get_basic_text("\nResults:"))
        for key, value in results.items():
            print(get_basic_text(f"{key}: {value}"))

def main():
    print_ascii_art()
    while True:
        print(get_basic_text("\nChoose an action:"))
        print(get_basic_text("1. Search by email"))
        print(get_basic_text("2. Exit"))
        
        choice = input(get_basic_text("\nYour choice: ")).strip().lower()
        
        if choice == '2':
            print(get_basic_text("Exiting the program..."))
            break
        
        if choice != '1':
            print(get_basic_text("Error: Invalid choice."))
            continue
        
        if choice == '1':
            email = input(get_basic_text("\nEnter email for verification: "))
            simulate_search_effect()
            email_results = search_email(email)
            display_results(email_results)
    
if __name__ == "__main__":
    main()
