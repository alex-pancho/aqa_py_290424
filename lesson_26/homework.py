import requests

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"


xpath_1 = '//*[name()='path' and contains(@d,'M26.25 29.')]'
xpath_2 = '//*[name()='path' and contains(@d,'M44.4548 2')]'
xpath_3 = '//p[@class='hero-descriptor_descr lead']'
xpath_4 = '//button[@class='hero-descriptor_btn btn btn-primary']'
xpath_5 = '//div[@class='col-12 col-lg-8']'
xpath_6 = '//section[@class='section hero']'
xpath_7 = '//button[@title='Смотреть']'
xpath_8 = '//div[@class='ytp-title-text']'
xpath_9 = '//div[@class='ytp-share-icon']'
xpath_10 = '//div[@class='ytp-watch-later-title']'
xpath_11 = '//div[@class='ytp-cued-thumbnail-overlay-image']'
xpath_12 = '//button[@class='btn btn-outline-white header_signin']'
xpath_13 = '//button[@class='header-link -guest']'
xpath_14 = '//button[normalize-space()='Contacts']'
xpath_15 = '//div[@class='header_inner d-flex justify-content-between align-items-center']'
xpath_16 = '//div[@id='aboutSection']'
xpath_17 = '//p[normalize-space()='Log fuel expenses']'
xpath_18 = '//p[contains(text(),'Keep track of your replacement schedule and plan y')]'
xpath_19 = '//div[@class='col-12 col-lg-6 mt-lg-0 mt-md-5 mt-sm-4 mt-3']//img[@alt='Instructions']'
xpath_20 = '//p[normalize-space()='Instructions and manuals']'
xpath_21 = '//p[contains(text(),'Watch over 100 instructions and repair your car yo')]'
xpath_22 = '//div[class='col-md-6 d-flex flex-column align-items-center align-items-md-start'] h2'
xpath_23 = '//p[contains(text(),'Watch over 100 instructions and repair your car yo')]'
xpath_24 = '//span[@class='socials_icon icon icon-facebook']'
xpath_25 = '//span[@class='socials_icon icon icon-instagram']'
xpath_26 = '//span[@class='socials_icon icon icon-linkedin']'
xpath_27 = '//span[@class='socials_icon icon icon-telegram']'
xpath_28 = '//span[@class='socials_icon icon icon-youtube']'
xpath_29 = '//a[@class='contacts_link display-4']'
xpath_30 = '//a[@class='contacts_link h4']'
xpath_31 = '//div[@id='contactsSection']'
xpath_32 = '//div[@class='col-md-6 d-flex flex-column align-items-center align-items-md-end justify-content-md-end mb-2 mt-3 mt-md-0']'
xpath_33 = '//div[@class='col-md-6 d-flex flex-column align-items-center align-items-md-start']'
xpath_34 = '//footer[@class='footer d-flex align-items-center']'
xpath_35 = '//div[@class='col footer_item -right']'
xpath_36 = '//*[name()='path' and contains(@d,'M16.8847 6')]'
xpath_37 = '//div[@class='col-7 d-flex flex-column justify-content-center footer_item -left']'
xpath_38 = '//p[normalize-space()='© 2021 Hillel IT school']'
xpath_39 = '//p[contains(text(),'Hillel auto developed in Hillel IT school for educ')]'
xpath_40 = '//div[@class='ytp-watch-later-icon']'
xpath_41 = '//div[@class='ytp-share-title']'
xpath_42 = '//p[contains(text(), 'With the help of the Hillel auto project, you will have the opportunity to get hands-on experience in manual testing.')]'
xpath_43 = '//p[contains(@class, 'hero-descriptor_descr') and contains(@class, 'lead') and text()='With the help of the Hillel auto project, you will have the opportunity to get hands-on experience in manual testing.']'
xpath_44 = '//p[contains(@class, 'about-block_descr') and contains(@class, 'lead') and text()='Keep track of your replacement schedule and plan your vehicle maintenance expenses in advance.']'
xpath_45 = '//p[contains(@class, 'about-block_descr') and contains(@class, 'lead') and text()='Watch over 100 instructions and repair your car yourself.']'
xpath_46 = '//p[contains(@class, 'about-block_title') and contains(@class, 'h2') and text()='Instructions and manuals']'
xpath_47 = '//p[contains(@class, 'about-block_title') and contains(@class, 'h2') and text()='Log fuel expenses']'
xpath_48 = '//button[contains(@class, 'hero-descriptor_btn') and contains(@class, 'btn-primary') and text()='Sign up']'
xpath_49 = '//button[contains(@class, 'btn btn-outline-white') and contains(@class, 'header_signin') and text()='Sign In']'
xpath_50 = '//button[contains(@class, 'header-link') and contains(@class, 'guest') and text()='Guest log in']'