import requests
from bs4 import BeautifulSoup


# def search_bing(query, num_results=3):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/B04BFF"
#     }

#     response = requests.get(
#         f"https://www.bing.com/search?q={query}", headers=headers)
#     soup = BeautifulSoup(response.content, "html.parser")
#     results = soup.find_all("li", class_="b_algo")[:num_results]

#     summaries = []
#     for result in results:
#         summary = result.find("p").get_text()
#         summaries.append(summary)

#     return summaries

def search_bing(query, num_results=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/B04BFF"
    }

    response = requests.get(
        f"https://www.bing.com/search?q={query}", headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("li", class_="b_algo")[:num_results]

    summaries = []
    for result in results:
        summary = result.find("p").get_text()
        if len(summary) < 30:
            url = result.find("a")["href"]
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.find("p").get_text()
            summary = " ".join(text.split())
        summaries.append(summary)

    return summaries
