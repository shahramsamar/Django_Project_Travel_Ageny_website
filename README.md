# Django Project Travel Agency Website

A Django project for building a travel agency website that allows users to browse travel destinations, book trips, and access other travel-related services. The website includes functionalities such as user registration, trip booking, and viewing available tours.

## Features

- **User Registration and Login**: Allows users to register, log in, and manage their accounts.
- **Tour Booking**: Users can browse different travel packages and book trips.
- **Destination Catalog**: Display a list of available travel destinations with detailed information.
- **Trip Management**: Users can view, update, and cancel their bookings.
- **Admin Dashboard**: An admin panel to manage users, destinations, and bookings.

## Requirements

- **Python 3.x**
- **Django**: A high-level Python web framework.
- **PostgreSQL** (or other database systems): The database to store user and trip information.
- **Django Allauth**: For handling user authentication, registration, and login.
- **Django Crispy Forms**: For better styling of forms.
- **Django REST Framework** (optional): For building APIs (if needed).

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/Django_Project_Travel_Ageny_website.git
    cd Django_Project_Travel_Ageny_website
    ```

2. **Install Dependencies:**

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the Database**:

    Modify the `settings.py` file to configure the database connection. By default, Django uses SQLite, but you can switch to PostgreSQL or any other database by modifying the database settings.

    Example configuration for PostgreSQL:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'travel_agency_db',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

4. **Apply Migrations**:

    Run the following command to apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser (Admin)**:

    To create an admin user for accessing the Django admin dashboard, run:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:

    To start the server, use the following command:

    ```bash
    python manage.py runserver
    ```

    The website will be available at `http://127.0.0.1:8000/`.

### How to Use

1. **User Registration**:
   - Navigate to the registration page and create a new user account with a valid email and password.

2. **Login**:
   - After registration, log in to your account to access booking and destination features.

3. **Browse Destinations**:
   - Explore available travel destinations and their details.

4. **Book a Trip**:
   - Once logged in, choose a destination and book a trip.

5. **Admin Panel**:
   - Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage users, destinations, and bookings.

### Project Structure

- `travel_agency/`: Main project folder.
    - `settings.py`: Django settings file.
    - `urls.py`: URL routing for the project.
    - `wsgi.py`: WSGI configuration for deployment.
    - `asgi.py`: ASGI configuration for deployment.
- `tours/`: Application handling tours and bookings.
    - `models.py`: Contains models for trips, bookings, and destinations.
    - `views.py`: Contains views for rendering pages and handling bookings.
    - `forms.py`: Contains forms for user interaction (booking, registration, etc.).
    - `urls.py`: Routing for the tours application.
    - `templates/`: HTML files for rendering web pages.
        - `booking_form.html`: A form for booking trips.
        - `destination_list.html`: Displays available destinations.
        - `index.html`: The homepage of the travel agency website.
    - `static/`: CSS, JavaScript, and image files.
        - `css/`: Stylesheets for the website.
        - `images/`: Image resources for the website.
- `templates/`: Global templates for the website (e.g., navigation bar, footer).
- `requirements.txt`: Lists all the required Python libraries for the project.

### Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

### License

This project is open-source and available for educational purposes.

### API Documentation

If you need to build APIs for the project, Django REST Framework can be used to expose endpoints for tours, users, and bookings. The API documentation can be automatically generated if you set up the Django REST framework.

For example, to get a list of available tours, you might have:

- **GET /api/tours/** - Get a list of all available tours.
- **POST /api/bookings/** - Create a new booking.

---

This `README.md` provides detailed installation, usage, and project structure instructions for the Travel Agency website built with Django. It highlights the main features such as user registration, trip booking, and the admin panel while explaining how to set up the project, database, and server.

