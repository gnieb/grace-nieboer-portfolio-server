from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrapeOddball():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Define the URL
    url= "https://oddball.io/jobs/"

    # load the web page
    driver.get(url)

    # set maximum time to load the web page in seconds
    driver.implicitly_wait(10)

    jobs = driver.find_elements(By.CLASS_NAME, 'job')

    open_roles = []

    for job in jobs:
        job_link = job.find_element(By.TAG_NAME, 'a').get_attribute('href')
        job_title = job.find_element(By.CSS_SELECTOR, 'span.title').text
        new_job = {
            'link': job_link,
            'title':job_title
        }
        open_roles.append(new_job)
    return open_roles


