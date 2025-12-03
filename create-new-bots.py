#!/usr/bin/env python3
"""
Quick script to create new MTG bot files from the avatar template
Updates product name, URL, price, and Chrome profile path
"""

import os

# Read the template
with open('avatar-collector-chrome-bot.py', 'r') as f:
    template = f.read()

# New products configuration
products = [
    {
        'name': 'Aetherdrift Collector Booster Box',
        'url': 'https://www.amazon.com/dp/B0DNV4FC7Y',
        'max_price': 280,
        'filename': 'aetherdrift-collector-chrome-bot.py',
        'profile_dir': 'aetherdrift_chrome_bot',
        'log_file': 'aetherdrift_bot.log',
        'port': '9224',
        'quantity': 2,
        'print_name': 'AETHERDRIFT'
    },
    {
        'name': 'Foundations Collector Booster Box',
        'url': 'https://www.amazon.com/dp/B0D9KZ7MRG',
        'max_price': 270,
        'filename': 'foundations-collector-chrome-bot.py',
        'profile_dir': 'foundations_chrome_bot',
        'log_file': 'foundations_bot.log',
        'port': '9225',
        'quantity': 2,
        'print_name': 'FOUNDATIONS'
    },
    {
        'name': 'Bloomburrow Collector Booster Box',
        'url': 'https://www.amazon.com/dp/B0CTKX417N',
        'max_price': 260,
        'filename': 'bloomburrow-collector-chrome-bot.py',
        'profile_dir': 'bloomburrow_chrome_bot',
        'log_file': 'bloomburrow_bot.log',
        'port': '9226',
        'quantity': 2,
        'print_name': 'BLOOMBURROW'
    }
]

for product in products:
    print(f"Creating {product['filename']}...")

    # Replace configuration values
    new_content = template

    # Update docstring
    new_content = new_content.replace(
        'CHROME VERSION - Avatar Collector Box Bot',
        f"CHROME VERSION - {product['name']} Bot"
    )

    # Update configuration section
    new_content = new_content.replace(
        'PRODUCT_NAME = "Avatar: The Last Airbender Collector Booster Box"',
        f'PRODUCT_NAME = "{product["name"]}"'
    )
    new_content = new_content.replace(
        'PRODUCT_URL = "https://www.amazon.com/Magic-Gathering-Airbender-Collector-Collectible/dp/B0FJNQ3DHX"',
        f'PRODUCT_URL = "{product["url"]}"'
    )
    new_content = new_content.replace(
        'MAX_PRICE = 500',
        f'MAX_PRICE = {product["max_price"]}'
    )

    # Update logging
    new_content = new_content.replace(
        "logging.FileHandler('avatar_bot.log')",
        f"logging.FileHandler('{product['log_file']}')"
    )

    # Update Chrome profile
    new_content = new_content.replace(
        "--user-data-dir=C:\\\\temp\\\\avatar_chrome_bot",
        f"--user-data-dir=C:\\\\temp\\\\{product['profile_dir']}"
    )

    # Update remote debugging port
    new_content = new_content.replace(
        '--remote-debugging-port=9223',
        f"--remote-debugging-port={product['port']}"
    )

    # Update print statements
    new_content = new_content.replace(
        'Starting Chrome for Avatar monitoring...',
        f"Starting Chrome for {product['name']} monitoring..."
    )
    new_content = new_content.replace(
        'CHROME AVATAR COLLECTORS BOX BOT',
        f"CHROME {product['print_name']} BOT"
    )
    new_content = new_content.replace(
        'Target Quantity: 4 boxes',
        f"Target Quantity: {product['quantity']} boxes"
    )
    new_content = new_content.replace(
        'Press Enter to start Chrome Avatar monitoring...',
        f"Press Enter to start Chrome {product['name']} monitoring..."
    )
    new_content = new_content.replace(
        'ATTEMPTING TO ADD 4 AVATAR COLLECTOR BOXES TO CART...',
        f"ATTEMPTING TO ADD {product['quantity']} {product['print_name']} BOXES TO CART..."
    )
    new_content = new_content.replace(
        'AVATAR COLLECTORS BOX AVAILABLE FROM AMAZON!',
        f"{product['print_name']} AVAILABLE FROM AMAZON!"
    )

    # Update quantity from 4 to 2 for new products
    new_content = new_content.replace(
        "option[value='4']",
        f"option[value='{product['quantity']}']"
    )
    new_content = new_content.replace(
        'quantity_dropdown.send_keys("4")',
        f'quantity_dropdown.send_keys("{product["quantity"]}")'
    )
    new_content = new_content.replace(
        'Set quantity to 4',
        f"Set quantity to {product['quantity']}"
    )
    new_content = new_content.replace(
        'Typed quantity as 4',
        f"Typed quantity as {product['quantity']}"
    )
    new_content = new_content.replace(
        'Updated cart quantity to 4',
        f"Updated cart quantity to {product['quantity']}"
    )

    # Update ASIN safety check (extract ASIN from URL)
    asin = product['url'].split('/')[-1]
    new_content = new_content.replace(
        "'B0FJNQ3DHX'",
        f"'{asin}'"
    )
    new_content = new_content.replace(
        'Expected ASIN B0FJNQ3DHX',
        f'Expected ASIN {asin}'
    )
    new_content = new_content.replace(
        'URL contains ASIN: B0FJNQ3DHX',
        f'URL contains ASIN: {asin}'
    )

    # Update title verification
    title_keywords = product['name'].lower().split()[0:2]  # First two words
    if 'avatar' in template:
        # Replace avatar/airbender checks with product-specific keywords
        new_content = new_content.replace(
            "if 'avatar' not in page_title and 'airbender' not in page_title:",
            f"if '{title_keywords[0]}' not in page_title:"
        )

    # Update final print statements
    new_content = new_content.replace(
        'Avatar Chrome bot stopped',
        f"{product['name']} Chrome bot stopped"
    )

    # Write the new file
    with open(product['filename'], 'w') as f:
        f.write(new_content)

    print(f"✅ Created {product['filename']}")

print("\n✅ All 3 new bot files created!")
print("\nNew bots:")
print("  - aetherdrift-collector-chrome-bot.py (Preorder - Feb 2025)")
print("  - foundations-collector-chrome-bot.py (Current set)")
print("  - bloomburrow-collector-chrome-bot.py (Summer 2024 set)")
print("\nTo run on Windows:")
print('  cd "C:\\Users\\client1\\Dropbox\\CardTracker\\Agressive-Store-Bots"')
print("  py aetherdrift-collector-chrome-bot.py")
