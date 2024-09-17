import requests
# send get request to the jsonplaceholder API
response = requests.get('https://jsonplaceholder.typicode.com/posts')
# check the status code

print(response.status_code)

# parse the response content as json
data = response.json()

# print the first 5 posts
for post in data[:5]:
    print(post)

    