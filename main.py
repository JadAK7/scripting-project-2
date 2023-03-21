import re

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

