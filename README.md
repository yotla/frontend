# Task Management Frontend

This project is a simple frontend for a task management SaaS, built with Python, FastAPI, and Jinja2 templates. It serves as a single-page application to display tasks for a user.

## Features

*   **FastAPI Backend**: Serves the main HTML page and a JSON endpoint for tasks.
*   **Jinja2 Templating**: Used for the initial HTML page structure.
*   **Client-Side Rendering**: JavaScript fetches task data from a `/tasks` endpoint and dynamically renders task cards.
*   **Configurable**: Settings can be managed via environment variables, a `config.json` file, or command-line arguments.
*   **Basic Styling**: Includes minimal CSS for a clean task display.
*   **Placeholder Backend Integration**: Contains placeholder functions for fetching and updating tasks, designed to be integrated with a real REST API backend.

## Project Structure

```
├── main.py                 # Main FastAPI application, defines endpoints
├── requirements.txt        # Python dependencies
├── config.json             # Optional: for JSON-based configuration (create if needed)
├── src/
│   ├── config.py           # Handles configuration loading (env, json, argv)
│   └── templates/
│       └── index.html      # Jinja2 template for the single-page app
└── static/
    └── style.css           # CSS styles for the application
```

## Setup

1.  **Clone the repository** (if applicable):
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Create and activate a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The application uses `src/config.py` to manage configuration. Values are retrieved in the following order of precedence:

1.  **Environment Variables**: Set any configuration key as an environment variable (e.g., `export PORT=8001`).
2.  **`config.json` File**: Create a `config.json` file in the project root directory. Example:
    ```json
    {
        "PORT": 8002,
        "LOG_LEVEL": "DEBUG"
    }
    ```
3.  **Command-Line Arguments**: Pass arguments when running the script (e.g., `python main.py PORT=8003`).
4.  **Default Values**: If a key is not found in any of the above, a default value specified in the code (via `Config.get('KEY', 'default')`) will be used.

Key configuration options you might use (you can define your own as needed):
*   `HOST`: The host address to run the server on (default: `127.0.0.1` or `0.0.0.0` in some contexts).
*   `PORT`: The port to run the server on (default: `8000`).
*   `LOG_LEVEL`: Logging level for the application (e.g., `INFO`, `DEBUG`).
*   `BACKEND_API_URL`: URL for your actual task management backend API.

## Running the Application

To start the FastAPI development server, run the following command from the project root directory:

```bash
uvicorn main:app --reload
```

*   `main:app`: Tells Uvicorn to look for an object named `app` in the `main.py` file.
*   `--reload`: Enables auto-reload, so the server restarts when code changes are detected.

You can then access the application in your web browser, typically at `http://127.0.0.1:8000` (or the host/port you configured).

The `/` route serves the HTML page, which then makes a client-side request to `/tasks` to fetch and display the task data.

## Development Notes

*   The `main.py` file contains placeholder functions (`fetch_tasks_from_backend`, `update_task_status_in_backend`). These need to be implemented to communicate with your actual backend service.
*   The `/tasks` endpoint in `main.py` currently returns a hardcoded list of tasks for demonstration.
*   Styling in `static/style.css` and `src/templates/index.html` is minimal and can be expanded.
