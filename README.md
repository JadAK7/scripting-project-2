# scripting-project-2

## Introduction
The goal of this project is to create a Python script that can be run on a website to discover subdomains, directories, and files that are not easily visible to the user. These hidden links can potentially lead to pages with vulnerabilities that could be exploited. The script should take a website's URL as an argument, and use two provided text files to identify potential subdomains and directories. Then, the script should scan the html of the given URL to get all links found in the href attribute of the <a> tags.
  
## Steps
1. Get URL from arguments. Use regex to get the domain of the website, without the https:// and the www.
2. Read both files that were given and store them in arrays respectively.
3. Iterate over each array. For the subdomains array, concatenate it at the beginning of the domain and check if it is valid. If yes, write the new URL to the result bat file; if not, continue. Same thing for the directories and files array.
4. Retreive the html of the URL given by the user, use regex to retreive all links found inside the href attributes of the <a> tags. Store all found links inside a result bat file.
  
## Challenges
The main challenge was testing the valid URLs as they would take a lot of time ot finish. To solve it, a small sample was taken from the given files to test whether valid URLs would be properly written in the result file.
