# Restaurant Web App

This is a comprehensive web application for a restaurant, developed using Django, HTML, and Jinja templates. The application allows customers to perform the following actions:

- Register and log in to their accounts.
- Browse and order various types of food, including pizza, burgers, fries, and pasta.
- Book a table for dining at the restaurant.

This project is hosted on GitHub: [Restaurant Web App](https://github.com/gitChandan123/Restaurant/tree/main

## Features

### 1. **User Authentication**
- **Registration**: New users can sign up with their email, username, and password.
- **Login**: Existing users can log in securely to access their accounts.
- **Session Management**: The application uses Django's session framework to manage user sessions.

### 2. **Food Ordering**
- A dynamic menu displays available food items categorized into different types (e.g., pizza, burgers, fries, pasta).
- Customers can add items to their cart and place an order.
- Real-time price calculation is available for items in the cart.

### 3. **Table Booking**
- Users can select a date and time to book a table at the restaurant.
- The system checks for availability and confirms the booking.

### 4. **Admin Panel**
- The Django admin panel is configured for managing user accounts, food items, and table bookings.
- Admins can add, update, or remove menu items and monitor orders.

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Templates**: Jinja (Django's templating engine)
- **Database**: SQLite (default Django database; can be replaced with PostgreSQL or MySQL as needed)
- **Authentication**: Django’s built-in authentication system

## Installation

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)
- Virtualenv (optional but recommended)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/gitChandan123/Restaurant.git
   cd Restaurant
   ```

2. **Create a Virtual Environment** (optional)
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Open your browser and navigate to `http://127.0.0.1:8000` to access the web app.
   - For the admin panel, visit `http://127.0.0.1:8000/admin`.

## Directory Structure

```
Restaurant/
├── manage.py          # Django's management script
├── Restaurant/        # Project settings and configurations
├── food/              # App handling food menu and orders
├── booking/           # App handling table bookings
├── templates/         # Jinja templates for frontend
├── static/            # Static files (CSS, JS, images)
├── db.sqlite3         # SQLite database (auto-generated after migrations)
└── requirements.txt   # List of dependencies
```

## Usage

### 1. **User Registration and Login**
- Navigate to the home page and click on "Sign Up" to create a new account.
- After registration, log in using your credentials.

### 2. **Browse Menu and Order Food**
- Browse the menu to view available food items.
- Add desired items to your cart.
- Proceed to checkout to place the order.

### 3. **Book a Table**
- Navigate to the "Book a Table" section.
- Select a date, time, and the number of guests.
- Confirm the booking.

### 4. **Admin Actions**
- Log in to the admin panel using the superuser account.
- Manage menu items, user accounts, orders, and table bookings.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your fork.
4. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or issues, please feel free to contact the project owner via [GitHub Issues](https://github.com/gitChandan123/Restaurant/issues).
write it for the github readme code
