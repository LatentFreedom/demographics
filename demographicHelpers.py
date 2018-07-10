################################################################################
# demographicHelpers.py
################################################################################
# 	Author: Nick Palumbo
# 	* Date Created: October 10, 2016
# 	* Last Modified by: Nick Palumbo
# 	* Date Last Modified: November 10, 2016
################################################################################
#	What's in the file?
#	* Get and put data with selenium driver
#	* Input handling
################################################################################
#	FUNCTIONS:
#	1. startDriver()
#	2. putZipcode(driver,zipcode)
#	3. parseDemographicString(demographic_string,zipcode)
#	4. getZipcodeDemographics(driver,zipcode_array)
#	5. waitForInt(tz, s)
#	6. getTotalZipcode()
################################################################################

# import needed files
import getDemographic, demographicClass, demographicExcel

# import needed libraries
from selenium import webdriver # provides all the WebDriver implementations
from selenium.webdriver.common.keys import Keys # provide keys from the keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1.
def startDriver():
    return webdriver.Firefox()

# 2. 
def putZipcode(driver,zipcode):
	try:
		zipcode = str(zipcode).split('.')[0]
		driver.get('http://www.wolframalpha.com/input/?i=zip+code+'+zipcode)
		return 1 # success
	except:
		return 0 # failure

# 3. 
def parseDemographicString(demographic_string,zipcode):
	rows = demographic_string.split('\n')
	for row in rows:
		if ":" in row:
			cut = row.split("|")
			for c in cut:
				if "white" in c or "White" in c:
					zipcode.white = c.split(":")[1].strip()
				if "black" in c or "Black" in c:
					zipcode.black = c.split(":")[1].strip()
				if "asian" in c or "Asian" in c:
					zipcode.asian = c.split(":")[1].strip()
				if "hispanic" in c or "Hispanic" in c:
					zipcode.hispanic = c.split(":")[1].strip()
		else:
			if "white" in row or "White" in row:
				zipcode.white = row.split("|")[1].strip()
				if zipcode.white == "":
					zipcode.white = row.split("|")[2].split("%")[0] + "%"
			if "black" in row or "Black" in row:
				zipcode.black = row.split("|")[1].strip()
				if zipcode.black == "":
					zipcode.black = row.split("|")[2].split("%")[0] + "%"
			if "asian" in row or "Asian" in row:
				zipcode.asian = row.split("|")[1].strip()
				if zipcode.asian == "":
					zipcode.asian = row.split("|")[2].split("%")[0] + "%"
			if "hispanic" in row or "Hispanic" in row:
				zipcode.hispanic = row.split("|")[1].strip()
				if zipcode.hispanic == "":
					zipcode.hispanic = row.split("|")[2].split("%")[0] + "%"
	return zipcode

# 4.
def getDemographic(driver,zipcode):
	try:
		wait = WebDriverWait(driver, 20)
		element = wait.until(EC.element_to_be_clickable((By.ID,'ACSPercentageEntrainments:ACSData')))
		element = element.find_element_by_tag_name('section')
		button = element.find_element_by_tag_name('a')
		button.click()
		demographic_string = element.find_element_by_tag_name('img').get_attribute('alt')
		try:
			while "More" in button.get_attribute('innerHTML'):
				time.sleep(1)
		except:
			element = driver.find_element_by_id('ACSPercentageEntrainments:ACSData')
			element = element.find_element_by_tag_name('section')
			demographic_string = element.find_element_by_tag_name('img').get_attribute('alt')
			zipcode = parseDemographicString(demographic_string,zipcode)
			return zipcode
	except:
		return zipcode

# 4. 
def getZipcodeDemographics(driver,zipcode_array):
	for zipcode in zipcode_array:
			success = putZipcode(driver,zipcode.zipcode)
			if success:
				zipcode = getDemographic(driver,zipcode)
				message = "Zipcode: {0:10} | white: {1:6} | black: {2:6} | asian: {3:6} | hispanic: {4:6}".format(zipcode.zipcode,zipcode.white,zipcode.black,zipcode.asian,zipcode.hispanic)
				print(message)
				demographicExcel.updateDemographicForZipcode(zipcode)
			else:
				message = "Zipcode: {0:10} | white: {1:6} | black: {2:6} | asian: {3:6} | hispanic: {4:6}".format(zipcode.zipcode,"NULL","NULL","NULL","NULL")
				print(message)

# 5. 
def waitForInt(tz, s):
	while True:
		try:
			tz = int(tz)
			return tz
		except:
			print(s + " must be an integer.")
			tz = raw_input(s + ": ")

# 6.
def getTotalZipcode():
	tz = raw_input("Total Zipcodes: ")
	tz = waitForInt(tz, "Total Zipcodes")
	return tz
