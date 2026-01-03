# Claude Code Rules - Backend (Python FastAPI + SQLModel)

You are an expert AI assistant specializing in backend development for the Todo Full-Stack Web Application. Your primary goal is to implement the backend API using Python FastAPI and SQLModel ORM with PostgreSQL database and Better Auth for JWT authentication.

## Task Context

**Project**: Todo Full-Stack Web Application
**Backend Stack**: Python FastAPI, SQLModel ORM, Neon Serverless PostgreSQL
**Authentication**: Better Auth with JWT tokens
**Target**: RESTful API with JWT-secured endpoints

## Core Backend Components

### 1. Database Models
- Create `users` table (managed by Better Auth)
- Create `tasks` table with fields: id, user_id, title, description, completed, created_at, updated_at
- Implement proper relationships and foreign key constraints
- Add database indexes for `tasks.user_id` and `tasks.completed` for efficient queries

### 2. API Endpoints
- **GET** `/api/{user_id}/tasks`: List all tasks for a user
  - Include query parameters for `status` (all, pending, completed) and `sort` (created date, title)
  - Filter tasks by authenticated user
  - Return JSON array of tasks

- **POST** `/api/{user_id}/tasks`: Create a new task
  - Require title, accept optional description
  - Associate task with logged-in user
  - Return created task as JSON

- **GET** `/api/{user_id}/tasks/{id}`: Get task details
  - Validate task ownership
  - Return task as JSON

- **PUT** `/api/{user_id}/tasks/{id}`: Update a task
  - Validate task ownership
  - Update title and description
  - Return updated task as JSON

- **DELETE** `/api/{user_id}/tasks/{id}`: Delete a task
  - Validate task ownership
  - Return confirmation of deletion

- **PATCH** `/api/{user_id}/tasks/{id}/complete`: Toggle task completion
  - Validate task ownership
  - Toggle `completed` status
  - Return updated task as JSON

### 3. JWT Authentication Integration
- Configure Better Auth to issue JWT tokens
- Implement middleware to validate JWT tokens in FastAPI
- Decode JWT to extract user information
- Reject unauthorized requests with `401 Unauthorized` responses
- Ensure all endpoints validate JWT authentication

### 4. Business Logic
- Implement task ownership enforcement (users can only access their own tasks)
- Validate task data (title required, proper formatting)
- Handle edge cases (invalid task IDs, unauthorized access)
- Implement proper error handling and responses

## Technical Guidelines

### FastAPI Specific
- Use Pydantic models for request/response validation
- Implement proper API documentation with automatic OpenAPI generation
- Use dependency injection for authentication validation
- Follow FastAPI best practices for routing and error handling

### SQLModel Guidelines
- Define models with proper field types and constraints
- Implement relationships between tables
- Use proper indexing for performance
- Handle database transactions appropriately

### Security Guidelines
- Validate JWT tokens for all API endpoints
- Implement proper user isolation (users can only access their own data)
- Validate all user inputs to prevent injection attacks
- Use parameterized queries to prevent SQL injection

### Database Guidelines
- Use Neon Serverless PostgreSQL
- Implement proper connection pooling
- Handle database errors gracefully
- Use async database operations for better performance

## API Response Format
- Use consistent JSON response format
- Include proper HTTP status codes
- Return meaningful error messages
- Follow RESTful API design principles

## Testing
- Write unit tests for all API endpoints
- Test JWT authentication and authorization
- Validate data models and database operations
- Test error handling and edge cases
- Perform integration testing for the complete API flow