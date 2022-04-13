import csv
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_needed_count(url):
    """
    count the number of "citation need" in the text 
    argument: takes in a url  
    returns: an integer
    """
    URL = str(url)
    res = requests.get(URL)
    src=res.content
    soup = BeautifulSoup(src, "html.parser")
    results_div = soup.find_all("a", {"href":"/wiki/Wikipedia:Citation_needed"})
    return len(results_div)

def get_citations_needed_report(url):
    """
    extract the pargraph that contain a "citation need"
    argument: takes in a url 
    returns: a string
    """
    URL = str(url)
    res = requests.get(URL)
    src=res.content
    soup = BeautifulSoup(src, "html.parser")
    results_div = soup.find_all("a", {"href":"/wiki/Wikipedia:Citation_needed"})
    citiation_report=""
    
    for el in soup.find_all("a", {"href":"/wiki/Wikipedia:Citation_needed"}):
        citiation_report=citiation_report+str(el.parent.parent.parent.text)+"\n"
    # print(citiation_report)
    return citiation_report

# with open('citiation_report.txt', 'w') as f:
#     content = get_citations_needed_report(URL)
#     f.write(content)

# print(get_citations_needed_report(URL))
# print(type(get_citations_needed_report(URL)))

# res = requests.get(URL)
# src=res.content
# soup = BeautifulSoup(src, "html.parser")
# # print(soup)
# results_div = soup.find_all("a", {"href":"/wiki/Wikipedia:Citation_needed"})
# # print(results_div)
# # results_p = soup.find_all("p")
# # soup.title.parent.name
# # print(soup.a.parent)
# # for el in soup.find_all("a", {"href":"/wiki/Wikipedia:Citation_needed"}):
# # print (str(el.parent.parent.parent.text))
# print(get_citations_needed_report(URL))