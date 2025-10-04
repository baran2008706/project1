import sqlite3
import datetime

conn = sqlite3.connect()
cursor = conn.cursor()

while True:
    user_entry = int(input("""entry(1:new product registration,
    2:edit product information,
    3:new costumer registration,
    4:edit costumer information,
    5:show list of all products,
    6:show list of all costumers,
    7:exit):
    """))

    if user_entry == 1:
        n_name = input("enter the new products name: ")
        n_price = int(input("enter the new products price: "))
        n_number = int(input("enter how many of the new product you have: "))
        n_category = input("enter which category the new product is in: ")
        cursor.execute("INSERT INTO product(name, price, number, category) VALUES(?, ?, ?, ?)",
                       (n_name, n_price, n_number, n_category))
        conn.commit()
        print("product added successfully")

    if user_entry == 2:
        product_id = int(input("enter the id of the product you want to update: "))
        u_name = input("enter the new name of the product:")
        u_price = int(input("enter the new price for the product: "))
        u_number = int(input("enter how many of the product you have: "))
        u_category = input("enter the category the product is in: ")
        cursor.execute("UPDATE product SET name = ?, price = ?, number = ?, category = ? WHERE id = ?",
                       (u_name, u_price, u_number, u_category, product_id))
        conn.commit()
        print("product updated successfully")

    if user_entry == 3:
        new_city = int(input("enter which city the new costumer lives at: "))
        new_birth_date = input("enter the new costumers birth date(yyyy-mm-dd): ")
        new_phone_number = input("enter the new costumers phone number: ")
        new_name = input("enter the new costumers name: ")
        cursor.execute("INSERT INTO costumer(city, birth_date, phone_number, name) VALUES(?, ?, ?, ?)",
                       (new_city, new_birth_date, new_phone_number, new_name))
        conn.commit()
        print("costumer added successfully")

    if user_entry == 4:
        costumer_id = int(input("enter the id of the costumer you want to update: "))
        up_city = int(input("enter which city the costumer lives in: "))
        up_birth_date = input("enter the costumers birthday(yyyy-mm-dd): ")
        up_phone_number = input("enter the costumers new phone number: ")
        up_name = input("enter the costumers name: ")
        cursor.execute("UPDATE costumer SET city = ?, birth_date = ?, phone_number = ?, name = ?, WHERE id = ?",
                       (up_city, up_birth_date, up_phone_number, up_name, costumer_id))
        conn.commit()
        print("costumer updated successfully")

    if user_entry == 5:
        cursor.execute("SELECT * FROM product")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    if user_entry == 6:
        cursor.execute("SELECT * FROM  costumer")
        rows = cursor.fetchall()
        for row in rows:
            print(rows)

    if user_entry == 7:
        break
