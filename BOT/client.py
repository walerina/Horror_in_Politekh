from aiogram import types 
from createBot import dp,bot
from aiogram.dispatcher import Dispatcher  
from keyboard import kb_client,kb_client2,kb_client3,kb_client4,kb_client5,kb_client6,kb_client7,kb_client8,kb_client9,kb_client10,kb_client11,kb_client13,kb_client14,kb_client15,kb_client16,kb_client17
from time import sleep
from aiogram.types import ReplyKeyboardRemove

#@dp.message_handler(commands=['start','help'])
async def comand_start(message):
	await message.answer('Пробурчав какое-то невнятое проклятье, ты переворачиваешься на другой бок, чтобы продолжить спать... Но не тут-то было. Ты спишь на чем-то холодном, и это явно не кровать.Ты открываешь глаза; ты... ')
	photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/991f2981796a0295004bc904b023d4b3ca16f2c7/image.jpg'
	await bot.send_photo(message.chat.id, photo=photo_url, caption='Чёрт побери, а где это ты находишься?', reply_markup=kb_client2)

async def plot(message):
	if message.text =='Осмотреться' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image2.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Оборачиваешься. Позади — жутковатая комната.')
		await message.answer('Ты смутно помнишь, что ты студент по имени Петр; смутно помнишь, что учишься в Политехе, но черт бы побрал всех демонов преисподней — как ты сюда попал?!В кармане (одет ты не в пижаму, а во что-то уличное-непонятное) нет ни телефона, ни ключей — только фонарик.Внезапно нога задевает какую-то бумажку. Подняв ее, читаешь напечатанную на ней надпись: “Ищи выход, введя четыре цифры напротив существ с девятью смертями: цифры эти гласят о времени рождения тьмы, окружающей тебя. Избегай неверных дверей”.Бурчишь что-то недовольное, а по спине тем временем пробегают мурашки. Что за чушь?...Гулкая и сырая тишина коридора начинает напрягать.',reply_markup=kb_client3)
	if message.text=='Попробовать открыть двери в помещении' :
		await message.answer('Бесполезно. Все двери заблокированы.')
	if message.text=='Пойти вперед по коридору' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image3.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты делаешь несколько шагов вперед. Посмотрев налево, обнаруживаешь окно. Похоже, ты оказался в главном здании Политеха, и это случилось ночью.', reply_markup=kb_client4)
	if message.text=='Попробовать открыть окно' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image4.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Бесполезно. Окно словно приклеено намертво, и применять силу бессмысленно.')
	if message.text=='Попробовать открыть какую-то из ближайших дверей' :
		await message.answer('Бесполезно, всё заперто.')
	if message.text=='Пойти дальше по коридору' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image5.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты идешь вперед. Гулкую тишину нарушает только стук шагов о каменный пол. Сырая прохлада овевает кожу.',reply_markup=ReplyKeyboardRemove())
		await message.answer('Ты помнишь, что где-то здесь должна быть лестница, которая ведет на первый этаж... Подходишь ближе, но ничего нет — сплошная стена.“Это уже несмешно”, — бурчишь сквозь сжатые зубы. Если тебе попадутся обещанные существа с девятью смертями, уж им-то ты отомстишь за все эти ночные похождения. Итак, ты продолжаешь идти.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image6.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Внезапно замечаешь дверь с кодовым замком.',reply_markup=kb_client5)
	if message.text=='Сдернуть скотч с двери и попробовать ввести код':
		await message.answer('Ты пытаешься ввести код.',reply_markup=kb_client7)
	if message.text=='1899' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image8.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Введя код, ты надавливаешь на ручку, и та внезапно поддается. Открыв дверь, видишь впереди только полную темноту; не думая ни о чем, ты делаешь шаг вперед......И в темноте впереди появляется… нечто.Дверь позади тебя с глухим стуком захлопывается.')	
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново?Тогда нажмите кнопку ниже.',reply_markup=kb_client)
	if( message.text=='9898' or message.text=='0000'or message.text=='1234') :
		await message.answer('Похоже, код неверный.',reply_markup=kb_client6)
	if message.text=='Снова попробовать ввести код':
		await message.answer('Ты пытаешься ввести код.',reply_markup=kb_client7)
	if message.text=='Проигнорировать дверь и пойти дальше':
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image7.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Некоторое время ты переминаешься с ноги на ногу у двери, но, в конечном итоге, решаешь, что лучше лишний раз ничего не трогать, и продолжаешь идти. Окна и двери по-прежнему заблокированы; даже если двери и открыты, за ними находятся лишь тупики в виде стен.')	
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagea.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Гулкую тишину нарушает только стук шагов о каменный пол... Позади раздается странный шорох, но позади никого не оказалось. Немного погодя, ты продолжаешь идти, с каждым шагом приближаясь к концу коридора.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imageb.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Впереди — дверь с надписью “Выход”.Слева ты замечаешь тупиковый проход, из него доносится шорох...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagec.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='И внезапно страх, сжимавший тебе горло, ослабевает.“Кошечки”, — выдыхаешь ты.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imaged.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url ,caption=' Рот непроизвольно складывается в вечное, неумирающее кс-кс-кс — но кошки, услышав его, вздрагивают и в панике разбегаются по углам. Ну, ничего.')
		await message.answer('Зато справа ты видишь дверь с кодовым замком.', reply_markup=kb_client8)
	if message.text=='Пойти в дверь с надписью “Выход”' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagee.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты выходишь в дверь.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagef.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Справа — какие-то шкафы и темнота, но они тебя не смущают; ты делаешь шаг на лестницу...')
		await message.answer('В темноте раздается стук, смутно напоминающий клацанье зубов, а затем в щиколотку вонзается что-то холодное и очень острое. Зубы.')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново?Тогда нажмите кнопку ниже.',reply_markup=kb_client)
	if message.text=='Подойти к двери с кодовым замком' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image1.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url,caption='К твоему счастью, дверь была приоткрыта.Внезапно сзади раздаются странный шорох и звук, напоминающий клацанье зубов; сердце падает в пятки; ты делаешь быстрый шаг вперед; дверь позади захлопывается... Ты сползаешь вниз по двери и садишься на пол. Немного переведя дух, ты понимаешь, что оказался в НИКе. Около тебя лежит записка. Взяв ее, читаешь: “Найди карту. Цифра 9 — твой главный символ. Коснись ее”.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image3.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='На стенде тебя привлекает рука. Странная эта рука какая-то… Ты на всякий случай машешь ей кулаком.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image4.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Обе двери не открываются; очевидно, придется идти вперед по коридору. Стенды светятся, но вокруг — никого, кроме тишины... Ты сжимаешь руки в кулаки: ты полон решимости выбраться из этого лабиринта и наконец-то разобраться в происходящем!')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image5.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты выходишь в абсолютно пустой холл, и только стук шагов нарушает тишину. Замечаешь, что одна из кабинок лифта находится на этом этаже. Взгляд скользит по разным дверям и коридорам...')
		await message.answer('И внезапно позади раздается очень быстрый и очень неприятный стук, похожий на стук крохотных ножек.',reply_markup=kb_client9)
	if message.text=='Побежать вперед, к выходу' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image6.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты бежишь, не тратя время на то, чтобы обернуться; сердце безумно колотится.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image7.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Дверь выхода всё ближе; карта Политеха тоже приближается, и…')
		await message.answer('...И ТЫ ИЗДАЕШЬ ДИКИЙ КРИК, КОГДА ОСТРЫЕ ПАЛЬЦЫ ПРОТЫКАЮТ ШЕЮ')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново?Тогда нажмите кнопку ниже.',reply_markup=kb_client)
	if message.text=='Побежать в ближнюю дверь справа' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image10.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты бежишь, не тратя время на то, чтобы обернуться; сердце безумно колотится...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image11.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url,caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image12.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url,caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image13.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url,caption='...')
		await message.answer('...И ТЫ ИЗДАЕШЬ ДИКИЙ КРИК, КОГДА ОСТРЫЕ ПАЛЬЦЫ ПРОТЫКАЮТ ШЕЮ')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново?Тогда нажмите кнопку ниже.',reply_markup=kb_client)
	if message.text=='Побежать в дальнюю дверь справа' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image14.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты бежишь, не тратя время на то, чтобы обернуться; сердце безумно колотится...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image15.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты стремительно бежишь вниз...')
		await message.answer('...И ТЫ ИЗДАЕШЬ ДИКИЙ КРИК, КОГДА ОСТРЫЕ ПАЛЬЦЫ ПРОТЫКАЮТ ШЕЮ')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново?Тогда нажмите кнопку ниже.',reply_markup=kb_client)
	if message.text=='Побежать к лифту' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image16.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты бежишь, не тратя время на то, чтобы обернуться; сердце безумно колотится; на нажатие кнопки лифт мгновенно реагирует открытием дверей.')
		await message.answer('Ты заскакиваешь внутрь и судорожно жмёшь все кнопки. Дверь закрывается, и…')
		await message.answer('...И ЧТО-ТО ЧЕРНОЕ СНАРУЖИ СТРЕМИТЕЛЬНО ПРИСКАКИВАЕТ И БЬЕТСЯ О СТЕКЛО')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image17.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Лифт едет вниз. Ты замер от ужаса. Похоже, это была рука. На нулевом этаже двери раскрываются.')
		await message.answer('Сердце готово выпрыгнуть из груди. О Господи. Судя по всему, эта тварь очень быстро движется по разным коридорам и лестницам, и спасти от нее может только лифт. Судя по скачкам, она еще и прыгает на какую-то высоту, а из-за того, что она маленькая, она может пробраться почти где угодно... “П-п-п...“ — губы хотят произнести “проклятье“, но складываются в “помогите“.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image18.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты выходишь из лифта.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image19.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Открыв дверь, ты попадаешь в пустое полутемное помещение. Пустое и очень тихое.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image20.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Смотришь направо. За дальней дверью, судя по всему, лестница наверх; за ближней — то ли комната, то ли коридор. Рядом с тобой находится дверь в туалет.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image21.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Смотришь налево. Там тоже два прохода.',reply_markup=kb_client10)
	if message.text=='Побежать в проход слева' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image8.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты бежишь, не тратя время на то, чтобы обернуться; сердце безумно колотится. От статуи в виде рук оно начинает колотиться еще быстрее; ты начинаешь бежать еще стремительней, и...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagee9.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url,caption='...')
		await message.answer('...И ТЫ ИЗДАЕШЬ ДИКИЙ КРИК, КОГДА ОСТРЫЕ ПАЛЬЦЫ ПРОТЫКАЮТ ШЕЮ')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново?Тогда нажмите кнопку ниже.',reply_markup=kb_client)	
	if message.text=='Пойти в дальнюю дверь справа' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image22.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Быстрым шагом направляешься к лестнице.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image23.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Начинаешь подниматься...')
		await message.answer('...Hа твою макушку капает холодная и вязкая жидкость. Ты поднимаешь голову и смотришь наверх. Холодная рука хватает тебя за лицо. ПАЛЬЦЫ ВПИВАЮТСЯ В КОЖУ. ЗЕМЛЯ УХОДИТ ИЗ-ПОД НОГ, ПОСЛЕ ГРОМКОГО ЩЕЛЧКА ТЫ ПЕРЕСТАЁШЬ ЧУВСТВОВАТЬ СВОЁ ТЕЛО.')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново? Тогда нажмите кнопку ниже.',reply_markup=kb_client)	
	if message.text=='Пойти в ближнюю дверь справа' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image24.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты заходишь. Впереди расстилается... коридор. Справа — темнота с несколькими заблокированными дверями (как ты уже понял, почти все двери в этом месте заблокированы), спереди — коридор.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image25.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты пошёл вперёд. Где-то далеко позади послышался быстрый-быстрый стук, но ты по инерции идешь, в груди похолодело.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image26.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		await message.answer('Позади раздался грохот открывающихся-закрывающихся дверей. На мгновение всё затихло. Вскоре ты услышал стук, он приближался… Без раздумий ты рванул вперёд, но было уже поздно: склизкая холодная рука схватила тебя за ногу и поволокла по коридору. Чёрные пальцы залезли под кожу, от боли ты потерял сознание.')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново? Тогда нажмите кнопку ниже.',reply_markup=kb_client)
	if message.text=='Пойти в дальнюю дверь слева' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image27.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты заходишь. Дверь с надписью “Выход“ оказывается заблокированной')
		await message.answer('В этот момент со стороны лестницы раздается ритмичный звук, похожий на стук крохотных ножек. Быстрым движением ты закрываешь дверь и замираешь.')
		await message.answer('За дверью слышны шорохи и постукивание, как будто кто-то ощупывает дверь.Ты пытаешься не дышать — и ждешь…')
		await message.answer('Наконец, звук замирает: остается только тишина… Ты делаешь беззвучный выдох облегчения, и ручка закрытой двери… медленно опускается вниз. Дверь со скрипом приоткрылась. За ней проползает несколько черных пальцев.')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново? Тогда нажмите кнопку ниже.',reply_markup=kb_client)
	if message.text=='Пойти в ближнюю дверь слева' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image31.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты заходишь. Двери слева оказались заблокированными — впрочем, как и почти все остальные двери в этом мерзком месте. Яркая пустота коридора пугает — как и монотонный гул ламп.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image32.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Гул ламп давит на плечи... И в этот момент где-то позади себя ты слышишь ... Быстрый ритмичный звук, похожий на стук маленьких ножек.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image33.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты дошел до развилки. Можно побежать налево...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image34.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='или направо. Взгляд скользнул по потолку... Тонкая догадка, едва уловимая, посетила голову. Главное — не упустить ее из-за паники.')
		await message.answer('Куда же ты пойдёшь?',reply_markup=kb_client11)
	if message.text=='Побежать направо' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image35.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты направляешься направо. Добегаешь до развилки, чувствуя, как сердце безумно колотится. Слышишь, что быстрый стук, до этого далекий, как будто бы начал приближаться.')
		await message.answer('Дверь слева оказалась заблокированной. Ты прыгаешь в темноту, лицом в угол, надеясь спрятаться в этой черноте. Быстрый стук-топот приближается, и сердце готово разорваться от страха. Затем стук… почему-то затихает. Ты не дышишь, закрываешь глаза и терпеливо ждешь, затаив робкую надежду на спасение... Кто-то тихонько стучит пальцем тебе по затылку.')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново? Тогда нажмите кнопку ниже.',reply_markup=kb_client)
	if message.text=='Побежать налево' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image36.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Направляешься налево, за угол. Все двери, как и ожидалось, заблокированы. Зато есть дыры на потолке!')
		await message.answer('Ты залезаешь на коробку, а потом в дыру; затем отпихиваешь ногой коробку, полностью вскарабкиваешься в темноту и замираешь. В этот момент далекий стук начинает приближаться; став совсем громким, он замер. Ты перестаешь дышать. Затем снова раздается стук. Кажется, тварь побежала куда-то в другой коридор. Ты продолжаешь ждать. Снова раздается стук; стук удаляется… Наконец, всё затихает.')
		await message.answer('Ты возвращаешься. Судя по черным следам, рука вышла с лестницы (наверно, лестница ведет на первый этаж). Видимо, руку побеспокоили, но, не найдя жертву, она вернулась в свою витрину. Тебя трясет. Не хочется бурчать ни на ночь, ни на двери.Господи помилуй, теперь ты никогда не будешь грозить экспонатам кулаком. Ни за что. От мыслей о том, что было бы, если бы ты погрозил черному квадрату Малевича, по коже пробегают мурашки. Хотя, возможно, руке было плевать на угрозы — она просто хотела мяса...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image37.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='На цыпочках ты выходишь на лестницу. Действительно: эта лестница ведет на первый этаж.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image38.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Аккуратно выглядываешь. Да, витрина с рукой далеко отсюда, так что можно прокрасться незамеченным.')
		await message.answer('Тишайше крадешься вперед.Никого.' , reply_markup=kb_client13)
		await message.answer('Дверь закрыта.',reply_markup=kb_client13)	
	if message.text=='Пойти в туалет' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image28.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты заходишь в туалет.')
		await message.answer('За дверью раздается ритмичный звук, похожий на стук крохотных ножек.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image29.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты забегаешь в кабинку и тихо встаешь на унитаз, чтобы не было видно ног.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image30.jpeg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		await message.answer('За дверью туалета раздается быстрый стук, грохот и звук открывающихся дверей. Через миг всё затихает. Дверь в туалет со скрипом открывается — оно пробралась сюда. Ты ждешь, стараясь не дышать. Ритмичные постукивания эхом отдаются в голове и нагоняют панику — тварь явно ползает туда-сюда. Тень остановилась перед кабинкой. Твой взгляд не отрывался от щели под дверью. Черная рука забежала в кабинку. Резким прыжком она хватает тебя за горло.')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново? Тогда нажмите кнопку ниже.',reply_markup=kb_client)
	if message.text=='Подойти к карте' :
		await message.answer('Впереди простирается карта кампусов. Парочка зданий так и просит: “прикоснись ко мне“.' , reply_markup=kb_client14)
	if message.text=='Коснуться главного здания' :
		await message.answer('Ты прикасаешься к главному зданию…')
		await message.answer('...И тут же понимаешь, что зря это сделал. С диким воплем ты отдергиваешь руку, но уже поздно: события начали забываться. “ТОЛЬКО НЕ СНАЧАЛА“ — отчаянный крик оглашает стены холла, но в следующий миг ты падаешь в темноту. ')
		await message.answer('Ваш путь начинается сначала. Нажмите кнопку ниже.',reply_markup=kb_client)
	if message.text=='Коснуться 9 корпуса' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image42.jpeg '
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты прикасаешься к 9 корпусу...')
		await message.answer('...И мир вокруг начинает кружиться.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Издав утомленный стон, ты поднялся. Снова тихая рекреация. Снова никого (“Кроме разве что монстров, уж они-то здесь наверняка будут”). Тебя трясет. Ты хочешь под одеяло, но вместо одеяла рядом с ногами обнаружилась всего лишь очередная записка: “Ищи в месте с девятью кругами ключ к вершине башни“.')
		await message.answer('...' ,reply_markup=kb_client15)
	if message.text=='Пойти на лестницу' :
		await message.answer('Ты выходишь на лестницу.',reply_markup=kb_client16)
	if message.text=='Пойти направо' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image5 (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты движешься по коридору; двери сменяются дверями; стены скользят мимо тебя...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image6 (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image7 (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image8 (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Дверь слева, ведущая на лестницу, заперта; остается только один коридор...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image9 (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagea (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imageb (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...Но всё закрыто. Тупик.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты вернулся к началу.')
		await message.answer('...' , reply_markup=kb_client15)
	if message.text=='Пойти налево' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image2 (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image3 (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image4 (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Все двери заблокированы. Тупик.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты вернулся к началу.')
		await message.answer('...' , reply_markup=kb_client15)
	if message.text=='Подняться' :
		await message.answer('Поднимаешься. Двери на всех этажах, увы, заблокированы.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagec (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imaged (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagee (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagef (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image10.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image11.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image122.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='На самом верху обнаружилась темная дверь, однако она заперта.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты вернулся к началу.')
		await message.answer('...' , reply_markup=kb_client15)
	if message.text=='Спуститься' :
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image13.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Дверь на первом этаже заблокирована, однако еще ниже ты обнаруживаешь... подвал.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image14.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image15.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image16.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='В полной темноте приходится пользоваться фонариком.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image17.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Сырость окутывает, отзываясь мурашками по коже. Убежище... По пути ты проверял множество дверей на наличие их запертости, но проверять эту дверь... как-то не хочется. На полу ты видишь что-то блестящее. Это похоже на ключ. Поднимаешь с пола...И вдруг дверь убежища начинает трястись, а за ней раздается хрип.')
		await message.answer('Ты бегом поднимаешься на уровень этажа, с которого пришел. Сзади раздаются хлюпанья и хрип.' , reply_markup=kb_client17)
	if message.text=='Вернуться на этаж':
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Ты вернулся к начальной развилке. ')
		await message.answer('Со всех сторон приближался топот. Бежать некуда, тебя нагоняют иссохшие зомби. Через секунду они бросаются на тебя, и ты чувствуешь... как твое сердце вырывают из груди.')
		await message.answer('Вы погибли, но это не единственный исход этой истории. Хотите начать заново? Тогда нажмите кнопку ниже.',reply_markup=kb_client)
	if message.text=='Побежать наверх' :
		await message.answer('Поднимаешься. Двери на всех этажах, увы, заблокированы.')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagec (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imaged (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagee (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imagef (2).jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image10.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image11.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/image122.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='На самом верху обнаружилась темная дверь, однако она заперта.')
		await message.answer('Но у тебя есть ключ.')
		await message.answer('Ты судорожно впихиваешь ключ, сдергивая приклеенные к двери бумажки; сзади топот и хрип становятся все ближе; ты оборачиваешься, замечая на лестнице каких-то жутких иссохших зомби; ты хватаешься за ручку, открываешь, заскакиваешь внутрь, и!')
		photo_url='https://raw.githubusercontent.com/walerina/Horror_in_Politekh/main/imageNEW.jpg'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='...Ты на винтовой лестнице.')
		await message.answer('Вопя судорожные “помогите”, ты бежишь вниз по лестнице. Вокруг — только полумрак и синий свет. Тебя окружает жуткий металлический гул. Голова кружится; когда-то ты хотел попасть в башню Политеха, но только не сейчас; ты бежишь всё ниже, и ниже, и ниже... Внизу обнаруживается дверь — ты пинком открываешь ее, и...')
		await message.answer('— Эй! Прекращай! Ты открываешь глаза. Тебя держат несколько соседей по общаге; один скорчился на полу. Похоже, ты только что пнул его ногой. — Не идите в Политех, — сипишь иссохшими губами. — Не идите, там... Там твари с зубами, и живая рука, и зомби, понимаете, там зомби-студенты из убежища! Это был не сон, я был там на самом деле, если бы меня убил монстр, я бы умер от разрыва сердца, не идите в Политех, заклинаю вас, НЕ ИДИТЕ! — в порыве паники ты начал трясти одного из соседей за плечи. — Блин, какие зомби? Ты кукухой двинулся? Вышмат страшнее так-то, — отвечает сосед. — Да и рано ты как-то сдулся. Мы ведь только первокурсники. Теперь несколько лет мучиться. Остальные весело посмеиваются. Первокурсники... Мы только первокурсники, а впереди — и превращение в зомби перед сессией, и злые зубастые улыбки преподавателей, и черные иссохшие руки, которые отрывают у студентов, пойманных за списыванием, и... и отчаяние, и кошмар, и вечное бегство! Ты издаешь стон ужаса.')
		photo_url='https://sun9-9.userapi.com/impf/c840438/v840438405/3816b/QZQJObMB6OI.jpg?size=300x299&quality=96&sign=46c7bbb15f548048952c0099924cea97&type=album'
		await bot.send_photo(message.chat.id, photo=photo_url, caption='Поздравляем, вы проши квест!')
		await message.answer('Победа! Вы нашли истинную концовку и помогли Петру пережить эту ночь. Мы благодарим вас за прохождение этого текстового квеста. Если хотите начать заново и посмотереть другие концовки, нажмите кнопку ниже.',reply_markup=kb_client)
	

def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(comand_start, commands=['start','help'])
	dp.register_message_handler(plot)
	
	
	
	