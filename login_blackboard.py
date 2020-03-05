from selenium import webdriver
from time import sleep
import sys
import values


def main(user, pwd, course, page_name):
    url = "https://elearning.uminho.pt"

    # --- open firefox on url
    driver = webdriver.Firefox()
    driver.get(url)

    # --- verify if title has "Blackboard"
    assert "Blackboard Learn" in driver.title

    sleep(values.LOADING_TIME)
    # --- fill username
    username = driver.find_element_by_id("user_id")
    username.clear()
    username.send_keys(user)
    # --- fill password
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys(pwd)

    # --- press login button
    driver.find_element_by_id("entry-login").click()
    sleep(values.LOADING_TIME)

    # --- access course page
    driver.find_element_by_partial_link_text(course).click()
    sleep(values.LOADING_TIME)

    # --- open documents
    driver.find_element_by_partial_link_text(page_name).click()



def get_course():

    # --- loop through all courses added
    for i in range(0, len(values.UC_SHORT)):
        if sys.argv[1] == values.UC_SHORT[i]:
            # --- return values associated with the chosen course
            return values.UC_FULL_NAME[i], values.UC_PAGE[i]


if len(sys.argv) > 2:
    print("Too many values")

else:
    course, page_name = get_course()
    main(values.USERNAME, values.PASSWORD, course, page_name)
