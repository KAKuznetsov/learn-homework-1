"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_age_text = input("Введите свой возраст: ")
    user_age_text_clean = user_age_text.replace(",", ".")
    user_age_text_float = float(user_age_text_clean)

    # print(user_age_text_clean)
    # print(type(user_age_text))
    # print(type(user_age_text_clean))
    # print(type(user_age_text_float))

    def type_of_task(age):
        if age < 0:
            return "Введите пожалуйста реальный возраст, больше нуля!"
        elif age < 7:
            return "Вам необходимо учиться в детском саду!"
        elif age < 17:
            return "Вам необходимо учиться в школе!"
        elif age < 23:
            return "Вам необходимо учиться в ВУЗе!" 
        else:
            return "Вам необходимо работать!"         

    user_result = type_of_task(user_age_text_float)
    print(user_result)


if __name__ == "__main__":
    main()
