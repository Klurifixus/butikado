# Earn-Shop

## Project Overview

Earn-Shop is an online storefront specializing in hip-hop and skate clothing, skateboards, and exclusive watches.

## High-Level Architecture

- **Web Server**: [Details about the web server setup]
- **WSGI Application**: `butikado.wsgi.application` serves as the entry point for WSGI-compatible servers.
- **Database**: Production uses [Production Database], with SQLite for development.
- **Static/Media Files**: Static files are managed by WhiteNoise, with media served via Cloudinary.
- **Third-party Services**: Stripe for payments, Mailgun for email services.

## Settings.py Overview

- **Installed Apps**: Lists each Django app (`home`, `products`, 'bag', 'checkout', 'profiles') and their purpose.
- **Middleware**: Describes each middleware component in the `MIDDLEWARE` setting.
- **Templates**: Outlines the structure and location of template directories.
- **Static Files**: Details static file management using `STATIC_ROOT` and `STATIC_URL`.
- **Media Files**: Explains the management and serving of media files, particularly through Cloudinary.
- **Authentication**: Details the Django Allauth system for authentication.
- **Email Configuration**: Documents the setup for email dispatch via Mailgun.
- **Security Settings**: Outlines SSL and cookie security settings for production.

## URLs and Routing

- **Core URL Patterns**: The butikado/urls.py defines core URL patterns for the project, including routes for the admin interface, user accounts (via Django Allauth), and specific app sections like home, products, bag, checkout, profiles, and blog. It also includes custom paths for terms of use and privacy policy pages, alongside configuration to serve media files in development. This setup organizes access to different parts of the application, ensuring clear navigation and functionality separation.
- **App URL Patterns**: Each app within the project defines its own URL patterns, which map URLs to their corresponding views. For instance, the home app includes routes for the landing page and other static pages, products app handles product listings and detail views, bag app manages shopping cart functionality, checkout app oversees the payment process, and profiles app manages user profiles. The blog app provides URLs for blog posts and categories. These patterns ensure that each section of the application is accessible through a clear and logical URL structure.

## Database Schema

### `UserProfile`
- Extends the default Django `User` model to include profile data.
- Fields include contact and address information, loyalty purchase count, and discount eligibility.

### `Category`
- Represents different product categories.
- Includes fields for category name and a friendly (display) name.

### `Product`
- Core model representing products for sale.
- Fields include SKU, name, description, price, rating, and image information.

### `Size`
- Represents available sizes for products.
- Tied to the `Product` model and includes size and quantity fields.

### `Order`
- Model to store order information.
- Includes fields for user details, order totals, and Stripe payment ID.

### `OrderLineItem`
- Represents individual items within an order.
- Connected to both `Order` and `Product` models, includes quantity and total for the line item.

### `BlogPost`
- Model for creating blog posts on the site.
- Includes title, content, author, and associated media like images and videos.

### `SubCategory`
- Subcategories for more granular organization within categories.
- References a parent category from predefined choices.

### `PostInteraction`
- Tracks user interactions with blog posts, such as likes and dislikes.
- Tied to both the `User` and `BlogPost` models.

### Validators and Helper Functions
- Includes custom validators for YouTube URLs and square images.
- Helper functions for generating unique order numbers and updating totals.

-------------------------------------------------------------------------
### User

- **User** (Django's built-in User model)
  - Fields: `username`, `email`, `password`, etc.

### UserProfile

- **UserProfile**
  - `user` (FK to User, OneToOne)
  - `default_phone_number`
  - `default_street_address1`
  - `default_street_address2`
  - `default_town_or_city`
  - `default_county`
  - `default_postcode`
  - `default_country` (CountryField)
  - `loyalty_purchase_count`
  - `is_eligible_for_discount`

### Blog

- **SubCategory**
  - `name`
  - `parent_category` (Choices: Skate, Music, History)
- **BlogPost**
  - `title`
  - `subcategory` (FK to SubCategory)
  - `image` (CloudinaryField)
  - `youtube_video_url`
  - `uploaded_video` (CloudinaryField)
  - `content`
  - `author` (FK to User)
  - `published_date`
  - `slug`
  - `likes`
  - `dislikes`
- **PostInteraction**
  - `user` (FK to User)
  - `post` (FK to BlogPost)
  - `liked`
  - `disliked`

### Products

- **Category**
  - `name`
  - `friendly_name`
- **Product**
  - `category` (FK to Category)
  - `sku`
  - `name`
  - `description`
  - `has_sizes`
  - `price`
  - `rating`
  - `image_url`
  - `image` (ImageField)
- **Size**
  - `product` (FK to Product)
  - `size`
  - `quantity`

### Orders

- **Order**
  - `order_number`
  - `user_profile` (FK to UserProfile)
  - `full_name`
  - `email`
  - `phone_number`
  - `country` (CountryField)
  - `postcode`
  - `town_or_city`
  - `street_address1`
  - `street_address2`
  - `county`
  - `date`
  - `delivery_cost`
  - `order_total`
  - `grand_total`
  - `original_bag`
  - `stripe_pid`
- **OrderLineItem**
  - `order` (FK to Order)
  - `product` (FK to Product)
  - `product_size`
  - `quantity`
  - `lineitem_total`

## Notes

- **UserProfile** is automatically created or updated when a **User** instance is saved, ensuring each user has a corresponding profile for additional information.
- **BlogPost** supports multimedia content with fields for images and videos, including validation for YouTube URLs and square images.
- **Order** and **OrderLineItem** models manage the purchasing process, from cart to checkout, including calculation of total costs and management of delivery details.
- **Category** and **SubCategory** models facilitate the organization of blog content and products into hierarchical structures for easier navigation and filtering.

## Entity-Relationship Diagram (ERD)

[Link to ERD Markdown File](ERD.md)


## Deployment Process

- **Version Control**: This meticulous approach extends to our version control practices, where we leverage Git and GitHub's capabilities to foster collaboration and streamline our development cycles. By integrating user stories directly into our GitHub workflow and meticulously organizing our sprint board, we establish a transparent and efficient process. Utilizing tags and milestones, we categorize and visually map out the project's evolution on our board. Moreover, employing hashtags in our commit messages allows us to precisely link updates to their respective issues or tasks, ensuring a cohesive development narrative and facilitating easier tracking and review of changes. This systematic organization not only enhances project visibility but also optimizes our team's coordination and productivity.
- **Hosting**: Our project's hosting and operational infrastructure leverages several key services to ensure a robust and seamless experience. We host our platform on Squarespace, known for its reliability and ease of use, ensuring our site is always accessible and performing optimally. For authentication, we integrate Django Allauth, offering a comprehensive solution for account management. Our database needs are met by Heroku Postgres, providing a scalable and secure database service. Email communications are powered by Mailgun, enabling reliable delivery of transactional and marketing emails. For payments, we trust Stripe, ensuring secure and smooth payment processes. Additionally, we use Google Tag Manager and Facebook for analytics and marketing efforts, respectively, allowing us to track performance and engage with our audience effectively. Alongside our existing infrastructure, we incorporate Cloudinary for managing our media assets. This service streamlines the upload, storage, and optimization of images and videos, enhancing the user experience with fast-loading media content. Cloudinary's robust API and comprehensive toolset allow us to automate and refine our media handling processes, ensuring high-quality visuals across our platform.

## Testing

- **Test Framework**: Our project utilizes the Django test framework to ensure the reliability and stability of our application. This framework allows us to write and execute tests covering various parts of our application, identifying any issues early in the development process. We've faced challenges, such as cleaning our GitHub history due to inadvertently published sensitive information. We addressed this by using git filter-branch, deleting blobs, and removing old pull requests, which temporarily impacted our deployment visibility. Additionally, setting up PostgreSQL without Docker presented hurdles. By converting our database schema from SQLite to PostgreSQL, we overcame these obstacles, enabling our application to operate smoothly.
- **Test Cases**: For testing, we've implemented a blend of manual and automated strategies to ensure our application's functionality and user experience. Our automated tests include unit and integration tests within the Django framework, enhancing our code's reliability. We've utilized autopep8 for code linting and adhered to W3C standards for HTML and CSS validation, addressing potential issues. Tools like Django's debug mode, developer console, and Lighthouse have been pivotal for debugging and performance optimization. Manual testing efforts have included purchase simulations, email delivery verification, domain and DNS testing, with Beekeeper aiding in database visualization. However, due to certain constraints, testing for responsiveness was not feasible.

## Contribution Guidelines

- **Code Contributions**: To contribute code to our project, we encourage developers to fork the repository, make their changes in a new branch, and submit a pull request for review. This process allows for discussion about the proposed changes and ensures that contributions are carefully integrated. We recommend following the project's coding standards and submitting well-documented code to facilitate the review process.
- **Issue Tracking**: We manage bugs and feature requests using GitHub Issues. This platform allows us to track ongoing problems and new ideas efficiently, categorize them with labels, and assign tasks to team members. Contributors can report new issues, and the development team prioritizes them based on the project's needs. We also use milestones to group issues related to specific project phases or release targets, facilitating organization and planning.
## Update and Maintenance

- **Versioning**: Our project employs semantic versioning for managing releases, ensuring clarity and predictability in the development cycle. Each version is structured as MAJOR.MINOR.PATCH, where increments indicate breaking changes, new features without breaking existing functionality, and bug fixes, respectively. The requirements.txt file is meticulously updated to reflect the dependencies for each version, guaranteeing compatibility and stability. This systematic approach aids in efficiently tracking changes and deploying new versions.
- **Database Migrations**: We handle database migrations through Django's built-in migrations framework, enabling us to apply changes to our database schema systematically. This process involves generating migration files by detecting changes to our models, and then applying these migrations to update the database structure accordingly. This ensures that our database schema stays in sync with our models, facilitating a robust and adaptable development environment.
## Diagrams and Visual Aids

- **Model Relationships**: [Link to ERD Markdown File](ERD.md)

## Documentation Hosting

- Web Server Setup
Domain: Managed by Squarespace, allowing us to have a custom domain for a professional web presence.
Hosting Platform: Squarespace hosts our site, offering robust servers and uptime guarantees.
Content Management: Documentation updates are handled through the Squarespace content management system, which offers intuitive tools for editing and publishing content.
Design and Layout: We use Squarespace's templates and design tools to create an aesthetically pleasing layout that enhances readability and navigation.
Email Service
Provider: Mailgun, integrated with our domain for reliable email delivery and management.
Configuration: Set up to handle documentation-related correspondence, with automated responses and filtering to streamline communication.
Database
Database Service: Heroku Postgres, a managed SQL database service provided as an add-on by Heroku.
Integration: Linked to our Squarespace site via backend configurations, allowing dynamic content updates and user interaction data to be stored securely.
Maintenance: Regular backups and updates are conducted to ensure data integrity and security.

- **Squarespace**: [Visit Squarespace](https://www.squarespace.com) for website creation and hosting services.
- **Heroku**: [Explore Heroku](https://www.heroku.com) for cloud platform services that enable app deployment and operations.
- **Mailgun**: For email automation services, check out [Mailgun](https://www.mailgun.com).
- **PostgreSQL**: Find more information about the open-source object-relational database system at [PostgreSQL official site]
  (https://www.postgresql.org).


```markdown



