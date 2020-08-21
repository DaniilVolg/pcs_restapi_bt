def test_amazon_items(py):
    py.visit("https://www.amazon.com/")
    py.get("#twotabsearchtextbox").type("headphones").submit()
    py.getx("//div[@class='rush-component']//div[@class='rush-component']//span[@class='a-size-medium a-color-base a-text-normal'][contains(text(),'COWIN E7 Active Noise Cancelling Headphones Blueto')]").click()
    #locator for item field
    assert_field = py.getx("//span[@id='productTitle']")
    #locator for price field
    assert_price = py.getx("//span[@id='price_inside_buybox']")
    #assertion part
    assert_field.should().contain_text("COWIN E7 Active Noise Cancelling Headphones Bluetooth Headphones with Microphone Deep Bass Wireless Headphones Over Ear, Comfortable Protein Earpads, 30 Hours Playtime for Travel/Work, Black")
    assert_price.should().contain_text("$50.99")
