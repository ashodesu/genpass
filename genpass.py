import random
import string
import pyperclip
import configparser

def read_password_rules():
    config = configparser.ConfigParser()
    config.read('rules.conf')
    
    rules = {}
    if 'Password' in config:
        rules['length'] = config['Password'].getint('length', 12)  # Default length 12
        rules['uppercase'] = config['Password'].getboolean('uppercase', True)
        rules['lowercase'] = config['Password'].getboolean('lowercase', True)
        rules['numbers'] = config['Password'].getboolean('numbers', True)
        rules['special'] = config['Password'].getboolean('special', True)
    else:
        # Default rules if config file not found or invalid
        rules = {
            'length': 12,
            'uppercase': True,
            'lowercase': True,
            'numbers': True,
            'special': True
        }
    return rules

def generate_password(rules):
    characters = ''
    if rules['lowercase']:
        characters += string.ascii_lowercase
    if rules['uppercase']:
        characters += string.ascii_uppercase
    if rules['numbers']:
        characters += string.digits
    if rules['special']:
        characters += string.punctuation
    
    if not characters:
        characters = string.ascii_letters + string.digits  # Fallback if no rules selected
        
    password = ''.join(random.choice(characters) for _ in range(rules['length']))
    return password

def main():
    rules = read_password_rules()
    password = generate_password(rules)
    pyperclip.copy(password)
    print(f"Generated password: {password}")
    print("Password has been copied to clipboard!")

if __name__ == "__main__":
    main()
