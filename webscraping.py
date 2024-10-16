from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import sys
import json

# Reconfigure sys.stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Set up Selenium and ChromeDriver
service = Service("C:/Users/Ayush Pratap Singh/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  # Path to your chromedriver

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Open the website
driver.get('https://questions.examside.com/past-years/medical/question/pa-bob-is-whirled-in-a-horizontal-circle-by-means-of-a-str-neet-physics-units-and-measurement-a1ywbaz1hp11jcmo')

# Wait for the page to load fully
time.sleep(3)

page_seen = 0
count = 0

# Initialize a list to store all questions
data = []

# Loop through the pages until the defined number of pages
total_pages_to_scrape = 5  # Define how many pages you want to scrape
for i in range(total_pages_to_scrape):
  
    # print(Fore.RED + Back.YELLOW + f"\n\n Scraping started on Page No {page_seen+1}\n" + Style.RESET_ALL)

    # Scraping questions and options for a single page
    for _ in range(0, 4):
        try:
            check_answer_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Check Answer Button']")  # Using aria-label to find the button
            check_answer_button.click()  # Click the Check Answer button
            time.sleep(3)  # Wait for the answer to load
        except Exception as e:
            print(f"Error clicking the Check Answer button: {e}")

    question_css_sel = [
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(3) > div.flex.flex-col.gap-2.max-md\:card.max-md\:pt-3 > div.question.xl\:text-lg.px-4.py-2\.5",
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(4) > div.flex.flex-col.gap-2.max-md\:card.max-md\:pt-3 > div.question.xl\:text-lg.px-4.py-2\.5",
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(6) > div.flex.flex-col.gap-2.max-md\:card.max-md\:pt-3 > div.question.xl\:text-lg.px-4.py-2\.5",
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(7) > div.flex.flex-col.gap-2.max-md\:card.max-md\:pt-3 > div.question.xl\:text-lg.px-4.py-2\.5"
        ]

    answer_css_sel = [
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(3) > div.flex.flex-col.gap-2.max-md\:card.max-md\:py-2 > div",
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(4) > div.flex.flex-col.gap-2.max-md\:card.max-md\:py-2 > div",
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(6) > div.flex.flex-col.gap-2.max-md\:card.max-md\:py-2 > div",
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(7) > div.flex.flex-col.gap-2.max-md\:card.max-md\:py-2 > div"
        ]

    options_css_sel = [
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(3) > div.options.md\:px-4.flex.flex-col.gap-2.lg\:gap-4",
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(4) > div.options.md\:px-4.flex.flex-col.gap-2.lg\:gap-4",
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(6) > div.options.md\:px-4.flex.flex-col.gap-2.lg\:gap-4",
            r"body > div:nth-child(1) > div.app > main > div > div > div.main-container.flex.flex-wrap.gap-2.lg\:gap-4 > div.flex-grow.flex.flex-col.gap-2.lg\:gap-4 > div:nth-child(7) > div.options.md\:px-4.flex.flex-col.gap-2.lg\:gap-4"
        ]

    for index in range(0, 4):
        question_data = {}
        question_data["question"] = None
        question_data["option 1"] = []
        question_data["option 2"] = []
        question_data["option 3"] = []
        question_data["option 4"] = []
        question_data["answer"] = None
        question_data["correct_option"] = None

        # Locate question
        try:
            question = driver.find_element(By.CSS_SELECTOR, question_css_sel[index])
            question_html = question.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
            if '<img>' in question_html:
                break
            question_data["question"] = question_html
        except Exception as e:
            print(f"Error locating question: {e}")
            break

        # Locate the options
        try:
            options_container = driver.find_element(By.CSS_SELECTOR, options_css_sel[index])
            options = options_container.find_elements(By.CSS_SELECTOR, "div.grow.question.xl\:text-lg")

            imgy = 0
            print(f"Found {len(options)} options for question {index + 1}")
            if len(options) == 4:
                for i, option in enumerate(options):
                    option_html = option.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
                    if '<img>' in option_html:
                        imgy = 1
                        break
                    question_data[f"option {i + 1}"] = option_html

                    # Get the CSS color value
                    color = option.value_of_css_property("color")
                    print(f"Option {i + 1} color: {color}")

                    # Compare the color to determine the correct option
                    if color == "rgba(34, 197, 94, 1)":  # This is the color for the correct option
                        question_data["correct_option"] = f"{i + 1}"
            else:
                print(f"Expected 4 options, but found {len(options)} for question {index + 1}")
        except Exception as e:
            print(f"Error locating options: {e}")

        if imgy == 1:
            break
        
        # Locate the answer and correct option
        try:
            answer = driver.find_element(By.CSS_SELECTOR, answer_css_sel[index])
            answer_html = answer.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
            if '<img>' in answer_html:
                break
            question_data["answer"] = answer_html
        except Exception as e:
            print(f"Error locating answer: {e}")

        # Append question data to the main list
        if question_data["answer"] is not None:
            data.append(question_data)
            count += 1

    # Click the NEXT button to go to the next page
    try:
        next_button = driver.find_element(By.LINK_TEXT, "NEXT")  # Use link text to find the NEXT button
        driver.execute_script("arguments[0].click();", next_button)  # Click the NEXT button to load the next set of questions
        time.sleep(3)  # Wait for the new questions to load
    except Exception as e:
        print("No more pages to navigate or error occurred:", e)
        break

    # Seen all questions on a single page
    page_seen += 1
    time.sleep(3)

# Close the browser once done
driver.quit()

# Write data to a JSON file with all double quotes replaced with single quotes and no newline characters
folder_path = './Data/NEET/Physics/3_Motion_in_a_Plane'  # Change this to your desired folder path

# Write data to a JSON file in the specified folder
json_file_path = folder_path + '.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Data has been successfully saved to questions_data.json.\nTotal questions saved = {count}\nPage seen = {page_seen}")

