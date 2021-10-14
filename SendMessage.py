from Functions import import_or_install
import_or_install('pandas')
import_or_install('selenium')
from Functions import write_to_csv
from Functions import level_of_interest
from Functions import calculate_corr_tags
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
import re


def matchfixing(openingszin, kwantiteit):
    # Driver path
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        executable_path=r'C:/Users/timva/.wdm/drivers/chromedriver/win32/90.0.4430.24/chromedriver.exe',
        chrome_options=options)
    target_url = 'https://www.theinnercircle.co/auth/linkedin-connect'
    exportFile = #Insert Export Directory
    num_rows = 0
    Reps = kwantiteit

    # Check amount of rows in csv for index
    for row in open(exportFile):
        num_rows += 1

    # ...........................................Going to the webz...........................
    # Select landing page
    driver.get(target_url)

    # Type email and password and login
    UserElement = driver.find_element_by_css_selector('#username')
    ActionChains(driver).move_to_element(UserElement).send_keys(
        '''Insert inlog Email''' ).perform()  # clicking not necessary
    time.sleep(random.uniform(1, 4))
    PassElement = driver.find_element_by_css_selector('#password')
    ActionChains(driver).move_to_element(PassElement).click().send_keys('''Insert Password''').perform()
    time.sleep(random.uniform(1, 4))
    driver.find_element_by_css_selector('#app__container > main > div.flavor > form > div.login__form_action_container.login__form_action_container--multiple-actions > button').click()

    # ..................Loop through profiles, check if known and send message...................................................
    # Open member list file and act depending on if member already exists
    with open(exportFile) as f:
        for i in range(Reps):
            # Find profile, send message and go back to home screen
            # ProfileButton
            driver.find_element_by_xpath('/html/body/div[1]/div[8]/div[3]/div[1]/div/div[1]/a[1]').click()
            time.sleep(4)
            # Profile Information
            Name = driver.find_element_by_css_selector('body > div.wrapper > div.container_16.container > div.grid_7.main > div.padding_top > div:nth-child(1) > a > span.username.name-big').text
            print(Name)
            Age = driver.find_element_by_css_selector('body > div.wrapper > div.container_16.container > div.grid_7.main > div.padding_top > div:nth-child(1) > a > span.age.name-big').text.replace(
                ', ', '').__str__()
            print(Age)
            Member = driver.current_url[-8:]
            print(Member)

            # Check if member already exists in Datafile
            if Member in f.read():
                print("Member known")
                # Click Like button
                driver.find_element_by_css_selector('body > div.wrapper > div.container_16.container > div.grid_7.main > div.match-buttons > div.match-button.desktop-like > a').click()
                time.sleep(random.uniform(1, 4))
                # Check if it's a match
                try:
                    time.sleep(random.uniform(1, 4))
                    # Try of we can click on continue button if we have a match. Else continue.
                    driver.find_element_by_css_selector(
                        'body > div.overlay > div > a.button.button-action.button-big.button-light.keep-looking').click()
                    print('Het is een match!')
                    time.sleep(random.uniform(1, 4))
                    # Go back to Home screen
                    driver.find_element_by_xpath('//*[@id="hamburger"]').click()
                    time.sleep(random.uniform(1, 4))
                    driver.find_element_by_xpath('/html/body/nav/ul/li[1]/a').click()
                    time.sleep(random.uniform(1, 4))
                except NoSuchElementException:
                    print('No Match, so continue!')
                    # Go back to Home screen
                    driver.find_element_by_xpath('//*[@id="hamburger"]').click()
                    time.sleep(random.uniform(1, 4))
                    driver.find_element_by_xpath('/html/body/nav/ul/li[1]/a').click()
                    time.sleep(random.uniform(1, 4))
                # Go back to Home screen
                driver.find_element_by_xpath('//*[@id="hamburger"]').click()
                time.sleep(random.uniform(1, 4))
                driver.find_element_by_xpath('/html/body/nav/ul/li[1]/a').click()
                time.sleep(random.uniform(1, 4))
            else:
                print("Member unknown")
                # Create list of tags on profile
                tagsListSelf = ['Cocktail Enthusiast', 'Omnivore', 'Home Cook', 'Night Owl', 'Board Gamer', 'Dance Machine', 'Tabloid Fan', 'Chart Lover', 'Artist', 'Footballer', 'Runner', 'Road Tripper', 'Ski Bum', 'Work hard & Play hard', 'Casual Dresser']
                print(tagsListSelf)
                tagsListOther = list(driver.find_elements_by_css_selector(
                    'body > div.wrapper > div.container_16.container > div.grid_10.main > div > div.widget.answers-widget > div > span'))
                print(tagsListOther)
                """
                # Calculate percentage corresponding tags
                c = calculate_corr_tags(listOther=tagsListOther, listSelf=tagsListSelf)
                print('Aantal corresponding tags = ' + c.__str__())
                print('Aantal tags op profiel = ' + len(tagsListOther).__str__())
                # Calculate percentage of corresponding tags
                percCorrTags = (c / len(tagsListOther)) * 100
                # Set decimals
                percCorrTags = "{:.3f}".format(percCorrTags) + '%'
                print(percCorrTags)
                """
                # click on MessageButton
                driver.find_element_by_xpath('/html/body/div[1]/div[8]/div[1]/div[4]/div[1]/a').click()
                time.sleep(random.uniform(1, 4))         
                # Text Message insert
                TextElement = driver.find_element_by_xpath('//*[@id="text"]')
                ActionChains(driver).move_to_element(TextElement).send_keys('Hi ' + Name + ', ' +
                    level_of_interest(level=openingszin)).perform()
                # clicking not necessary
                time.sleep(random.uniform(1, 4))
                # Text Message Send
                driver.find_element_by_xpath('//*[@id="submit"]').click()
                time.sleep(random.uniform(1, 4))
                # Close message screen
                driver.find_element_by_css_selector('body > div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-draggable.ui-resizable > div.ui-dialog-titlebar.ui-corner-all.ui-widget-header.ui-helper-clearfix.ui-draggable-handle > button > span.ui-button-icon.ui-icon.ui-icon-closethick').click()
                time.sleep(random.uniform(1, 4))
                # Click Like button
                driver.find_element_by_css_selector('body > div.wrapper > div.container_16.container > div.grid_7.main > div.match-buttons > div.match-button.desktop-like > a').click()
                time.sleep(random.uniform(1, 4))
                # Write data to csv
                write_to_csv(name=Name, age=Age, member=Member, sentence_id=openingszin, num_rows=num_rows)
                # Check if it's a match
                try:
                    time.sleep(random.uniform(1, 4))
                    # Try of we can click on continue button if we have a match. Else continue.
                    driver.find_element_by_css_selector(
                        'body > div.overlay > div > a.button.button-action.button-big.button-light.keep-looking').click()
                    print('Het is een match!')
                    time.sleep(random.uniform(1, 4))
                    # Go back to Home screen
                    driver.find_element_by_xpath('//*[@id="hamburger"]').click()
                    time.sleep(random.uniform(1, 4))
                    driver.find_element_by_xpath('/html/body/nav/ul/li[1]/a').click()
                    time.sleep(random.uniform(1, 4))
                except NoSuchElementException:
                    print('No Match, so continue!')
                    # Go back to Home screen
                    driver.find_element_by_xpath('//*[@id="hamburger"]').click()
                    time.sleep(random.uniform(1, 4))
                    driver.find_element_by_xpath('/html/body/nav/ul/li[1]/a').click()
                    time.sleep(random.uniform(1, 4))
    # Wait 10 seconds and close driver
    time.sleep(5)
    driver.close()
