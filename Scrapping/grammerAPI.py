import requests

def grammer_correction(text):
    url = "https://api.languagetool.org/v2/check"
    payload = {
        "text": text,
        "language": "en-US"
    }
    response = requests.post(url, data=payload)

    #check if request was successful
    if response.status_code == 200:
        result = response.json()
    # extract the matches (corrections/suggestions)
        matches = result.get("matches", [])

        if matches:
            print("Grammer issue found:")
            for match in matches:
                print(f"Issue: {match['message']}")
                print(f"Suggested Correction: {match['replacements']}")
                print(f"Context: {match['context']['text']}")
                print("_"*40)
        else:
            print("No grammer issue found")
    else:
        print(f"Error: {response.status_code}")

# Test the function
text = "I is a student"
grammer_correction(text)
    

   