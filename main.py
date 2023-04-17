import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

rangee = int(input("How many accounts to create?"))

for i in range(rangee):
    # open the browser
    driver = webdriver.Chrome()

    # go to the page
    driver.get("https://guarda.com/app/create?redirectUri=%2Fapp%2F")

    # find the password field and enter the password
    password_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_input.send_keys("130106066vb")

    # Find the password confirmation field and enter the password
    confirm_password_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Confirm password']"))
    )
    confirm_password_input.send_keys("password")

    # find the "I've written it down" button and click on it
    written_password_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "writtenPasswordDown"))
    )
    written_password_button.click()

    # find the "Download Backup" button and click on it
    download_backup_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "creationDownloadBackup"))
    )
    download_backup_button.click()

    time.sleep(3)

    downloads_dir = os.path.expanduser('~/Downloads')
    # get a list of all files in the download directory
    all_files = os.listdir(downloads_dir)
    # We get a list of all files with the extension .txt
    txt_files = [f for f in all_files if f.endswith('.txt')]
    # Sort the list of files by date of change
    sorted_files = sorted(txt_files, key=lambda x: os.path.getmtime(os.path.join(downloads_dir, x)), reverse=True)

    last_file = sorted_files[0]
    file_path = os.path.join(downloads_dir, last_file)
    with open(file_path) as f:
        file_content = f.read()


    with open("wallets.txt", 'a') as cont:
        cont.write(f"{file_content}\n\n\n")

    # close the browser
    driver.quit()

