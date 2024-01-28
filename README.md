# E-Commerce Website Project

This repository contains the code for an e-commerce website built using Django and MongoDB. The project includes models for products, product images, contacts, addresses, and orders.

## Project Structure

- **models.py**: Defines Django models for products, product images, contacts, addresses, and orders.
- **views.py**: Contains views for handling different aspects of the e-commerce website.
- **templates/**: Includes HTML templates for rendering different pages.
- **static/**: Contains static files such as CSS and JavaScript.
- **requirements.txt**: Lists the Python packages required for running the project.
- **manage.py**: Django management script for various administrative tasks.
- **Stripe payment**: Integrate with stripe payment integration. 

## Prerequisites

Install the following things:

- Python
- Django
- Djongo (Django MongoDB connector)

## Setup
1. Install dependencies:

`bash`
Copy code
pip install -r requirements.txt
Run migrations:

`bash`
python manage.py makemigrations
python manage.py migrate
Create a superuser:

`bash`
python manage.py createsuperuser
Follow the prompts to create an admin user.

Run the development server:

`bash`
python manage.py runserver
Visit http://localhost:8000 in your web browser.

# Django Models
## Products
`Name:` Name of the product.
`Description:` Description of the product.
`Category:` Category of the product (Electronic, Fashion, Education, Vehicles).
`Price:` Price of the product.
`Date:` Date the product was added.
## ProductImage
`Product:` Foreign key referencing the associated product.
`Image:` Image file for the product.
## Contact
`Name:` Name of the person contacting.
`Email:` Email address of the person.
`Phone:` Phone number of the person.
`Message:` Message sent by the person.
## Address
`Name:` Name associated with the address.
`Address:` Physical address.
`Code:` Postal code.
`Mobile:` Mobile number.
`Email:` Email address (unique).
`Province:` Province in which the address is located.
`City:` City in which the address is located.
`Area:` Specific area within the city.
## Order
`Address:` One-to-one relationship with an Address. 
`ItemJson:` JSON representation of ordered items.
## Contributors
Your Name (@Samiullah)

E:\Root Folder\Programs\Python_Projects\Djanjo\ecomerence_env\README.md