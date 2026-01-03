# Data Model: Todo Full-Stack Web Application

**Feature**: 2-todo-fullstack
**Date**: 2025-12-28
**Status**: Draft

## Overview

This document defines the data models for the Todo Full-Stack Web Application, including entity definitions, relationships, and validation rules based on the feature specification.

## Entity: User

Managed by Better Auth system.

**Fields:**
- `id`: string (Primary Key) - Unique identifier for the user
- `email`: string (Unique) - User's email address for authentication
- `name`: string - User's display name
- `created_at`: timestamp - When the user account was created

**Relationships:**
- One-to-Many: User has many Tasks (via `user_id` foreign key)

## Entity: Task

**Fields:**
- `id`: integer (Primary Key) - Unique identifier for the task
- `user_id`: string (Foreign Key) - References the User who owns this task
- `title`: string (Required) - The task title (cannot be empty)
- `description`: string (Optional) - Additional details about the task
- `completed`: boolean - Whether the task is completed (default: false)
- `created_at`: timestamp - When the task was created
- `updated_at`: timestamp - When the task was last updated

**Validation Rules:**
- `title` must not be empty (FR-007)
- `user_id` must reference a valid user (enforces FR-002)
- All tasks must be associated with a logged-in user (FR-002)

**State Transitions:**
- `completed: false` → `completed: true` (when user marks task complete)
- `completed: true` → `completed: false` (when user marks task incomplete)

## Relationships

**User → Task (One-to-Many)**
- A User can own many Tasks
- A Task belongs to exactly one User
- Enforced by `user_id` foreign key in Task table
- Required to enforce FR-009 (users only see their own tasks)

## Constraints

1. **Task Ownership**: Each task must be associated with a valid user (FR-002)
2. **User Isolation**: Users can only access tasks where `user_id` matches their own ID (FR-009)
3. **Title Validation**: Task titles cannot be empty (FR-007)
4. **Data Persistence**: Tasks must be stored in PostgreSQL database (FR-003)

## Indexes

- Index on `user_id` for efficient filtering by user (FR-013)
- Index on `completed` for efficient filtering by status (FR-013)
- Index on `created_at` for efficient sorting by creation date (FR-013)
- Composite index on (`user_id`, `completed`) for efficient combined filtering

## Access Patterns

1. **Get all tasks for user**: Query by `user_id` (User Story 1)
2. **Filter by completion status**: Query by `user_id` and `completed` (User Story 1)
3. **Update task**: Update by `id` with `user_id` verification (User Story 2)
4. **Delete task**: Delete by `id` with `user_id` verification (User Story 2)
5. **Toggle completion**: Update `completed` by `id` with `user_id` verification (User Story 3)