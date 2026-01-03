# REST API Endpoints Specification: Todo Full-Stack Web Application

**Project**: Todo Full-Stack Web Application
**Phase**: II – Full-Stack Multi-User with Authentication
**Created**: 2025-12-28
**Status**: Draft

## Overview

This document specifies the REST API endpoints for the Todo Full-Stack Web Application. All endpoints require JWT authentication in the Authorization header and enforce task ownership (users can only access their own tasks).

## Authentication

All API endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <JWT_TOKEN>
```

## API Endpoints

### Tasks Resource

#### GET `/api/{user_id}/tasks`
**Description**: List all tasks for a user with optional filtering and sorting

**Parameters**:
- `user_id` (path): The ID of the authenticated user
- `status` (query, optional): Filter by completion status (`all`, `pending`, `completed`)
- `sort` (query, optional): Sort by field (`created_at`, `title`)

**Response**:
```
Status: 200 OK
Content-Type: application/json
{
  "tasks": [
    {
      "id": 1,
      "user_id": "user123",
      "title": "Sample task",
      "description": "Sample description",
      "completed": false,
      "created_at": "2025-12-28T10:00:00Z",
      "updated_at": "2025-12-28T10:00:00Z"
    }
  ]
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing JWT token
- `404 Not Found`: User does not exist

#### POST `/api/{user_id}/tasks`
**Description**: Create a new task for the specified user

**Parameters**:
- `user_id` (path): The ID of the authenticated user

**Request Body**:
```json
{
  "title": "Task title (required)",
  "description": "Task description (optional)"
}
```

**Response**:
```
Status: 201 Created
Content-Type: application/json
{
  "id": 1,
  "user_id": "user123",
  "title": "Task title",
  "description": "Task description",
  "completed": false,
  "created_at": "2025-12-28T10:00:00Z",
  "updated_at": "2025-12-28T10:00:00Z"
}
```

**Error Responses**:
- `400 Bad Request`: Title is empty or invalid input
- `401 Unauthorized`: Invalid or missing JWT token
- `404 Not Found`: User does not exist

#### GET `/api/{user_id}/tasks/{id}`
**Description**: Get details of a specific task

**Parameters**:
- `user_id` (path): The ID of the authenticated user
- `id` (path): The ID of the task

**Response**:
```
Status: 200 OK
Content-Type: application/json
{
  "id": 1,
  "user_id": "user123",
  "title": "Task title",
  "description": "Task description",
  "completed": false,
  "created_at": "2025-12-28T10:00:00Z",
  "updated_at": "2025-12-28T10:00:00Z"
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing JWT token
- `404 Not Found`: Task or user does not exist

#### PUT `/api/{user_id}/tasks/{id}`
**Description**: Update an existing task

**Parameters**:
- `user_id` (path): The ID of the authenticated user
- `id` (path): The ID of the task

**Request Body**:
```json
{
  "title": "Updated task title",
  "description": "Updated task description"
}
```

**Response**:
```
Status: 200 OK
Content-Type: application/json
{
  "id": 1,
  "user_id": "user123",
  "title": "Updated task title",
  "description": "Updated task description",
  "completed": false,
  "created_at": "2025-12-28T10:00:00Z",
  "updated_at": "2025-12-28T11:00:00Z"
}
```

**Error Responses**:
- `400 Bad Request`: Title is empty or invalid input
- `401 Unauthorized`: Invalid or missing JWT token
- `404 Not Found`: Task or user does not exist

#### DELETE `/api/{user_id}/tasks/{id}`
**Description**: Delete a specific task

**Parameters**:
- `user_id` (path): The ID of the authenticated user
- `id` (path): The ID of the task

**Response**:
```
Status: 204 No Content
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing JWT token
- `404 Not Found`: Task or user does not exist

#### PATCH `/api/{user_id}/tasks/{id}/complete`
**Description**: Toggle the completion status of a task

**Parameters**:
- `user_id` (path): The ID of the authenticated user
- `id` (path): The ID of the task

**Response**:
```
Status: 200 OK
Content-Type: application/json
{
  "id": 1,
  "user_id": "user123",
  "title": "Task title",
  "description": "Task description",
  "completed": true,
  "created_at": "2025-12-28T10:00:00Z",
  "updated_at": "2025-12-28T11:00:00Z"
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing JWT token
- `404 Not Found`: Task or user does not exist

## Security Requirements

1. **JWT Authentication**: All endpoints require a valid JWT token in the Authorization header
2. **Task Ownership**: Users can only access tasks associated with their user ID
3. **Data Validation**: All input data must be validated before processing
4. **Error Handling**: Return appropriate HTTP status codes and error messages

## Performance Requirements

1. **Response Time**: All endpoints should respond within 2 seconds
2. **Rate Limiting**: Implement rate limiting to prevent abuse
3. **Caching**: Implement appropriate caching for frequently accessed data

## Compliance

All endpoints must comply with the requirements specified in the project constitution and feature specification documents.