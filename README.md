# MTG Collector Box Auto-Purchase Bots

**Last Updated:** 2025-12-03
**Purpose:** Automated monitoring and purchasing of Magic: The Gathering Collector Booster Boxes from Amazon

---

## 🎯 QUICK START (2025 MTG Bots)

### Current Bots (December 2025):
1. **aetherdrift-collector-chrome-bot.py** - Preorder monitoring (Feb 2025 release)
2. **foundations-collector-chrome-bot.py** - Core set with long print run
3. **bloomburrow-collector-chrome-bot.py** - Popular summer 2024 set

### Running a Bot:
```cmd
cd "C:\Users\client1\Dropbox\CardTracker\Agressive-Store-Bots"
py aetherdrift-collector-chrome-bot.py
```

**📋 Product List:** See [PRODUCT-TRACKING-LIST.md](PRODUCT-TRACKING-LIST.md) for detailed product information
**🆕 Setup Guide:** See [NEW-PRODUCTS-2025.md](NEW-PRODUCTS-2025.md) for quick setup instructions

---

## ⚠️ IMPORTANT WARNINGS

- **Amazon ToS:** These bots violate Amazon Terms of Service - use at your own risk
- **Automated Purchases:** Bots attempt to automatically add items to cart and checkout
- **Manual Login Required:** You must log into Amazon when the bot starts
- **Chrome Profiles:** Each bot uses a separate Chrome profile to avoid conflicts

---

## 📦 Original Generic Bot Instructions

Hello GitHub, I would like to share my method of creating a aggressive Bestbuy Bot in Python. I will be using Beautifulsoup4, Selenium, and Twilio in this script. Please continue reading this for instructions on how to set up bot.

If you guys need instructions to set up Newegg Bot or Amazon Bot go to my Google Drive here.

[Newegg](https://docs.google.com/document/d/1xcjMNAdIkPhpz6msJqtGEPkikk-0FP5AB8ciKRa_OMY/edit?usp=sharing)

[Amazon](https://docs.google.com/document/d/1zYQ1W-htAN5aWVw5kMb5NLa7ZwZB47cwqNZao73eiK4/edit?usp=sharing)


**You can test bot with this URL.**

	https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&qp=currentprice_facet%3DPrice~Less%20than%20%2425&sc=Global&st=hdmi&type=page&usc=All%20Categories
	
**Do Not Use a URL like this. If you compare both URL's you'll see the difference. Make sure URL looks like the page above. Otherwise bot will not work.**

	https://www.bestbuy.com/site/dynex-6-hdmi-cable-black/6405508.p?skuId=6405508

**1. Download Pycharm Community Edition & Firefox.**

[PyCharm Community Edition](https://www.jetbrains.com/pycharm/download)

[FireFox](https://www.mozilla.org/en-US/firefox/new/)

**2. Create a new project called bestbuybot and select create.**
![](images/step2.png)

**3. Go to terminal and type:**
'pip install -r requirements.txt' (pip3 if using python3)

![](images/step3.png)

**4. Right click bestbuybot folder, and create new python file.**
![](images/step4.png)

**5. Copy and paste bestbuy aggressive bot script in that python file you just created.**
![](images/step5.png)

**6. Fill out the script with your personal information.**

	* Twilio Information(optional)

	* CVV number

	* Add your Firefox profile. To find Firefox profile type "about:profiles" in firefox. It is the Root Directory path.
![](images/step6.png)


**7. To run bot, click run then select bestbuy.**

![](images/step7.png)
