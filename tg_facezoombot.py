from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, InlineQueryHandler
import sys, logging

from handlerFunctions import *

def runBot(botToken):
	print("running bot")

	updater = Updater(token=botToken)

	#/start, /help
	start_handler = CommandHandler(['start', 'help'], startDef)
	updater.dispatcher.add_handler(start_handler)

	#images
	image_handler = MessageHandler(Filters.photo, imageDef)
	updater.dispatcher.add_handler(image_handler)

	updater.start_polling()

if len(sys.argv) >= 2:
	#print exceptions
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
	runBot(sys.argv[1])
else:
	print("specify token pls")