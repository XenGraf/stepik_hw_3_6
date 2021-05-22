import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contain_add_to_basket_btn(browser):
    browser.get(link)
    time.sleep(30)
    basket_btn = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert basket_btn, "No such element"
