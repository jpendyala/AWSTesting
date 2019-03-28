import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.csv'

# downloading with urllib

# import the urllib package
import urllib

# Copy a network object to a local file
urllib.urlretrieve(url, "tutorial.csv")

# downloading with requests

# # import the requests library
# import requests
#
# # download the file contents in binary format
# r = requests.get(url)
#
# # open method to open a file on your system and write the contents
# with open("tutorial1.json", "wb") as code:
#     code.write(r.content)