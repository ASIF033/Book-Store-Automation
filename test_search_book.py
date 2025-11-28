from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.book_page import BookPage


def test_search_git_pocket_guide():
    driver = webdriver.Chrome()
    driver.maximize_window()

    home = HomePage(driver)
    home.visit("https://demoqa.com/books")

    # Search book
    home.search_book("Git Pocket Guide")
    wait = WebDriverWait(driver, 10)
    book_element = wait.until(EC.visibility_of_element_located(HomePage.BOOK_TITLE_LINK))

    # Validate search result
    book_link_text = driver.find_element(*HomePage.BOOK_TITLE_LINK).text
    assert "Git Pocket Guide" in book_link_text

    # Click book and verify details
    home.select_book()
    book_page = BookPage(driver)
    assert "Git Pocket Guide" in book_page.get_book_title()
    assert "Richard E. Silverman" in book_page.get_book_author()

    driver.quit()
