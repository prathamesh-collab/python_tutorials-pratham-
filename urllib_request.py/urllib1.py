#!/usr/bin/env python3

#import urllib.request module
import urllib.request


#create a response module 
#use urllib.request.urlopen method to ping our url
response = urllib.request.urlopen("http://gymbuddy.ga")

#print our url 
print(response)

#print code 
print(response.code)

#this is list of hypertext transfer protocol(HTTP) response status code . status codes are issued by a server in response to a clients request made to the serverv


#all http request code are clasified into 5 types


#1xx (Informational) : The request was received, continuing process
#2xx (Successful)    : The request was successfully received, understood and accepted
#3xx (Redirection)   : Further action needs to be taken in order to complete the request
#4xx (Client Error)  : The request contains bad syntax or cannot be fulfilled
#5xx (Server Error)  : The server failed to fulfill an apparently valid request

#detail imfo in this link https://en.wikipedia.org/wiki/List_of_HTTP_status_codes 

