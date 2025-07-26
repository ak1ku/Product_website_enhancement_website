# Product Catalog

This project is a Django-based web application for managing a product catalog, allowing users to browse products, manage their profiles, and utilize a shopping cart and wishlist feature.

## Features

- User registration and authentication
- Product listing with filtering options
- Detailed product view with reviews
- Add products to cart and manage cart items
- Wishlist functionality
- User profile management

## Technologies Used

- Django
- HTML/CSS
- JavaScript
- Bootstrap/TailwindCSS (for UI improvements)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd product-catalog
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Deployment

For deployment, you can use platforms like Heroku, Render, or Vercel. Follow the respective platform's documentation for deploying Django applications.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.