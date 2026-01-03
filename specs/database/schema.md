# Database Schema Specification: Todo Full-Stack Web Application

**Project**: Todo Full-Stack Web Application
**Phase**: II – Full-Stack Multi-User with Authentication
**Created**: 2025-12-28
**Status**: Draft

## Overview

This document specifies the database schema for the Todo Full-Stack Web Application using Neon Serverless PostgreSQL. The schema includes tables for user authentication (managed by Better Auth) and task management.

## Database Configuration

- **Database**: Neon Serverless PostgreSQL
- **Connection**: Connection pooling with async support
- **Encoding**: UTF-8
- **Timezone**: UTC

## Tables

### Users Table (Managed by Better Auth)

The users table is managed by Better Auth and contains user authentication information.

**Schema**:
```sql
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    name TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

**Fields**:
- `id`: String (Primary Key) - Unique identifier for the user
- `email`: String (Unique) - User's email address for authentication
- `name`: String - User's display name
- `created_at`: Timestamp - When the user account was created

**Indexes**:
- `users_email_idx`: UNIQUE INDEX ON (email)
- `users_created_at_idx`: INDEX ON (created_at)

### Tasks Table

The tasks table stores the todo tasks for each user.

**Schema**:
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

**Fields**:
- `id`: Integer (Primary Key, Auto-increment) - Unique identifier for the task
- `user_id`: String (Foreign Key) - References the User who owns this task
- `title`: Text (Required) - The task title (cannot be empty)
- `description`: Text (Optional) - Additional details about the task
- `completed`: Boolean - Whether the task is completed (default: false)
- `created_at`: Timestamp - When the task was created
- `updated_at`: Timestamp - When the task was last updated

**Constraints**:
- `tasks_title_check`: CHECK (LENGTH(TRIM(title)) > 0) - Title cannot be empty
- `tasks_user_id_fkey`: FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE

**Indexes**:
- `tasks_user_id_idx`: INDEX ON (user_id) - For efficient user-based queries
- `tasks_completed_idx`: INDEX ON (completed) - For efficient status-based queries
- `tasks_created_at_idx`: INDEX ON (created_at) - For efficient sorting by creation date
- `tasks_user_completed_idx`: COMPOSITE INDEX ON (user_id, completed) - For efficient combined filtering

## Relationships

### User → Task (One-to-Many)
- A User can own many Tasks
- A Task belongs to exactly one User
- Enforced by `user_id` foreign key in Tasks table
- CASCADE DELETE: When a user is deleted, all their tasks are automatically deleted

## Data Integrity

### Constraints
1. **Task Title**: Must not be empty (enforced by `tasks_title_check`)
2. **User Association**: All tasks must be associated with a valid user (enforced by foreign key)
3. **Referential Integrity**: Foreign key constraint ensures user exists when task is created

### Validation Rules
1. **Title Validation**: Task titles cannot be empty or contain only whitespace
2. **Ownership**: Tasks can only be accessed by their owner (enforced at application level)
3. **Data Types**: All fields have appropriate data types to ensure data integrity

## Performance Considerations

### Indexes
- Primary indexes on all primary keys (auto-created)
- Index on `user_id` for efficient user-based queries
- Index on `completed` for efficient status-based queries
- Composite index on (`user_id`, `completed`) for combined filtering
- Index on `created_at` for efficient sorting

### Query Optimization
- Queries should filter by `user_id` first to leverage the user index
- Use the composite index for combined user and status filtering
- Consider partial indexes for frequently queried subsets

## Security Requirements

### Access Control
- Database access restricted to application backend only
- No direct database access from frontend
- All queries must be parameterized to prevent SQL injection

### Data Protection
- Sensitive user data encrypted at rest
- Connection encryption (TLS) required for all database connections
- Audit logging for access to sensitive data

## Migration Strategy

### Initial Schema
1. Create `users` table (managed by Better Auth)
2. Create `tasks` table with all required fields and constraints
3. Create all necessary indexes
4. Set up foreign key relationships

### Future Changes
- Use migration scripts for any schema changes
- Maintain backward compatibility where possible
- Update this specification when schema changes are made

## Compliance

The database schema must comply with:
1. Requirements in the project constitution regarding data storage
2. Requirements in the feature specification regarding task ownership
3. Security requirements for user data protection
4. Performance requirements for query response times