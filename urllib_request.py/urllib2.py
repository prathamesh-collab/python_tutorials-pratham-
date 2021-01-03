#!/usr/bin/env python3


#import urllib.request module
import urllib.request


#create a variable and stored my username and password in that 
username_password = {'username':'prathamesh sawant','password':'000pratu00'}


#use urllib.parse.urlencode and call our storable username and password 
#use .encode  and 'utf-8' 
encoded = urllib.parse.urlencode(username_password).encode('utf-8')


#create response variable and use urlopen method to acces our url
response = urllib.request.urlopen('http://gymbuddy.ga/wp-admin', encoded)

print(response)

print(response.code)




