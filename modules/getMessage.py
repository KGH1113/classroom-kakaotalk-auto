from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def getMessage():
    CHROME_DRIVER_PATH = "./assets/chromedriver/chromedriver"
    service = Service(executable_path=CHROME_DRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(service=service, options=options)

    print("Getting the login page...")
    driver.get(
        "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fclassroom.google.com&ifkv=ASKXGp3tneXNHauAstemR2Y1KeZrtHwugzH56RxFAqGNbCC_rL-8jk3dWGGyvzwrMHiRrk0UA9a6hQ&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S655278659%3A1701512347707631&theme=glif"
    )
    time.sleep(3)
    print("Done")
    time.sleep(0.2)
    print()

    print("Inputing the ID...")
    driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input",
    ).send_keys("21201s23@seoun.sen.ms.kr")

    driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button",
    ).click()
    time.sleep(3)
    print("Done")
    time.sleep(0.2)
    print()

    print("Inputing the PW & Moving to classes page...")
    driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input",
    ).send_keys("seoun1234")

    driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button",
    ).click()
    time.sleep(9)
    print("Done")
    time.sleep(0.2)
    print()

    print("Getting the class list & Moving to {0}...".format("서운중 2학년 12반"))
    for i in range(
        1,
        len(
            driver.find_element(
                By.XPATH, "/html/body/c-wiz/div[2]/div/div[8]/div/ol"
            ).find_elements(By.XPATH, "*")
        )
        + 1,
    ):
        if (
            driver.find_element(
                By.XPATH,
                "/html/body/c-wiz/div[2]/div/div[8]/div/ol/li[{0}]/div[1]/div[3]/h2/a[1]/div[1]".format(
                    i
                ),
            ).get_attribute("innerHTML")
            == "서운중 2학년 12반"
        ):
            driver.find_element(
                By.XPATH,
                "/html/body/c-wiz/div[2]/div/div[8]/div/ol/li[{0}]/div[1]/div[3]/h2/a[1]".format(
                    i
                ),
            ).click()

    time.sleep(7)
    print("Done")
    time.sleep(0.2)
    print()
    print()

    return driver.find_element(
        By.XPATH,
        "/html/body/c-wiz[2]/div[2]/div/div[7]/div[2]/main/section/div/div[2]/div[1]/div[2]/div[1]/span",
    ).text


if __name__ == "__main__":
    print(getMessage())
