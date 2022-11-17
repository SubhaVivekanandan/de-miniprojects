from main import get_productList, get_courierList, get_orderList, save_products_file, save_orders_file, save_couriers_file

# Positive tests
def test_get_product_List():
    expected = {'name': 'Coke Zero','price': '0.8'}
    actual = get_productList()
    assert expected in actual
    
def test_get_courier_List():
    expected = {'name': 'john', 'phone_number': '0789887334'}
    actual = get_courierList()
    assert expected in actual
    
def test_get_order_List():
    expected = {'courier': '1', 'customer_address': '12Street', 'customer_name': 'John', 'customer_phone': '7898858', 'items':'1', 'status':'preparing'}
    actual = get_orderList()
    assert expected in actual
    
def test_save_product_csv_file():
    expected = True
    actual = save_products_file()
    assert actual == expected
    
def test_save_courier_csv_file():
    expected = True
    actual = save_couriers_file()
    assert actual == expected
    
def test_save_order_csv_file():
    expected = True
    actual = save_orders_file()
    assert actual == expected

# Negative tests
def test_not_in_product_List():
    expected = {'name': 'Coke Nt there','price': '0.8'}
    actual = get_productList()
    assert not expected in actual
    
def test_not_in_courier_List():
    expected = {'name': 'Subha', 'phone_number': '0789887334'}
    actual = get_courierList()
    assert not expected in actual
    
def test_not_in_order_List():
    expected = {'courier': '1', 'customer_address': '12Street', 'customer_name': 'Subha', 'customer_phone': '7898858', 'items':'1', 'status':'preparing'}
    actual = get_orderList()
    assert not expected in actual
