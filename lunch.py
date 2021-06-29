# Файл  lunch.py

class Lunch:                 
    def __init__(self):                             #  Создать/внедрить Customer, Emloyee
        self.cust = Customer()
        self.emp1 = Employee()

    def order(self, foodName):                      # Начать эмуляцию заказа
                                                    # экземпляром Customer 
        self.cust.placeOrder(foodName, self.emp1)
    def result (self):                              # Запросить у экземпляра Customer
                                                    # название блюда
        self.cust.printFood()

class Customer:
    def __init__(self):                             # Инициализировать блюдо с помощью None
        self.food = None
    def placeOrder(self, foodName, employee):       # Разместить заказ для
                                                    # экземпляра Employee
        self.food = employee.takeOrder(foodName)
    def printFood(self):                            # Вывести название блюда
        print(self.food.name)

class Employee:
    def takeOrder(self, foodName):                  # Возвратить блюдо с желаемым названием
        return Food(foodName)

class Food:
    def __init__(self, name):                       # Сохранить название блюда
        self.name = name

if __name__ == '__main__':
    x = Lunch()                                     # Код самотестирования
    x.order('burritos')                             # Если запускается, не импортируется
    x.result()
    x.order('pizza')
    x.result()
    
    
