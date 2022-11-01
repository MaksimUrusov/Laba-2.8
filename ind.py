#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys


def get_shop():
    """""
    Запросить данные о продукте.
    """""
    shop = input("Магазин: ")
    product = input("Название товара: ")
    cost = float(input("Стоимость товара: "))

    # Создать словарь
    return {
        'shop': shop,
        'product': product,
        'cost': cost,
    }


def display_shops(shops):
    """""
    Отобразить список работников
    """""
    # Проверить что список работников не пуст
    if shops:
        # Заголовок таблицы
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Магазин",
                "Товар",
                "Стоимость товара"
            )
        )
        print(line)

        for idx, shops in enumerate(shops, 1):
            print(
                '| {:^4} | {:<30} | {:<20} | {:<15} |'.format(
                    idx,
                    shops.get('shop', ''),
                    shops.get('product', ''),
                    round(shops.get('cost', ''), 2),
                    ' ' * 5
                )
            )

        print(line)

    else:
        print("Список магазинов пуст. Дабавить новый магазин")
        shop = get_shop()
        shops.append(shop)

        if len(shops) > 1:
            shops.sort(key=lambda d: d.get('shop', ''))


def select_shop(shops, addedtovar):
    """""
    Выбрать необходимый Магазин
    """""
    result = [shop for shop in shops if shop.get('shop', '') == addedtovar]
    return result


def main():
    """""
    Главная функция программы
    """""
    print("help - список всех команд")
    # Список магазинов
    shops = []

    # Организовать бесконечный цикл запроса команд
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            shop = get_shop()
            shops.append(shop)

            if len(shops) > 1:
                shops.sort(key=lambda d: d.get('shop', ''))

        elif command == 'list':
            display_shops(shops)

        elif command == 'select':
            print("Введите магазин, информацию о котором хотите получить: ")
            tov = input()
            selected = select_shop(shops, tov)
            display_shops(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить магазин;")
            print("list - вывести список магазинов;")
            print("select - запросить информацию о магазине;")
            print("help - вывести список команд;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная комманда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
