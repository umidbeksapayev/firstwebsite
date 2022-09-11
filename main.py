from turtle import title
from pywebio.output import put_file,put_html
from pywebio.session import hold
from frontend import get_info
from beckend import fillDoc
title = '<h1 style="text-align:center">Ўзбекистон Республикаси фуқаросининг\
  хорижга чиқиш биометрик паспортини расмийлаштириш учун АНКЕТА</h1>'
put_html(title)

userinfo=get_info()
fileename=fillDoc(userinfo)
text = "<h3>Анкета тайёр. Юклаб олиш учун қуйидаги боғламани босинг.</h3>"
put_html(text)

with open (fileename,'rb') as fayl:
    anketa=fayl.read()
    put_file(fileename,content=anketa)
    hold()

