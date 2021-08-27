import requests
from bs4 import BeautifulSoup
Products_to_track =[
    {
        "Product_URL":"https://www.amazon.in/Redmi-Note-Frost-White-Storage/dp/B0948NV5PH/ref=sr_1_17?crid=2NCTA4C6TLFQA&dchild=1&keywords=mobile+phones+under+15000&qid=1629977878&sprefix=mobile%2Caps%2C427&sr=8-17",
        "name":"RedmiNote",
        "target_price":16000
    },
    {
        "Product_URL":"https://www.amazon.in/Samsung-Galaxy-Storage-Triple-Camera/dp/B08RSY2653/ref=sr_1_15?crid=2NCTA4C6TLFQA&dchild=1&keywords=mobile+phones+under+15000&qid=1629977878&sprefix=mobile%2Caps%2C427&sr=8-15",
        "name":"Samsung_Galaxy",
        "target_price":11000
    },
    {
        "Product_URL":"https://www.amazon.in/Nokia-G20-Smartphone-4G-Storage/dp/B0986MQRFB/ref=sr_1_1_sspa?crid=2NCTA4C6TLFQA&dchild=1&keywords=mobile+phones+under+15000&qid=1629977878&sprefix=mobile%2Caps%2C427&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzWVhYVlRZUjlaVUMmZW5jcnlwdGVkSWQ9QTA1MjE5MDExSkdIS1FTV05LTVdHJmVuY3J5cHRlZEFkSWQ9QTA1NDYwNzEzQlZBWlVGMzlNRk1MJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
        "name":"Nokia_G20",
        "target_price":11000
    },
    {
        "Product_URL":"https://www.amazon.in/realme-narzo-Racing-128GB-Storage/dp/B099SJHHQL/ref=sr_1_20?crid=2NCTA4C6TLFQA&dchild=1&keywords=mobile+phones+under+15000&qid=1629977878&sprefix=mobile%2Caps%2C427&sr=8-20",
        "name":"RealMe_Narzo",
        "target_price":15000
    }
    
]
def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    Soup = BeautifulSoup(page.content, 'html.parser')
    Product_price = Soup.find(id="priceblock_dealprice")
    if (Product_price == None):
        Product_price = Soup.find(id="priceblock_ourprice")

    return Product_price.getText()

result_file= open('my_result_file.text','w')

try:
    for every_product in Products_to_track:
        returned_product_price = give_product_price(every_product.get("Product_URL"))
        print(returned_product_price + every_product.get("name"))

        my_product_price = returned_product_price[1:]
        my_product_price = my_product_price.replace(",", "")
        my_product_price = float(my_product_price)
        my_product_price = int(my_product_price)

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name")+'=='+'Available at target price--'+'Current price---'+str(my_product_price)+'\n')
        else:
            print("Still at current price")

finally:
    result_file.close()
