# Wiki Encyclopedia
#### Video Demo: <URL [HERE](https://youtu.be/nR0r3UnYiAs)>
#### Description:
Wiki Encyclopedia is a web application that allows users to view, search, create, and edit encyclopedia entries written in Markdown.

## File Contents

### Models (`models.py`)
- No custom models are defined; entries are stored as Markdown files in the `entries/` directory.

### Views (`views.py`)
- `index`: Displays a list of all encyclopedia entries
- `entry`: Shows the content of a specific entry
- `search`: Allows users to search for entries by title or substring
- `new`: Enables users to create new entries
- `edit`: Loads entry content for editing
- `update`: Saves changes to an entry
- `randomSelect`: Redirects to a random entry

### URLs (`urls.py`)
Defines all routes for the application, including viewing, searching, creating, editing, and selecting random entries.

### Templates
HTML templates for rendering the user interface:
- `index.html`: Main page listing all entries
- `page.html`: Displays entry content
- `search.html`: Search results page
- `new.html`: New entry creation page
- `edit.html`: Entry editing page
- `error.html`: Error messages
- `layout.html`: Base template for consistent layout

### Static Files
- `styles.css`: CSS for styling the application

### Entries (`entries/`)
Markdown files for each encyclopedia entry (e.g., `Python.md`, `HTML.md`, etc.)

## How to Run the Application

1. Clone the repository or download the project files.
2. Ensure you have Python and Django installed on your system.
3. Navigate to the project directory:
   ```
   cd wiki
   ```
4. Apply migrations to set up the database (if needed):
   ```
   python manage.py makemigrations encyclopedia
   python manage.py migrate
   ```
5. Create a superuser to access the admin panel (optional):
   ```
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```
7. Open a web browser and navigate to `http://127.0.0.1:8000` to use the application.

## Additional Information

- **Admin Interface**: Use Django's admin panel at `/admin` to manage users (if needed).
- **Requirements**: Built with Django, requires Python 3.6 or higher.
- **Entries**: All encyclopedia entries are stored as Markdown files in the `entries/` directory.
- **Static Files**: Includes CSS for styling the user interface.
