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

    recovery =  filedialog.askopenfilename(initialdir = "/home/$USER/",title = "Select recovery",filetypes = (("IMG","*.img"),("all files","*.*")))
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
        isdevice = str(subprocess.check_output('fastboot devices', shell=True))
        if 'fastboot' in isdevice and 'no permissions' not in isdevice:
            check_button.config(image=check_ok)
            print(f'LOG:{isdevice}')
            progress = 2
        else:
            check_button.config(image=check_f)
            print(f'LOG:DEVICE IS NOT CONNECTED OR NO PERMISSIONS')

def fisting():
    if progress >= 2:
        flash_result = str(subprocess.check_output('fastboot flash recovery {}'.format(recovery), shell=True))
        flash_button.config(image=flash_ok)
        final()

def final():
        done = Toplevel(root)
        done.title("")
        done.geometry("250x125")
        done_label = Label(done, text='Flashing is done', font="sans-serif 9")
        done_label.place(relx=.34, rely=.09)
        done_label1 = Label(done, text='Hold up and power buttons', font="sans-serif 9")
        done_label1.place(relx=.236, rely=.24)
        done_label2 = Label(done, text='To enter recovery mode', font="sans-serif 9")
        done_label2.place(relx=.27, rely=.39)
        done_button = Button(done, image=done_png, border="0", command=root.quit)
        done_button.pack()
        done_button.place(relx=.41, rely=.6)

#window
root = Tk()
root.title("Simple Recovery Flasher")
root.geometry("400x600")
root.call('wm', 'iconphoto', root._w, PhotoImage(file="media/icon.png"))

#content
done_png = PhotoImage(file="media/button_ok.png")

label1 = Label(text='1. Please, select your recovery', font="sans-serif 13")
label1.place(relx=.22, rely=.04)

select_png = PhotoImage(file="media/button_select.png")
select_f = PhotoImage(file="media/button_select_fail.png")
select_ok = PhotoImage(file="media/button_select_ok.png")
select_button = Button(root, image=select_png, border="0", command=ass)
select_button.pack()
select_button.place(relx=.35,rely=.1)

label2 = Label(text='2. Reboot your phone into fastboot', font="sans-serif 13")
label2.place(relx=.175, rely=.27)

label3 = Label(text='and connect to PC via usb', font="sans-serif 13")
label3.place(relx=.267, rely=.3)

fastboot_png = PhotoImage(file="media/fastboot.png")
fpanel = Label(root, image = fastboot_png)
fpanel.pack()
fpanel.place(relx=.37, rely=0.35)

check_png = PhotoImage(file="media/button_check.png")
check_f = PhotoImage(file="media/button_check_fail.png")
check_ok = PhotoImage(file="media/button_check_ok.png")
check_button = Button(root, image=check_png, border="0", command=slave)
check_button.pack()
check_button.place(relx=.37,rely=.575)

label4 = Label(text='3. Make sure bootloader is unlocked,', font="sans-serif 13")
label4.place(relx=.16, rely=.74)

label5 = Label(text='you and your phone are ready and click', font="sans-serif 13")
label5.place(relx=.134, rely=.77)

flash_png = PhotoImage(file="media/button_flash.png")
flash_f = PhotoImage(file="media/button_flash_fail.png")
flash_ok = PhotoImage(file="media/button_flash_ok.png")
flash_button = Button(root, image=flash_png, border="0", command=fisting)
flash_button.pack()
flash_button.place(relx=.36,rely=.83)

root.mainloop()
