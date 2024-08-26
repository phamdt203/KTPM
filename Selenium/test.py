import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_case_tc01(driver):
    result = {"Test Case": "Kiểm tra tính năng đặt hàng", "Status": "Fail", "Message": ""}

    driver.get("https://hoasenhome.vn/checkout")
    driver.maximize_window()

    dat_hang_button = driver.find_element(By.XPATH, '//button[contains(text(), "Tiến hành đặt hàng")]')
    dat_hang_button.click()

    try:
        change_address_button = driver.find_element(By.XPATH, '//button[contains(text(), "Đổi địa chỉ")]')
        change_address_button.click()
        
        name_input = driver.find_element(By.NAME, 'name')
        name_input.send_keys('Phạm Đình Tiến')

        phone_input = driver.find_element(By.NAME, 'phone')
        phone_input.send_keys('03937255596')

        address_input = driver.find_element(By.NAME, 'address')
        address_input.send_keys('Số 298 Đường Cầu Diễn')

        province_select = Select(driver.find_element(By.NAME, 'province'))
        province_select.select_by_visible_text('Hà Nội')

        # Click vào “Quận/huyện" và chọn “Quận Bắc Từ Liệm"
        district_select = Select(driver.find_element(By.NAME, 'district'))
        district_select.select_by_visible_text('Bắc Từ Liêm')

        # Click vào “Phường/Xã" và chọn “Phường Minh Khai"
        ward_select = Select(driver.find_element(By.NAME, 'ward'))
        ward_select.select_by_visible_text('Minh Khai')

        product_transfer_button = driver.find_element(By.XPATH, '//button[contains(text(), "Giao hàng đến địa chỉ này")]')
        product_transfer_button.click()

        place_order_button = driver.find_element(By.XPATH, '//button[contains(text(), "Xác nhận mua hàng")]')
        place_order_button.click()

        if driver.current_url != "https://hoasenhome.vn/checkout":
            result["Status"] = "Pass"
            result["Message"] = "Đặt sản phẩm thành công."
        else:
            result["Message"] = "Đặt sản phẩm không thành công."
    except Exception as e:
        result["Message"] = str(e)
    return result


def test_case_tc02(driver):
    result = {"Test Case": "Kiểm tra tính năng đặt hàng", "Status": "Fail", "Message": ""}

    driver.get("https://hoasenhome.vn/checkout")
    driver.maximize_window()

    dat_hang_button = driver.find_element(By.XPATH, '//button[contains(text(), "Tiến hành đặt hàng")]')
    dat_hang_button.click()

    try:
        change_address_button = driver.find_element(By.XPATH, '//button[contains(text(), "Đổi địa chỉ")]')
        change_address_button.click()

        phone_input = driver.find_element(By.NAME, 'phone')
        phone_input.send_keys('03937255596')

        address_input = driver.find_element(By.NAME, 'address')
        address_input.send_keys('Số 298 Đường Cầu Diễn')

        province_select = Select(driver.find_element(By.NAME, 'province'))
        province_select.select_by_visible_text('Hà Nội')

        # Click vào “Quận/huyện" và chọn “Quận Bắc Từ Liệm"
        district_select = Select(driver.find_element(By.NAME, 'district'))
        district_select.select_by_visible_text('Bắc Từ Liêm')

        # Click vào “Phường/Xã" và chọn “Phường Minh Khai"
        ward_select = Select(driver.find_element(By.NAME, 'ward'))
        ward_select.select_by_visible_text('Minh Khai')

        product_transfer_button = driver.find_element(By.XPATH,
                                                      '//button[contains(text(), "Giao hàng đến địa chỉ này")]')
        product_transfer_button.click()

        place_order_button = driver.find_element(By.XPATH, '//button[contains(text(), "Xác nhận mua hàng")]')
        place_order_button.click()

        if driver.current_url != "https://hoasenhome.vn/checkout":
            result["Status"] = "Pass"
            result["Message"] = "Nhập thiếu tên khách hàng."
        else:
            result["Message"] = "Đặt sản phẩm thành công."
    except Exception as e:
        result["Message"] = str(e)
    return result


def test_case_tc03(driver):
    result = {"Test Case": "Kiểm tra tính năng đặt hàng", "Status": "Fail", "Message": ""}

    driver.get("https://hoasenhome.vn/cart")
    driver.maximize_window()

    dat_hang_button = driver.find_element(By.XPATH, '//button[contains(text(), "Tiến hành đặt hàng")]')
    dat_hang_button.click()

    try:
        change_address_button = driver.find_element(By.XPATH, '//button[contains(text(), "Đổi địa chỉ")]')
        change_address_button.click()

        name_input = driver.find_element(By.NAME, 'name')
        name_input.send_keys('Phạm Đình Tiến')

        address_input = driver.find_element(By.NAME, 'address')
        address_input.send_keys('Số 298 Đường Cầu Diễn')

        province_select = Select(driver.find_element(By.NAME, 'province'))
        province_select.select_by_visible_text('Hà Nội')

        # Click vào “Quận/huyện" và chọn “Quận Bắc Từ Liệm"
        district_select = Select(driver.find_element(By.NAME, 'district'))
        district_select.select_by_visible_text('Bắc Từ Liêm')

        # Click vào “Phường/Xã" và chọn “Phường Minh Khai"
        ward_select = Select(driver.find_element(By.NAME, 'ward'))
        ward_select.select_by_visible_text('Minh Khai')

        product_transfer_button = driver.find_element(By.XPATH, '//button[contains(text(), "Giao hàng đến địa chỉ này")]')
        product_transfer_button.click()

        place_order_button = driver.find_element(By.XPATH, '//button[contains(text(), "Xác nhận mua hàng")]')
        place_order_button.click()

        if driver.current_url != "https://hoasenhome.vn/checkout":
            result["Status"] = "Pass"
            result["Message"] = "Nhập thiếu số điện thoại."
        else:
            result["Message"] = "Đặt sản phẩm thành công."
    except Exception as e:
        result["Message"] = str(e)
    return result

def save_results_to_excel(results, file_name="KTDH_results.csv"):
    df = pd.DataFrame(results)
    df.to_csv(file_name)

def main():
    driver = webdriver.Chrome()
    results = []

    try:
        results.append(test_case_tc01(driver))
        results.append(test_case_tc02(driver))
        results.append(test_case_tc03(driver))
    finally:
        driver.quit()
        save_results_to_excel(results)

if __name__ == "__main__":
    main()