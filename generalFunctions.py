import os

#delete image from disk
def deleteFile(fileName):
	try:
		os.remove(fileName)
	except FileNotFoundError:
		print('deleting image failed!')