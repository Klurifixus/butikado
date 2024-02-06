# Earn-Shop: Hip-Hop Clothing E-commerce Platform

Welcome to Earn-Shop, the ultimate online destination for men's hip-hop clothing and accessories inspired by the vibrant styles of the '90s. Our platform caters to enthusiasts of skate, hip-hop, reggae, and the iconic '90s hip-hop fashion scene. Earn-Shop is built with dedication to offer a seamless shopping experience, featuring a curated collection of garments that embody the spirit of hip-hop culture.

## Features

- **Wide Selection of Products**: From urban T-shirts and hoodies to accessories, find exclusive items that resonate with the hip-hop and skate culture.
- **Secure Payment Gateway**: Integrated Stripe payment for a smooth and secure checkout process.
- **User Accounts**: Powered by Django's allauth, offering user authentication, registration, and account management.
- **Email Confirmation**: Utilizing Mailgun for order confirmation and communication.
- **Enhanced SEO**: Google Tag Manager (GTM) integration and a dedicated blog section to boost search engine visibility through engaging content.
- **Responsive Design**: Crafted with mobile and desktop users in mind, ensuring a great shopping experience on any device.

## Built With

- **Front-end**: HTML5, CSS3 with custom styles, Bootstrap 4 for responsive design, JavaScript for interactive elements.
- **Back-end**: Django 4.2 for robust back-end capabilities.
- **Database**: SQLite for development and PostgreSQL for production.
- **Payment Processing**: Stripe to handle financial transactions securely.
- **User Authentication**: Django Allauth for user management.
- **Email Delivery**: Mailgun for sending confirmation emails.
- **Media Storage**: Cloudinary for storing and managing media files efficiently.
- **SEO Optimization**: Google Tag Manager, Sitemap , Facebook for SEO and tracking analytics.

## Design

![Link to Color Theme](media/themecolor.png)
Our design philosophy is deeply rooted in the vibrant essence of '90s hip-hop culture and the rebellious spirit of skateboarding. The color theme, visualized in the linked image, draws from these dynamic eras, combining warm oranges and deep browns to evoke nostalgia and energy. We've meticulously chosen fonts like "Permanent Marker" to capture the bold and expressive graffiti art characteristic of hip-hop's golden age. Every element, from the background to interactive components, is crafted to immerse users in a shopping experience that not only resonates with the era's aesthetic but also meets modern expectations of functionality and responsiveness.

### Wireframes

[Link to Wireframes Markdown File](WIREFRAMES.md)

### Tests

[Link to Tests Markdown File](TESTING.md)

### Project overview

[Link to The project overview Markdown File](PROJECTOVERVIEW.md)


## Responsive Design

[Link to Responsive Markdown File](RESPONSIVE.md)

## Known, Issues and future Feature

### Styling or bugs:
[Issue #35 on GitHub](https://github.com/Klurifixus/butikado/issues/35)
[Issue #36 on GitHub](https://github.com/Klurifixus/butikado/issues/36)
[Issue #37 on GitHub](https://github.com/Klurifixus/butikado/issues/37)

### Future Features:
[Issue #14 on GitHub](https://github.com/Klurifixus/butikado/issues/14)
[Issue Draft on GitHub](https://github.com/users/Klurifixus/projects/16?pane=issue&itemId=51650410)
[Issue #28 on GitHub](https://github.com/Klurifixus/butikado/issues/28)
[Issue #22 on GitHub](https://github.com/Klurifixus/butikado/issues/22)
[Issue #38 on GitHub](https://github.com/Klurifixus/butikado/issues/38)

### Infomation about the future:
-Future enhancements for this page include updating profile pictures and enabling login through Google, Facebook, and Instagram for user convenience. There will also be features for users to save their favorite products, view them easily, and comment on blog posts, drawing inspiration from the [GitHub project for Submission project 4](https://github.com/Klurifixus/TheCornerForum/tree/herokugoal?tab=readme-ov-file#). This project's insights will significantly influence the upcoming functionalities, enhancing user engagement and interaction on the platform.

### ProjectBoard on Github
[Earn-shop project Board](https://github.com/users/Klurifixus/projects/16)

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python 3.8 or later
- pip
- A Mailgun account for email services
- A Stripe account for payment processing
- A Cloudinary account for media storage

### Installation

1. **Clone the repository**

   ```bash
    git clone https://github.com/Klurifixus/butikado.git
    cd earn-shop
    ```

2. **Set up a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**
   Create a .env file in the root directory and populate it with the necessary API keys and secrets as shown in the settings.py file.

5. **Run migrations to set up the database**
    ```bash
    python manage.py migrate # Navigate to http://localhost:8000 to view the app.
    ```

### Setting Up Your Development Environment

## Stripe Integration
1. Create a Stripe Account: Sign up at Stripe and navigate to the dashboard to retrieve your API keys.

2. Configure Stripe Keys: In your project's settings, add the following lines:
    ```bash
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', 'your_stripe_public_key')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', 'your_stripe_secret_key')
    ```

3. Use Environment Variables: Store your Stripe API keys in your .env file for local development and configure them in Heroku's Config   Vars for production.

## Django Allauth for Authentication
1. Install Django Allauth: Add 'allauth', 'allauth.account', and 'allauth.socialaccount' to your INSTALLED_APPS in settings.py.

2. Configure URLs: Include Allauth URLs in your project's urls.py:
    ```bash
    urlpatterns = [
    path('accounts/', include('allauth.urls')),
    ...]```

3.  Customize Allauth Settings: Configure your authentication settings in settings.py, such as ACCOUNT_AUTHENTICATION_METHOD,   ACCOUNT_EMAIL_REQUIRED, etc.   

## PostgreSQL Database on Heroku
1. Add PostgreSQL Add-on: From your Heroku dashboard, add the Heroku Postgres add-on to your application.

2. Configure Database URL: Heroku sets the DATABASE_URL environment variable for your application. Use it in your settings.py:
    ```bash
    import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}
```

3. Migrate Your Database: Run heroku run python manage.py migrate to migrate your database schema to Heroku Postgres.

## Mailgun for Email Delivery
1. Add Mailgun Add-on: In the Heroku dashboard, add the Mailgun add-on to your application.

2. Retrieve API Keys and SMTP Details: From the Mailgun dashboard, get your domain, API key, and SMTP credentials.

3. Configure Email Settings in Django: Update your settings.py with Mailgun SMTP settings:
    ```bash
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.mailgun.org'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = os.getenv('MAILGUN_SMTP_LOGIN')
    EMAIL_HOST_PASSWORD = os.getenv('MAILGUN_SMTP_PASSWORD')
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'Your Email <mail@example.com>'
    ```

4. Set Environment Variables: Store your Mailgun credentials in the .env file and configure them in Heroku's Config Vars.

## Additional Resources
* Stripe Documentation: https://stripe.com/docs
* Django Allauth Documentation: https://django-allauth.readthedocs.io/en/latest/installation.html
* Heroku Postgres: https://devcenter.heroku.com/articles/heroku-postgresql
* Mailgun with Django: https://documentation.mailgun.com/en/latest/quickstart-sending.html#send-with-smtp-or-api

### Contributing
    -We welcome contributions to Earn-Shop! If you have suggestions or improvements, please fork the repo and create a pull request.

### License:
    -Distributed under the MIT License. See LICENSE for more information. 

### Acknowledgements:
    - This project was inspired by and built upon the educational content from Code Institute's Boutique Ado project.      
    - Thanks to all the open-source packages and tools that made this project possible.
