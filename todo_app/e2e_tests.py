from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestTodoAppE2E:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
        cls.driver.get('http://127.0.0.1:8000/')

    def test_create_todo_item(self):
        """Simulate creating a new Todo item."""
        driver = self.driver
        # Simulate user input
        driver.find_element(By.NAME, 'title').send_keys("New Todo")
        driver.find_element(By.NAME, 'description').send_keys("E2E Testing")
        driver.find_element(By.NAME, 'due_date').send_keys("2024-12-31")
        driver.find_element(By.ID, 'submit-button').click()

        time.sleep(2)  # Wait for the page to refresh
        assert "New Todo" in driver.page_source

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
