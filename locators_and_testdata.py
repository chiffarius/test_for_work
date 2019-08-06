# instantiate an empty dict
context_data = {"users": {}, "test_data": {}, "locator": {}}

# Users for tests (login,password,ability to authenticate successfully)
context_data["users"][1] = ("negativeguy", "notrightpassword", False)
context_data["users"][2] = ("mipasudaru@armail.in", "testuser101", True)

# Test_data
context_data["test_data"]["testlink"] = "https://vk.com"

context_data["test_data"]["not_real_name"] = "1324"
context_data["test_data"]["real_name"] = "John"
context_data["test_data"]["not_real_surname"] = "1324"
context_data["test_data"]["real_surname"] = "Smith"


context_data["test_data"]["facebook_url_login"] = "https://www.facebook.com/login"
# Locators by XPath
context_data["locator"]["index_header"] = "//div[@id='page_header']"

context_data["locator"]["index_footer"] = "//div[@id='index_footer_wrap']"
context_data["locator"][
    "index_footer_about_left"] = "//div[@id='index_footer_wrap']/div[@id='bottom_nav']/div[@class='footer_copy fl_l']/a"
context_data["locator"]["index_footer_about_centre"] = "//div[@id='index_footer_wrap']//a[@class='bnav_a'][1]"
context_data["locator"]["index_footer_terms"] = "//div[@id='index_footer_wrap']//a[@class='bnav_a'][3]"
context_data["locator"]["index_footer_ads"] = "//div[@id='index_footer_wrap']//a[@class='bnav_a'][4]"
context_data["locator"]["index_footer_dev"] = "//div[@id='index_footer_wrap']//a[@class='bnav_a'][5]"

context_data["locator"]["index_english_language"] = "//div[@id='index_footer_wrap']//a[@class='footer_lang_link'][1]"
context_data["locator"]["index_russian_language"] = "//div[@id='index_footer_wrap']//a[@class='footer_lang_link'][2]"
context_data["locator"]["index_ukrainian_language"] = "//div[@id='index_footer_wrap']//a[@class='footer_lang_link'][3]"
context_data["locator"]["index_additional_language"] = "//div[@id='index_footer_wrap']//a[@class='footer_lang_link'][4]"
context_data["locator"]["index_all_language_selector"] = "//div[@id='index_footer_wrap']" \
                                                         "//a[@class='footer_lang_link'][contains(@onclick,'vk.al')]"

context_data["locator"]["vk_for_android_button"] = "//a[@class='LoginMobilePromoDevice LoginMobilePromoDevice--android " \
                                                   "LoginMobilePromoDevice--ru']/span[" \
                                                   "@class='LoginMobilePromoDevice__button flat_button " \
                                                   "secondary button_light'] "
context_data["locator"]["vk_for_ios_button"] = "//a[@class='LoginMobilePromoDevice LoginMobilePromoDevice--ios " \
                                               "LoginMobilePromoDevice--ru']/span[" \
                                               "@class='LoginMobilePromoDevice__button flat_button " \
                                               "secondary button_light'] "
context_data["locator"]["all_products"] = "//a[@class='login_all_products_button']"

context_data["locator"]["link_to_index_on_header_icon"] = "//a[@class='top_home_link fl_l']"
context_data["locator"]["search_bar"] = "//input[@id='ts_input']"
context_data["locator"]["switch_to_english"] = "//a[@id='top_switch_lang']"

context_data["locator"]["index_login"] = "//form[@id='index_login_form']"
context_data["locator"]["index_login_email"] = "//input[@id='index_email']"
context_data["locator"]["index_login_password"] = "//input[@id='index_pass']"
context_data["locator"]["index_login_button"] = "//button[@id='index_login_button']"
context_data["locator"]["index_login_forgot_password"] = "//a[@id='index_forgot']"

context_data["locator"]["index_registration_form"] = "//div[@id='ij_form']"
context_data["locator"]["index_registration_form_name"] = "//input[@id='ij_first_name']"
context_data["locator"]["index_registration_form_surname"] = "//input[@id='ij_last_name']"
context_data["locator"]["index_registration_form_day"] = "//td[@id='dropdown1']"
context_data["locator"]["index_registration_form_day_value"] = "//li[@id='option_list_options_container_1_7']"
context_data["locator"]["index_registration_form_month"] = "//td[@id='dropdown2']"
context_data["locator"]["index_registration_form_month_value"] = "//li[@id='option_list_options_container_2_7']"
context_data["locator"]["index_registration_form_year"] = "//td[@id='dropdown3']"
context_data["locator"]["index_registration_form_year_value"] = "//li[@id='option_list_options_container_3_7']"
context_data["locator"]["index_registration_form_sex_female"] = "//div[@id='ij_sex_row']/div[@class='radiobtn'][1]"
context_data["locator"]["index_registration_form_sex_male"] = "//div[@id='ij_sex_row']/div[@class='radiobtn'][2]"
context_data["locator"]["index_registration_form_submit"] = "//button[@id='ij_submit']"
context_data["locator"]["index_registration_form_facebook_login"] = "//div[@class='fb-login-button " \
                                                                    "index_fb_continue_with_btn fb_iframe_widget'] "
context_data["locator"]["index_registration_form_name_error"] = "//div[@class='tt_w ij_tt tt_right'][1]" \
                                                                "/div[@class='wrapped']/div[@class='tt_text']"
context_data["locator"]["index_registration_form_surname_error"] = "//div[@class='tt_w ij_tt tt_right'][1]" \
                                                                "/div[@class='wrapped']/div[@class='tt_text']"
context_data["locator"]["index_registration_form_date_error"] = "//div[@class='tt_w ij_tt tt_right'][1]" \
                                                               "/div[@class='wrapped']/div[@class='tt_text']"
context_data["locator"]["index_registration_form_sex_error"] = "//div[@class='tt_w ij_tt tt_right'][1]" \
                                                               "/div[@class='wrapped']/div[@class='tt_text']"