# MTG Product Tracking List - December 2025

**Last Updated:** 2025-12-03
**Purpose:** Definitive list of MTG products to monitor with current bots

---

## 🎯 CURRENTLY CONFIGURED BOTS

These are the 3 new bots created and ready to run:

### 1. **Aetherdrift Collector Booster Box** ⭐ PRIORITY
- **Bot File:** `aetherdrift-collector-chrome-bot.py`
- **Amazon URL:** https://www.amazon.com/dp/B0DNV4FC7Y
- **ASIN:** B0DNV4FC7Y
- **Release Date:** February 14, 2025 **(PREORDER)**
- **MSRP:** $220-250
- **Bot Max Price:** $280
- **Target Quantity:** 2 boxes
- **Check Interval:** 15 seconds
- **Status:** Available for preorder
- **Why Monitor:** New set releasing in 2 months, preorders sell out fast
- **Best Time to Monitor:** Now through Feb 14, 2025
- **Expected Restocks:** Frequent before release, limited after release

---

### 2. **Foundations Collector Booster Box** ⭐ STEADY INCOME
- **Bot File:** `foundations-collector-chrome-bot.py`
- **Amazon URL:** https://www.amazon.com/dp/B0D9KZ7MRG
- **ASIN:** B0D9KZ7MRG
- **Release Date:** November 15, 2024
- **MSRP:** $220-250
- **Bot Max Price:** $270
- **Target Quantity:** 2 boxes
- **Check Interval:** 15 seconds
- **Status:** In stock, regular restocks
- **Why Monitor:** Core set with long print run (3+ years), consistent availability
- **Best Time to Monitor:** Anytime (always in rotation)
- **Expected Restocks:** Daily/weekly, very predictable

---

### 3. **Bloomburrow Collector Booster Box** ⭐ VALUE PLAY
- **Bot File:** `bloomburrow-collector-chrome-bot.py`
- **Amazon URL:** https://www.amazon.com/dp/B0CTKX417N
- **ASIN:** B0CTKX417N
- **Release Date:** August 2, 2024
- **MSRP:** $200-230
- **Bot Max Price:** $260
- **Target Quantity:** 2 boxes
- **Check Interval:** 15 seconds
- **Status:** Regular restocks
- **Why Monitor:** Popular summer set, good secondary market value
- **Best Time to Monitor:** Now through early 2025
- **Expected Restocks:** Weekly, decreasing frequency over time

---

## 📅 UPCOMING RELEASES TO WATCH

### Tarkir: Dragonstorm (April 2025)
- **Amazon URL:** Not yet available
- **Expected Preorder:** January/February 2025
- **MSRP Estimate:** $220-250
- **Why Watch:** Return to popular plane, high anticipated demand
- **Action:** Add bot when preorder goes live

### Modern Horizons 4 (May/June 2025)
- **Amazon URL:** Not yet available
- **Expected Preorder:** March/April 2025
- **MSRP Estimate:** $260-300+ (premium set)
- **Why Watch:** Modern Horizons sets always sell out instantly
- **Action:** HIGH PRIORITY when announced

---

## 🔄 RECENT SETS STILL WORTH MONITORING

### Duskmourn: House of Horror Collector Box
- **Amazon:** Search "Duskmourn Collector Booster Box"
- **Release:** September 27, 2024
- **MSRP:** ~$230
- **Status:** Occasional restocks
- **Bot Recommendation:** Add if you want 4th bot

### Murders at Karlov Manor Collector Box
- **Amazon:** Search "Murders at Karlov Manor Collector"
- **Release:** February 2024
- **MSRP:** ~$220
- **Status:** Sporadic restocks
- **Bot Recommendation:** Low priority

---

## ❌ PRODUCTS TO AVOID (Limited/Sold Out)

### Avatar: The Last Airbender
- **Current Bot:** `avatar-collector-chrome-bot.py` (OLD)
- **Status:** Limited edition crossover, mostly sold out
- **MSRP:** $500+
- **Why Avoid:** Extremely limited print run, unlikely restocks
- **Action:** REPLACE with Aetherdrift bot

### Spider-Man Bundle
- **Current Bot:** `spider-man-chrome-bot.py` (OLD)
- **Status:** Discontinued/flopped
- **MSRP:** $60-150
- **Why Avoid:** Poor sales, no demand, no restocks
- **Action:** REPLACE with Foundations bot

### Final Fantasy
- **Current Bot:** `final-fantasy-chrome-bot.py` (OLD)
- **Status:** Sold out since September 26
- **MSRP:** $150-200
- **Why Avoid:** Limited crossover set, extremely limited restocks
- **Action:** REPLACE with Bloomburrow bot

---

## 🛍️ RETAILER COMPARISON

| Retailer | Pros | Cons | Bot Support |
|----------|------|------|-------------|
| **Amazon** | Fast shipping, easy returns, consistent stock | Higher prices, bot detection | ✅ Full support |
| **TCGPlayer** | Best prices, huge selection | Slower shipping, multiple sellers | ❌ Not supported |
| **Card Kingdom** | Excellent service, buylist | Limited collector boxes | ❌ Not supported |
| **Best Buy** | Good prices, in-store pickup | Limited MTG selection | ⚠️ Possible (would need new bot) |
| **GameStop** | In-store availability | Inconsistent stock | ⚠️ Possible (would need new bot) |

**Current Focus:** Amazon only (most reliable for automation)

---

## 📊 PRICE TRACKING RECOMMENDATIONS

### What to Pay for Collector Boxes:

| Set | MSRP | Good Deal | Fair Price | Overpriced |
|-----|------|-----------|------------|------------|
| **Aetherdrift** | $220-250 | <$240 | $240-270 | >$280 |
| **Foundations** | $220-250 | <$240 | $240-265 | >$270 |
| **Bloomburrow** | $200-230 | <$220 | $220-255 | >$260 |
| **Duskmourn** | $220-250 | <$235 | $235-260 | >$265 |

**Bot Max Prices Set:**
- Aetherdrift: $280 (allows for small premium on preorder)
- Foundations: $270 (standard markup)
- Bloomburrow: $260 (value play)

---

## ⏰ MONITORING SCHEDULE RECOMMENDATIONS

### Optimal Bot Running Times:

**Weekdays:**
- 6AM-10AM EST: Amazon restocks common
- 12PM-2PM EST: Midday restocks
- 5PM-8PM EST: Evening restocks

**Weekends:**
- Saturday 8AM-12PM EST: Weekend restocks
- Sunday: Generally slower

**Special Events:**
- New set releases: Monitor 24/7 for 48 hours
- Preorder announcements: Monitor 24/7 for 24 hours
- Black Friday/Cyber Monday: Monitor 24/7

**Current Recommendation:**
- Run Aetherdrift bot daily 8AM-6PM (preorder window)
- Run Foundations bot 2-3 times per week (steady availability)
- Run Bloomburrow bot 1-2 times per week (moderate frequency)

---

## 🔧 BOT CONFIGURATION QUICK REFERENCE

```python
# Aetherdrift
PRODUCT_NAME = "Aetherdrift Collector Booster Box"
PRODUCT_URL = "https://www.amazon.com/dp/B0DNV4FC7Y"
MAX_PRICE = 280
REFRESH_SECONDS = 15
QUANTITY = 2

# Foundations
PRODUCT_NAME = "Foundations Collector Booster Box"
PRODUCT_URL = "https://www.amazon.com/dp/B0D9KZ7MRG"
MAX_PRICE = 270
REFRESH_SECONDS = 15
QUANTITY = 2

# Bloomburrow
PRODUCT_NAME = "Bloomburrow Collector Booster Box"
PRODUCT_URL = "https://www.amazon.com/dp/B0CTKX417N"
MAX_PRICE = 260
REFRESH_SECONDS = 15
QUANTITY = 2
```

---

## 📈 EXPECTED ROI & FLIP POTENTIAL

### Collector Box Flipping Strategy:

**Aetherdrift (Preorder):**
- Buy at: $240-280
- Expected market price at release: $280-320
- Potential profit: $20-60 per box
- Hold time: 2-3 months
- Risk: Medium (new set, unknown demand)

**Foundations (Long-term hold):**
- Buy at: $240-270
- Expected price in 6-12 months: $300-350
- Potential profit: $60-110 per box
- Hold time: 6-12 months
- Risk: Low (core set, guaranteed long-term value)

**Bloomburrow (Quick flip):**
- Buy at: $220-260
- Current market price: $260-290
- Potential profit: $20-50 per box
- Hold time: Immediate to 3 months
- Risk: Low (established demand)

---

## 🚨 ALERTS & NOTIFICATIONS

### When Bots Find Stock:

1. **Add to cart automatically** (configured in bot)
2. **Alert sound** (Windows notification)
3. **Console output** (bot terminal shows big alerts)
4. **Manual checkout** (you complete the purchase)

### What to Do When Alerted:

1. Check the browser window (bot opens it)
2. Verify product and price
3. Log into Amazon if needed
4. Complete checkout manually
5. Let bot continue monitoring for more stock

---

## 📱 MOBILE MONITORING (Future Enhancement)

**Not Currently Supported:**
- Discord webhook notifications
- SMS/text alerts
- Email notifications
- Mobile app integration

**Possible Future Addition:**
- Add Twilio SMS (already in requirements.txt)
- Add Discord webhooks
- Integrate with existing URL-Monitor Discord bot

---

## 🔗 USEFUL LINKS

- **Amazon MTG Collector Boosters:** https://www.amazon.com/stores/MagicTheGathering/page/D01C48B3-6844-4B6F-B1AF-59A5B4665469
- **Wizards Products Page:** https://magic.wizards.com/en/products
- **MTGGoldfish Price Tracker:** https://www.mtggoldfish.com/prices/select
- **TCGPlayer Market Prices:** https://www.tcgplayer.com/search/magic/product?productLineName=magic&q=collector%20booster%20box

---

## 📝 MAINTENANCE LOG

### 2025-12-03: Initial Setup
- Created 3 new bots for current MTG products
- Replaced outdated Avatar/Spider-Man/Final Fantasy bots
- Set competitive max prices based on market research
- Configured for 2-box purchases (safer than 4)

### Next Review: 2025-01-15
- Check Aetherdrift preorder status
- Monitor Foundations restock frequency
- Evaluate Bloomburrow market prices
- Research Tarkir Dragonstorm preorder dates

---

**Questions or updates?** Edit this file and commit to GitHub!

**Last Updated:** 2025-12-03 05:50 PST
