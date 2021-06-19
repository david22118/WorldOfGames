from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path="c:/chromedriver.exe", options=chrome_options)

score_game_url = 'http://127.0.0.1:8777/get_score'
error_message = "Error 404"
success_message = "The score is"


def test_scores_service(url):
    browser.get(url)

    score = browser.find_element_by_id("score")
    score_description = score.get_attribute('innerText')

    if score_description in error_message:
        if score_description == "404":
            return False
    elif 1 < int(score_description) < 1000:
        return True

    browser.close()


def main_function(url):
    status = test_scores_service(url)
    if status:
        return 0
    else:
        return -1


main_function(score_game_url)
