#!/usr/bin/env python3.7



#handling the errors while chnaging the directory

# importing all necessary libraries
import sys, os

# initial directory
cwd = os.getcwd()

# some non existing directory
fd = 'false_dir / temp'

# trying to insert to flase directory
try:
	os.chdir(fd)
	print("Inserting inside-", os.getcwd())

# Caching the exception
except:
	print("Something wrong with specified\
		directory. Exception- ", sys.exc_info())

# handling with finally
finally:
	print("Restoring the path")
	os.chdir(cwd)
	print("Current directory is-", os.getcwd())

