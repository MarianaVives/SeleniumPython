from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    driver = browserInstance;
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers");
    driver.maximize_window();
    driver.implicitly_wait(
        5);  # if any element is not shown in the page it will wait a max for that element to show up.
    print("Title: " + driver.title);
    print("URL: " + driver.current_url);

    items = [];
    prices = [];
    discount_price = [];
    header_index = 0;
    headers_list = driver.find_elements(By.CSS_SELECTOR, "thead tr th");
    driver.find_element(By.CSS_SELECTOR, "thead tr th:nth-child(1)").click();
    print("Successfully sorted in Ascending Order");
    print(len(headers_list));
    for h in headers_list:
        header_index = header_index + 1;
        item_li = driver.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(" + str(header_index) + ")");
        for i in item_li:
            if header_index == 1:
                items.append(i.text);
                print(i.text)
            elif header_index == 2:
                prices.append(i.text);
                print(i.text)
            else:
                discount_price.append(i.text);
                print(i.text)
    browser_items_sorted_list = items;
    browser_prices_sorted_list = prices;
    browser_discount_prices_sorted_list = discount_price;
    items.sort();
    prices.sort();
    discount_price.sort();
    assert browser_items_sorted_list == items;
    assert browser_prices_sorted_list == prices;
    assert browser_discount_prices_sorted_list == discount_price;
    print("Successfully validated that items are sorted correctly.");