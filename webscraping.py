from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Reconfigure sys.stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Set up Selenium and ChromeDriver
service = Service('C:/Users/Ayush Pratap Singh/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')  # Path to your chromedriver

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Open the website
driver.get('https://questions.examside.com/past-years/medical/question/pin-an-electrical-circuit-the-voltage-is-measured-as-v-neet-physics-units-and-measurement-wcruwr8r9njsklel')

# Wait for the page to load fully
time.sleep(3)

# Loop through the pages until there are no more questions
while True:
    # Locate the question
    try:
        question = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\\:gap-4 > div:nth-child(3) > div.flex.flex-col.gap-2.max-md\\:card.max-md\\:pt-3 > div.question.xl\\:text-lg.px-4.py-2\\.5 > p")
        print(f"Question: {question.text}")
    except Exception as e:
        print(f"Error locating question: {e}")
        break

    # Locate the options
    try:
        options = driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\\:gap-4 > div:nth-child(3) > div.options.md\\:px-4.flex.flex-col.gap-2.lg\\:gap-4 > div > div.grow.question.xl\\:text-lg")
        for i, option in enumerate(options):
            print(f"Option {i + 1}: {option.text}")
    except Exception as e:
        print(f"Error locating options: {e}")

    # # Click the first option (or adjust to your logic)
    # if options:
    #     options[0].click()  # Click the first option for demonstration
    #     time.sleep(1)  # Wait briefly before clicking the check answer button

    # Locate and click the 'Check Answer' button
    try:
        check_answer_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Check Answer Button']")  # Using aria-label to find the button
        check_answer_button.click()  # Click the Check Answer button
        time.sleep(4)  # Wait for the answer to load
    except Exception as e:
        print(f"Error clicking the Check Answer button: {e}")

    # Locate the answer
    try:
        answer = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(6) > div.options.md\:px-4.flex.flex-col.gap-2.lg\:gap-4 > div.flex.items-center.gap-2.max-md\:card.md\:rounded.px-4.py-4.dark\:border-gray-500.md\:border-2.cursor-pointer.select-none.transition-all.relative.bg-opacity-20.border-2.\!border-green-500.text-green-500.bg-green-600 > div.shrink-0.flex.items-center.justify-center.text-white.text-sm.rounded-\[50\%\].w-\[25px\].h-\[25px\].bg-blue-600.bg-green-600")
        print(f"Answer: {answer.text}")
    except Exception as e:
        print(f"Error locating answer: {e}")

    # Check if the "NEXT" button is available
    try:
        next_button = driver.find_element(By.LINK_TEXT, 'NEXT')  # Use link text to find the NEXT button
        next_button.click()  # Click the NEXT button to load the next set of questions
        time.sleep(3)  # Wait for the new questions to load
    except Exception as e:
        print("No more pages to navigate or error occurred:", e)
        break

# Close the browser once done
driver.quit()