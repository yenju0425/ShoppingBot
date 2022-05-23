import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# TODO: 填入可能的搶貨網址 (可能隨時被改變，搶貨前1分鐘需再確認)
url = "https://24h.pchome.com.tw/prod/DRADD4-A900BEOMC"

# TODO: 填入信用卡安全碼
cvv = "---"

# 直接抓取Chrome使用者設定檔 (需安裝)
# 事前登入可不需再次輸入帳密以節省時間
options = webdriver.chrome.options.Options()
options.add_argument(r"--user-data-dir=C:\Users\Rick\AppData\Local\Google\Chrome\User Data")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 啟動機器人 (Windows)
driver = webdriver.Chrome(executable_path="./chromedriver", options=options)

while True:
    try:
        driver.get(url)

        # 檢查上架
        driver.find_element_by_xpath('//button[text()="加入購物車"]')

        # 放入購物車
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//li[@id='ButtonContainer']/button"))
        )
        driver.find_element_by_xpath("//li[@id='ButtonContainer']/button").click()
        print("放入購物車...Succeed")

        # 前往購物車
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "ico_cart"))
        )
        element = driver.find_element_by_id('ico_cart')
        webdriver.ActionChains(driver).move_to_element(element).perform()
        driver.find_element_by_id('ico_cart').click()
        print("前往購物車...Succeed")

        # 前往結帳
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//li[@class='CC']/a[@class='ui-btn']"))
        )
        driver.find_element_by_xpath("//li[@class='CC']/a[@class='ui-btn']").click()
        print("前往結帳...Succeed")

        # 勾選確認
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[@id='warning-timelimit_btn_confirm']"))
        )
        driver.find_element_by_xpath("//a[@id='warning-timelimit_btn_confirm']").click()
        print("勾選確認...Succeed")

        # 填入資料
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='multi_CVV2Num']"))
        )
        elem = driver.find_element_by_xpath("//input[@name='multi_CVV2Num']")
        elem.send_keys(cvv)
        print("填入資料...Succeed")
        
        # 送出訂單
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[@id='btnSubmit']"))
        )
        driver.find_element_by_xpath("//a[@id='btnSubmit']").click()
        print("送出訂單...Succeed")

        break

    except Exception as e:
        print(e.__class__.__name__)
        time.sleep(0.25)
