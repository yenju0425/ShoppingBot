import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# 設定momo網址
url_momo = "https://www.momoshop.com.tw/main/Main.jsp"

# TODO: 填入可能的搶貨網址 (可能隨時被改變，搶貨前1分鐘需再確認)
url = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8935671"

# TODO: 填入信用卡安全碼
cvv = "---"

# 直接抓取Chrome使用者設定檔 (需安裝)
# 事前登入可不需再次輸入帳密以節省時間
options = webdriver.chrome.options.Options()
options.add_argument(r"--user-data-dir=C:\Users\Rick\AppData\Local\Google\Chrome\User Data")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 啟動機器人 (Windows)
driver = webdriver.Chrome(executable_path="./chromedriver", options=options)

driver.get(url_momo)

# 點擊登入
WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.XPATH, "//span[@class='CL1']"))
)
driver.find_element_by_xpath("//span[@class='CL1']").click()
print("點擊登入...Succeed")

# Google登入
WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.XPATH, "//img[@title='Google登入']"))
)
driver.find_element_by_xpath("//img[@title='Google登入']").click()
print("Google登入...Succeed")

# 選擇帳戶
WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.XPATH, "//div[@data-identifier='yenju0425@gmail.com']"))
)
driver.find_element_by_xpath("//div[@data-identifier='yenju0425@gmail.com']").click()
print("選擇帳戶...Succeed")

time.sleep(3) # 登入需要花時間，直接進入迴圈刷新會導致登入失敗，緩衝3秒 (視搶貨的激進程度調整)

counter = 0
while True:
    try:
        driver.get(url)
        print(counter)
        counter = counter + 1

        # 檢查上架
        driver.find_element_by_xpath('//img[@title="直接購買"]')

        # 直接購買
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//dt[@id='buy_yes']"))
        )
        driver.find_element_by_xpath("//dt[@id='buy_yes']").click()
        print("直接購買...Succeed")

        # 結帳
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//li[@class='checkoutBtn']"))
        )
        driver.find_element_by_xpath("//li[@class='checkoutBtn']").click()
        print("結帳...Succeed")

        # 填入資料
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='cardCVV']"))
        )
        elem = driver.find_element_by_xpath("//input[@name='cardCVV']")
        elem.send_keys(cvv)
        print("填入資料...Succeed")

        # 送出訂單
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[@id='orderSave']"))
        )
        driver.find_element_by_xpath("//a[@id='orderSave']").click()
        print("送出訂單...Succeed")

        break

    except Exception as e:
        print(e.__class__.__name__)
        time.sleep(0.26)