# Delivery Management Telegram Bot

A Telegram bot for managing orders with real-time status updates, built using Django and `python-telegram-bot`. This project enables users to check the status of their orders by sending their order ID to the bot.

---


## Project Overview

The **Delivery Management Telegram Bot** allows users to query the status of their orders by simply sending their order ID to the bot. The bot fetches the order status from a Django backend and responds with the order’s details including status, product name, and order creation date. 

### Features:
- **Order Lookup:** Users can query their orders by entering the order ID.
- **Order Status:** The bot provides real-time updates on the status of the order (Pending, In Progress, Delivered).
- **Django Backend:** The bot is connected to a Django project with an integrated database to store and manage order information.
- **Telegram Integration:** The bot is built using the `python-telegram-bot` library, making it easy to integrate with Telegram.

---

## Technologies Used

- **Python 3.x**
- **Django** (for backend)
- **python-telegram-bot** (for Telegram bot integration)
- **PostgreSQL** (for database)
- **asgiref.sync** (to handle synchronous Django ORM calls in an asynchronous bot context)




