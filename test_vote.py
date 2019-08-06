import allure
import driver_commands as dc


@allure.title("registration form name error")
def test_name_error_on_registration(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_name"],
                        data_bag["test_data"]["not_real_name"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_surname"],
                        data_bag["test_data"]["real_surname"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_submit"])
    assert dc.element_visible(driver, data_bag["locator"]["index_registration_form_name_error"])


@allure.title("registration form surname error")
def test_surname_error_on_registration(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_name"],
                        data_bag["test_data"]["real_name"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_surname"],
                        data_bag["test_data"]["not_real_surname"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_submit"])
    assert dc.element_visible(driver, data_bag["locator"]["index_registration_form_surname_error"])


@allure.title("registration form date error")
def test_date_error_on_registration(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_name"],
                        data_bag["test_data"]["real_name"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_surname"],
                        data_bag["test_data"]["real_surname"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_submit"])
    assert dc.element_visible(driver, data_bag["locator"]["index_registration_form_date_error"])


@allure.title("registration form sex error")
def test_sex_error_on_registration(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_name"],
                        data_bag["test_data"]["real_name"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_surname"],
                        data_bag["test_data"]["real_surname"])
    dc.dropdown_choose_value(driver, data_bag["locator"]["index_registration_form_day"],
                             data_bag["locator"]["index_registration_form_day_value"])
    dc.dropdown_choose_value(driver, data_bag["locator"]["index_registration_form_month"],
                             data_bag["locator"]["index_registration_form_month_value"])
    dc.dropdown_choose_value(driver, data_bag["locator"]["index_registration_form_year"],
                             data_bag["locator"]["index_registration_form_year_value"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_submit"])
    assert dc.element_visible(driver, data_bag["locator"]["index_registration_form_sex_error"])


@allure.title("check for link on left side to lead to about page")
def test_left_about_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["index_footer_about_left"])
    assert dc.compare_current_url(driver, str(data_bag["test_data"]["testlink"] + "/about"))


@allure.title("check for link on centre to lead to about page")
def test_centre_about_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["index_footer_about_centre"])
    assert dc.compare_current_url(driver, str(data_bag["test_data"]["testlink"] + "/about"))


@allure.title("check for link to lead to terms")
def test_footer_terms_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["index_footer_terms"])
    assert dc.compare_current_url(driver, str(data_bag["test_data"]["testlink"] + "/terms"))


@allure.title("check for link for ads lead to login page first")
def test_footer_ads_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["index_footer_ads"])
    assert dc.compare_current_url(driver, str(data_bag["test_data"]["testlink"] + "/login"))


@allure.title("check for link for developers lead to tools for developers")
def test_footer_dev_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["index_footer_dev"])
    assert dc.compare_current_url(driver, str(data_bag["test_data"]["testlink"] + "/dev"))


@allure.title("check for facebook login opens facebook's widget")
def test_registration_facebook_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_facebook_login"])
    url = dc.close_current_tab_and_save_url(driver)
    assert data_bag["test_data"]["facebook_url_login"] in url


@allure.title("check for link to lead to appstore")
def test_ios_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["vk_for_ios_button"])
    url = dc.close_current_tab_and_save_url(driver)
    assert "https://apps.apple.com/ru/app/id564177498" in url


@allure.title("check for link to lead to play store")
def test_android_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["vk_for_android_button"])
    url = dc.close_current_tab_and_save_url(driver)
    assert "https://play.google.com/store/apps/details?id=com.vkontakte.android" in url


@allure.title("check for link to lead to products")
def test_products_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["all_products"])
    assert dc.compare_current_url(driver, str(data_bag["test_data"]["testlink"] + "/products"))
