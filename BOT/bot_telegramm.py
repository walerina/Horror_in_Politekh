from aiogram.utils import executor
import client
from createBot import dp


client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True)

