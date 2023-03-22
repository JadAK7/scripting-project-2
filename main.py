import re
import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Please include website url")
        sys.exit()

    website_url = sys.argv[1]
    
    url = re.search(r"(https://www\.|https://)?(.*)", website_url).group(2)

    html = ''
    try:
        response = requests.get('https://' + url)
    except requests.exceptions.ConnectionError as e:
        print('An error occurred:', e)
    else:
        print(response.status_code)
        html = response.text


    directories = []
    subdomains = []
    with open('subdomains_dictionary.bat', 'r') as f:
        for line in f:
            match = re.match(r'^\S+$', line)
            if match:
                subdomain = match.string
                subdomains.append(subdomain)
    with open('dirs_dictionary.bat', 'r') as f:
        for line in f:
            match = re.match(r'^\S+$', line)
            if match:
                directory = match.string
                directories.append(directory)
                
    return html

main()