from selenium import webdriver
from pages.home_page import HomePage
from pages.book_page import BookPage
from pages.login_page import LoginPage


def test_login_add_book():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Navigate and login
    driver.get("https://demoqa.com/login")
    login_page = LoginPage(driver)
    login_page.login("your_username", "your_password")

    # Go to Book Store
    home = HomePage(driver)
    home.visit("https://demoqa.com/books")
    home.search_book("Git Pocket Guide")
    home.select_book()

    book_page = BookPage(driver)
    book_page.add_book()

    driver.quit()
