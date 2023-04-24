
TOKEN = '5996822625:AAFdfL3lK79gTZ2ckxQ5Uq9ym1KBlbRM35M'
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
bot = Bot(TOKEN)
dp = Dispatcher(bot)
ikb = InlineKeyboardMarkup(row_width=2)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b = KeyboardButton(text="/start")
kb.add(b)
async def on_startup(_):
    print('I have been started up')


s_MESSAGE = """
Выбери команду снизу 
👇🏻
<b>/start</b> - <em>список команд</em>
<b>/description</b> - <em>описание бота</em>
<b>/pick</b> - <em>выбор группы мышц</em>
<b>/help</b> - <em>подробное описание количетва повторений для каждого упражнения</em>
<b>/programm</b> - <em>программа тренировок для набора мышечной массы</em>
<b>/programm_detail</b> - <em>подробное описание любого дня тренировки</em>
"""

h_MESSAGE = """
Количество повторений упражнения в зале для набора мышечной массы зависит от нескольких факторов, таких как индивидуальные особенности организма, уровень физической подготовленности, цели тренировок и тип упражнения.

Общепринятой рекомендацией является выполнение 8-12 повторений в каждом подходе на большинстве упражнений для набора мышечной массы. Это количество повторений обеспечивает оптимальную стимуляцию мышечных волокон, способствует росту мышечной массы и силы.

Однако, если целью тренировок является увеличение выносливости мышц, то количество повторений может быть увеличено до 15-20 в каждом подходе.

Важно также учитывать, что для достижения максимального эффекта необходимо изменять количество повторений и веса в зависимости от уровня подготовленности и прогресса в тренировках.
"""

p_MESSAGE = """
3-дневная программа тренировок для набора мышечной массы


График тренировок:
Понедельник - грудь и трицепс
Вторник - отдых
Среда - спина и бицепс
Четверг - отдых
Пятница - ноги и плечи

/programm_detail - подробное описание каждого дня
"""
album_chest = types.MediaGroup()
album_chest.attach_photo(photo="https://webpulse.imgsmail.ru/imgpreview?mb=webpulse&key=pulse_cabinet-image-d0c6c861-d4f9-4a15-96e4-8da4649bb234")
album_chest.attach_photo(photo="https://webpulse.imgsmail.ru/imgpreview?mb=webpulse&key=pulse_cabinet-image-5bee0d78-1acc-4bd8-ba53-3dcaf1f6d430")
album_chest.attach_photo(photo="https://avatars.dzeninfra.ru/get-zen_doc/3446134/pub_5edf169db7b200124a0db2a8_5edf2498dc508b6b094a198c/scale_1200")

album_triceps = types.MediaGroup()
album_triceps.attach_photo(photo="https://www.inspireusafoundation.org/wp-content/uploads/2021/08/cable-push-down-768x590.png")
album_triceps.attach_photo(photo="https://www.inspireusafoundation.org/wp-content/uploads/2021/08/close-grip-bench-press-768x367.png")
album_triceps.attach_photo(photo="https://mia-bags.ru/wp-content/uploads/2/e/1/2e136af36ca55150c5babd42be02b937.jpeg")

album_back = types.MediaGroup()
album_back.attach_photo(photo="https://www.inspireusafoundation.org/wp-content/uploads/2022/11/pull-up-variations.jpg")
album_back.attach_photo(photo="https://webpulse.imgsmail.ru/imgpreview?mb=webpulse&key=pulse_cabinet-image-9d62563e-f37e-454c-96b2-5e3bf68d0a3d")
album_back.attach_photo(photo="https://www.mybodycreator.com/content/files/exercises/47.png")

album_biceps = types.MediaGroup()
album_biceps.attach_photo(photo="https://cross.expert/wp-content/uploads/2018/03/uprazhneniya-na-bitseps-podem-shtangi.jpeg")
album_biceps.attach_photo(photo="https://sv-sport.ru/wp-content/uploads/2/c/6/2c6a5303c5e1beb72b09d10dbdba6f41.jpeg")
album_biceps.attach_photo(photo="https://www.mentoday.ru/upload/img_cache/801/801d84eed539ffa9d3fe426201f08d62_cropped_666x500.jpg")

album_quadriceps = types.MediaGroup()
album_quadriceps.attach_photo(photo="https://www.inspireusafoundation.org/wp-content/uploads/2022/05/high-bar-squat-768x447.png")
album_quadriceps.attach_photo(photo="https://cdn.shopify.com/s/files/1/1876/4703/files/shutterstock_421042393_480x480.jpg?v=1644566569")
album_quadriceps.attach_photo(photo="https://avatars.dzeninfra.ru/get-zen_doc/1931664/pub_5d86351e2beb4900aec636c2_5d86377da06eaf00ad1d6bf2/scale_1200")

album_calves = types.MediaGroup()
album_calves.attach_photo(photo="https://images.squarespace-cdn.com/content/v1/5ffcea9416aee143500ea103/1638439412667-VVRLZIFSASOD7Q6TJNE7/7.%2BShouldered%2BSmith%2BMachine%2BStanding%2BCalf%2BRaises.png")
album_calves.attach_photo(photo="https://static.strengthlevel.com/images/illustrations/seated-calf-raise-1000x1000.jpg")

album_shoulders = types.MediaGroup()
album_shoulders.attach_photo(photo="https://generationiron.com/wp-content/uploads/2022/02/Screen-Shot-2022-03-09-at-6.51.14-PM.png")
album_shoulders.attach_photo(photo="https://s3.amazonaws.com/prod.skimble/assets/2416111/image_iphone.jpg")
album_shoulders.attach_photo(photo="https://www.inspireusafoundation.org/wp-content/uploads/2022/03/upright-row-768x578.png")

album_press = types.MediaGroup()
album_press.attach_photo(photo="https://ss.sport-express.ru/userfiles/materials/172/1727559/volga.jpg")
album_press.attach_photo(photo="https://qph.cf2.quoracdn.net/main-qimg-9f3b3d829223aefa978477541418d474-lq")

album_forearms = types.MediaGroup()
album_forearms.attach_photo(photo="https://www.inspireusafoundation.org/wp-content/uploads/2021/11/dumbbell-reverse-wrist-curl-benefits.jpg")
album_forearms.attach_photo(photo="https://mobilephysiotherapyclinic.in/wp-content/uploads/2022/02/813393198sst1644214778-1.jpg")

album_traps = types.MediaGroup()
album_traps.attach_photo(photo="https://www.mybodycreator.com/content/files/2020/05/10/446_M.png")
album_traps.attach_photo(photo="https://www.burnthefatinnercircle.com/members/images/1893b.jpg")
album_traps.attach_photo(photo="https://www.inspireusafoundation.org/wp-content/uploads/2022/03/upright-row-768x578.png")

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                         text=s_MESSAGE,
                         reply_markup=kb,
                         parse_mode="html")
    await message.delete()
@dp.message_handler(commands=['pick'])
async def pick_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='Верх',
                               callback_data="up")
    ib2 = InlineKeyboardButton(text='Низ',
                               callback_data="down")
    ikb.add(ib1, ib2)

    await bot.send_message(chat_id=message.from_user.id,
                           text='Выбери что ты будешь качать🏋🏻‍♂️',
                           reply_markup=ikb)
@dp.message_handler(commands=['programm'])
async def programm_command(message: types.Message):
    await message.answer(text=p_MESSAGE,)
    await message.delete()
@dp.message_handler(commands=['programm_detail'])
async def programm_detail_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=3)
    ib1 = InlineKeyboardButton(text='Понедельник',
                               callback_data="monday")
    ib2 = InlineKeyboardButton(text='Среда',
                               callback_data="wednesday")
    ib3 = InlineKeyboardButton(text='Пятница',
                               callback_data="friday")
    ikb.add(ib1, ib2, ib3)

    await bot.send_message(chat_id=message.from_user.id,
                           text='Выбери день',
                           reply_markup=ikb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=h_MESSAGE, parse_mode="html")
    await message.delete()
@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text=f'Привет!\nЭтот бот создан для прокачки определенной группы мышц!\nРад видеть тебя {message.from_user.full_name}!\n\nТелеграм-бот для тренировок в спортзале помогает пользователям быстро и удобно найти информацию о том, как правильно качать определенную группу мышц. Бот предоставляет подробные инструкции и рекомендации по выбору упражнений, количеству повторений и весу, необходимым для достижения желаемого результата.\n\nПользователи могут выбрать группу мышц, которую они хотели бы развить, например, грудные мышцы, бицепсы или квадрицепсы.')
    await message.delete()


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'monday':
        ikb = InlineKeyboardMarkup(row_width=2)
        ib2_1 = InlineKeyboardButton(text='Грудь',
                                     callback_data="chest_programm")
        ib2_2 = InlineKeyboardButton(text='Трицепс',
                                     callback_data="triceps_programm")

        ikb.add(ib2_1, ib2_2)
        await callback.message.answer(text='Выбери группу мышц',
                                      reply_markup=ikb)

    if callback.data == 'wednesday':
        ikb = InlineKeyboardMarkup(row_width=2)
        ib2_1 = InlineKeyboardButton(text='Спина',
                                     callback_data="back_programm")
        ib2_2 = InlineKeyboardButton(text='Бицепс',
                                     callback_data="biceps_programm")

        ikb.add(ib2_1, ib2_2)
        await callback.message.answer(text='Выбери группу мышц',
                                      reply_markup=ikb)

    if callback.data == 'friday':
        ikb = InlineKeyboardMarkup(row_width=3)
        ib2_1 = InlineKeyboardButton(text='Квадрицепсы',
                                     callback_data="quad_programm")
        ib2_2 = InlineKeyboardButton(text='Икры',
                                     callback_data="calves_programm")
        ib2_3 = InlineKeyboardButton(text='Плечи',
                                     callback_data="shoulders_programm")
        ikb.add(ib2_1, ib2_2, ib2_3)
        await callback.message.answer(text='Выбери группу мышц',
                                      reply_markup=ikb)


    if callback.data == 'chest_programm':
        await callback.message.answer_media_group(album_chest)
        ikb = InlineKeyboardMarkup(row_width=2)
        ib2_1 = InlineKeyboardButton(text='Грудь',
                                     callback_data="chest_programm")
        ib2_2 = InlineKeyboardButton(text='Трицепс',
                                     callback_data="triceps_programm")

        ikb.add(ib2_1, ib2_2)
        await callback.message.answer(text='Выбери группу мышц',
                                      reply_markup=ikb)
    if callback.data == 'triceps_programm':
        await callback.message.answer_media_group(album_triceps)

    if callback.data == 'back_programm':
        await callback.message.answer_media_group(album_back)
        ikb = InlineKeyboardMarkup(row_width=2)
        ib2_1 = InlineKeyboardButton(text='Спина',
                                     callback_data="back_programm")
        ib2_2 = InlineKeyboardButton(text='Бицепс',
                                     callback_data="biceps_programm")
        ikb.add(ib2_1, ib2_2)
        await callback.message.answer(text='Выбери группу мышц',
                                      reply_markup=ikb)
    if callback.data == 'biceps_programm':
        await callback.message.answer_media_group(album_biceps)

    if callback.data == 'quad_programm':
        await callback.message.answer_media_group(album_quadriceps)
        ikb = InlineKeyboardMarkup(row_width=2)
        ib2_1 = InlineKeyboardButton(text='Квадрицепсы',
                                     callback_data="quad_programm")
        ib2_2 = InlineKeyboardButton(text='Икры',
                                     callback_data="calves_programm")
        ib2_3 = InlineKeyboardButton(text='Плечи',
                                     callback_data="shoulders_programm")
        ikb.add(ib2_1, ib2_2)
        await callback.message.answer(text='Выбери группу мышц',
                                      reply_markup=ikb)

    if callback.data == 'calves_programm':
        await callback.message.answer_media_group(album_calves)
        ikb = InlineKeyboardMarkup(row_width=2)
        ib2_1 = InlineKeyboardButton(text='Квадрицепсы',
                                     callback_data="quad_programm")
        ib2_2 = InlineKeyboardButton(text='Икры',
                                     callback_data="calves_programm")
        ib2_3 = InlineKeyboardButton(text='Плечи',
                                     callback_data="shoulders_programm")
        ikb.add(ib2_1, ib2_2)
        await callback.message.answer(text='Выбери группу мышц',
                                      reply_markup=ikb)

    if callback.data == 'shoulders_programm':
        await callback.message.answer_media_group(album_shoulders)

    if callback.data == 'up':
        kb = InlineKeyboardMarkup(row_width=3)
        ib1_1 = InlineKeyboardButton(text='Бицепс',
                                   callback_data="biceps")
        ib1_2 = InlineKeyboardButton(text='Грудь',
                                   callback_data="chest")
        ib1_3 = InlineKeyboardButton(text='Пресс',
                                     callback_data="press")
        ib1_4 = InlineKeyboardButton(text='Предплечья',
                                     callback_data="forearms")
        ib1_5 = InlineKeyboardButton(text='Плечи',
                                     callback_data="shoulders")
        ib1_6 = InlineKeyboardButton(text='Трапеции',
                                     callback_data="traps")
        ib1_7 = InlineKeyboardButton(text='Спина',
                                     callback_data="back")
        ib1_8 = InlineKeyboardButton(text='Трицепс',
                                     callback_data="triceps")
        kb.add(ib1_1, ib1_2, ib1_3, ib1_4, ib1_5, ib1_6, ib1_7, ib1_8)
        await callback.message.answer(text='Выбери группу мышц, которую ты хочешь прокачать💪',
                                      reply_markup=kb)

    if callback.data == 'down':
        kb = InlineKeyboardMarkup(row_width=2)
        ib2_1 = InlineKeyboardButton(text='Икры',
                                     callback_data="calves")
        ib2_2 = InlineKeyboardButton(text='Квадрицепсы',
                                     callback_data="quadriceps")
        kb.add(ib2_1, ib2_2)
        await callback.message.answer(text='Выбери группу мышц, которую ты хочешь прокачать💪',
                                      reply_markup=kb)

    if callback.data == 'biceps':
        await callback.message.answer_media_group(album_biceps)
        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать🏋🏻‍♂️',
                               reply_markup=ikb)
    if callback.data == 'triceps':
        await callback.message.answer_media_group(album_triceps)
        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать🏋🏻‍♂️',
                                      reply_markup=ikb)
    if callback.data == 'chest':
        await callback.message.answer_media_group(album_chest)
        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать🏋🏻‍♂️',
                                      reply_markup=ikb)
    if callback.data == 'press':
        await callback.message.answer_media_group(album_press)

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать🏋🏻‍♂️',
                                      reply_markup=ikb)
    if callback.data == 'forearms':
        await callback.message.answer_media_group(album_forearms)

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать🏋🏻‍♂️',
                                      reply_markup=ikb)
    if callback.data == 'shoulders':
        await callback.message.answer_media_group(album_shoulders)

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать🏋🏻‍♂️',
                                      reply_markup=ikb)
    if callback.data == 'traps':
        await callback.message.answer_media_group(album_traps)

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать🏋🏻‍♂️',
                                      reply_markup=ikb)
    if callback.data == 'back':
        await callback.message.answer_media_group(album_back)

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать🏋🏻‍♂️',
                                      reply_markup=ikb)
    if callback.data == 'calves':
        await callback.message.answer_media_group(album_calves)

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать🏋🏻‍♂️',
                                      reply_markup=ikb)
    if callback.data == 'quadriceps':
        await callback.message.answer_media_group(album_quadriceps)

        ikb = InlineKeyboardMarkup(row_width=2)
        ib1 = InlineKeyboardButton(text='Верх',
                                   callback_data="up")
        ib2 = InlineKeyboardButton(text='Низ',
                                   callback_data="down")
        ikb.add(ib1, ib2)
        await callback.message.answer(text='Выбери что ты будешь качать🏋🏻‍♂️',
                                      reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
