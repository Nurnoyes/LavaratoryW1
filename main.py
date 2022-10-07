import json
import random
import xml.etree.ElementTree as ET


class MenuReader:
    def write(self,data, filename):
        data = json.dumps(data)
        data = json.loads(str(data))
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    def read(self,filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
data = {
    "TheMenu": [],
    "totalsum" : []
}
class Food:
    def __init__(self, name='',price=0,portion=0):
        self.price = price
        self.portion = portion
        self.name = name
    price = 0
    portion = ''
    name = ''
    def setFood(self, price, portion, name):
        self.price = price
        self.portion = portion
        self.name = name
class Drink:
    price = 0
    volume = 0.0
    name = ''
    alcohol = False

    def __init__(self,price=0,volume=0,name=0,alcohol=0):
        self.price = price
        self.volume = volume
        self.name = name
        self.alcohol = alcohol


    def setDrink(self, price, volume, name, alcohol):
        self.price = price;
        self.volume = volume;
        self.name = name;
        self.alcohol = alcohol;
TheDrinks = []
TheFood = []
class Menu:
    totalsum = 0;
    while (True):
        numofdrinks = input('Enter the amount of drinks which will be in the Menu: ')
        if numofdrinks.isdigit():
            numofdrinks = int(numofdrinks)
            break
        else:
            print("You didn't write an integer value. Please rewrite what is asked: ")
    while(True):
        numoffood = input('Enter the amount of food which will be in the Menu: ')
        if numoffood.isdigit():
            numoffood = int(numoffood)
            break
        else:
            print("You didn't write an integer value. Please rewrite what is asked: ")
    for i in range(numofdrinks):
        while(True):
            name = input('Enter the name of the drink: ')
            if name.isdigit():
                print("You didn't write a string , there is no such existing drink out there. Rewrite the name: ")
            else:
                name = str(name)
                break
        while (True):
            volume = input('Enter the volume of the drink: ')
            if volume.isdigit():
                volume = int(volume)
                break
            else:
                print("You didn't write an integer value. Please rewrite what is asked: ")
        while (True):
            price = input('Enter the price of the drink: ')
            if price.isdigit():
                price = int(price)
                break
            else:
                print("You didn't write an integer value. Please rewrite what is asked: ")
        alcohol = bool(input('If it has an alcohol, enter 1(else 0): '))

        obj = Drink(price, volume, name, alcohol).__dict__
        data['TheMenu'].append(obj)
        TheDrinks.append(obj)
    for i in range(numoffood):
        while (True):
            name = input('Enter the name of the food: ')
            if name.isdigit():
                print("You didn't write a string , there is no such existing food out there. Rewrite the name: ")
            else:
                name = str(name)
                break
        portion = int(input('Enter the portion of the food: '))
        price = int(input('Enter the price of the food: '))

        obj = Food(name,price,portion).__dict__
        data['TheMenu'].append(obj)
        TheFood.append(obj)
    def getSum(self):
        for i in range(len(data['TheMenu'])):
            self.totalsum += data['TheMenu'][i]['price'];
        data['totalsum'].append(self.totalsum)
        return self.totalsum
x = ET.Element('Order')
Firstp = Menu();
Firstp.getSum();
Firstperson = MenuReader();
Firstperson.write(data, 'data.json')
ourfile = Firstperson.read('data.json')

print("What do you want to order?We have:")
sum = 0
for i in TheDrinks:
        sum += 1
        print(str(sum) + '.' + str(i['name']) + " " + str(i['volume']) + " "+str(i['volume']))
while(True):
        thebuying = int(input('Enter what you want to buy(0 if nothing): '))
        if (thebuying == 0 or thebuying > sum) :
            break
        else:
            #y = ET.SubElement(x, (TheDrinks[thebuying-1]['name'] + " " + str(TheDrinks[thebuying-1]['price'])))
            y = ET.SubElement(x, (str(ourfile['TheMenu'][thebuying-1]['name']) + " "  + str(ourfile['TheMenu'][thebuying-1]['price'])))
            #data['TheMenu'].append(TheDrinks[thebuying-1])
            #totalsum += TheDrinks[thebuying-1]['price']
        agreement = str(input("Wanna order other drink?(Y if yes | N if No) "))
        if (agreement == 'Y'):
            continue
        else:
            sum = 0
            break
sum = 0
for i in TheFood:
        sum += 1
        print(str(sum) + "."+ str(i['name']) + ' potrion: ' + str(i['portion']) + ' price: ' +str(i['price']))
while (True):
        thebuying = int(input('Enter what you want to buy(0 if nothing): '))
        if (thebuying == 0 or thebuying > sum):
            break;
        else:
            y = ET.SubElement(x, (TheFood[thebuying - 1]['name'] + " " + str(TheFood[thebuying - 1]['price'])))
            #data['TheMenu'].append(TheFood[thebuying - 1])
            #totalsum += TheFood[thebuying-1]['price']
        agreement = str(input("Wanna order other drink?(Y if yes | N if No) "))
        if (agreement == 'Y'):
            continue
        else:
            #data['totalsum'].append(totalsum)
            break







print(Firstperson.read('data.json'))
ET.dump(x)
tree = ET.ElementTree(x)
tree.write("sample.xml")
