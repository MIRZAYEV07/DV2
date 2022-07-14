from telegram import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from .models import KelganTime,KetganVaqt
from geopy.geocoders import Nominatim
from .services import get_kelgan_time
from .googlesheets import make_sheet

geolocator = Nominatim(user_agent="example app")



def geo(l,m):

    return geolocator.reverse(f'{l}, {m}').raw



def start(update ,context):
    global user
    global user_id
    user = update.message.from_user.first_name
    user_id = update.message.from_user.id

    update.message.reply_text(f"SALOM {user} and {update.message.from_user.id}")
    buttons = [

        [KeyboardButton("Davomat"), KeyboardButton("Info")],

    ]
    update.message.reply_text(f"SALOM {user}",reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True))
    return 1

def davomat(update ,context):


    btn = [
            [InlineKeyboardButton("Keldim",callback_data="keldim"),InlineKeyboardButton("Bugunki vazifalarim",callback_data="vazifalar")],
            [InlineKeyboardButton("Joylashuv", callback_data="joylashuv"),InlineKeyboardButton("ketdim", callback_data="ketdim")]
           ]

    update.message.reply_text(f" davomat menu !",reply_markup=InlineKeyboardMarkup(btn))

    return 2

def vazifalar(update,context):
    update.message.reply_text(f" BUGUNKI VAZIFALAR: ")



def catch_task(update,context):
    global task
    task = update.message.text
    print(task)
    buttons = [

        [KeyboardButton("ortga qaytish")],

    ]
    update.message.reply_text("ortga qayting !",reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))

    return 1

def joylashuv(update,context):
    buttons = [
        [KeyboardButton("MENING JOYLASHUVIM", request_location=True)],

    ]

    update.message.reply_text(
        f" {user} , goelakatsiya jo'nating !",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, ))



def my_location(update , context):
    global joylashuv
    location = update.message.location

    joylashuv = geo(location.latitude,location.longitude)["display_name"]
    print(joylashuv)
    buttons = [
        [KeyboardButton("TASDIQLAYMAN")],

    ]

    update.message.reply_text(f"  {joylashuv} ",
                              reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, ))

    return 1


def inline_query(update,context):

    print(update)
    query = update.callback_query
    data = query.data
    if data == 'keldim':
        kelgan_vaqt = KelganTime()
        kelgan_vaqt.user = user
        kelgan_vaqt.save()
        query.message.delete()
        print(get_kelgan_time(user))
        davomat(query, context)
    elif data == 'ketdim':
        ketgan_vaqt = KetganVaqt()
        ketgan_vaqt.user = user
        ketgan_vaqt.save()
        query.message.delete()
        # make_sheet(user_id,user,ketgan_vaqti,kelgan_vaqti,sana,task,joylashuv)
        davomat(query, context)

    elif data == 'vazifalar':
        query.message.delete()
        vazifalar(query, context)

    elif data == 'joylashuv':
        query.message.delete()
        joylashuv(query, context)


# Create your views here.
