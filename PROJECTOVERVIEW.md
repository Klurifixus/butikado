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

- **Core URL Patterns**: Describes the URL patterns found in `butikado/urls.py`.
- **App URL Patterns**: Details the URL patterns and corresponding views for each app.

## Database Schema

- **Models**: Lists models and fields for each app.
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

Please note, as Markdown doesn't support embedding complex diagrams directly, it's recommended to create an ERD using a tool like Lucidchart, dbdiagram.io, or Draw.io, and then link to it here.

[Link to ERD](#)


- **Relationships**: Describes relationships between models, including foreign keys and many-to-many fields.

## Deployment Process

- **Version Control**: Explains the use of Git and the branching strategy.
- **CI/CD**: Details the Continuous Integration and Deployment pipeline.
- **Hosting**: Describes the hosting platform and additional operational services.

## Testing

- **Test Framework**: Information on the Django test framework or others in use.
- **Test Cases**: Types of tests (unit, integration, etc.) and testing practices.

## Contribution Guidelines

- **Code Contributions**: How to contribute code (forking, pull requests, etc.).
- **Issue Tracking**: How bugs and features are tracked and managed.

## Update and Maintenance

- **Versioning**: System for version control and new version releases.
- **Database Migrations**: Process for managing database changes.

## Diagrams and Visual Aids

- **Request Lifecycle**: [Link or embedded image for request flow diagram]
- **Model Relationships**: [Link or embedded image for ERD]
- **Infrastructure Layout**: [Link or embedded image for infrastructure diagram]

## Documentation Generation

- Instructions on how to generate and update documentation using Sphinx or MkDocs.

## Documentation Hosting

- Information on where and how the documentation is hosted (Read the Docs, GitHub Pages, etc.).

 `[Details about the web server setup]`) 

```markdown
![Alt text for the image](path-to-your-image.png)


