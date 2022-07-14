from django.core.management.base import BaseCommand
from telegram.ext import CommandHandler, Updater, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler
from ...views import start, davomat, inline_query, catch_task , my_location

TOKEN = "5540639592:AAFUrt2YwC8WSTcfRovFEU4zPj1Ubm0Rmrs"


class Command(BaseCommand):

    def handle(self, *args, **options):
        updater = Updater(TOKEN)

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                1: [MessageHandler(Filters.regex("Davomat"), davomat),
                    MessageHandler(Filters.regex("ortga qaytish"), davomat),
                    MessageHandler(Filters.regex("TASDIQLAYMAN"), davomat)],
                2: [CallbackQueryHandler(inline_query), CommandHandler('start', start),
                    MessageHandler(Filters.text, catch_task),
                    MessageHandler(Filters.location, my_location)],


            },
            fallbacks=[]
        )

        updater.dispatcher.add_handler(conv_handler)
        updater.start_polling()
        updater.idle()
