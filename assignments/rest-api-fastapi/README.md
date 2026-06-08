# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a practical REST API using the FastAPI framework. You'll learn how to create endpoints, handle HTTP requests, validate data, and work with JSON responses by constructing a simple task management API.

## 📝 Tasks

### 🛠️ Set Up FastAPI and Create Basic Endpoints

#### Description
Set up a FastAPI application and implement basic GET and POST endpoints for a task management system.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn
- Create a FastAPI application instance
- Define a GET endpoint (`/tasks`) that returns a list of sample tasks
- Define a POST endpoint (`/tasks`) that accepts a new task and adds it to the list
- Run the server using `uvicorn main:app --reload`
- Test endpoints using a REST client (Postman, curl, or browser)

### 🛠️ Add Data Validation and Task Operations

#### Description
Enhance the API by adding Pydantic models for data validation and implementing additional endpoints for updating and deleting tasks.

#### Requirements
Completed program should:

- Define a Pydantic `Task` model with fields: `id`, `title`, `description`, `completed`
- Use the model for request/response validation
- Implement a GET endpoint (`/tasks/{task_id}`) to retrieve a specific task
- Implement a PUT endpoint (`/tasks/{task_id}`) to update a task
- Implement a DELETE endpoint (`/tasks/{task_id}`) to remove a task
- Return appropriate HTTP status codes (200, 201, 404, etc.)

### 🛠️ Add Advanced Features (Stretch Goal)

#### Description
Implement error handling, request validation, and query parameters to make the API more robust and feature-rich.

#### Requirements
Completed program should:

- Add request body validation with error responses
- Implement query parameters (e.g., `/tasks?completed=true`)
- Add proper error handling with custom error messages
- Include HTTP exception handling for invalid operations
- Document API endpoints with docstrings
- (Optional) Add a simple in-memory database or file storage for persistence
