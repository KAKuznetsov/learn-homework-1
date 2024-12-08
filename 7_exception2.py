"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """ 
    try:
        price = float(price)
    except ValueError:
        print("Цену необходимо вводить с помщью цифр, а не словами")
    
    try:
        discount = float(discount)
    except ValueError:
        print("Размер скидки необходимо вводить с помщью цифр, а не словами")
    
    try:
        max_discount = int(max_discount)
    except ValueError:
        print("Размер максимальной скдики необходимо вводить с помщью цифр, а не словами")
    
    try:
        if max_discount >= 100:
            raise ValueError ("Максимальная скидка не должна быть больше 100 ")
    except TypeError:
        print("Невозможно сравнить данные разных типов, проверьте значения переданные в функцию, проверьте значение максимальной скидки")

    try:
        if discount >= max_discount:
            price_with_discount = price
        else:
            try:
                price_with_discount = price - (price * discount/ 100)
            except TypeError:
                print("Не могу Рассчитать цену со скидкой, проверьте введенные значения, являются ли они числами")
    except TypeError:
        print("Невозможно сравнить данные разных типов, проверьте значения переданные в функцию")
    
    # try:
    #     if isinstance(price_with_discount, str) is True:
    #         price_with_discount = None
    # except UnboundLocalError:
    #     print("Не удалось рассчитать цену без скидки, проверьте введенные значения")

    
    try:
        return price_with_discount
    except UnboundLocalError:
        print("Не удалось рассчитать цену без скидки, проверьте введенные значения")

    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
    print(discounted("сто", "десять",  "десять"))
    print(discounted(100, 5,  "десять"))