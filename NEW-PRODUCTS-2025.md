# NEW MTG Products to Monitor - December 2025

**Created:** 2025-12-03
**Purpose:** Replace outdated Avatar/Spider-Man/Final Fantasy products with current MTG releases

---

## ⚠️ Why Update?

Your current bots monitor:
- Avatar: The Last Airbender ($500) - Limited edition, May be sold out/discontinued
- Spider-Man Bundle ($150) - Discontinued/flopped
- Final Fantasy ($200) - Limited edition, sold out since Sept

**These are crossover products with limited restocks**. You'll have better success monitoring regular MTG sets with ongoing print runs.

---

## 🎯 RECOMMENDED PRODUCTS (December 2025)

### 1. **Aetherdrift Collector Booster Box** ⭐ TOP PICK
- **Amazon URL:** https://www.amazon.com/dp/B0DNV4FC7Y
- **Release Date:** February 14, 2025 (PREORDER NOW)
- **MSRP:** $220-250
- **Status:** Available for preorder
- **Why Monitor:** New set releasing soon, preorders sellout fast
- **Suggested Max Price:** $280
- **Bot File:** Create `aetherdrift-collector-chrome-bot.py`

```python
PRODUCT_NAME = "Aetherdrift Collector Booster Box"
PRODUCT_URL = "https://www.amazon.com/dp/B0DNV4FC7Y"
MAX_PRICE = 280
REFRESH_SECONDS = 15
```

---

### 2. **Foundations Collector Booster Box** ⭐ RECOMMENDED
- **Amazon URL:** https://www.amazon.com/dp/B0D9KZ7MRG
- **Release Date:** November 15, 2024 (CURRENTLY AVAILABLE)
- **MSRP:** $220-250
- **Status:** In stock, regular restocks
- **Why Monitor:** New core set, long print run, consistent availability
- **Suggested Max Price:** $270
- **Bot File:** Create `foundations-collector-chrome-bot.py`

```python
PRODUCT_NAME = "Foundations Collector Booster Box"
PRODUCT_URL = "https://www.amazon.com/dp/B0D9KZ7MRG"
MAX_PRICE = 270
REFRESH_SECONDS = 15
```

---

### 3. **Bloomburrow Collector Booster Box** ⭐ STEADY OPTION
- **Amazon URL:** https://www.amazon.com/dp/B0CTKX417N
- **Release Date:** August 2, 2024
- **MSRP:** $200-230
- **Status:** Regular restocks, steady availability
- **Why Monitor:** Popular summer set, good secondary market value
- **Suggested Max Price:** $260
- **Bot File:** Create `bloomburrow-collector-chrome-bot.py`

```python
PRODUCT_NAME = "Bloomburrow Collector Booster Box"
PRODUCT_URL = "https://www.amazon.com/dp/B0CTKX417N"
MAX_PRICE = 260
REFRESH_SECONDS = 15
```

---

## 🔄 ALTERNATIVE OPTIONS

### 4. **Duskmourn Collector Booster Box**
- **Amazon:** Search "Duskmourn Collector Booster Box" (URL not retrieved)
- **Release:** September 27, 2024
- **MSRP:** ~$230
- **Why:** Horror-themed set, ongoing availability

### 5. **Murders at Karlov Manor Collector Box**
- **Release:** February 2024
- **Status:** May still have restocks
- **Why:** Popular mystery-themed set

---

## 📋 HOW TO UPDATE YOUR BOTS

### Option A: Quick Update (Replace Existing Bots)
1. Open `avatar-collector-chrome-bot.py`
2. Replace lines 32-34 with Aetherdrift config above
3. Save as `aetherdrift-collector-chrome-bot.py`
4. Repeat for other products

### Option B: Keep Old Bots + Add New Ones
1. Copy `avatar-collector-chrome-bot.py` three times
2. Rename to: `aetherdrift-collector-chrome-bot.py`, `foundations-collector-chrome-bot.py`, `bloomburrow-collector-chrome-bot.py`
3. Update the PRODUCT_NAME, PRODUCT_URL, and MAX_PRICE in each
4. Update Chrome profile paths (line 63):
   ```python
   options.add_argument('--user-data-dir=C:\\temp\\aetherdrift_chrome_bot')
   options.add_argument('--user-data-dir=C:\\temp\\foundations_chrome_bot')
   options.add_argument('--user-data-dir=C:\\temp\\bloomburrow_chrome_bot')
   ```

---

## 🎮 RUNNING THE NEW BOTS

### On Windows:
```cmd
cd "C:\Users\client1\Dropbox\CardTracker\Agressive-Store-Bots"

# Run one bot at a time
py aetherdrift-collector-chrome-bot.py

# Or run multiple in separate command windows
start cmd /k py aetherdrift-collector-chrome-bot.py
start cmd /k py foundations-collector-chrome-bot.py
start cmd /k py bloomburrow-collector-chrome-bot.py
```

---

## 📊 PRICE COMPARISON

| Product | MSRP | Suggested Max | Current Amazon |
|---------|------|--------------|----------------|
| Aetherdrift | $220-250 | $280 | Preorder |
| Foundations | $220-250 | $270 | In Stock |
| Bloomburrow | $200-230 | $260 | In Stock |
| Avatar (OLD) | $500 | $500 | Limited |
| Spider-Man (OLD) | $60-90 | $150 | Discontinued |
| Final Fantasy (OLD) | $150 | $200 | Sold Out |

**Notice:** The new products have MUCH better availability and more reasonable prices!

---

## ⚠️ IMPORTANT NOTES

1. **Amazon ToS:** These bots still violate Amazon ToS - use at your own risk
2. **Rate Limiting:** Keep REFRESH_SECONDS at 12-15 to avoid bans
3. **Login Required:** You'll need to log into Amazon manually when bots start
4. **Multiple Bots:** Run each bot in a separate Chrome profile to avoid conflicts
5. **Headless Mode:** Set `HEADLESS = False` to see what's happening

---

## 🔗 USEFUL LINKS

- **Amazon MTG Collector Boosters:** https://www.amazon.com/stores/MagicTheGathering/page/D01C48B3-6844-4B6F-B1AF-59A5B4665469
- **Wizards Latest Products:** https://magic.wizards.com/en/products
- **TCGPlayer (Alternative):** https://www.tcgplayer.com/search/magic/product?productLineName=magic&q=collector%20booster%20box&view=grid

---

## 📝 NEXT STEPS

1. Review the recommended products above
2. Choose which products you want to monitor (1-3 recommended)
3. Update your bot files with new URLs and prices
4. Test one bot first before running all of them
5. Monitor for a few days to gauge restock patterns

**Questions?** Check the bot status files or reach out!

---

**Last Updated:** 2025-12-03 05:40 PST
