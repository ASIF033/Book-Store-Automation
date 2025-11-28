from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BookPage(BasePage):
    TITLE = (By.ID, "title-wrapper")
    AUTHOR = (By.ID, "author-wrapper")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add To Your Collection']")

    def get_book_title(self):
        return self.get_text(self.TITLE)

    def get_book_author(self):
        return self.get_text(self.AUTHOR)

    def add_book(self):
        self.click(self.ADD_BUTTON)
