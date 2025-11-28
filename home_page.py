from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "searchBox")
    BOOK_TITLE_LINK = (By.XPATH, "//a[text()='Git Pocket Guide']")

    def search_book(self, book_name):
        self.type_text(self.SEARCH_BOX, book_name)

    def select_book(self):
        self.click(self.BOOK_TITLE_LINK)
