from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text="""HEY HERE YOU CAN FIND THE BASIC COMMANDS OF MINE.IF YOU DON'T KNOW HOW TO USE COMMAND JOIN SUPPORT GROUP AND ASK.
<b><u>COMMANDS</u></b>
β send channel last message with
  forwerd tag to get the channel id π―
β /id - your tg id & info
β /telegraph - reply to below 5Mb media
  to get telegraph linkπ―
β /stickerid - Reply To Any Sticker to get sticker id
π€©THANKS FOR USING MEπ
""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("π€ ππ ππππ", callback_data="botz")
                  ],[
                  InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                  InlineKeyboardButton("π πππππ", callback_data="close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
ββββββ° πΌππ»ππΈ π±πΎπ β±ββ
ββ­ββββββββββββββββ£
ββ£βͺΌπ€α΄Κ Ι΄α΄α΄α΄ : {bot.mention}
ββ£βͺΌπ¦α΄α΄α΄  1 : <a href=https://t.me/JP_Jeol_org>α΄α΄α΄Κ</a>
ββ£βͺΌπ¨βπ»α΄α΄α΄  2 : <a href=https://t.me/mr_MKN>α΄Κ.α΄α΄Ι΄ α΄Ι’</a>
ββ£βͺΌβ£οΈsα΄α΄Κα΄α΄ α΄α΄α΄ : <a href=https://github.com/Jeolpaul/TG-MULTI-BOT>α΄Ι’-α΄α΄Κα΄Ιͺ-Κα΄α΄</a>
ββ£βͺΌπ‘Κα΄sα΄α΄α΄ α΄Ι΄ : <a href=https://dashboard.heroku.com>Κα΄Κα΄α΄α΄</a>
ββ£βͺΌπ£οΈΚα΄Ι΄Ι’α΄α΄Ι’α΄ : <a href=https://www.python.org>α΄Κα΄Κα΄Ι΄3</a>
ββ£βͺΌπΚΙͺΚΚα΄ΚΚ : <a href=https://github.com/pyrogram>α΄ΚΚα΄Ι’Κα΄α΄</a> 
ββ£βͺΌποΈα΄ α΄ΚsΙͺα΄Ι΄ : 1.0.3  
ββ°ββββββββββββββββ£
ββββββββββββββββββββ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                  InlineKeyboardButton("π πππππ", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}ππ»\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\nβ send channel last message with forwerd tag to get the channel id π―",          
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("β£οΈ πππππππ", url="https://t.me/BETA_BOTSUPPORT"),
                  InlineKeyboardButton("π’ πππππππ", url="https://t.me/BETA_UPDATES")
                  ],[            
                  InlineKeyboardButton("βΉοΈ ππππ", callback_data="help"),
                  InlineKeyboardButton("π πππ", callback_data="fun")
                  ],[
                  InlineKeyboardButton("π¨βπ» ππππ π¨βπ» ", callback_data="devs"),
                  InlineKeyboardButton("π€ πππππ", callback_data="about")
                  ]]
                  )
             )
   elif data == "devs":
         await msg.message.edit(
             text=f"This Bot will be made @JP_Jeol & @mr_MKN ",
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("π¨βπ» ππππ 1", url="https://t.me/JP_Jeol_org"),
                  InlineKeyboardButton("π¨βπ» ππππ 2", url="https://t.me/mr_MKN")
                  ],[
                  InlineKeyboardButton("β£οΈ ππππππ ππππ β£οΈ", url="https://github.com/Jeolpaul/TG-MULTI-BOT"),
                  ],[
                  InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                  InlineKeyboardButton("π πππππ", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=f"""<b><u>JUS TEST THIS COMMANDS π</u></b>
β /runs         
β /ikka      
β /dice     
β /arrow    
β /goal    
β /luck    
β /throw     
β /bowling  
β /tenpins    
""",      
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                 InlineKeyboardButton("π πππππ", callback_data="close")
                 ]]
                 )
             )
   elif data == "botz":
         await msg.message.edit(
             text="π€ This is My botz π",
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton("βΉοΈ πππππ πππ", url="https://t.me/GeorgeMalarobot"),
                     InlineKeyboardButton("π΅ πππππ πππ", url="https://t.me/Kochirajavu_musicbot")
                     ],[
                     InlineKeyboardButton("ποΈ πππππ πππππππ ποΈ", url="https://t.me/BETA_GROUPMANAGBOT")
                     ],[                   
                     InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                     InlineKeyboardButton("π πππππ", callback_data="close")
                     ]]
                     )
                 )
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass



@Client.on_callback_query(filters.regex('^nxt'))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [[
            InlineKeyboardButton('πΈβπ΅βπͺβπ¨βπ?βπ¦βπ±β', callback_data='style+special'),
            InlineKeyboardButton('ππππ°ππ΄π', callback_data='style+squares'),
            InlineKeyboardButton('ποΈποΈποΈπ°οΈποΈπ΄οΈποΈ', callback_data='style+squares_bold'),
            ],[
            InlineKeyboardButton('κͺκͺα¦κͺκͺΆκͺα₯΄π²κͺ', callback_data='style+andalucia'),
            InlineKeyboardButton('ηͺεε αε', callback_data='style+manga'),
            InlineKeyboardButton('SΜΎtΜΎiΜΎnΜΎkΜΎyΜΎ', callback_data='style+stinky'),
            ],[
            InlineKeyboardButton('BΝ¦Μ₯uΝ¦Μ₯bΝ¦Μ₯bΝ¦Μ₯lΝ¦Μ₯eΝ¦Μ₯sΝ¦Μ₯', callback_data='style+bubbles'),
            InlineKeyboardButton('UΝnΝdΝeΝrΝlΝiΝnΝeΝ', callback_data='style+underline'),
            InlineKeyboardButton('κκκ·κ©κκκ', callback_data='style+ladybug'),
            ],[
            InlineKeyboardButton('R?a?y?s?', callback_data='style+rays'),
            InlineKeyboardButton('B?i?r?d?s?', callback_data='style+birds'),
            InlineKeyboardButton('SΜΈlΜΈaΜΈsΜΈhΜΈ', callback_data='style+slash'),
            ],[
            InlineKeyboardButton('sβ tβ oβ pβ ', callback_data='style+stop'),
            InlineKeyboardButton('SΝΜΊkΝΜΊyΝΜΊlΝΜΊiΝΜΊnΝΜΊeΝΜΊ', callback_data='style+skyline'),
            InlineKeyboardButton('AΝrΝrΝoΝwΝsΝ', callback_data='style+arrows'),
            ],[
            InlineKeyboardButton('αͺαα­αΏα', callback_data='style+qvnes'),
            InlineKeyboardButton('SΜΆtΜΆrΜΆiΜΆkΜΆeΜΆ', callback_data='style+strike'),
            InlineKeyboardButton('FΰΌrΰΌoΰΌzΰΌeΰΌnΰΌ', callback_data='style+frozen')
            ],[
            InlineKeyboardButton('β¬οΈ Back', callback_data='nxt+0')
        ]]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)




@Client.on_callback_query(filters.regex('^style'))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')

    if style == 'typewriter':
        cls = Fonts.typewriter
    if style == 'outline':
        cls = Fonts.outline
    if style == 'serif':
        cls = Fonts.serief
    if style == 'bold_cool':
        cls = Fonts.bold_cool
    if style == 'cool':
        cls = Fonts.cool
    if style == 'small_cap':
        cls = Fonts.smallcap
    if style == 'script':
        cls = Fonts.script
    if style == 'script_bolt':
        cls = Fonts.bold_script
    if style == 'tiny':
        cls = Fonts.tiny
    if style == 'comic':
        cls = Fonts.comic
    if style == 'sans':
        cls = Fonts.san
    if style == 'slant_sans':
        cls = Fonts.slant_san
    if style == 'slant':
        cls = Fonts.slant
    if style == 'sim':
        cls = Fonts.sim
    if style == 'circles':
        cls = Fonts.circles
    if style == 'circle_dark':
        cls = Fonts.dark_circle
    if style == 'gothic':
        cls = Fonts.gothic
    if style == 'gothic_bolt':
        cls = Fonts.bold_gothic
    if style == 'cloud':
        cls = Fonts.cloud
    if style == 'happy':
        cls = Fonts.happy
    if style == 'sad':
        cls = Fonts.sad
    if style == 'special':
        cls = Fonts.special
    if style == 'squares':
        cls = Fonts.square
    if style == 'squares_bold':
        cls = Fonts.dark_square
    if style == 'andalucia':
        cls = Fonts.andalucia
    if style == 'manga':
        cls = Fonts.manga
    if style == 'stinky':
        cls = Fonts.stinky
    if style == 'bubbles':
        cls = Fonts.bubbles
    if style == 'underline':
        cls = Fonts.underline
    if style == 'ladybug':
        cls = Fonts.ladybug
    if style == 'rays':
        cls = Fonts.rays
    if style == 'birds':
        cls = Fonts.birds
    if style == 'slash':
        cls = Fonts.slash
    if style == 'stop':
        cls = Fonts.stop
    if style == 'skyline':
        cls = Fonts.skyline
    if style == 'arrows':
        cls = Fonts.arrows
    if style == 'qvnes':
        cls = Fonts.rvnes
    if style == 'strike':
        cls = Fonts.strike
    if style == 'frozen':
        cls = Fonts.frozen
    new_text = cls(m.message.reply_to_message.text)
    try:
        await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)
    except:
        pass


