import pymysql
from thefuzz import process

from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected")
    try:
        # подключаемся к бд
        with connection.cursor() as cursor:
            # Достаем все бренды из БД
            select_all_brands = "SELECT brand_id, name FROM brandnames"
            cursor.execute(select_all_brands)
            brands = cursor.fetchall()
            # Проходимся по брендам в цикле
            for brand in brands:
                brand_id = brand['brand_id']
                brand_name = brand['name']
                # Достаем из бд все продукты яндекс маркета которые свзяны с брендом
                product_brand_yandex = f"SELECT id, name FROM products WHERE brand_id = {brand_id} AND marketplace_id = 1"
                cursor.execute(product_brand_yandex)
                products_yandex = cursor.fetchall()

                # Достаем из бд все продукты wildberries которые свзяны с брендом
                product_brand_wildberries = f"SELECT id, name FROM products WHERE brand_id = {brand_id} AND marketplace_id = 2"
                cursor.execute(product_brand_wildberries)
                products_wildberries = cursor.fetchall()
                # Создаем список имен продуктов wildberries для работы библиотеки thefuzz, так как на вход она принимает список
                product_name = [product['name'] for product in products_wildberries]

                # Проходимся по продуктам яндекс маркета
                for product_y in products_yandex:
                    # Ищем совпадание с помощью библиоткеи thefuzz, на вход идет товар яндекс маркета, список товаров wildberries которые относятся к этому бренду
                    a = process.extractOne(product_y['name'], product_name)
                    # Если совпадение на 90 % и более то
                    if a[1] >= 90:
                        # проходися по списку продуктов wildberries
                        for product_wb in products_wildberries:
                            # Если имя продукта равно тому которе записано в а[0] (в а[0] записано имя продукта которое совпало )
                            if product_wb['name'] == a[0]:
                                # Печатаем результат product_y - продукт яндекса, product_wb - продукт wildberries
                                print(
                                    f"id: {product_y['id']}  name: {product_y['name']} == id: {product_wb['id']}  name: {product_wb['name']}")
                                break
    finally:
        connection.close()



except Exception as ex:
    print("Connection error")
    print(ex)
