# Quotebot

**Quotebot** is a lightweight Discord bot that generates aesthetic quote images from message replies. Just reply to someone’s message and mention the bot—Quotebot takes care of the rest.

## Goal

The purpose of Quotebot is to practice event-driven Discord bot development and integrate dynamic image generation using user data (name, avatar, and message content). It aims to replicate the functionality of quote-generation bots seen in Telegram or Reddit.

## Features

- Converts message replies into stylized quote images
- Captures sender's display name and avatar
- Automatically sends back the generated image in the same channel
- Temporary files are cleaned up after each use

## How It Works

1. You reply to someone’s message and mention the bot.
2. Quotebot fetches the original message, author info, and avatar.
3. `create_quote_image` generates the image.
4. The bot sends the image as a file.
5. `cleanup_image` deletes the temporary file.

## Libraries Used

- **discord.py** — For Discord bot events and message handling  
- **Pillow / OpenCV / other** — Used inside `image_generator.py` for image generation (assumed)  
- **os / shutil** — Likely used for cleanup logic

## Setup and Installation

1. Clone the repo and ensure you have Python 3.8+ installed  
2. Install dependencies (as per your `image_generator.py` logic):

    ```bash
    pip install discord.py pillow
    ```

3. Make sure your bot token is available:

    ```python
    client.run("your_token_here")
    ```

4. Run the bot:

    ```bash
    python main.py
    ```
