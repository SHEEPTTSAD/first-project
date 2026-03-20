from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        print("브라우저 실행")
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        try:
            print("사이트 접속")
            page.goto("https://www.saucedemo.com/")

            print("로그인 시도")
            page.locator("#user-name").fill("standard_user")
            page.locator("#password").fill("secret_sauce")
            page.locator("#login-button").click()

            page.wait_for_timeout(1000)

            if "inventory" not in page.url:
                print("로그인 실패")
                return
            
            print("로그인 성공")
            # -------------------------------------------------

            print("가방을 장바구니에 담기")
            page.locator("#add-to-cart-sauce-labs-backpack").click()

            print("장바구니 이동")
            page.locator(".shopping_cart_link").click()

            print("결제 시도")
            page.locator("#checkout").click()

            print("배송 정보 입력")
            page.locator("#first-name").fill("maple")
            page.locator("#last-name").fill("story")
            page.locator("#postal-code").fill("00429")
            page.locator("#continue").click()

            print("결제 버튼 클릭")
            page.locator("#finish").click()

            print("결제 성공")
            time.sleep(3)

        except Exception as e:
            print(f"테스트 실패: {e}")

        finally:
            browser.close()

if __name__ == "__main__":
    main()
