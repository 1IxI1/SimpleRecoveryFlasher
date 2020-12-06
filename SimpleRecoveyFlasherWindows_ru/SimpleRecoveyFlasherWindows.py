from tkinter import *
from tkinter import filedialog
import subprocess
import os

#declaration
progress = 0
recovery = ''

#functions
def ass():
    global progress, recovery

    recovery =  filedialog.askopenfilename(initialdir = "C;/",title = "Select recovery",filetypes = (("IMG","*.img"),("all files","*.*")))
    print(f'LOG:{recovery}') #log

    name_recovery = recovery.rpartition('/')[-1]

    if name_recovery.rpartition('.')[-1] == 'img' or name_recovery.rpartition('.')[-1] == 'IMG':
        select_button.config(image=select_ok)
        progress = 1
    else:
        select_button.config(image=select_f)
        progress = 0

def slave():
    global progress

    if progress >= 1:
        isdevice = str(subprocess.check_output('.\\fastboot devices'))
        if 'fastboot' in isdevice and 'no permissions' not in isdevice:
            check_button.config(image=check_ok)
            print(f'LOG:{isdevice}')
            progress = 2
        else:
            check_button.config(image=check_f)
            print(f'LOG:DEVICE IS NOT CONNECTED OR NO PERMISSIONS')

def fisting():
    if progress >= 2:
        flash_result = str(subprocess.check_output('.\\fastboot flash recovery {}'.format(recovery)))
        flash_button.config(image=flash_ok)
        final()

def final():
        done = Toplevel(root)
        done.title("")
        done.geometry("250x125")
        done_label = Label(done, text='Завершено', font="sans-serif 9")
        done_label.place(relx=.36, rely=.09)
        done_label1 = Label(done, text='Удерживайте вверх и выключить', font="sans-serif 9")
        done_label1.place(relx=.12, rely=.24)
        done_label2 = Label(done, text='Чтобы попасть в рекавери', font="sans-serif 9")
        done_label2.place(relx=.2, rely=.39)
        done_button = Button(done, image=done_png, border="0", command=root.quit)
        done_button.pack()
        done_button.place(relx=.38, rely=.6)

import sys
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
    
#window
root = Tk()
root.title("Simple Recovery Flasher")
root.geometry("400x600")
resource_path('media/icon.png')
root.call('wm', 'iconphoto', root._w, PhotoImage(file="media/icon.png"))

#content
resource_path('media/button_ok.png')
done_png = PhotoImage(file="media/button_ok.png")

label1 = Label(text='1. Выберите файл с рекавери', font="sans-serif 13")
label1.place(relx=.22, rely=.04)

resource_path('media/button_select.png')
resource_path('media/media/button_select_fail.png')
resource_path('media/button_select_ok.png')
select_png = PhotoImage(file="media/button_select.png")
select_f = PhotoImage(file="media/button_select_fail.png")
select_ok = PhotoImage(file="media/button_select_ok.png")
select_button = Button(root, image=select_png, border="0", command=ass)
select_button.pack()
select_button.place(relx=.33,rely=.1)

label2 = Label(text='2. Перезагрузите телефон в фастбут', font="sans-serif 13")
label2.place(relx=.14, rely=.25)

label3 = Label(text='и подключите к ПК по usb', font="sans-serif 13")
label3.place(relx=.267, rely=.28)

resource_path('media/fastboot.png')
fastboot_png = PhotoImage(file="media/fastboot.png")
fpanel = Label(root, image = fastboot_png)
fpanel.pack()
fpanel.place(relx=.37, rely=0.33)

resource_path('media/button_check.png')
resource_path('media/media/button_check_fail.png')
resource_path('media/button_check_ok.png')
check_png = PhotoImage(file="media/button_check.png")
check_f = PhotoImage(file="media/button_check_fail.png")
check_ok = PhotoImage(file="media/button_check_ok.png")
check_button = Button(root, image=check_png, border="0", command=slave)
check_button.pack()
check_button.place(relx=.31,rely=.555)

label4 = Label(text='3. Убедитесь, что загрузчик', font="sans-serif 13")
label4.place(relx=.225, rely=.707)

label5 = Label(text='разблокирован, ваш телефон', font="sans-serif 13")
label5.place(relx=.2, rely=.74)

label6 = Label(text='и вы готовы и нажимайте', font="sans-serif 13")
label6.place(relx=.256, rely=.773)

resource_path('media/button_flash.png')
resource_path('media/media/button_flash_fail.png')
resource_path('media/button_flash_ok.png')
flash_png = PhotoImage(file="media/button_flash.png")
flash_f = PhotoImage(file="media/button_flash_fail.png")
flash_ok = PhotoImage(file="media/button_flash_ok.png")
flash_button = Button(root, image=flash_png, border="0", command=fisting)
flash_button.pack()
flash_button.place(relx=.3,rely=.83)

root.mainloop()
