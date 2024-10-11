# import pytest
# from pages.base_page import homepage
#
# from pages.search import search_Select
# from pages.search import search_only
#
# def test_search_click_items(initialize_driver):
#     search = search_Select(initialize_driver)
#     mobile_results = search.search_items("vivo")
#     # assert len(mobile_results) > 0, "results not found"
#
# @pytest.mark.search
# @pytest.mark.parametrize("name",["vivo", "oppo", "redmi", "samsung", "iphone"])
# def test_search_items(initialize_driver,name):
#     homepage(initialize_driver)
#     search = search_only(initialize_driver)
#     results = search.search_items({name})
