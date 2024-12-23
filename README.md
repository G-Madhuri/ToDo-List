# Todo List Application

A simple Todo List app built using **Flask**, **HTML**, **CSS**, and **Bootstrap**. This app allows users to manage their tasks by adding, editing, marking as completed, and deleting them.

## Features
- **Add Tasks**: Add tasks with title, due date, and priority.
- **Edit Tasks**: Edit tasks to update title, due date, or priority.
- **Mark Tasks as Completed**: Mark tasks as completed with a visual strike-through.
- **Delete Tasks**: Delete tasks that are no longer needed.
- **Filter Tasks**: Filter tasks by their status (All, Completed, Pending).
- **Sort Tasks**: Sort tasks by due date or priority for better task management.

## Technologies Used
- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: In-memory (for demonstration purposes; can be replaced with a database like SQLite)

## Installation

### Prerequisites
Ensure you have **Python 3.x** installed on your machine.

### Steps to Run Locally:

1. **Clone the Repository**:
    git clone https://github.com/yourusername/todo-list-app.git
    cd todo-list-app


2. **Install Dependencies**:
    You will need **Flask** to run this app. Install it using pip:
    pip install flask

3. **Run the Application**:
    To start the Flask server, run the following command:
    python app.py

4. **Access the App**:
    Open a browser and go to `http://127.0.0.1:5000` to use the Todo List application.

## Project Structure

- **/static**: Contains the CSS file used for styling the app.
- **/templates**: Contains the HTML files that render the frontend of the app.
- **app.py**: The main Python file that contains the Flask routes and logic for handling tasks.

## Usage

1. **Add a Task**: Enter a task title, due date, and priority, then click "Add Task".
2. **Edit a Task**: Click the pencil icon next to a task to edit its details.
3. **Mark as Completed**: Click the checkmark icon next to a task to mark it as completed.
4. **Delete a Task**: Click the trash icon to delete a task from the list.
5. **Filter Tasks**: Use the "Filter" dropdown to view tasks based on their status (All, Completed, Pending).
6. **Sort Tasks**: Use the "Sort by Due Date" or "Sort by Priority" buttons to organize your tasks.

## Contributing

Feel free to fork the repository and submit pull requests for new features or bug fixes.

## Acknowledgments

- **Flask** for powering the backend.
- **Bootstrap** for providing a responsive and clean user interface.
