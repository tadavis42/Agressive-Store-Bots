#!/usr/bin/env python3
"""
CHROME VERSION - Spider-Man Bundle Bot
Replaces unstable Firefox version with reliable Chrome automation
"""

import time
import sys
import os
import random
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === CONFIGURATION ===
PRODUCT_NAME = "Magic: The Gathering Marvel's Spider-Man Bundle"
PRODUCT_URL = "https://www.amazon.com/gp/product/B0DV1VCPQF/ref=ox_sc_saved_image_2?smid=&psc=1"
MAX_PRICE = 150  # Updated price limit to match current pricing
REFRESH_SECONDS = 15  # Increased from 8 to reduce rate limiting
MAX_CHECKS_PER_HOUR = 200  # Limit to prevent Amazon blocking
COOLDOWN_MINUTES = 10  # Cooldown period after errors
HEADLESS = False

# Chrome configuration
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def create_chrome_driver():
    """Create Chrome driver for Spider-Man monitoring"""
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()

    if HEADLESS:
        options.add_argument('--headless')

    # Chrome-specific options for stability
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9224')  # Different port from Avatar bot
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-extensions')

    # SSL/TLS options to fix handshake errors
    options.add_argument('--ignore-ssl-errors-for-test')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-features=VizDisplayCompositor')
    options.add_argument('--ssl-version-fallback-min=tls1.2')

    # Use dedicated profile for Spider-Man bot
    options.add_argument('--user-data-dir=C:\\temp\\spiderman_chrome_bot')
    options.add_argument('--profile-directory=Default')

    # User agent
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    try:
        print("🔵 Starting Chrome for Spider-Man monitoring...")
        service = Service(ChromeDriverManager().install())

        # Set timeouts to handle connection issues
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_script_timeout(30)
        driver.set_window_size(1920, 1080)

        # Test connection
        driver.get("https://www.google.com")
        time.sleep(2)

        print("✅ Chrome started successfully!")
        return driver
    except Exception as e:
        print(f"❌ Chrome failed to start: {e}")
        # Clean up any hanging processes
        try:
            if 'driver' in locals():
                driver.quit()
        except:
            pass
        return None

def handle_amazon_dialogs(driver):
    """Handle Amazon session timeout dialogs like 'Keep Shopping?'"""
    try:
        # Check for various dialog selectors
        dialog_selectors = [
            "[data-action='a-modal-close']",  # Close modal button
            "button[aria-label='Close']",     # Close button
            "#a-popover-content-1 button",    # Popover close
            "button:contains('Keep shopping')", # Keep shopping button
            "button[data-action*='keep']",     # Keep shopping variations
            "[data-testid='keep-shopping']",   # Test ID based
            ".a-button-primary input[type='submit']", # Primary submit button
            "input[aria-label*='Keep']",       # Keep shopping input
            "#sp-cc-accept",                   # Cookie consent
            "input[value*='Continue']",        # Continue shopping
            "button[name='continue']",         # Continue button
        ]

        dialog_found = False
        for selector in dialog_selectors:
            try:
                dialog_elements = driver.find_elements(By.CSS_SELECTOR, selector)
                for element in dialog_elements:
                    if element.is_displayed():
                        print(f"🔄 Found Amazon dialog, clicking: {selector}")
                        element.click()
                        time.sleep(2)
                        dialog_found = True
                        break
                if dialog_found:
                    break
            except Exception as e:
                continue

        # Also check for text-based dialogs
        if not dialog_found:
            try:
                page_source = driver.page_source.lower()
                if any(phrase in page_source for phrase in ['keep shopping', 'session timeout', 'are you still there', 'continue shopping']):
                    print("🔄 Detected session dialog in page text")
                    # Try to find and click any visible buttons
                    buttons = driver.find_elements(By.TAG_NAME, "button")
                    for button in buttons:
                        if button.is_displayed() and button.is_enabled():
                            button_text = button.text.lower()
                            if any(word in button_text for word in ['continue', 'keep', 'ok', 'yes', 'shopping']):
                                print(f"🔄 Clicking dialog button: {button.text}")
                                button.click()
                                time.sleep(2)
                                dialog_found = True
                                break

                    # Also try input elements
                    if not dialog_found:
                        inputs = driver.find_elements(By.TAG_NAME, "input")
                        for inp in inputs:
                            if inp.is_displayed() and inp.is_enabled():
                                inp_value = inp.get_attribute('value') or ''
                                if any(word in inp_value.lower() for word in ['continue', 'keep', 'ok', 'yes']):
                                    print(f"🔄 Clicking dialog input: {inp_value}")
                                    inp.click()
                                    time.sleep(2)
                                    dialog_found = True
                                    break
            except Exception as e:
                pass

        return dialog_found
    except Exception as e:
        print(f"⚠️ Error handling dialogs: {e}")
        return False

def check_amazon_availability(driver):
    """Check if Spider-Man Bundle is available from Amazon Direct"""
    try:
        print(f"🔍 Checking {PRODUCT_NAME} at {datetime.now().strftime('%H:%M:%S')}")

        # Handle any session dialogs before checking availability
        handle_amazon_dialogs(driver)

        # Navigate to product page with timeout handling
        print(f"🌐 Loading product page...")
        try:
            driver.get(PRODUCT_URL)
            print("✅ Page navigation completed")
        except Exception as e:
            print(f"❌ Navigation error: {e}")
            return None

        # Wait for page to load with shorter timeout
        try:
            WebDriverWait(driver, 8).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("✅ Page body loaded")
        except Exception as e:
            print(f"❌ Page load timeout: {e}")
            return None

        # Handle any session dialogs after page load
        print("🔄 Checking for session dialogs...")
        handle_amazon_dialogs(driver)

        # Add small delay before analysis
        time.sleep(2)

        # Get page source for analysis
        print("📄 Analyzing page content...")
        try:
            page_source = driver.page_source.lower()
            print(f"✅ Page content loaded ({len(page_source)} characters)")
        except Exception as e:
            print(f"❌ Could not get page source: {e}")
            return None

        # Check for Amazon Direct availability
        amazon_direct_indicators = [
            'ships from and sold by amazon.com',
            'sold by amazon.com',
            'ships from: amazon.com',
            'sold by: amazon.com',
            'ships from amazon.com',
            'amazon.com as seller',
            'amazon.com seller'
        ]

        amazon_available = any(indicator in page_source for indicator in amazon_direct_indicators)

        # Check for unavailable indicators
        unavailable_indicators = [
            'currently unavailable',
            'temporarily out of stock',
            "we don't know when or if this item will be back",
            'this item is not available'
        ]

        unavailable = any(indicator in page_source for indicator in unavailable_indicators)

        # Check for add to cart button
        add_to_cart_available = False
        try:
            add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button")
            add_to_cart_available = add_to_cart_button.is_displayed() and add_to_cart_button.is_enabled()
        except NoSuchElementException:
            # Try alternative selectors
            try:
                alt_button = driver.find_element(By.CSS_SELECTOR, "[name='submit.add-to-cart']")
                add_to_cart_available = alt_button.is_displayed() and alt_button.is_enabled()
            except:
                add_to_cart_available = False

        # Try to extract price with better error handling
        current_price = None
        print("💰 Extracting price information...")
        try:
            price_selectors = [
                '.a-price .a-offscreen',
                '.a-price-whole',
                '[data-feature-name="corePrice"] .a-price .a-offscreen',
                '#priceblock_dealprice',
                '#priceblock_ourprice',
                '.a-price-range .a-offscreen',
                '.a-price.a-text-price .a-offscreen'
            ]

            for selector in price_selectors:
                try:
                    price_element = driver.find_element(By.CSS_SELECTOR, selector)
                    price_text = price_element.get_attribute('textContent') or price_element.text
                    if '$' in price_text:
                        # Extract numeric price
                        import re
                        price_match = re.search(r'\$([0-9,]+\.?[0-9]*)', price_text)
                        if price_match:
                            current_price = float(price_match.group(1).replace(',', ''))
                            print(f"✅ Price found with selector {selector}: ${current_price}")
                            break
                except Exception as selector_error:
                    continue

            if not current_price:
                print("⚠️ No price found with standard selectors")
        except Exception as e:
            print(f"⚠️ Price extraction error: {e}")

        # Determine status and action
        if amazon_available and add_to_cart_available:
            status = "🟢 AMAZON DIRECT - AVAILABLE TO PURCHASE!"
            action_required = True
        elif unavailable:
            status = "🔴 Currently unavailable"
            action_required = False
        elif add_to_cart_available:
            status = "🟡 Third-party sellers available"
            action_required = False
        else:
            status = "❓ Status unclear"
            action_required = False

        print(f"📊 Status: {status}")
        if current_price:
            print(f"💰 Price: ${current_price}")
            if current_price > MAX_PRICE:
                print(f"⚠️ Price above max (${MAX_PRICE})")
                action_required = False
        else:
            print("⚠️ Could not detect price")

        # Debug output
        print(f"🔍 Debug - Amazon Direct: {amazon_available}, Add to Cart: {add_to_cart_available}, Unavailable: {unavailable}")
        print(f"📄 Page title: {driver.title[:100]}...")

        return {
            'amazon_direct': amazon_available,
            'add_to_cart': add_to_cart_available,
            'price': current_price,
            'status': status,
            'action_required': action_required,
            'page_title': driver.title
        }

    except Exception as e:
        print(f"❌ Error checking availability: {e}")
        import traceback
        print(f"🔍 Full error trace: {traceback.format_exc()}")
        return None

def attempt_purchase(driver):
    """Attempt to add Spider-Man Bundle to cart with quantity 2"""
    try:
        print("🛒 ATTEMPTING TO ADD 2 SPIDER-MAN BUNDLES TO CART...")

        # First try to set quantity to 2
        try:
            quantity_dropdown = driver.find_element(By.CSS_SELECTOR, "#quantity")
            # Click dropdown to open options
            quantity_dropdown.click()
            time.sleep(1)

            # Try to select quantity 2
            try:
                quantity_2_option = driver.find_element(By.CSS_SELECTOR, "option[value='2']")
                quantity_2_option.click()
                print("📦 Set quantity to 2")
                time.sleep(1)
            except:
                # If no option for 2, try typing it
                quantity_dropdown.clear()
                quantity_dropdown.send_keys("2")
                print("📦 Typed quantity as 2")
                time.sleep(1)
        except:
            print("⚠️ Could not set quantity, using default")

        # Find and click add to cart button
        add_to_cart_selectors = [
            "#add-to-cart-button",
            "[name='submit.add-to-cart']",
            "[data-feature-name='addToCart'] input",
            "input[title*='Add to Cart']"
        ]

        for selector in add_to_cart_selectors:
            try:
                button = driver.find_element(By.CSS_SELECTOR, selector)
                if button.is_displayed() and button.is_enabled():
                    print(f"🎯 Found Add to Cart button: {selector}")
                    button.click()
                    print("✅ Clicked Add to Cart!")
                    time.sleep(3)  # Wait for response

                    # Check if we're on cart page or if there are any popups
                    current_url = driver.current_url
                    if 'cart' in current_url.lower() or 'gp/aws/cart' in current_url:
                        print("🎉 SUCCESS! Item added to cart!")
                        print("🚀 ATTEMPTING AUTO-CHECKOUT...")
                        return auto_checkout(driver)
                    else:
                        print("⚠️ Add to cart clicked, checking for popups...")
                        # Handle any popups or additional options
                        time.sleep(2)

                    break
            except Exception as e:
                print(f"❌ Could not click {selector}: {e}")
                continue

        return False

    except Exception as e:
        print(f"❌ Purchase attempt failed: {e}")
        return False

def auto_checkout(driver):
    """Automatically complete checkout process"""
    try:
        print("🛒 Navigating to checkout...")

        # Go to cart first if not already there
        if 'cart' not in driver.current_url.lower():
            driver.get("https://www.amazon.com/gp/cart/view.html")
            time.sleep(2)

        # Click "Proceed to checkout"
        checkout_selectors = [
            "[name='proceedToRetailCheckout']",
            "#sc-buy-box-ptc-button",
            "[data-feature-name='proceed-to-checkout-action']",
            "input[value*='Proceed to checkout']"
        ]

        for selector in checkout_selectors:
            try:
                checkout_btn = driver.find_element(By.CSS_SELECTOR, selector)
                if checkout_btn.is_displayed() and checkout_btn.is_enabled():
                    print(f"🎯 Found checkout button: {selector}")
                    checkout_btn.click()
                    print("✅ Clicked Proceed to Checkout!")
                    time.sleep(3)
                    break
            except:
                continue

        # Wait for checkout page to load
        time.sleep(3)

        # Click "Place your order" or "Buy now"
        place_order_selectors = [
            "#placeYourOrder",
            "[name='placeYourOrder1']",
            "#buyNow",
            "input[value*='Place your order']",
            "input[value*='Buy now']"
        ]

        for selector in place_order_selectors:
            try:
                order_btn = driver.find_element(By.CSS_SELECTOR, selector)
                if order_btn.is_displayed() and order_btn.is_enabled():
                    print(f"🎯 Found place order button: {selector}")
                    order_btn.click()
                    print("💳 ORDER PLACED AUTOMATICALLY!")
                    time.sleep(5)
                    return True
            except:
                continue

        print("⚠️ Could not find place order button - manual intervention needed")
        return False

    except Exception as e:
        print(f"❌ Auto-checkout failed: {e}")
        return False

def main():
    print("🕷️ CHROME SPIDER-MAN BUNDLE BOT")
    print("=" * 60)
    print(f"🎯 Product: {PRODUCT_NAME}")
    print(f"🔗 URL: {PRODUCT_URL}")
    print(f"💰 Max Price: ${MAX_PRICE}")
    print(f"⏰ Refresh Rate: {REFRESH_SECONDS} seconds")
    print(f"📦 Target Quantity: 2 bundles")
    print(f"🔵 Browser: Chrome (replacing unstable Firefox)")
    print()
    print("🚨 THIS BOT WILL ATTEMPT TO PURCHASE WHEN STOCK IS FOUND!")
    print("🚨 MAKE SURE YOU LOG INTO AMAZON IN THE BROWSER FIRST!")
    print()

    # Skip manual prompt if running automated
    if len(sys.argv) > 1 and sys.argv[1] == '--auto':
        print("🤖 Auto-mode: Starting monitoring immediately...")
    else:
        input("Press Enter to start Chrome Spider-Man monitoring... ")

    # Create Chrome driver
    driver = create_chrome_driver()
    if not driver:
        print("❌ Cannot start - Chrome driver failed")
        return

    try:
        # Navigate to Amazon login first
        print("🔐 Opening Amazon - Please log in if needed...")
        driver.get("https://www.amazon.com")
        time.sleep(5)

        # Give user time to log in if needed
        if len(sys.argv) <= 1 or sys.argv[1] != '--auto':
            input("Press Enter after logging into Amazon to start monitoring... ")

        check_count = 0
        consecutive_errors = 0
        start_time = datetime.now()
        last_cooldown = None

        while True:
            check_count += 1
            current_time = datetime.now()

            # Rate limiting: Check if we're exceeding limits
            if check_count > MAX_CHECKS_PER_HOUR:
                elapsed_hours = (current_time - start_time).total_seconds() / 3600
                if elapsed_hours < 1.0:
                    cooldown_time = 60 - (elapsed_hours * 60)
                    print(f"⚠️ Rate limit reached ({check_count} checks). Cooling down for {cooldown_time:.1f} minutes...")
                    time.sleep(cooldown_time * 60)
                    check_count = 0
                    start_time = current_time

            # Add randomized delay to avoid pattern detection
            base_delay = REFRESH_SECONDS
            random_delay = base_delay + random.uniform(2, 8)

            result = check_amazon_availability(driver)

            if result is None:
                consecutive_errors += 1
                print(f"❌ Error #{consecutive_errors}")

                # Implement progressive backoff
                if consecutive_errors >= 3:
                    backoff_minutes = min(consecutive_errors * 2, COOLDOWN_MINUTES)
                    print(f"⏸️ Too many errors, cooling down for {backoff_minutes} minutes...")
                    time.sleep(backoff_minutes * 60)
                    last_cooldown = current_time

                # Chrome is more stable, but still restart if too many errors
                if consecutive_errors >= 5:
                    print("🔄 Too many errors, restarting Chrome...")
                    try:
                        driver.quit()
                    except:
                        pass

                    driver = create_chrome_driver()
                    if not driver:
                        print("❌ Cannot restart - Chrome driver failed")
                        break

                    print("🔐 Navigating back to Amazon...")
                    driver.get("https://www.amazon.com")
                    time.sleep(5)
                    consecutive_errors = 0

                if consecutive_errors >= 8:
                    print("❌ Too many consecutive errors, stopping...")
                    break
                time.sleep(REFRESH_SECONDS)
                continue

            consecutive_errors = 0  # Reset error count

            if result['action_required']:
                print("🚨" * 20)
                print("🚨 SPIDER-MAN BUNDLE AVAILABLE FROM AMAZON! 🚨")
                print("🚨" * 20)

                # Attempt purchase
                success = attempt_purchase(driver)

                if success:
                    print("🎉 PURCHASE ATTEMPT SUCCESSFUL!")
                    print("💳 Complete checkout in the browser!")
                    break
                else:
                    print("⚠️ Purchase attempt failed, continuing monitoring...")

            # Use randomized delay to avoid detection
            print(f"⏳ Waiting {random_delay:.1f} seconds... (Check #{check_count})")
            time.sleep(random_delay)

    except KeyboardInterrupt:
        print("\n⏹️ Monitoring stopped by user")
    except Exception as e:
        print(f"\n💥 Fatal error: {e}")
    finally:
        print("🔄 Closing Chrome...")
        try:
            driver.quit()
        except:
            pass
        print("✅ Spider-Man Chrome bot stopped")

if __name__ == "__main__":
    main()