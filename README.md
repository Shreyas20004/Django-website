# Django Project

This is a Django project that includes user profile creation using Django signals.

## Prerequisites

- Python 3.x
- Django 3.x or later
- pip (Python package installer)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```sh
    python manage.py migrate
    ```

6. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:

    ```sh
    python manage.py runserver
    ```

8. Open your web browser and go to `http://127.0.0.1:8000/` to see the project in action.

## Usage

- To create a user profile, register a new user through the Django admin or any user registration form you have set up.
- The `Profile` model will be automatically created for each new user using Django signals.

## Project Structure

- `models.py`: Contains the `Profile` model.
- `signals.py`: Contains the signal handlers for creating user profiles.
- `views.py`: Contains the views for the project.
- `urls.py`: Contains the URL configurations for the project.
- `templates/`: Contains the HTML templates for the project.
- `static/`: Contains the static files (CSS, JavaScript, images) for the project.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
