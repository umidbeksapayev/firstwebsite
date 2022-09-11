from pywebio.input import input,input_group
def get_info():
    info=input_group("fuqoro haqida malumot",[input('Ism',name='ism'),
    input('Familiya',name='familiya'),
    input('Otasining ismi',name='Otasi'),
    input("Tug'ilgan yili",name='tyil'),
    input("Tug'ilgan kuni",name='tkun'),
    input("Tug'ilgan oy",name='toy'),
    input("Telefon raqami",name='traqam'),
    input("Pasport seriyasi",name='seriya'),
    input("Pasport raqami",name='raqami'),
    input("Pasport berilgan sana",name='pass_sana')])
    return info
get_info()