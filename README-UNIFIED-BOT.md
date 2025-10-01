# 🎯 Unified MTG Chrome Bot

**EXPERIMENTAL: Multi-product monitoring with known issues**

⚠️ **RECOMMENDATION**: Use individual Chrome bots instead for simpler, more reliable monitoring

## Quick Start

```cmd
py unified-mtg-chrome-bot.py
```

## What It Does

- **One Chrome Instance**: All products monitored in separate tabs
- **Smart Timing**: Each product has individual check frequencies
- **Auto-Purchase**: Attempts to buy when Amazon Direct stock is found
- **Resource Efficient**: Much lighter than running multiple browsers

## Current Configuration

| Product | URL | Max Price | Quantity | Check Every |
|---------|-----|-----------|----------|-------------|
| Avatar Collector Box | [Amazon Link](https://www.amazon.com/Magic-Gathering-Airbender-Collector-Collectible/dp/B0FJNQ3DHX) | $500 | 4 | 3 seconds |
| Spider-Man Bundle | [Amazon Link](https://www.amazon.com/dp/B0DV1VCPQF) | $150 | 2 | 8 seconds |

## How It Works

1. **Opens Chrome** with multiple tabs (one per product)
2. **You log into Amazon** once in the main tab
3. **Bot monitors all products** simultaneously
4. **When Amazon Direct stock appears** → Automatic purchase attempt

## Adding New Products

Edit the `PRODUCTS` list in `unified-mtg-chrome-bot.py`:

```python
PRODUCTS = [
    # Existing products...
    {
        "name": "Your New MTG Product",
        "url": "https://www.amazon.com/dp/PRODUCT_ASIN",
        "max_price": 200,
        "target_quantity": 1,
        "check_frequency": 5  # seconds between checks
    }
]
```

## Dependencies

```cmd
pip install selenium webdriver-manager
```

## Issues & Limitations

❌ **Chrome popup problems** - Constantly brings window to front
❌ **Complex setup** - Login verification, headless mode switching
❌ **Focus prevention fails** - Chrome options don't prevent popups
❌ **Tab management complexity** - More moving parts to break
❌ **Harder to debug** - Multiple products in one instance

## Advantages vs Individual Bots (In Theory)

✅ **Single Chrome instance** vs multiple browsers
✅ **Less CPU/memory usage** (if it worked properly)
✅ **One login process**
✅ **Easy to add/remove products**

## Why Individual Bots Are Better

✅ **Simple setup** - Just run and log in
✅ **No popup issues** - Each runs independently
✅ **Easy to restart** - One product fails, others continue
✅ **Clear monitoring** - One product per window
✅ **Less complex** - Fewer points of failure

## Monitoring Output

```
🔄 Monitoring Round #1 at 12:34:56
🔍 Checking Avatar: The Last Airbender... at 12:34:56
📊 Avatar: The Last Airbender... - 🔴 Currently unavailable
💰 Price: $44.99
🔍 Checking Spider-Man Bundle at 12:34:58
📊 Spider-Man Bundle - 🟡 Third-party sellers available
💰 Price: $149.99
```

## When Stock Is Found

```
🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨
🚨 AVATAR: THE LAST AIRBENDER COLLECTOR BOOSTER BOX AVAILABLE FROM AMAZON! 🚨
🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨
🛒 ATTEMPTING TO ADD 4 Avatar: The Last Airbender... TO CART...
📦 Set quantity to 4
🎯 Found Add to Cart button: #add-to-cart-button
✅ Clicked Add to Cart!
🎉 SUCCESS! Item added to cart!
🚀 ATTEMPTING AUTO-CHECKOUT...
```

## Browser Requirements

- **Chrome** installed at `C:\Program Files\Google\Chrome\Application\chrome.exe`
- **Amazon account** with payment info saved
- **Internet connection**

## Safety Notes

- ⚠️ **Violates Amazon ToS** - use at your own risk
- ⚠️ **Risk of account suspension**
- ⚠️ **Monitor for policy changes**
- ✅ **Consider Discord notification bot** as safer alternative

## Troubleshooting

**Chrome won't start:**
- Close all Chrome windows first
- Check Chrome path in script

**SSL errors:**
- Script includes SSL error handling
- Restart if issues persist

**Login issues:**
- Make sure you're logged into Amazon in the main tab
- Check for 2FA prompts

**Can't find product:**
- Verify Amazon URLs are correct and not expired
- Check product availability manually

## File Structure

```
unified-mtg-chrome-bot.py    # Main unified bot
spider-man-chrome-bot.py     # Individual Chrome bot (backup)
avatar-collector-chrome-bot.py  # Individual Chrome bot (backup)
CLAUDE-PROJECT-NOTES.md      # Full development history
README-UNIFIED-BOT.md        # This file
```

---

**🚀 The unified bot is the recommended approach for monitoring multiple MTG products efficiently!**