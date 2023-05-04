class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type,restaurant_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_rating=restaurant_rating
    def describe_restaurant(self):
        return "Название ресторана: %s, Тип кухни: %s, Рейтинг: %s" % (self.restaurant_name, self.cuisine_type,self.restaurant_rating)
    def open_restaurant(self):
        return "Ресторан открыт"
    def reit(self):
        rei=input("Введите рейтинг ресторана:")
        self.restaurant_rating = rei
        return "Актуальный рейтинг ресторана: %s" % (rei)


if __name__ == "__main__":
    r = Restaurant("Буше", "французская","4 звезды")
    m = Restaurant("Тайгер Лили", "Китайская", "5 звезд")
    j = Restaurant("Джеки Чан", "Паназиатская", "3 звезды")
    print(r.describe_restaurant())
    print(r.open_restaurant())
    print(r.reit())
    print(m.describe_restaurant())
    print(m.open_restaurant())
    print(m.reit())
    print(j.describe_restaurant())
    print(j.open_restaurant())
    print(j.reit())

