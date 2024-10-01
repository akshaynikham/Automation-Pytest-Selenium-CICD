from pages.search import flipkartSearch

def test_search_items(initialize_driver):
    search = flipkartSearch(initialize_driver)
    mobile_results = search.search_items("vivo")
    assert len(mobile_results) > 0, "results not found"

