from web_scraper.scraper import *

def test_get_citations_needed_count():
    url="https://en.wikipedia.org/wiki/History_of_Mexico"
    assert get_citations_needed_count(URL)==5

def test_type_get_citations_needed_report_citation():
    url="https://en.wikipedia.org/wiki/History_of_Mexico"
    assert type(get_citations_needed_report(URL))== type("<class 'str'>")


