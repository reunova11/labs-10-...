class Restaurant():
    def __init__(self, restaurant_name, cuisine_type,restaurant_rating,location,time):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_rating=restaurant_rating
        self.location=location
        self.time=time
    def describe_restaurant(self):
        #функция описания
        return "Название ресторана: %s , Тип кухни: %s, Рейтинг ресторана: %s " % (self.restaurant_name, self.cuisine_type,self.restaurant_rating)

    def Location(self):
        return "Ресторан находится: %s" %(self.location)
    def Time(self):
        #через словарь
        d=input("Введите день недели: ")
        b=["Понедельник", "Вторник","Среда","Четверг","Пятница"]
        if d in b:
            return "Сегодня режим работы ресторана: %s" % (self.time['Будни'])
        else:
            return "Сегодня режим работы ресторана: %s" % (self.time['Выходные'])
    def open_restaurant(self):
        return "Ресторан открыт"
    def reit(self):
        rei=input("Введите рейтинг: ")
        if self.restaurant_rating != rei:
            self.restaurant_rating=rei
            return "Новый рейтинг: %s" % (int(self.restaurant_rating))
    def flavorss(self):
    #наследует все свойства класса ресторан, можно добавлять новые
        return "Сорта мороженого в наличии: %s" % (", ".join(flavors))
    def append_flavors(self):
        print(self.flavorss())
        v=input("Какой вкус вы хотите добавить?")
        flavors.append(v)
        print(self.flavorss())
    def delete_flavors(self):
        print(self.flavorss())
        v = input("Какой вкус вы хотите удалить?")
        flavors.remove(v)
        print(self.flavorss())
    def is_flavor(self):
        v=input("Какой вкус вы ищете?: ")
        if v in flavors:
            return "Вкус есть в наличии:)"
        else:
            return "Данного вкуса нет:("

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type,restaurant_rating,flavors,location,time):
        super().__init__(restaurant_name,cuisine_type,restaurant_rating,location,time)
        self.flavors=flavors

restaurant_name=input("Введите название ресторана: ")
cuisine_type=input("Введите тип кухни: ")
restaurant_rating=5
flavors=[]
location=input("Введите описание местоположения ресторана: ")
time={'Будни': input("Режим работы в будни: "), 'Выходные' : input("Режим работы в выходные: ")}
n=int(input("Введите количество сортов мороженого: "))
for i in range(n):
    flavors.append(input("Введите сорт: "))
newRestaurant = IceCreamStand(restaurant_name,cuisine_type, restaurant_rating, flavors,location,time)
print(newRestaurant.describe_restaurant(),"\n" ,newRestaurant.open_restaurant(),"\n" ,newRestaurant.flavorss(),"\n",newRestaurant.reit())
print(newRestaurant.Location(),"\n",newRestaurant.Time())



from tkinter import *
from tkinter import messagebox


def describe():
    messagebox.showinfo(title='Описание ресторана', message=newRestaurant.describe_restaurant())
def fl():
    messagebox.showinfo(title='Сорта мороженого', message=newRestaurant.flavorss())
#создание окна
window = Tk()
window['bg'] = '#dff4f7'
window.title('Ресторан')
window.geometry('300x250')
window.resizable(width=False,height=False)
canvas = Canvas(window, height=300, width=250)
canvas.pack()
frame = Frame(window, bg='#f0b9ee', bd=5)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
title = Label(frame, text='Ресторан' + " " + newRestaurant.restaurant_name, bg='#ebd8ea', font=40)
title.pack()
btn = Button(frame,text='Описание ресторана', command=describe)
btn1 = Button(frame,text='Сорта мороженого', command=fl)
btn.pack()
btn1.pack()
window.mainloop()
#повторяется, чтобы не закрылось сразу