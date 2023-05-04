import json
def n1():
    with open('prod.json', encoding='utf-8') as f:
        prod = json.load(f)
        for p in prod['products']:
            print('Название: ' + p['name'])
            print('Цена: ' + str((p['price'])))
            print('Вес: ' + str(p['weight']))
            if (p['available']) == True:
                print("В Наличии")
            else:
                print("Нет в наличии!")
        a=input("Хотите ли вы что-нибудь добавить в БД?: ")
        if a=="Да":
            name=input("Введите название продукта: ")
            price=int(input("Введите цену продукта: "))
            weight= int(input("Введите вес продукта: "))
            availabl=input("Продукт есть в наличии?: Да или Нет. ")
            if availabl == "Да":
                available = True
            else:
                available=False
            new_product = {"name": name , "price": price,
                           "weight": weight,
                           "available": available}
            with open('prod.json', encoding='utf-8') as f:
                prod = json.load(f)
                prod['products'].append(new_product)
            with open('prod.json', 'w', encoding='utf8') as outfile:
                json.dump(prod, outfile, ensure_ascii=False, indent=2)
        if a=="Нет":
            print("Спасибо")
n1()

def n2():
    f=open('en-ru.txt','r',encoding='utf-8').readlines()
    nf = open("ru-en.txt", "w+")
    for i in f:
        rus=i.split(' - ')
        n=len(rus[1])
        n=n-1
        nf.write(rus[1][:n] + ' - ' + rus[0] + '\n')
    lines = sorted(nf.readlines())
    print(lines)
    for line in lines:
        print(line)
        #nf.write(line)
n2()