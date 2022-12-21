from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5677956355:AAGzUvm_-Ie71XMihvvimlI9QXDoHSojuXw").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server_start')
app.run_polling()


# =====================================================================================================================================

# import matplotlib.pyplot as plt
# import numpy as np

# list = [1, 2, 3, 4, 5, 2, 7, 1, 9]
# plt.plot(list)
# plt.show()

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()

# ====================================================================================================================================


# import emoji

# print(emoji.emojize('Python is :thumbs_up:')) # Python is 👍
# print(emoji.emojize('Python is :thumbsup:', language='alias')) # Python is 👍
# # По умолчанию используется английский язык ( language='en' ), но также поддерживаются следующие языки:
# print(emoji.demojize('Python is 👍')) # Python is :thumbs_up: - так можно посмотреть название смайла
# print(emoji.emojize("Python is fun :red_heart:")) # Python is fun ❤️
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type")) # Python is fun ❤️
# print(emoji.is_emoji("👍")) # True
# print(emoji.demojize('Код для этого эмодзи: 🤝'))
# print(emoji.emojize('этот смайл :handshake:'))

# =====================================================================================================================================

# from progress.bar import Bar
# import time # импорт библиотеки time

# bar = Bar('Processing', max = 20) # установили 20 тиков
# for i in range(20):
#     time.sleep(1) # таймер торможения 1 секунда
#     bar.next()
# bar.finish()