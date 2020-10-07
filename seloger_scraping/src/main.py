"""Main module : project launcher"""

try:
    from SearchSeLoger import SearchSeLoger
except Exception as e:
    from seloger_scraping.src.SearchSeLoger import SearchSeLoger


if __name__ == "__main__":
    searchSeLoger = SearchSeLoger(False)
    searchSeLoger.fill_field_city('Paris')
    searchSeLoger.uncheck_field_house()
