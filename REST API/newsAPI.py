import requests
def NewsfromBBC():
    # bbc news api parameter
    query_params = {
        "sources": "bbc-news",
        "apikey": "4dbc17e007ab436fb66416009dfb59a8"

    }
    main_url = " https://newsapi.org/v2/top-headlines"
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    # getting all articles in a string article
    article = open_bbc_page["articles"]
    results = []
    for ar in article:
        results.append(ar["title"])
    return results
