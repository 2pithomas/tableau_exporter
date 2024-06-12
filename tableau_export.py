
import datetime
import os, sys
from datetime import date, datetime, timedelta
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

os.environ['SE_AVOID_STATS'] = 'True'
if os.environ.get('SE_AVOID_STATS') == 'True':
    print("SE_AVOID_STATS is set to True. Telemetry is disabled.")
else:
    print("Did not verify SE_AVOID_STATS is set to True. Telemetry is disabled.")

start = time.time()

# call the function at that bottom that will then take orgs as the input

# input your team/ org or applicable names into the empty list
teams = []
# Setting views of the dashboard for increased efficiency. The URL does not change and its one less function to program. 
views = []

# Creating a week number variable using datetime that can be used throughout the script. Simple but powerful logic. 
lastweek = datetime.now() - timedelta(7)
MSTATWK = lastweek.strftime("%W")
mw = str(MSTATWK)
print(mw)

# folder structure logic that adapts to the date parts we are working with. 
year = datetime.now().year
root = "C:\\Users\\"
yearstr = root + str(year)
wstr = yearstr + '\\' + 'Week' + mw
print(wstr)

# Checking to make sure the folder structure exists, if not then create it
try:
    os.mkdir(yearstr)
except FileExistsError:
    print(f"Folder '{yearstr}' already exists.")
try:
    os.mkdir(wstr)
except FileExistsError:
    print(f"Folder '{wstr}' already exists.")

### START OF WEBSCRAPING ###

def screenshot(orgs, views):

    for org, view in zip(orgs, views):
        # print(org, view)
        img = f"{org}.png"
        impath = wstr + '\\' + img
        print(impath)
        if os.path.exists(impath):
            print(f"screenshot already exists")
            continue

        try:
            options = webdriver.ChromeOptions()
            prefs = {'download.default_directory': wstr, "download.prompt_for_download": False, "download.directory_upgrade": True}
            options.add_experimental_option("detach", True)
            options.add_experimental_option('prefs', prefs)
            # I have found that headless does not work given the current state of tableau, chrome for testing in this specific case
            options.add_argument("--start-maximized")
            service = Service(r"C:\Workspace\chromedriver-win64\chromedriver-win64\chromedriver.exe")
            driver = webdriver.Chrome(service=service, options=options)
            driver.get(view)
            driver.implicitly_wait(20)

            ### This section will be commented out by default as it may only apply to some, and will cause errors for others. ###

            # auth = driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]")
            # driver.implicitly_wait(2)
            # # I have found that just passing in username for authentication works after manually signing in once
            # auth.send_keys("user.name@company.com")
            # nxt = driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input")
            # driver.implicitly_wait(2)
            # nxt.click()
            # driver.implicitly_wait(15)

            # This section is where we will actually identify the download button we need on the dashboard ###

            toolbar_iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
            # Switch to the toolbar iframe
            driver.switch_to.frame(toolbar_iframe)
            toolbar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "download")))
            toolbar.click()
            driver.implicitly_wait(5)

            imex = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[1]/div")
            driver.implicitly_wait(5)
            imex.click()
            time.sleep(10)

            # the default chromium download name tends to be summary, but we will rename that to our appropriate name. 
            download = wstr + '\\' + 'Summary.png'
            os.rename(download, impath)

            driver.quit()

        except Exception as e:
            print(f"Error exporting '{impath}' dashboard image:", str(e))

screenshot(teams, views)

end = time.time()
# print time is in seconds to show the amount of time elapsed while the script ran
print((str(end - start)[0:5]) + " Seconds Elapsed")
print('done')
