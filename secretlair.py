import os
from pathlib import Path
import sys
import time
from sys import platform
from backports import configparser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from twilio.rest import Client
from webdriver_manager.firefox import GeckoDriverManager
from twilio.base.exceptions import TwilioRestException
from selenium.webdriver.firefox.options import FirefoxProfile
from selenium.webdriver.firefox.options import Options

global profile_path

# ----- setting up the Secret Lair bot! -----

# 1. Secret Lair credentials (if login required)
username = ''
password = ''

# 2. Main Config
url = 'https://secretlair.wizards.com/en'  # Secret Lair main page URL
max_price = 100  # Enter your Max Price you're willing to pay for Secret Lair drops
webpage_refresh_timer = 10  # Default 10 seconds for Secret Lair (slower than Amazon)
test_mode = True  # Set False for live purchasing. If True, it will only monitor without buying
headless_mode = False  # Set False for testing. If True, it will hide Firefox in background

# 3. Twilio Information (Optional)
toNumber = 'Your_Phone_Number'
fromNumber = 'Twilio_Phone_Number'
accountSid = 'Twilio_SSID'
authToken = 'Twilio_AuthToken'
client = Client(accountSid, authToken)

# ----- You are done setting up the bot! -----

def time_sleep(x, driver):
    for i in range(x, -1, -1):
        sys.stdout.write('\r')
        sys.stdout.write('Monitoring Secret Lair. Refreshing in{:2d} seconds'.format(i))
        sys.stdout.flush()
        time.sleep(1)
    driver.execute_script('window.localStorage.clear();')

    if not attempting_to_buy:
        driver.execute_script('window.localStorage.clear();')
        try:
            driver.refresh()
        except WebDriverException:
            print('Error while refreshing - internet down?')
        sys.stdout.write('\r')
        sys.stdout.write('Monitoring Secret Lair. Refreshing in{:2d} seconds'.format(i))
        sys.stdout.flush()

def get_profile_path():
    global profile_path
    if platform == 'linux' or platform == 'linux2':
        profile_path = Path(os.getenv('HOME')) / '.mozilla' / 'firefox'
    elif platform == 'darwin':
        profile_path = Path(os.getenv('HOME')) / 'Library' / 'Application Support' / 'Firefox'
    elif platform == 'win32':
        profile_path = Path(os.getenv('APPDATA')) / 'Mozilla' / 'Firefox'
    if not profile_path.exists():
        raise FileNotFoundError("Mozilla profile doesn't exist and/or can't be located on this machine.")
    return profile_path

def get_default_profile(profile_path2):
    mozilla_profile_ini = profile_path2 / 'profiles.ini'
    profile = configparser.ConfigParser()
    profile.read(mozilla_profile_ini)
    return profile.get('Profile0', 'Path')

def secret_lair_monitor():
    global attempting_to_buy
    attempting_to_buy = False

    print('🌟 Starting Secret Lair Monitor...')
    print(f'🎯 Target URL: {url}')
    print(f'💰 Max Price: ${max_price}')
    print(f'🔄 Refresh Rate: {webpage_refresh_timer} seconds')
    print(f'🧪 Test Mode: {test_mode}')
    print('')

    # Firefox setup
    try:
        profile_path_var = get_profile_path()
        default_profile = get_default_profile(profile_path_var)
        profile = FirefoxProfile(profile_path_var / default_profile)

        options = Options()
        if headless_mode:
            options.add_argument('--headless')

        print('🦊 Starting Firefox browser...')
        driver = webdriver.Firefox(firefox_profile=profile, options=options)

    except Exception as e:
        print(f'❌ Firefox setup error: {e}')
        return

    # Navigate to Secret Lair
    try:
        print('🌐 Navigating to Secret Lair...')
        driver.get(url)
        time.sleep(5)  # Let page load

    except Exception as e:
        print(f'❌ Navigation error: {e}')
        driver.quit()
        return

    # Monitoring loop
    print('👀 Starting Secret Lair monitoring loop...')
    print('🔍 Looking for new drops, price changes, and availability...')

    previous_drops = set()

    while True:
        try:
            # Look for Secret Lair drops
            current_drops = detect_secret_lair_drops(driver)

            # Check for new drops
            new_drops = current_drops - previous_drops
            if new_drops:
                print(f'\\n🚨 NEW SECRET LAIR DROP(S) DETECTED! 🚨')
                for drop in new_drops:
                    print(f'🆕 New Drop: {drop}')

                    # Send notification
                    send_notification(f'🌟 New Secret Lair Drop: {drop}')

                    # Try to purchase if not in test mode
                    if not test_mode:
                        attempt_purchase(driver, drop)
                    else:
                        print(f'🧪 Test Mode: Would attempt to purchase {drop}')

            previous_drops = current_drops

            # Wait before next check
            time_sleep(webpage_refresh_timer, driver)

        except KeyboardInterrupt:
            print('\\n⏹️ Monitoring stopped by user')
            break
        except Exception as e:
            print(f'\\n❌ Monitoring error: {e}')
            time.sleep(5)
            continue

    driver.quit()
    print('✅ Secret Lair monitor stopped')

def detect_secret_lair_drops(driver):
    """Detect available Secret Lair drops on the page"""
    drops = set()

    try:
        # Common selectors for Secret Lair products
        selectors = [
            '.product-card',
            '.drop-card',
            '.product-item',
            '[data-product]',
            '.product-title',
            'h2, h3, h4'  # Titles that might contain drop names
        ]

        for selector in selectors:
            try:
                elements = driver.find_elements('css selector', selector)
                for element in elements:
                    text = element.text.strip()
                    if text and ('secret lair' in text.lower() or 'drop' in text.lower() or '$' in text):
                        drops.add(text[:100])  # Limit length
            except:
                continue

        # Also check page title and main content
        try:
            page_text = driver.find_element('tag name', 'body').text
            if 'new' in page_text.lower() and 'secret lair' in page_text.lower():
                drops.add('New Secret Lair content detected')
        except:
            pass

    except Exception as e:
        print(f'❌ Error detecting drops: {e}')

    return drops

def attempt_purchase(driver, drop_name):
    """Attempt to purchase a Secret Lair drop"""
    global attempting_to_buy
    attempting_to_buy = True

    print(f'🛒 Attempting to purchase: {drop_name}')

    try:
        # Look for "Add to Cart" or "Buy Now" buttons
        purchase_selectors = [
            'button[data-action="add-to-cart"]',
            'button:contains("Add to Cart")',
            'button:contains("Buy Now")',
            'input[value*="Add"]',
            '.add-to-cart',
            '.buy-now',
            '.purchase-button'
        ]

        purchase_button = None
        for selector in purchase_selectors:
            try:
                purchase_button = driver.find_element('css selector', selector)
                if purchase_button.is_displayed() and purchase_button.is_enabled():
                    break
            except:
                continue

        if purchase_button:
            print('🎯 Found purchase button, clicking...')
            purchase_button.click()
            time.sleep(2)

            # Check if we need to continue to checkout
            try:
                checkout_button = driver.find_element('css selector', 'button:contains("Checkout"), .checkout-button, [data-action="checkout"]')
                if checkout_button.is_displayed():
                    print('💳 Proceeding to checkout...')
                    checkout_button.click()
            except:
                print('ℹ️ No additional checkout step found')

            print('✅ Purchase attempt completed!')
            send_notification(f'🎉 Successfully attempted purchase of {drop_name}')

        else:
            print('❌ No purchase button found')

    except Exception as e:
        print(f'❌ Purchase error: {e}')
    finally:
        attempting_to_buy = False

def send_notification(message):
    """Send notification via Twilio if configured"""
    print(f'📱 {message}')

    # Twilio notification (if configured)
    if toNumber != 'Your_Phone_Number' and fromNumber != 'Twilio_Phone_Number':
        try:
            client.messages.create(
                body=message,
                from_=fromNumber,
                to=toNumber
            )
            print('📨 SMS notification sent')
        except Exception as e:
            print(f'❌ SMS error: {e}')

if __name__ == "__main__":
    print('🌟 SECRET LAIR AGGRESSIVE MONITOR 🌟')
    print('====================================')
    print('Based on the aggressive store bot framework')
    print('Adapted for Secret Lair drop monitoring')
    print('')

    # Configuration check
    if test_mode:
        print('🧪 RUNNING IN TEST MODE')
        print('   - Will monitor for drops')
        print('   - Will NOT actually purchase')
        print('   - Change test_mode = False to enable purchasing')
        print('')

    try:
        secret_lair_monitor()
    except KeyboardInterrupt:
        print('\\n⏹️ Program interrupted by user')
    except Exception as e:
        print(f'\\n💥 Fatal error: {e}')