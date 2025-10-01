import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    raise RuntimeError("API_TOKEN не задан. Создайте файл .env с API_TOKEN=ваш_токен")

# Все уроки в одном массиве
LESSONS = [
    {
        "title": "Урок 1: Искусственный интеллект",
        "text": """<b>Искусственный интеллект (ИИ)</b> — это область
компьютерных наук, где создаются системы, способные
выполнять задачи, требующие мышления: распознавать
образы, понимать язык, принимать решения и творить.

🧠 <b>Как это работает?</b>
В основе ИИ лежат алгоритмы, которые учатся на
больших массивах данных. Например:

нейросети анализируют миллионы изображений и распознают лица и предметы;

языковые модели «читают» тексты и отвечают на вопросы;

системы прогнозирования видят прошлые данные и делают предсказания.

🔎 Где мы встречаем ИИ:
— рекомендации фильмов и музыки,
— карты с пробками,
— голосовые помощники,
— переводчики десятков языков.

Но главное – ИИ незаменим в <b>работе и творчестве.</b> С его помощью можно за минуты:
📸 создать фото,
✍️ написать текст,
🎨 придумать идеи,
📊 анализировать данные и принимать решения.

<b>Почему важно освоить ИИ?</b>
Потому что он уже часть жизни и профессий. Те, кто умеют использовать его, экономят время, работают продуктивнее и быстрее растут в карьере или бизнесе.""",
        "file": "leson1/Frame 139.png",
        "video": None,
        "type": "photo"
    },
    {
        "title": "Урок 2: DeepSeek",
        "text": """📘<b> Урок 2.</b> 
Сегодня познакомимся с бесплатным сервисом DeepSeek - это 
площадка, где можно тренироваться в работе с нейросетями:
 — разберём, что там можно делать,
 — посмотрим, какие инструменты есть внутри,
 — научимся находить нужные функции и быстро применять их на практике.
<b>DeepSeek</b> - отличный способ начать уверенно использовать ИИ и почувствовать, что у тебя под рукой целая лаборатория для экспериментов ✨
""",
        "file": "leson 2/Frame 140.png",
        "video": "leson 2/output_iphone.mp4",
        "type": "photo"
    },
    {
        "title": "Урок 3. Практическая работа с нейрофотосессиями",
        "text": """<b>Урок 3. Практическая работа с нейрофотосессиями</b>

Теория без практики - это просто информация.
Поэтому в следующих уроках мы переходим <b>к созданию реального контента</b> 🎯

Для практической части понадобится доступ к <b>LIME AI - боту</b>, который мы будем изучать. 

<b>Здесь ты сможешь:</b>
— создавать фотореалистичные изображения со своим лицом
— работать с готовыми стилями и создавать собственные
— генерировать контент по текстовым запросам
— применять техники из курса на практике

<b>Важный момент:</b> чтобы полноценно пройти практическую часть и закрепить материал, потребуется тестовый доступ к боту <b><a href="https://t.me/Lime_AI_bot?start=lessons">@Lime_AI_bot</a></b>
<b>Для участников курса мы подготовили специальные условия:</b>
✅ Тестовый доступ за 329₽ 
✅ 15 генераций в базовом пакете
✅ Дополнительно 30 генераций по промокоду <b>LIME30</b> - только для участников обучения

Этого хватит, чтобы пройти все практические задания курса и понять, подходит ли тебе этот инструмент для дальнейшей работы.

<b>Скорее приступай к знакомству с нейросетью</b> 📸""",
        "file": "leson 3/Frame 142.png",
        "video": "leson 3/IMG_7586.mp4",
        "type": "photo"
    },
    {
        "title": "Урок 4. Создание аватара в LIME AI",
        "text": """📘 <b>Урок 4. Создание аватара в LIME AI</b>
В этом уроке мы  разберёмся, как правильно работать с аватарами 💚
✨ В этом уроке ты узнаешь:
 — как создать свой первый аватар,
 — где и как можно докупать дополнительные аватары,
 — какие фото подходят для аватара,
 — какие фото использовать нельзя 
Аватар - это основа твоих нейрофотосессий, поэтому важно сделать его правильно 🌿""",
        "file": "leson 4/Frame 143.png",
        "video": "leson 4/video-output-D99B3CC5-727B-46B3-9424-A058EC8AACE1-1.mp4",
        "type": "photo"
    },
    {
        "title": "Урок 5.1. Создание аватара в LIME AI",
        "text": """📘 <b>Урок 5. Часть 1. Режим Творца</b>
В этом уроке познакомимся с режимом <b>Творца.</b>
 Ты узнаешь, как работать с промтами - короткими 
текстовыми описаниями, по которым нейросеть создаёт 
изображения.
Это первый шаг к тому, чтобы полностью управлять 
результатом и воплощать свои идеи в визуалы ✨""",
        "file": "leson 5.1/Frame 144.png",
        "video": "leson 5.1/IMG_7534.mp4",
        "type": "photo"
    },
    {
        "title": "Урок 5.2. Создание аватара в LIME AI",
        "text": """📘 <b>Урок 5. Часть 2.</b> 
В этой части урока мы разберёмся подробнее с промтами:
 — как правильно формулировать запросы для нейросети,
 — какие ошибки чаще всего делают новички,
 — как написать промт для LIME AI в DeepSeek,
Это основа работы с нейросетями: чем лучше ты 
владеешь промтами, тем круче получаются результаты ✨
<b>Для урока тебе понадобится промт для DeepSeek:</b>
Составь промт для генерации fashion-фотографии 
{укажите ваш пол и тематику}.  
⚠️ Не указывай пол, волосы, лицо и фигуру.  
Используй только слово «Модель».  
Укажи: 
— кадрирование и позу, 
— одежду и аксессуары, 
— макияж (только макияж, без описания лица), 
— фон и атмосферу, 
— финальный стиль.  
Формат: связный текст, начинающийся словами 
«На изображении — Модель …».
""",
        "file": "leson 5.2/Frame 145.png",
        "video": "leson 5.2/video-output-83886686-CD70-47FC-8BC0-87739B4A930D-2.mp4",
        "type": "photo"
    },
    {
        "title": "Урок 6. Создание аватара в LIME AI",
        "text": """📘 <b>Урок 6. Создание нейрофотосессии в LIME AI с помощью 
DeepSeek</b>
В этом уроке мы разберём, как создавать полноценную 
нейрофотосессию - серию снимков в едином стиле.
 Ты узнаешь:
 - как получить серию кадров, похожих на настоящую фотосессию 📸

✨ <b>Промт, который пригодится для урока:</b>

Сгенерируй 4 уникальных промта для нейрофотосессии в стиле 
[ВСТАВЬ СТИЛЬ, напр. "на яхте"].
 Важно: все 4 промпта должны содержать одинаковый стиль одежды 
и аксессуаров, одинаковую общую атмосферу и визуальный стиль, 
чтобы фотографии выглядели как серия снимков одной фотосессии.
В каждом промпте можно менять:
- Позу модели
- Ракурс и композицию (очень крупный план, крупный план и 
средний план)
- Динамику, движение ткани и взаимодействие с окружением
- Освещение и настроение
Фокусируйся на:
- Профессиональном художественном стиле
- Сохранении единого визуального языка во всей серии
В качестве обозначения человека пиши «модель».
 Пиши промты на русском языке.
""",
        "file": "leson 6/Frame 146.png",
        "video": "leson 6/video-output-574D80C7-22F8-4931-8EBC-3A73F574AE03-3.mp4",
        "type": "photo"
    },
    {
        "title": "Урок 7. Создание аватара в LIME AI",
        "text": """📘<b> Урок 7. Оживление фотографий</b>
Сегодня познакомимся с функцией <b>оживления фото</b> ✨
 Мы покажем, как из одного изображения можно создать 
короткое видео, и какие запросы лучше всего 
использовать, чтобы результат выглядел максимально 
естественно и красиво.
Это простой способ превратить статичное фото в 
динамичное короткое видео 🌿
""",
        "gif": "leson 7/converted_animation.mp4",
        "video": "leson 7/IMG_7493.mp4"
    },
    {
        "title": "Урок 8. Создание аватара в LIME AI",
        "text": """📘 <b>Урок 8. Фото по референсу</b>
Сегодня познакомимся с режимом, который позволяет 
создавать изображения по <b>референсу.</b>
 Ты загружаешь фото-пример  и нейросеть генерирует 
новые снимки в похожем стиле.
В этом уроке мы разберём:
 — как работает режим «по референсу»,
 
✨ Этот инструмент помогает легко повторять 
понравившиеся образы и создавать новые вариации по 
готовым примерам
""",
        "file": "leson 8/Frame 149.png",
        "video": "leson 8/IMG_7565 (1).mp4",
        "type": "photo"
    },
    {
        "title": "Урок 9. Создание аватара в LIME AI",
        "text": """📘 <b>Урок 9. Стили</b>
Сегодня познакомимся с режимом,в котором можно 
найти множество <b>стилей</b> в LIME AI 💚
✨ В боте доступны разные стили для генерации 
изображений, каждый стиль имеет свои преимущества:
 — помогает быстрее получить нужный результат без 
выдумывания промтов,
 — делает фото более гармоничными и 
профессиональными,
 — экономит время и даёт готовый визуал под задачу 
Скорее смотри видео, чтобы разобраться""",
        "file": "leson 9/Frame 150.png",
        "video": "leson 9/IMG_7456.mp4",
        "type": "photo"
    },
    {
        "title": "Урок 10. Создание аватара в LIME AI",
        "text": """📘 <b>Урок 10. Партнёрская программа</b>
В этом уроке ты узнаешь:
 — что такое партнёрская программа LIME AI,
 — как работает система реферальных ссылок,
 — какие бонусы можно получать, приглашая новых 
пользователей.
Партнёрка - это возможность зарабатывать вместе с 
сервисом, просто делясь ссылкой 💚""",
        "file": "leson 10/Frame 151.png",
        "video": "leson 10/IMG_7451.MOV",
        "type": "photo"
    },
    {
        "title": "Урок 11. Создание аватара в LIME AI",
        "text": """📘 <b>Урок 11. Постобработка: если хочется реалистичнее</b>
В этом уроке мы разберём, как довести фото до идеала 
с помощью дополнительной обработки ✨
Ты узнаешь:
 — как работать в lightroom
 — как улучшить свет, цвет и детали
Это простой способ сделать результат максимально 
реалистичным и профессиональным""",
        "file": "leson 11/Frame 152.png",
        "video": "leson 11/video-output-9AC55AE6-697E-42FF-8D6F-22DE6ACB5D6B-1.mp4",
        "type": "photo"
    },
    # ➕ остальные уроки по такому же формату
]

# Прогресс пользователей
user_progress = {}


bot = Bot(token=API_TOKEN)

def get_button(text: str, callback: str):
    return types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton(text=text, callback_data=callback)]]
    )


# Старт
async def cmd_start(message: types.Message):
    photo = FSInputFile("first/Frame 137.png")

    long_text = """<b>Привет! Добро пожаловать в обучающий бот от LIME AI</b> 💚

Здесь тебя ждёт простое и бесплатное обучение нейросетям:
 — Короткие уроки без лишней теории;
 — Интересная практика;
 — Полезные материалы;
 — Советы, которые помогут создавать стильный и востребованный контент.

🚀 Готов начать? Тогда переходи к первому уроку!"""

    kb = get_button("🚀 Начинаем", "start_course")

    await message.answer_photo(
    photo=photo,
    parse_mode="HTML",  # ← здесь
    caption=long_text,
    reply_markup=kb
)




# Отправка урока
# Начало курса
# Начало курса
async def start_course(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_progress[user_id] = {"idx": 0}

    # Первый урок (отдельная кнопка)
    lesson = LESSONS[0]

    # Фото + текст в caption + кнопка
    if lesson.get("file") and lesson.get("text"):
        await bot.send_photo(
            callback.message.chat.id,
            FSInputFile(lesson["file"]),
            caption=lesson["text"],
            parse_mode="HTML",
            reply_markup=get_button("СЛЕДУЮЩИЙ УРОК", "next_lesson")
        )
    elif lesson.get("file"):  # если только фото
        await bot.send_photo(
            callback.message.chat.id,
            FSInputFile(lesson["file"]),
            parse_mode="HTML",
            reply_markup=get_button("СЛЕДУЮЩИЙ УРОК", "next_lesson")
        )
    elif lesson.get("text"):  # если только текст
        await bot.send_message(
            callback.message.chat.id,
            lesson["text"],
            parse_mode="HTML",
            reply_markup=get_button("СЛЕДУЮЩИЙ УРОК", "next_lesson")
        )

    # Сдвигаем индекс сразу
    user_progress[user_id]["idx"] = 1

    await callback.answer()


video_cache = {}  # ключ — путь к файлу, значение — file_id

async def send_video_cached(chat_id: int, path: str, button):
    """Отправка видео с кэшированием file_id и кнопкой, сразу с кнопкой"""
    if path in video_cache:
        await bot.send_video(
            chat_id,
            video_cache[path],
            width=1080,
            height=2340,
            supports_streaming=True,
            reply_markup=button
        )
    else:
        sent_video = await bot.send_video(
            chat_id,
            FSInputFile(path),
            width=1080,
            height=2340,
            supports_streaming=True,
            reply_markup=button
        )
        video_cache[path] = sent_video.video.file_id



# Отправка урока
async def send_lesson(chat_id: int, user_id: int):
    progress = user_progress[user_id]
    idx = progress["idx"]

    # Проверка на конец курса
    if idx >= len(LESSONS):
        text = """🎉 <b>Поздравляем!</b> 🎉
Вы успешно прошли обучение и теперь готовы к 
новым достижениям вместе с <b>LIME AI</b> 🚀
Не спешите выходить из этого бота - обучение здесь не 
заканчивается. Вас ждут новые уроки, фишки и 
полезные материалы, которые помогут ещё лучше 
освоить нейросети и использовать их в своих проектах 🌿✨
<b>Продолжайте открывать для себя возможности 
LIME AI и шаг за шагом создавайте всё более 
крутой контент в <a href="https://t.me/Lime_AI_bot?start=lessons">@Lime_AI_bot</a></b>💡"""
        try:
            await bot.send_photo(chat_id, FSInputFile("end/end.png"), parse_mode="HTML", caption=text)
        except Exception as e:
            await bot.send_message(chat_id, f"Ошибка загрузки картинки: {e}\n\n{text}")
        user_progress.pop(user_id, None)
        return

    lesson = LESSONS[idx]

    # Кнопка только для видео
    if idx == len(LESSONS) - 1:
        button = get_button("Завершить обучение", "finish_course")
    else:
        button = get_button("СЛЕДУЮЩИЙ УРОК", "next_lesson")

    # Фото с caption (кнопка не нужна)
    if lesson.get("type") == "photo" and lesson.get("file"):
        await bot.send_photo(chat_id, FSInputFile(lesson["file"]), caption=lesson.get("text", ""), parse_mode="HTML")

    # GIF с caption (кнопка не нужна)
    elif lesson.get("gif"):
        await bot.send_animation(chat_id, FSInputFile(lesson["gif"]), caption=lesson.get("text", ""), parse_mode="HTML")

    # Видео с кнопкой
    if lesson.get("video"):
        try:
            await send_video_cached(chat_id, lesson["video"], button)
        except FileNotFoundError:
            await bot.send_message(chat_id, "Видео не найдено", reply_markup=button)
    else:
        # Если медиа нет, только текст (кнопка не нужна)
        if not lesson.get("gif") and not lesson.get("file") and lesson.get("text"):
            await bot.send_message(chat_id, lesson.get("text", ""), parse_mode="HTML")

    # Обновляем прогресс
    progress["idx"] += 1




async def finish_course(callback: types.CallbackQuery):
    await callback.answer()

    text = """🎉 Поздравляем! 🎉
Вы успешно прошли обучение и теперь готовы к 
новым достижениям вместе с LIME AI 🚀
Не спешите выходить из этого бота - обучение здесь не 
заканчивается. Вас ждут новые уроки, фишки и 
полезные материалы, которые помогут ещё лучше 
освоить нейросети и использовать их в своих проектах 🌿✨
Продолжайте открывать для себя возможности 
LIME AI и шаг за шагом создавайте всё более 
крутой контент в <a href="https://t.me/Lime_AI_bot?start=lessons">@Lime_AI_bot</a>💡"""

    # Отправляем фото с caption
    try:
        await callback.message.answer_photo(
            FSInputFile("end/end.png"),
            caption=text
            parse_mode="HTML"
        )
    except Exception as e:
        await callback.message.answer(f"⚠️ Ошибка загрузки фото: {e}\n\n{text}")

    # очищаем прогресс
    user_progress.pop(callback.from_user.id, None)


# Кнопка "Продолжить"
async def next_lesson(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_id in user_progress:
        await callback.answer()  # отвечаем сразу, чтобы Telegram не ругался
        await send_lesson(callback.message.chat.id, user_id)
    else:
        await callback.message.answer("Сначала нажми /start")
        await callback.answer()



# Основной цикл
async def main():
    dp = Dispatcher()
    dp.callback_query.register(finish_course, F.data == "finish_course")
    dp.message.register(cmd_start, Command("start"))
    dp.callback_query.register(start_course, F.data == "start_course")
    dp.callback_query.register(next_lesson, F.data == "next_lesson")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
