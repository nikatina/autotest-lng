def test_adding_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    adding_btn = browser.find_element_by_css_selector(".btn-add-to-baskett")
    assert adding_btn.text, f"Add to basket button is not exist"
