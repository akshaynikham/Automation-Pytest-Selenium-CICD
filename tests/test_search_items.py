from pages.search import search_items

def test_search_items(initialize_driver):
    search_items(initialize_driver)