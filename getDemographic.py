################################################################################
# getDemographic.py
################################################################################
# 	Author: Nick Palumbo
# 	* Date Created: November 12, 2016
# 	* Last Modified by: Nick Palumbo
# 	* Date Last Modified: November 12, 2016
################################################################################
#
# 	Scrape demographic information from wolfram alpha.
# 	* Given a zipcode, the site will return the given demographics.
# 	* This script allows an excel sheet to be used to import information.
# 	* Imort addresses and given radius.
# 	* Wrtie to the excel sheet the given demographics given inputs.
#
# 	Website: http://www.wolframalpha.com
#
################################################################################

# import needed files
import demographicExcel, demographicHelpers

# import needed libraries
from selenium import webdriver # provides all the WebDriver implementations
from selenium.webdriver.common.keys import Keys # provide keys from the keyboard
import time

def main():
	total_zipcodes = demographicHelpers.getTotalZipcode()
	zipcode_array = demographicExcel.makeZipcodeArray(total_zipcodes)
	driver = demographicHelpers.startDriver() # start the driver to be used
	demographicHelpers.getZipcodeDemographics(driver,zipcode_array)
	driver.quit()

if __name__ == "__main__":
	main()