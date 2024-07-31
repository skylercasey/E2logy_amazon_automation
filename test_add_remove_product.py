
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains





def test_Login():
    options=Options()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.in/b/ref=surl_fashion/?_encoding=UTF8&node=6648217031&pd_rd_w=sC81d&content-id=amzn1.sym.fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_p=fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_r=XYDTAHJ1XQ9B9N3G9MAM&pd_rd_wg=SW9W5&pd_rd_r=a6216d69-4dc6-42bd-9aa9-872eb0380028")
    # this code is for the browser to be stay alive
    sign_in_hover_element=driver.find_element(By.ID,"nav-link-accountList-nav-line-1")
    actions=ActionChains(driver)
    actions.move_to_element(sign_in_hover_element).perform()
    actions.move_to_element(driver.find_element(By.XPATH,"(//span[@class='nav-action-inner'])[1]")).click().perform()
    driver.find_element(By.XPATH,"//input[@type='email']").send_keys("9657878369")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Belly@2306")
    driver.find_element(By.XPATH,"//span[@id='auth-signin-button']").click()




def test_Add_to_cart():
    #this code is for the browser to be stay alive
    options=Options()
    options.add_experimental_option("detach",True)
    driver= webdriver.Chrome(options=options)

    #Maximizing the window
    driver.maximize_window()

    #getting the Amazon url and navigating to amazon
    driver.get("https://www.amazon.in/b/ref=surl_fashion/?_encoding=UTF8&node=6648217031&pd_rd_w=sC81d&content-id=amzn1.sym.fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_p=fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_r=XYDTAHJ1XQ9B9N3G9MAM&pd_rd_wg=SW9W5&pd_rd_r=a6216d69-4dc6-42bd-9aa9-872eb0380028")

    #going to search box and giving data
    search_box=driver.find_element(By.ID,"twotabsearchtextbox")
    search_box.send_keys("iPhone Xr")

    #submitting the form
    driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
    time.sleep(4)  #giving some time to load page

    #selecting the product
    driver.find_element(By.XPATH,"(//div[@class='a-section aok-relative s-image-tall-aspect'])[1]").click()
    time.sleep(4)

    #switching to the another tab as product page is opening in another url
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

    #clicking to the Add to cart button
    driver.find_element(By.XPATH,"//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']").click()
    time.sleep(5)

    # checkout button
    driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
    print("Item added to the cart Successfully")
def test_delete_Product_from_cart():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    # Maximizing the window
    driver.maximize_window()

    # getting the Amazon url and navigating to amazon
    driver.get(
        "https://www.amazon.in/b/ref=surl_fashion/?_encoding=UTF8&node=6648217031&pd_rd_w=sC81d&content-id=amzn1.sym.fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_p=fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_r=XYDTAHJ1XQ9B9N3G9MAM&pd_rd_wg=SW9W5&pd_rd_r=a6216d69-4dc6-42bd-9aa9-872eb0380028")

    # going to search box and giving data
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("iPhone Xr")

    # submitting the form
    driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
    time.sleep(4)  # giving some time to load page

    # selecting the product
    driver.find_element(By.XPATH, "(//div[@class='a-section aok-relative s-image-tall-aspect'])[1]").click()
    time.sleep(4)

    # switching to the another tab as product page is opening in another url
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

    # clicking to the Add to cart button
    driver.find_element(By.XPATH,
                        "//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']").click()
    time.sleep(5)

    # checkout button
    driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
    print("Item added to the cart Successfully")

    # delete

    dropdown = driver.find_element(By.XPATH,"//span[@id='a-autoid-0-announce']")  # Replace "dropdown_id" with the ID of your dropdown
    dropdown.click()

    # Find the desired option within the dropdown and click on it
    option_to_select = driver.find_element(By.XPATH, "//a[@id='quantity_0']")  # Replace with your option text
    option_to_select.click()
    print("Item removed from the cart Successfully")
