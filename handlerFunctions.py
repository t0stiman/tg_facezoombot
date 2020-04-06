import os
from random import randint
from telegram import InlineQueryResultArticle, InputTextMessageContent

from faceZoom import doFaceZoom
from generalFunctions import deleteFile

#==============================================================================

#/start, /help
def startDef(bot, update):
	replyText = "Hi, I'm FaceZoomBot! Send me an image with a face in it, and I will zoom in on it."
	bot.send_message(chat_id=update.message.chat_id, text=replyText)

#images
def imageDef(bot, update):
	print('received image')

	#download and save image on disk
	photoID = update.message.photo[-1].file_id
	thePhoto = bot.get_file(photoID)

	readyToSave = False
	while not readyToSave:
		localFilename = str(randint(0, 100000000))
		#check if file exists
		readyToSave = not os.path.isfile(localFilename)
	localFilename += '.jpg'

	thePhoto.download(localFilename)
	print('saved image as: '+localFilename)

	success = doFaceZoom(localFilename)
	if success:
		#send zoomed image
		bot.send_photo(chat_id=update.message.chat_id, photo=open(localFilename, 'rb'))
		print('sent image')

	print('deleting image')
	deleteFile(localFilename)

	#print empty line
	print()