# Quickstart Guide: Todo Full-Stack Web Application

**Feature**: 2-todo-fullstack
**Date**: 2025-12-28
**Status**: Draft

## Overview

This guide provides instructions for setting up and running the Todo Full-Stack Web Application locally for development and testing.

## Prerequisites

- Node.js 18+ (for frontend development)
- Python 3.11+ (for backend development)
- PostgreSQL (or access to Neon Serverless PostgreSQL)
- pnpm or npm (for frontend package management)
- uv or pip (for Python package management)

## Environment Setup

### Backend Setup

1. **Install Python dependencies:**
   ```bash
   cd backend
   uv venv  # or python -m venv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Update the .env file with your database connection and auth settings
   ```

3. **Database setup:**
   ```bash
   # Run database migrations
   python -m alembic upgrade head
   ```

4. **Start the backend server:**
   ```bash
   python -m uvicorn src.main:app --reload --port 8000
   ```

### Frontend Setup

1. **Install Node.js dependencies:**
   ```bash
   cd frontend
   pnpm install  # or npm install
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env.local
   # Update the .env.local file with your backend API URL
   ```

3. **Start the frontend development server:**
   ```bash
   pnpm dev  # or npm run dev
   ```

## Running the Application

### Development Mode

1. Start the backend server (port 8000):
   ```bash
   cd backend
   python -m uvicorn src.main:app --reload
   ```

2. In a separate terminal, start the frontend (port 3000):
   ```bash
   cd frontend
   pnpm dev
   ```

3. Access the application at `http://localhost:3000`

### Production Build

1. **Build the frontend:**
   ```bash
   cd frontend
   pnpm build
   ```

2. **Serve the application:**
   - Backend API remains on port 8000
   - Frontend can be served via Next.js static export or integrated with backend

## API Endpoints

The application exposes the following REST API endpoints:

- `GET /api/{user_id}/tasks` - List all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get task details
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion

All endpoints require JWT authentication in the Authorization header.

## Authentication

The application uses Better Auth for user authentication:

1. Users can sign up at `/signup`
2. Users can sign in at `/login`
3. JWT tokens are automatically included in API requests
4. All API endpoints validate JWT tokens

## Database Schema

The application uses PostgreSQL with the following tables:

- `user` - Managed by Better Auth (id, email, name, created_at)
- `task` - Custom table (id, user_id, title, description, completed, created_at, updated_at)

## Development Workflow

1. **Feature Development:**
   - Create feature branches following the pattern `###-feature-name`
   - Implement frontend and backend components separately
   - Write tests for new functionality
   - Update documentation as needed

2. **Testing:**
   - Run backend tests: `pytest`
   - Run frontend tests: `pnpm test`
   - Integration tests cover API interactions

3. **Code Quality:**
   - Python: Use black for formatting, flake8 for linting
   - TypeScript: Use prettier for formatting, eslint for linting
   - Commit messages follow conventional commits specification

## Troubleshooting

### Common Issues

1. **Database Connection Issues:**
   - Verify database URL in environment variables
   - Check database credentials and permissions

2. **Authentication Issues:**
   - Ensure JWT secret is properly configured
   - Verify auth endpoints are accessible

3. **Frontend-Backend Communication:**
   - Confirm API base URL is correctly set in frontend
   - Check CORS settings if developing locally

### Development Tips

1. **API Testing:**
   - Use the auto-generated API documentation at `/docs`
   - Test endpoints directly in the browser

2. **Frontend Development:**
   - Use Next.js hot reloading for rapid development
   - Leverage Tailwind CSS utility classes for styling

3. **Database Changes:**
   - Use Alembic for database migrations
   - Always backup data before running migrations