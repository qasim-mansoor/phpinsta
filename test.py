import re

# The Instagram URL


# Define the regex pattern to extract the reel ID


def getid(url):
    reel_id = re.findall(r'/reel/([^/]+)', url)[0]
    print(reel_id)
# print("No match found.")

url = "https://www.instagram.com/reel/CwhD_tsyfnb/"
getid(url)
