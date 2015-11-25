#!/usr/bin/env python2.7
__author__ = 'marcsantiago'
try:
	from easygui import enterbox, msgbox
except ImportError:
	print("Program requires that the easygui module be installed")
	print("To install the easygui module on unix or linux")
	print("type [pip install easygui] terminal")
	print("If you have windows and are using active state python pip will work as well, if not\
	you can get the package here http://easygui.sourceforge.net")

from sys import exit
import urllib

zipcode = enterbox("Please enter 5 digit zip code")

if len(zipcode) < 5 or zipcode.isdigit() == False or len(zipcode) > 5:
	msgbox("Invalid zipcode! Zipcode you have entered is less than 5 digits, greater than5, or you have entered a non number. Exiting program...", title="Error")
	exit(1)

url = "http://www.wunderground.com/cgi-bin/findweather/hdfForecast?query={}".format(zipcode)
weather_page = urllib.urlopen(url)
html_content = weather_page.read()

condition = html_content[html_content.find("now:"):html_content.find("temp_now:")]
temp = html_content[html_content.find("temp_now:"):html_content.find("high_now:")]
location = html_content[html_content.find("loc:"):html_content.find("content_template:")]


condition = condition.replace("now: ", "").replace("'", "").replace(",","")
temp = temp.replace("temp_now: ", "").replace("'", "").replace(",","").replace(" &deg;F", "")
location = location.replace("loc: ", "").replace("'", "").replace(",","")

msgbox(msg="Location = %s \n Current Weather Condition = %s \n Currrent Temperature = %sF \n" % (location, condition, temp), title="Weather Report")
