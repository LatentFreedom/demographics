################################################################################
# demographicExcel.py
################################################################################
# 	Author: Nick Palumbo
# 	* Date Created: November 12, 2016
# 	* Last Modified by: Nick Palumbo
# 	* Date Last Modified: November 12, 2016
################################################################################
#	What's in the file?
#	* Save and read data from excel
################################################################################
#	FUNCTIONS:
#	1. makeZipcodeArray(total_zipcodes)
#	2. updateDemographicForZipcode(demographic,y,n)
################################################################################

# import needed files
import getDemographic, demographicClass

# import needed libraries
import xlrd
from xlrd import open_workbook
import xlutils
from xlutils.copy import copy
import random

########################################
########## WORKBOOK           ##########
########################################

# create an workbook that will be used to read from
workbookRead = xlrd.open_workbook('demographic.xls')
worksheet_zipcode_read = workbookRead.sheet_by_name('zipcode')

# create a workbook that will be used to write to
workbook = open_workbook("demographic.xls")
workbookWrite = copy(workbook)
worksheet_zipcode_write = workbookWrite.get_sheet(0)

########################################
##########  GET               ##########
########################################
# 1. 
def makeZipcodeArray(total_zipcodes):
	zipcode_array = [demographicClass.Zipcode("NULL",0,0,0,0,0) for i in range(0,total_zipcodes)]
	i = 1
	for zipcode in zipcode_array:
		zipcode.zipcode = 	worksheet_zipcode_read.cell(i,0).value
		zipcode.y = i
		i += 1
	return zipcode_array

########################################
##########  UPDATE            ##########
########################################
# 2. 
def updateDemographicForZipcode(zipcode):
	worksheet_zipcode_write.write(zipcode.y,1,zipcode.white)
	worksheet_zipcode_write.write(zipcode.y,2,zipcode.black)
	worksheet_zipcode_write.write(zipcode.y,3,zipcode.asian)
	worksheet_zipcode_write.write(zipcode.y,4,zipcode.hispanic)
	workbookWrite.save('demographic.xls')
