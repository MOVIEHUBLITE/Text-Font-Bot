from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from variables import STAT_STICK, PICS, ADMIN, DELAY
import asyncio
import random


WAIT_MSG = """"<b>Processing ...</b>"""



@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    insert(int(message.chat.id))
    await message.reply_chat_action("Typing")
    await asyncio.sleep(DELAY)
    m=await message.reply_sticker(STAT_STICK)
    await asyncio.sleep(DELAY)
    await m.delete()             
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}šš»\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\nā send channel last message with forwerd tag to get the channel id šÆ",               
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ā£ļø ššššššš", url="https://t.me/BETA_BOTSUPPORT"),
            InlineKeyboardButton("š¢ ššššššš", url="https://t.me/BETA_UPDATES")
            ],[            
            InlineKeyboardButton("ā¹ļø šššš", callback_data="help"),
            InlineKeyboardButton("š ššš", callback_data="fun")
            ],[
            InlineKeyboardButton("šØāš» šššš šØāš» ", callback_data="devs"),
            InlineKeyboardButton("š¤ ššššš", callback_data="about")
            ]]
            )
        )
         
@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(client: Client, message: Message):    
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")





@Client.on_message(filters.private & filters.incoming & filters.text)
async def style_buttons(c, m, cb=False):
    buttons = [[
        InlineKeyboardButton('šš¢ššš ššššš', callback_data='style+typewriter'),
        InlineKeyboardButton('šš¦š„šššš', callback_data='style+outline'),
        InlineKeyboardButton('ššš«š¢š', callback_data='style+serif'),
        ],[
        InlineKeyboardButton('šŗšššš', callback_data='style+bold_cool'),
        InlineKeyboardButton('ššššš', callback_data='style+cool'),
        InlineKeyboardButton('Sį“į“ŹŹ Cį“į“s', callback_data='style+small_cap'),
        ],[
        InlineKeyboardButton('ššøšš¾šš', callback_data='style+script'),
        InlineKeyboardButton('š¼š¬š»š²š¹š½', callback_data='style+script_bolt'),
        InlineKeyboardButton('įµā±āæŹø', callback_data='style+tiny'),
        ],[
        InlineKeyboardButton('įOį°Iį', callback_data='style+comic'),
        InlineKeyboardButton('š¦š®š»š', callback_data='style+sans'),
        InlineKeyboardButton('ššš£šØ', callback_data='style+slant_sans'),
        ],[
        InlineKeyboardButton('šš¢šÆš“', callback_data='style+slant'),
        InlineKeyboardButton('š²šŗšš', callback_data='style+sim'),
         InlineKeyboardButton('āøļøā¾ļøāļøāøļøāļøāŗļøāļø', callback_data='style+circles'),
        ],[
        InlineKeyboardButton('šļøšļøš”ļøšļøšļøšļøš¢ļø', callback_data='style+circle_dark'),
        InlineKeyboardButton('šš¬š±š„š¦š ', callback_data='style+gothic'),
        InlineKeyboardButton('š²ššššš', callback_data='style+gothic_bolt'),
        ],[
        InlineKeyboardButton('CĶ”ĶlĶ”ĶoĶ”ĶuĶ”ĶdĶ”ĶsĶ”Ķ', callback_data='style+cloud'),
        InlineKeyboardButton('HĢĢaĢĢpĢĢpĢĢyĢĢ', callback_data='style+happy'),
        InlineKeyboardButton('SĢĢaĢĢdĢĢ', callback_data='style+sad'),
        ],[
        InlineKeyboardButton('Next ā”ļø', callback_data="nxt")
    ]]
    if not cb:
        await m.reply_text(m.text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))

