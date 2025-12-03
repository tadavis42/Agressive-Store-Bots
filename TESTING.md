# Testing Guide for TMNT Bot on tadbox

**Last Updated:** 2025-12-03
**Bot:** tmnt-collector-chrome-bot.py
**Platform:** Linux (tadbox Ubuntu 24.04)

---

## Prerequisites

### 1. Verify Python Environment
```bash
cd /home/tadavis/bots/CardTracker/Agressive-Store-Bots
source venv/bin/activate
python3 --version  # Should be Python 3.x
```

### 2. Verify Dependencies
```bash
pip list | grep -E "selenium|webdriver-manager|beautifulsoup4"
```

Should show:
- selenium
- webdriver-manager
- beautifulsoup4
- twilio (optional)

### 3. Install Chromium (if not already installed)
```bash
# Check if chromium is installed
which chromium chromium-browser

# If not installed, install via apt:
sudo apt update
sudo apt install -y chromium-browser chromium-chromedriver

# OR install via snap:
sudo snap install chromium
```

---

## Testing Steps

### Test 1: Dry Run (Check for Errors)
```bash
cd /home/tadavis/bots/CardTracker/Agressive-Store-Bots
source venv/bin/activate

# Run bot - it will ask you to press Enter to start
python3 tmnt-collector-chrome-bot.py
```

**Expected behavior:**
1. Bot starts and prints configuration
2. Opens Chrome/Chromium browser window
3. Asks you to log into Amazon
4. Press Enter to start monitoring
5. Bot checks product availability every 5-13 seconds

**What to watch for:**
- Chrome/Chromium opens successfully
- Amazon page loads without errors
- No webdriver errors in console
- Bot displays status updates

### Test 2: Headless Mode (Background Operation)
Edit the bot configuration:
```bash
nano tmnt-collector-chrome-bot.py
```

Change line 41:
```python
HEADLESS = False  # Change to True
```

Then run:
```bash
python3 tmnt-collector-chrome-bot.py --auto
```

**Expected behavior:**
- No browser window opens
- Bot runs in background
- Status messages appear in terminal
- Log file created: `tmnt_bot.log`

### Test 3: Check Logs
```bash
# View real-time logs
tail -f tmnt_bot.log

# View last 50 lines
tail -50 tmnt_bot.log

# Search for errors
grep -i error tmnt_bot.log
```

---

## Running Bot Continuously

### Option 1: Screen Session (Recommended)
```bash
# Create new screen session
screen -S tmnt-bot

# Inside screen, activate venv and run bot
cd /home/tadavis/bots/CardTracker/Agressive-Store-Bots
source venv/bin/activate
python3 tmnt-collector-chrome-bot.py --auto

# Detach from screen: Ctrl+A then D
# Reattach to screen: screen -r tmnt-bot
# List screens: screen -ls
```

### Option 2: Background Process
```bash
cd /home/tadavis/bots/CardTracker/Agressive-Store-Bots
source venv/bin/activate
nohup python3 tmnt-collector-chrome-bot.py --auto > tmnt_output.log 2>&1 &

# Get process ID
echo $!

# Check if running
ps aux | grep tmnt-collector

# Stop bot
pkill -f tmnt-collector-chrome-bot.py
```

### Option 3: Systemd Service (Most Robust)
Create service file:
```bash
sudo nano /etc/systemd/system/tmnt-bot.service
```

Add:
```ini
[Unit]
Description=TMNT Collector Box Amazon Monitor Bot
After=network.target

[Service]
Type=simple
User=tadavis
WorkingDirectory=/home/tadavis/bots/CardTracker/Agressive-Store-Bots
Environment="PATH=/home/tadavis/bots/CardTracker/Agressive-Store-Bots/venv/bin"
ExecStart=/home/tadavis/bots/CardTracker/Agressive-Store-Bots/venv/bin/python3 tmnt-collector-chrome-bot.py --auto
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable tmnt-bot.service
sudo systemctl start tmnt-bot.service
sudo systemctl status tmnt-bot.service

# View logs
sudo journalctl -u tmnt-bot.service -f
```

---

## Troubleshooting

### Issue: Chrome/Chromium Not Found
**Error:** `WebDriverException: chrome not reachable`

**Solution:**
```bash
# Install Chromium
sudo apt install -y chromium-browser chromium-chromedriver

# Or via snap
sudo snap install chromium

# Update webdriver-manager cache
cd /home/tadavis/bots/CardTracker/Agressive-Store-Bots
source venv/bin/activate
pip install --upgrade webdriver-manager
```

### Issue: Permission Denied on Chrome Profile
**Error:** `Permission denied: '/tmp/tmnt_chrome_bot'`

**Solution:**
```bash
# Clear old profile
rm -rf /tmp/tmnt_chrome_bot

# Create with correct permissions
mkdir -p /tmp/tmnt_chrome_bot
chmod 755 /tmp/tmnt_chrome_bot
```

### Issue: Amazon Blocks Bot
**Symptoms:**
- CAPTCHA appears
- "We're sorry, something went wrong" message
- Rate limiting errors

**Solution:**
1. Increase `REFRESH_SECONDS` in bot configuration (currently 5s, try 10-15s)
2. Add more random delays
3. Run less frequently
4. Use residential IP or VPN

### Issue: Bot Stops Responding
**Check:**
```bash
# See if process is hung
ps aux | grep tmnt-collector

# Kill and restart
pkill -f tmnt-collector-chrome-bot.py

# Check system resources
top
df -h
free -h
```

---

## Monitoring Recommendations

### Best Times to Run
Based on Amazon restock patterns:

**High Priority Times:**
- Weekdays: 6AM-10AM EST (morning restocks)
- Weekdays: 12PM-2PM EST (midday restocks)
- Weekdays: 5PM-8PM EST (evening restocks)
- Saturday: 8AM-12PM EST (weekend restocks)

**Lower Priority:**
- Sundays (generally slower)
- Late night hours (11PM-5AM)

### Suggested Schedule
**Before March 6, 2026 release:**
- Run continuously during business hours (8AM-8PM EST)
- Monitor logs daily for activity

**After March 6, 2026 release:**
- Run 24/7 for first 2 weeks
- Then scale back to high-priority times

---

## Performance Metrics

### What to Track
1. **Check frequency:** Should average 1 check every 6-13 seconds
2. **Error rate:** Should be < 5% of checks
3. **Restart frequency:** Should not restart more than 2-3 times per hour
4. **Memory usage:** Should stay under 500MB

### Check Metrics
```bash
# Count total checks in last hour
grep "Checking TMNT" tmnt_bot.log | tail -500 | wc -l

# Count errors in last hour
grep -i error tmnt_bot.log | tail -100 | wc -l

# Check memory usage
ps aux | grep tmnt-collector | awk '{print $6/1024 " MB"}'
```

---

## Product Information

### TMNT Collector Booster Box Details
- **Amazon URL:** https://www.amazon.com/Magic-Gathering-Teenage-Collector-Collectible/dp/B0FR6HHZKB
- **ASIN:** B0FR6HHZKB
- **MSRP:** $456 (WotC suggested $37.99 per pack x 12)
- **Current Market:** $1000+ (resale)
- **Release Date:** March 6, 2026
- **Preorder Status:** Sold out in 5 minutes (October 2025)

### Contents
- 12 Collector Booster Packs
- 15 foil cards per pack (180 total)
- Exclusive Kevin Eastman "Headliner" art cards
- Traditional Foil double-sided tokens

### Why High Value
1. Limited print run (Universes Beyond set)
2. Nostalgia factor (TMNT franchise)
3. Exclusive art by original creator
4. Sold out instantly on all major retailers
5. High resale demand from collectors

---

## Security Notes

### Amazon ToS
⚠️ **WARNING:** This bot violates Amazon Terms of Service

**Risks:**
- Account suspension
- Purchase cancellations
- IP bans

**Mitigation:**
- Use dedicated Amazon account for bot
- Don't run 24/7 at high frequency
- Add random delays
- Monitor manually as backup

### Bot Safety Features
The bot includes safety checks:
1. Verifies correct product ASIN before purchase
2. Verifies product title contains "TMNT" or "Teenage Mutant Ninja Turtles"
3. Checks price against MAX_PRICE ($500 limit)
4. Logs all actions for audit trail
5. Requires manual Amazon login (no stored credentials)

---

## Next Steps After Testing

1. **Verify bot works:** Run Test 1 above
2. **Check logs:** Ensure no errors
3. **Set up continuous run:** Use Screen or systemd
4. **Monitor daily:** Check logs for activity
5. **Be ready:** When bot finds stock, act fast (5 minute sellout window)

---

## Quick Reference Commands

```bash
# Start bot in screen
screen -S tmnt-bot
cd /home/tadavis/bots/CardTracker/Agressive-Store-Bots && source venv/bin/activate && python3 tmnt-collector-chrome-bot.py --auto

# Detach: Ctrl+A then D
# Reattach: screen -r tmnt-bot

# Check logs
tail -f tmnt_bot.log

# Stop bot
pkill -f tmnt-collector-chrome-bot.py

# Check if running
ps aux | grep tmnt-collector
```

---

**Questions?** Check the bot code comments or commit history on GitHub:
https://github.com/tadavis42/Agressive-Store-Bots
