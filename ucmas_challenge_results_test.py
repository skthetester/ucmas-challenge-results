import requests
import re

response = requests.get("https://ucmaschallenge.com")
print(response)
print(response.text)
if re.search( 'congratulations', response.text, re.IGNORECASE) : 
    print("Results available now!")
else:
    assert(False)