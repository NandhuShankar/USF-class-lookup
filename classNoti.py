#Setup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
ROWNUM = "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > p:nth-child(10) > b:nth-child(1)"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://usfweb.usf.edu/DSS/StaffScheduleSearch")

#Select Semester
#semesterVal = str(input("Enter the Semester (input 202208 for fall 2022): "))
semester_dropdown = Select(driver.find_element(By.NAME, "P_SEMESTER"))
semester_dropdown.select_by_value("202208")

#Select course title
searchTitle = driver.find_element(By.ID, "P_REF")
searchTitle.send_keys("81151")

#Enters selection
driver.find_element(By.CLASS_NAME, "button").click()

#Wait for next page 
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.quit

#Get the number of classes
rowNum = driver.find_element(By.CSS_SELECTOR, ROWNUM)
rowNum = int(rowNum.text)
print(f"We found {rowNum} entries")

# Create an array of classes whos class is open
openClass = []

#Iterates through table, scraping info
for x in range(rowNum):
    #CRN Number
    crnNum = driver.find_element(By.CSS_SELECTOR, "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > p:nth-child(8) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child("+ str(x+2) + ") > td:nth-child(4)")
    crnNum = str(crnNum.text)

    #Subject Number
    subjNum = driver.find_element(By.CSS_SELECTOR, "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > p:nth-child(8) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(" + str(x+2)+ ") > td:nth-child(5) > a:nth-child(1)")
    subjNum = str(subjNum.text)

    #Class Number
    classNum = driver.find_element(By.CSS_SELECTOR, "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > p:nth-child(8) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(" + str(x+2) + ") > td:nth-child(6)")
    classNum = str(classNum.text)

    #Class Name
    className = driver.find_element(By.CSS_SELECTOR, "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > p:nth-child(8) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(" + str(x+2)+") > td:nth-child(8)")
    className = str(className.text)

    #Status
    classStatus = driver.find_element(By.CSS_SELECTOR, "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > p:nth-child(8) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child("+str(x+2)+") > td:nth-child(11)")
    classStatus = str(classStatus.text)

    #Time
    classTime = driver.find_element(By.CSS_SELECTOR, "body > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(1) > p:nth-child(8) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child("+str(x+2)+") > td:nth-child(18)")
    classTime = str(classTime.text)

    # creates an array with all of the row info
    row = [crnNum, subjNum, classNum, className, classStatus, classTime]

    #Prints the class lists
    print(row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5])

    # if the class is open, add it to the open class array
    if row[4] == "Open":
        openClass.append(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}")

# Check the open class array to see if any classes are open. Else, return no classes
if len(openClass) != 0:
    print(f"There are {len(openClass)} open classes")
    for x in openClass:
        print(x)
else:
    print("There are no open classes")

#Closes webpage
driver.close()
driver.quit()

