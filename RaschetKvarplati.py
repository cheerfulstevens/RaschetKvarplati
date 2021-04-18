from tkinter import*
import tkinter.messagebox as box

window = Tk()
window.title('Расчет коммунальных услуг')
window.geometry("980x500")
window.resizable(width=False, height=False)

#Расчет холодной воды
text = Label(window, text='Расчет коммунальных услуг по холодной воде. ')
text.pack()

text1 = Label(window, text='Введите предыдущие показатели счетчика холодной воды: ')
text1.place(x=10, y=35)
frame = Frame(window)
cwater = Entry(frame)



text2 = Label(window, text='Введите текущие показатели счетчика холодной воды: ')
text2.place(x=10,y=55)
ccwater = Entry(frame)

text3 = Label(window, text='Введите тарифную ставку: ')
text3.place(x=10,y=75)
rate = Entry(frame)



def dialog():
    global result_1
    result_1 = (float(ccwater.get())-float(cwater.get())) * float(rate.get())
    box.showinfo('Результат расчета стоимости холодной воды: ', float(result_1))
    
btn = Button(frame, text = 'Расчитать', command = dialog)
btn.pack(side = RIGHT, padx = 5)
cwater.pack ()
ccwater.pack ()
rate.pack ()
frame.pack (padx = 20, pady =20)



#Расчет горячей воды

text4 = Label(window, text='Расчет коммунальных услуг по горячей воде. ')
text4.place(x=350, y=110)

text5 = Label(window, text='Введите предыдущие показатели счетчика горячей воды: ')
text5.place(x=10, y=135)
frame_2 = Frame(window)
hwater = Entry(frame_2)


text6 = Label(window, text='Введите текущие показатели счетчика горячей воды: ')
text6.place(x=10,y=155)
chwater = Entry(frame_2)

text7 = Label(window, text='Введите тарифную ставку: ')
text7.place(x=10,y=175)
rate_2 = Entry(frame_2)


def dialog_2():
    global result_2
    result_2 = (float(chwater.get())-float(hwater.get())) * float(rate_2.get())
    box.showinfo('Результат расчета стоимости горячей воды: ', float(result_2))
    
btn = Button(frame_2, text = 'Расчитать', command = dialog_2)
btn.pack(side = RIGHT, padx = 5)
hwater.pack ()
chwater.pack ()
rate_2.pack ()
frame_2.pack (padx = 20, pady =20)



#Расчет газа

text8 = Label(window, text='Расчет коммунальных услуг по газу. ')
text8.place(x=350, y=210)

text9 = Label(window, text='Введите предыдущие показатели счетчика газа: ')
text9.place(x=10, y=235)
frame_3 = Frame(window)
gas = Entry(frame_3)


text10 = Label(window, text='Введите текущие показатели счетчика газа: ')
text10.place(x=10,y=255)
cgas = Entry(frame_3)

text11 = Label(window, text='Введите тарифную ставку: ')
text11.place(x=10,y=275)
rate_3 = Entry(frame_3)


def dialog_3():
    global result_3
    result_3 = (float(cgas.get())-float(gas.get())) * float(rate_3.get())
    box.showinfo('Результат расчета стоимости газа: ', float(result_3))
    
btn = Button(frame_3, text = 'Расчитать', command = dialog_3)
btn.pack(side = RIGHT, padx = 5)
gas.pack ()
cgas.pack ()
rate_3.pack ()
frame_3.pack (padx = 20, pady =20)

#Расчет электричества

text12 = Label(window, text='Расчет коммунальных услуг по электричеству. ')
text12.place(x=350, y=305)

text13 = Label(window, text='Введите предыдущие показатели счетчика электричества: ')
text13.place(x=10, y=330)
frame_4 = Frame(window)
electric = Entry(frame_4)


text14 = Label(window, text='Введите текущие показатели счетчика электричества: ')
text14.place(x=10,y=350)
celectric = Entry(frame_4)

text15 = Label(window, text='Введите тарифную ставку: ')
text15.place(x=10,y=370)
rate_4 = Entry(frame_4)


def dialog_4():
    global result_4
    result_4 = (float(celectric.get())- float(electric.get())) * float(rate_4.get())
    box.showinfo('Результат расчета стоимости электричества: ', float(result_4))
    
btn = Button(frame_4, text = 'Расчитать', command = dialog_4)
btn.pack(side = RIGHT, padx = 5)
electric.pack ()
celectric.pack ()
rate_4.pack ()
frame_4.pack (padx = 20, pady =20)

#Расчет общей стоимости

text16 = Label(window, text='Общие расходы: ')
text16.place(x=300, y=430)
frame_5 = Frame(window)




def dialog_5():
    
    result_cwater = (float(ccwater.get()) - float(cwater.get())) * float(rate.get())
    result_hwater = (float(chwater.get()) - float(hwater.get())) * float(rate_2.get())
    result_gas = (float(cgas.get()) - float(gas.get())) * float(rate_3.get())
    result_electric = (float(celectric.get()) - float(electric.get())) * float(rate_4.get())
    result_total = result_cwater + result_hwater + result_electric + result_gas
    box.showinfo('Результат расчета стоимости газа: ', float(result_total))
    
btn = Button(frame_5, text = 'Узнать общие расходы', command = dialog_5)
btn.pack(side = RIGHT, padx = 5)
frame_5.pack (padx = 20, pady =20)

window.mainloop()
