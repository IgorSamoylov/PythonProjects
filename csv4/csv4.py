

from collections import namedtuple

with open('input_6_3_4.csv', 'r', encoding='utf-8') as f:
    product_names = f.readline().split(';')
    product_names.remove('')
    print(product_names)
    market_and_prices = f.readlines()
    result_products_list = []
    for price in market_and_prices:
        price_str = price.split(';')
        prices_list = price_str[1:-1] + [int(price_str[-1])]
        result_prod_prices = []
        for index, price in enumerate(prices_list):
            #breakpoint()
            #n_tuple = namedtuple('ProductPrices', 'Название продукта стоимость')
            result_prod_prices.append((product_names[index], price))

        result_prod_prices.sort(key=lambda tup: tup[0], reverse=False)
        
        result_products_list.append((price_str[0], result_prod_prices))
    result_products_list.sort(key=lambda tup: tup[0], reverse=False)
    print(result_products_list)

    min_price = 2_000_000
    min_name = ''
    min_market = ''
    for record in result_products_list:
        print('\n\n', record[0], '\n')
        for product_price in record[1]:
            print(product_price[0], product_price[1])
            if int(product_price[1]) < min_price:
                min_price = int(product_price[1])
                min_name = product_price[0]
                min_market = record[0]
    
    print(min_name, min_market)
    


