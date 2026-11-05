import pandas as pd

books = {
    "Название": ["Python", "Java", "C++", "AI", "Django", "React"],
    "Автор": ["John", "Mike", "Alex", "David", "Tom", "Sam"],
    "Год издания": [2018, 2010, 2020, 2022, 2015, 2024],
    "Цена": [25, 30, 20, 40, 35, 28]
}

df = pd.DataFrame(books)

print("Все книги:")
print(df)

print("\nСредняя цена:")
print(df["Цена"].mean())

print("\nКниги после 2015 года:")
print(df[df["Год издания"] > 2015])

print("\nСортировка по цене:")
print(df.sort_values(by="Цена"))




orders = pd.read_csv("orders.csv")

print("\nПервые 10 заказов:")
print(orders.head(10))

print("\nКоличество заказов каждого клиента:")
print(orders["Клиент"].value_counts())

print("\nМаксимальная сумма:")
print(orders["Сумма"].max())

print("\nМинимальная сумма:")
print(orders["Сумма"].min())

print("\nОбщая сумма заказов:")
print(orders["Сумма"].sum())






products = {
    "Продукт": ["Мясо", "Рис", "Хлеб", "Рыба", "Сыр",
                "Яблоко", "Курица", "Орехи", "Молоко", "Картофель"],
    "Категория": ["Мясо", "Крупы", "Выпечка", "Мясо", "Молочные",
                  "Фрукты", "Мясо", "Орехи", "Молочные", "Овощи"],
    "Калории": [350, 130, 265, 200, 400, 52, 320, 600, 60, 80],
    "Белки": [25, 3, 9, 22, 25, 0, 31, 20, 3, 2]
}

df = pd.DataFrame(products)

print("\nВсе продукты:")
print(df)

print("\nПродукты с калорийностью выше 300:")
print(df[df["Калории"] > 300])

print("\nСреднее количество белков по категориям:")
print(df.groupby("Категория")["Белки"].mean())

print("\nСортировка по калорийности:")
print(df.sort_values(by="Калории", ascending=False))







employees = {
    "Имя": ["Ali", "Samir", "Elmar", "Ali", "Murad",
            "Elmar", "Samir", "Murad"],
    "Проект": ["Website", "AI", "Website", "Mobile",
               "AI", "Mobile", "Website", "AI"],
    "Часы": [10, 15, 20, 12, 18, 25, 10, 14]
}

df = pd.DataFrame(employees)

print("\nВсе сотрудники:")
print(df)

print("\nОбщее количество часов по сотрудникам:")
print(df.groupby("Имя")["Часы"].sum())

print("\nОбщее количество часов по проектам:")
print(df.groupby("Проект")["Часы"].sum())

print("\nСотрудник с наибольшим количеством часов:")
print(df.groupby("Имя")["Часы"].sum().idxmax())






tickets = {
    "Фильм": ["Avatar", "Batman", "Avatar", "Joker",
              "Batman", "Joker", "Avatar", "Batman",
              "Joker", "Avatar", "Batman", "Joker"],
    "Город": ["Baku", "Baku", "Ganja", "Sumgait",
              "Ganja", "Baku", "Sumgait", "Baku",
              "Ganja", "Ganja", "Sumgait", "Sumgait"],
    "Проданные билеты": [100, 150, 80, 120, 90, 110,
                         70, 130, 60, 95, 85, 140]
}

df = pd.DataFrame(tickets)

print("\nВсе продажи:")
print(df)

print("\nКоличество билетов по фильмам:")
print(df.groupby("Фильм")["Проданные билеты"].sum())

print("\nКоличество билетов по городам:")
print(df.groupby("Город")["Проданные билеты"].sum())

print("\nФильм с наибольшими продажами:")
print(df.groupby("Фильм")["Проданные билеты"].sum().idxmax())