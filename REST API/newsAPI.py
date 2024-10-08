# importing requests package
import requests

def NewsFromBBC():

    query_params = {
    "source": "bbc-news",
    "sortBy": "top",
    "apiKey": "ef2a5e17463242299c5a9c33c7a5df2d"
    }
    main_url = " https://newsapi.org/v1/articles"
    
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    
    # getting all articles in a string article
    article = open_bbc_page["articles"]
    
    # empty list which will
    # contain all trending news
    results = []
    
    for ar in article:
        results.append(ar["title"])
    
    for i in range(len(results)):
    
    # printing all trending news
        print(i + 1, results[i])
    
    #to read the news out loud for us
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)

# Driver Code
if __name__ == '__main__':

# function call
    NewsFromBBC()