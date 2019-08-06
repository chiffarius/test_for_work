import allure
import driver_commands as dc
import time



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


@allure.title("registration form follow-up")
def test_continue_registration(driver, data_bag):
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
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_sex_female"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_submit"])
    time.sleep(1)
    url = driver.current_url
    dc.uielement_click(driver, data_bag["locator"]["index_registration_return_to_index_page"])
    assert "https://vk.com/join?act=finish" in url


@allure.title("change language to English with a shortcut in top-right corner")
def test_change_to_english(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["change_language_to_english"])
    assert "VK for mobile devices" in dc.element_text(driver, data_bag["locator"]["login_mobile_header"])


@allure.title("extra validation on index page registration form for name")
def test_more_name_validation_at_registration(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_name"],
                        data_bag["test_data"]["not_quite_real_name"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_surname"],
                        data_bag["test_data"]["real_surname"])
    dc.dropdown_choose_value(driver, data_bag["locator"]["index_registration_form_day"],
                             data_bag["locator"]["index_registration_form_day_value"])
    dc.dropdown_choose_value(driver, data_bag["locator"]["index_registration_form_month"],
                             data_bag["locator"]["index_registration_form_month_value"])
    dc.dropdown_choose_value(driver, data_bag["locator"]["index_registration_form_year"],
                             data_bag["locator"]["index_registration_form_year_value"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_submit"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_sex_female"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_submit"])
    time.sleep(2)
    driver.delete_all_cookies()
    assert "join?act=finish" not in driver.current_url

@allure.title("extra validation on index page registration form for surname")
def test_more_surname_validation_at_registration(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_name"],
                        data_bag["test_data"]["real_name"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_registration_form_surname"],
                        data_bag["test_data"]["not_quite_real_surname"])
    dc.dropdown_choose_value(driver, data_bag["locator"]["index_registration_form_day"],
                             data_bag["locator"]["index_registration_form_day_value"])
    dc.dropdown_choose_value(driver, data_bag["locator"]["index_registration_form_month"],
                             data_bag["locator"]["index_registration_form_month_value"])
    dc.dropdown_choose_value(driver, data_bag["locator"]["index_registration_form_year"],
                             data_bag["locator"]["index_registration_form_year_value"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_submit"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_sex_female"])
    dc.uielement_click(driver, data_bag["locator"]["index_registration_form_submit"])
    time.sleep(2)
    driver.delete_all_cookies()
    assert "join?act=finish" not in driver.current_url

@allure.title("sex selector is visible on the page on russian version")
def test_sex_selector_in_russian_version(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver,data_bag["locator"]["index_russian_language"])
    assert dc.element_visible(driver,data_bag["locator"]["index_registration_form_sex_female"])


@allure.title("link for forget password lead to restore password page")
def test_forgot_password_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uielement_click(driver, data_bag["locator"]["index_login_forgot_password"])
    assert dc.compare_current_url(driver, str(data_bag["test_data"]["testlink"] + "/restore"))

@allure.title("testing failed quick login attempt leading to separate login page")
def test_failed_login_to_separate_login_screen(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uifield_sendkeys(driver,data_bag["locator"]["index_login_email"],data_bag["users"][1][0])
    dc.uifield_sendkeys(driver, data_bag["locator"]["index_login_password"], data_bag["users"][1][1])
    dc.uielement_click(driver, data_bag["locator"]["index_login_button"])
    assert dc.compare_current_url(driver, "https://vk.com/login")

@allure.title("test search functionality")
def test_footer_dev_link(driver, data_bag):
    dc.driver_get(driver, data_bag["test_data"]["testlink"])
    dc.uifield_sendkeys(driver, data_bag["locator"]["search_bar"],"verycommonsearchterm")
    dc.uifield_sendkeys(driver, data_bag["locator"]["search_bar"],u'\ue007')
    assert dc.compare_current_url(driver, str(data_bag["test_data"]["testlink"] + "/search"))

