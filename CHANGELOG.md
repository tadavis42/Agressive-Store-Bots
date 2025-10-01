# Changelog - MTG Bot System

All notable changes to the MTG monitoring bot system are documented in this file.

## [2.1.0] - 2025-09-28

### 🚀 Major Enhancements

#### Speed Optimization & Anti-Detection
- **Final Fantasy Bot**: Enhanced monitoring speed from 18s → 8s checks
- **Advanced Anti-Detection**: Human-like behavior patterns, random scrolling, variable timeouts
- **Webdriver Masking**: Removes automation indicators, adds realistic browser fingerprints
- **Randomized Timing**: Variable delays (2-12s) with occasional human-like breaks (30-90s)

#### Discord Bot Optimization
- **Disabled Reddit Monitoring**: Removed noisy Reddit news updates that were drowning out product alerts
- **Enhanced Product Focus**: Clean notifications for actual stock availability only
- **Added Final Fantasy**: New product monitoring in Discord configuration
- **Updated URLs & Prices**: Fixed Spider-Man product URL and price targets

### 🔧 Bot Improvements

#### All Chrome Bots
- **Enhanced Rate Limiting**: Progressive backoff with randomized delays
- **Better Error Handling**: Comprehensive timeout and navigation error management
- **Debug Enhancement**: Detailed progress tracking and status reporting

#### Spider-Man Bot
- **URL Fix**: Updated to correct Amazon product URL with proper parameters
- **Price Update**: Increased max price from $60 → $150 to match current market
- **Enhanced Detection**: Better Amazon Direct seller identification

#### Avatar Bot
- **Rate Limiting**: Improved timing (12s checks) with randomization
- **Detection Logic**: Enhanced availability status checking

### 📋 Configuration Updates
- **Discord Config**: Added Final Fantasy product monitoring
- **Target Prices**: Updated all product price thresholds
- **Check Intervals**: Optimized timing across all monitoring systems

### 🛡️ Security & Stealth
- **Advanced Browser Fingerprinting**: Realistic plugins, languages, and properties
- **Human Behavior Simulation**: Random page interactions, scrolling patterns
- **Pattern Avoidance**: Non-uniform timing and occasional breaks
- **Enhanced Chrome Options**: Additional stealth flags and configurations

---

## [2.0.1] - 2025-09-24

### 🔧 Critical Fixes

#### Amazon Session Dialog Handling
- **Added**: `handle_amazon_dialogs()` function to all Chrome bots
- **Fixed**: "Keep Shopping?" dialog interruptions
- **Resolved**: "Status unclear" repeated messages
- **Enhanced**: Automatic dismissal of Amazon session timeouts

#### Rate Limiting Protection
- **Spider-Man Bot**: 8s → 15s checks with randomization
- **Avatar Bot**: 3s → 12s checks with randomization
- **Added**: Progressive backoff after consecutive errors
- **Enhanced**: Cooldown periods and error recovery

### 🆕 New Features
- **Final Fantasy Bot**: Created new Chrome bot for Chocobo Bundle monitoring
- **Enhanced Error Handling**: Better timeout management and recovery
- **Debug Logging**: Comprehensive status reporting and error tracking

---

## [2.0.0] - 2025-09-22

### 🎉 Initial Release
- **Chrome Bot Architecture**: Individual monitoring bots for each product
- **Discord Integration**: URL-Monitor bot with Quick Purchase features
- **Multi-Product Support**: Avatar, Spider-Man, and Secret Lair monitoring
- **Automated Purchasing**: Full checkout automation with quantity management
- **Anti-Detection**: Basic stealth features and profile management

### 🎯 Core Features
- **Amazon Direct Focus**: Only purchase from Amazon, ignore third-party sellers
- **Real-time Monitoring**: Continuous availability checking
- **Quick Purchase**: Instant browser opening for manual completion
- **Error Recovery**: Automatic restart and reconnection handling
- **Profile Management**: Dedicated Chrome profiles for each bot

---

## Key Files Modified

### Python Bots
- `final-fantasy-chrome-bot.py` - Enhanced speed & anti-detection
- `spider-man-chrome-bot.py` - URL fix & enhanced detection
- `avatar-collector-chrome-bot.py` - Rate limiting improvements
- All bots: Session dialog handling, error recovery

### Discord Bot
- `src/core/discord-bot.js` - Disabled Reddit monitoring
- `config.json` - Added Final Fantasy, updated URLs/prices

### Documentation
- `ACTUAL-WORKING-STATUS.md` - Current system status
- `CURRENT-STATUS.md` - Quick reference guide
- `CLAUDE-PROJECT-NOTES.md` - Technical documentation
- `CHANGELOG.md` - This file

## Migration Notes

### From v2.0.1 to v2.1.0
1. **Restart all Chrome bots** to use enhanced anti-detection
2. **Restart Discord bot** to disable Reddit monitoring
3. **Monitor effectiveness** of faster Final Fantasy checks
4. **Consider target evaluation** - current products may have limited restocks

### Breaking Changes
- Discord bot no longer sends Reddit notifications
- Final Fantasy bot now checks every 8 seconds (much faster)
- Spider-Man bot URL changed to new Amazon format

## Performance Improvements

### Speed Gains
- Final Fantasy: 2.25x faster monitoring (18s → 8s average)
- All bots: Enhanced randomization prevents detection
- Discord: Eliminated noise, focus on actionable alerts

### Reliability
- Advanced error recovery and timeout handling
- Human-like behavior patterns reduce blocking risk
- Progressive backoff prevents rate limiting issues

---

**For technical support or questions, refer to the detailed documentation in `CLAUDE-PROJECT-NOTES.md`**