from selenium import common


def check_exists_by_css(browser, css_sel):
    try:
        browser.find_element_by_css_selector(css_sel)
    except common.exceptions.NoSuchElementException:
        return False
    return True


def test_adding_button_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    is_elem_exist = check_exists_by_css(browser, ".btn-add-to-basket")
    assert is_elem_exist is True, "'Add to basket' button is not exist"
