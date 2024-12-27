from asgiref.sync import sync_to_async
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize Django
django.setup()

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from orders.models import Order  # Import Order model after django.setup()

BOT_TOKEN = ''
BOT_USERNAME: Final = '@'


@sync_to_async
def get_order_by_id(order_id: int) -> str:
    """
    Synchronously retrieves the order by its ID and returns a string with its details.
    This function is wrapped with sync_to_async to allow use in an async context.
    """
    try:
        # Search for the order in the database
        order = Order.objects.get(id=order_id)
        return (
            f"Order ID: {order.id}\n"
            f"Status: {order.get_status_display()}\n"  # Use get_status_display() for a readable status
            f"Created: {order.created.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Product: {order.product_name}\n"
            f"Address: {order.address}"
        )
    except Order.DoesNotExist:
        return f"Order with ID {order_id} does not exist."


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles the /start command.
    """
    username = update.message.from_user.username
    await update.message.reply_text(
        f"Hello, {username}! I am a Management Order Bot.\nPlease enter your Order ID to check its status."
    )


async def handle_order_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles messages sent to the bot. Expects an order ID as the input.
    """
    text = update.message.text.strip()
    if text.isdigit():
        # If the message is a number, assume it's an order ID
        order_id = int(text)
        response = await get_order_by_id(order_id)  # Use await to handle the async function
    else:
        # If the message is not a number, send an error message
        response = "Invalid input. Please send a valid numeric Order ID."

    await update.message.reply_text(response)


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_order_query))

    print('Polling...')
    app.run_polling(poll_interval=3)
