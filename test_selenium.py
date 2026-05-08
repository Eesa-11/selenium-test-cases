import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os

class TestWebApplication(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up Chrome driver with headless mode"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.base_url = os.getenv('APP_URL', 'http://localhost:5000')
        cls.driver.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls):
        """Close browser after all tests"""
        cls.driver.quit()
    
    # Test Case 1: Verify home page loads
    def test_01_home_page_loads(self):
        """Test if home page loads successfully"""
        self.driver.get(self.base_url)
        self.assertIn("Home - Test Application", self.driver.title)
        print("✓ Test 1 Passed: Home page loads")
    
    # Test Case 2: Verify welcome message
    def test_02_welcome_message_present(self):
        """Test if welcome message is displayed"""
        self.driver.get(self.base_url)
        welcome = self.driver.find_element(By.ID, "welcome-message")
        self.assertEqual(welcome.text, "Welcome to Test Application")
        print("✓ Test 2 Passed: Welcome message displayed")
    
    # Test Case 3: Verify navigation menu
    def test_03_navigation_menu_exists(self):
        """Test if navigation menu is present"""
        self.driver.get(self.base_url)
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, ".nav a")
        self.assertGreaterEqual(len(nav_links), 5)
        print("✓ Test 3 Passed: Navigation menu exists")
    
    # Test Case 4: Navigate to Users page
    def test_04_navigate_to_users_page(self):
        """Test navigation to users page"""
        self.driver.get(self.base_url)
        users_link = self.driver.find_element(By.LINK_TEXT, "Users")
        users_link.click()
        time.sleep(1)
        self.assertIn("Users List", self.driver.page_source)
        print("✓ Test 4 Passed: Navigate to users page")
    
    # Test Case 5: Navigate to Add User page
    def test_05_navigate_to_add_user_page(self):
        """Test navigation to add user page"""
        self.driver.get(self.base_url)
        add_user_link = self.driver.find_element(By.LINK_TEXT, "Add User")
        add_user_link.click()
        time.sleep(1)
        self.assertIn("Add New User", self.driver.page_source)
        print("✓ Test 5 Passed: Navigate to add user page")
    
    # Test Case 6: Add a new user
    def test_06_add_new_user(self):
        """Test adding a new user"""
        self.driver.get(f"{self.base_url}/add_user")
        
        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        age_input = self.driver.find_element(By.ID, "age")
        submit_btn = self.driver.find_element(By.ID, "submit-btn")
        
        name_input.send_keys("John Doe")
        email_input.send_keys("john@example.com")
        age_input.send_keys("25")
        submit_btn.click()
        
        time.sleep(2)
        self.assertIn("John Doe", self.driver.page_source)
        print("✓ Test 6 Passed: User added successfully")
    
    # Test Case 7: Verify user in users list
    def test_07_verify_user_in_list(self):
        """Test if added user appears in users list"""
        self.driver.get(f"{self.base_url}/users")
        time.sleep(1)
        users = self.driver.find_elements(By.CLASS_NAME, "user-name")
        user_names = [user.text for user in users]
        self.assertIn("John Doe", user_names)
        print("✓ Test 7 Passed: User appears in list")
    
    # Test Case 8: Navigate to Products page
    def test_08_navigate_to_products_page(self):
        """Test navigation to products page"""
        self.driver.get(self.base_url)
        products_link = self.driver.find_element(By.LINK_TEXT, "Products")
        products_link.click()
        time.sleep(1)
        self.assertIn("Products List", self.driver.page_source)
        print("✓ Test 8 Passed: Navigate to products page")
    
    # Test Case 9: Navigate to Add Product page
    def test_09_navigate_to_add_product_page(self):
        """Test navigation to add product page"""
        self.driver.get(self.base_url)
        add_product_link = self.driver.find_element(By.LINK_TEXT, "Add Product")
        add_product_link.click()
        time.sleep(1)
        self.assertIn("Add New Product", self.driver.page_source)
        print("✓ Test 9 Passed: Navigate to add product page")
    
    # Test Case 10: Add a new product
    def test_10_add_new_product(self):
        """Test adding a new product"""
        self.driver.get(f"{self.base_url}/add_product")
        
        name_input = self.driver.find_element(By.ID, "product-name")
        price_input = self.driver.find_element(By.ID, "product-price")
        quantity_input = self.driver.find_element(By.ID, "product-quantity")
        submit_btn = self.driver.find_element(By.ID, "submit-product-btn")
        
        name_input.send_keys("Laptop")
        price_input.send_keys("999.99")
        quantity_input.send_keys("10")
        submit_btn.click()
        
        time.sleep(2)
        self.assertIn("Laptop", self.driver.page_source)
        print("✓ Test 10 Passed: Product added successfully")
    
    # Test Case 11: Verify product in products list
    def test_11_verify_product_in_list(self):
        """Test if added product appears in products list"""
        self.driver.get(f"{self.base_url}/products")
        time.sleep(1)
        products = self.driver.find_elements(By.CLASS_NAME, "product-name")
        product_names = [product.text for product in products]
        self.assertIn("Laptop", product_names)
        print("✓ Test 11 Passed: Product appears in list")
    
    # Test Case 12: Navigate to Search page
    def test_12_navigate_to_search_page(self):
        """Test navigation to search user page"""
        self.driver.get(self.base_url)
        search_link = self.driver.find_element(By.LINK_TEXT, "Search User")
        search_link.click()
        time.sleep(1)
        self.assertIn("Search User", self.driver.page_source)
        print("✓ Test 12 Passed: Navigate to search page")
    
    # Test Case 13: Search for existing user
    def test_13_search_existing_user(self):
        """Test searching for an existing user"""
        self.driver.get(f"{self.base_url}/search_user")
        
        search_input = self.driver.find_element(By.ID, "search-input")
        search_btn = self.driver.find_element(By.ID, "search-btn")
        
        search_input.send_keys("John")
        search_btn.click()
        
        time.sleep(2)
        self.assertIn("Search Results", self.driver.page_source)
        print("✓ Test 13 Passed: Search functionality works")
    
    # Test Case 14: Verify search results
    def test_14_verify_search_results(self):
        """Test if search returns correct results"""
        self.driver.get(f"{self.base_url}/search_user")
        
        search_input = self.driver.find_element(By.ID, "search-input")
        search_btn = self.driver.find_element(By.ID, "search-btn")
        
        search_input.send_keys("John")
        search_btn.click()
        
        time.sleep(2)
        results = self.driver.find_elements(By.CLASS_NAME, "result-row")
        self.assertGreater(len(results), 0)
        print("✓ Test 14 Passed: Search results displayed")
    
    # Test Case 15: Verify users table structure
    def test_15_verify_users_table_structure(self):
        """Test if users table has correct structure"""
        self.driver.get(f"{self.base_url}/users")
        time.sleep(1)
        
        table = self.driver.find_element(By.ID, "users-table")
        headers = table.find_elements(By.TAG_NAME, "th")
        header_texts = [header.text for header in headers]
        
        expected_headers = ["ID", "Name", "Email", "Age", "Action"]
        self.assertEqual(header_texts, expected_headers)
        print("✓ Test 15 Passed: Users table structure correct")
    
    # Test Case 16: Verify products table structure
    def test_16_verify_products_table_structure(self):
        """Test if products table has correct structure"""
        self.driver.get(f"{self.base_url}/products")
        time.sleep(1)
        
        table = self.driver.find_element(By.ID, "products-table")
        headers = table.find_elements(By.TAG_NAME, "th")
        header_texts = [header.text for header in headers]
        
        expected_headers = ["ID", "Name", "Price", "Quantity"]
        self.assertEqual(header_texts, expected_headers)
        print("✓ Test 16 Passed: Products table structure correct")

if __name__ == '__main__':
    unittest.main(verbosity=2)