from loggers.default_logger import Logger

logger = Logger.get_logger("test_case6")

# import requests

url = 'https://www.timeanddate.com/holidays/canada/'  # replace with your desired URL
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Print the raw HTML content of the page
#     print(response.text)
# else:
#     print(f"Failed to retrieve content. Status code: {response.status_code}")


import urllib.request

#url = 'https://example.com'  # replace with your desired URL

try:
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(html.decode('utf-8'))  # print HTML content (decoded as UTF-8)
except Exception as e:
    print(f"Failed to retrieve content. Error: {e}")
