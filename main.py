import re
import sys

if len(sys.argv) != 2:
    print("Please include website url")
    sys.exit()

website_url = sys.argv[1]

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

