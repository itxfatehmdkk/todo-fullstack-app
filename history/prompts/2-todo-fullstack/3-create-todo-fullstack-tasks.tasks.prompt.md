---
id: 3
title: Create Todo Fullstack Tasks
stage: tasks
date: 2025-12-28
surface: agent
model: Claude Sonnet 4.5
feature: todo-fullstack
branch: 2-todo-fullstack
user: Fateh Mohammad
command: sp.task
labels: [tasks, todo-app, full-stack, implementation]
links:
  spec: specs/2-todo-fullstack/spec.md
  plan: specs/2-todo-fullstack/plan.md
  tasks: specs/2-todo-fullstack/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/2-todo-fullstack/tasks.md
 - frontend/CLAUDE.md
 - backend/CLAUDE.md
 - specs/api/rest-endpoints.md
 - specs/database/schema.md
 - CLAUDE.md
tests:
 - none
---

## Prompt

```text
let update the task.md too ''' # /sp.task – Todo Full-Stack Web Application: Task Breakdown

**Project**: Todo Full-Stack Web Application
**Phase**: II – Full-Stack Multi-User with Authentication
**Created**: 2025-12-28
**Status**: Draft

---

## 1. Backend Tasks (FastAPI + SQLModel)

### Task 1.1 – Database Setup
- Create `users` table (managed by Better Auth)
- Create `tasks` table (with fields: id, user_id, title, description, completed, created_at, updated_at)
- Add indexes for `tasks.user_id` and `tasks.completed`

### Task 1.2 – API Endpoint: List Tasks
- Method: GET `/api/{user_id}/tasks`
- Include query parameters for `status` and `sort`
- Filter tasks by authenticated user
- Return JSON array of tasks

### Task 1.3 – API Endpoint: Create Task
- Method: POST `/api/{user_id}/tasks`
- Require title, optional description
- Associate task with logged-in user
- Return created task as JSON

### Task 1.4 – API Endpoint: Get Task Details
- Method: GET `/api/{user_id}/tasks/{id}`
- Validate task ownership
- Return task as JSON

### Task 1.5 – API Endpoint: Update Task
- Method: PUT `/api/{user_id}/tasks/{id}`
- Validate task ownership
- Update title and description
- Return updated task as JSON

### Task 1.6 – API Endpoint: Delete Task
- Method: DELETE `/api/{user_id}/tasks/{id}`
- Validate task ownership
- Return confirmation of deletion

### Task 1.7 – API Endpoint: Toggle Task Completion
- Method: PATCH `/api/{user_id}/tasks/{id}/complete`
- Validate task ownership
- Toggle `completed` status
- Return updated task as JSON

### Task 1.8 – JWT Authentication Integration
- Configure Better Auth to issue JWT
- Add middleware to FastAPI to validate JWT
- Decode token to get user info
- Reject unauthorized requests with `401 Unauthorized`

---

## 2. Frontend Tasks (Next.js + Tailwind CSS)

### Task 2.1 – Authentication Pages
- Signup page
- Login page
- Session management using JWT
- Redirect to task dashboard after login

### Task 2.2 – Task Dashboard
- Display all tasks for logged-in user
- Show filtering and sorting options
- Use **task cards** with status indicators:
  - Green ✓ for completed
  - Red ○ for incomplete
- Hover effect: shadow + scale

### Task 2.3 – Add / Update Task Form
- Modal or drawer for adding/updating tasks
- Inputs: title (required), description (optional)
- Buttons: submit (green), cancel (gray)
- Inline validation for title

### Task 2.4 – Delete Task
- Add delete button to each task card
- Show confirmation toast
- Animate removal from task list

### Task 2.5 – Toggle Completion
- Add toggle button/icon on task card
- Animate status change
- Update backend via PATCH API

### Task 2.6 – Filters & Sorting
- Dropdown or buttons for:
  - Status: All, Pending, Completed
  - Sort: Created date, Title
- Apply filter/sort to task list in UI
- Update API requests accordingly

### Task 2.7 – UI/UX Enhancements
- Responsive design: desktop (3-column), tablet (2-column), mobile (1-column)
- Smooth transitions for add, update, delete, complete
- Toast notifications:
  - Success: green
  - Error: red
- Dark mode toggle (optional)

---

## 3. Testing & Validation Tasks

### Task 3.1 – Unit & Integration Tests
- Test all backend APIs for:
  - Valid JWT
  - Unauthorized requests
  - Task ownership
  - Filtering & sorting
- Test frontend components for:
  - Correct rendering
  - Responsive behavior
  - Task CRUD operations
  - Visual indicators

### Task 3.2 – End-to-End Testing
- Create a new user
- Add multiple tasks
- Update, delete, complete tasks
- Verify backend database reflects changes
- Ensure only user-specific tasks are visible

---

## 4. Monorepo & Spec-Kit Tasks

### Task 4.1 – CLAUDE.md Updates
- Root CLAUDE.md: Update project overview & workflow
- Frontend CLAUDE.md: Update component guidelines & Tailwind styling
- Backend CLAUDE.md: Update FastAPI conventions & JWT integration

### Task 4.2 – Spec Files Update
- Update `/specs/features/task-crud.md` for full-stack context
- Update `/specs/api/rest-endpoints.md` to reflect JWT-secured endpoints
- Update `/specs/database/schema.md` for persistent storage

---

## 5. Final Step

- **/sp.implement**
  - Use all above tasks to generate **full-stack implementation**
  - Include backend, frontend, database, authentication, styling, filtering, sorting, and all UI/UX enhancements
  - Ensure task ownership, JWT validation, and responsive frontend

---
'''
```

## Response snapshot

Created the comprehensive task breakdown for the Todo Full-Stack Web Application. The tasks include:

- Backend tasks for FastAPI + SQLModel implementation
- Frontend tasks for Next.js + Tailwind CSS implementation
- Testing and validation tasks
- Monorepo and spec-kit updates

Additionally created:
- CLAUDE.md files for frontend and backend directories with specific guidelines
- API specification for REST endpoints with JWT authentication
- Database schema specification for PostgreSQL with proper relationships and indexes
- Updated root CLAUDE.md with project overview and workflow

All required artifacts are now in place for the implementation phase.

## Outcome

- ✅ Impact: Created complete task breakdown for full-stack todo application implementation
- 🧪 Tests: none
- 📁 Files: Created tasks.md, frontend/CLAUDE.md, backend/CLAUDE.md, specs/api/rest-endpoints.md, specs/database/schema.md, updated CLAUDE.md
- 🔁 Next prompts: Ready to proceed with /sp.implement to execute the tasks
- 🧠 Reflection: Task breakdown provides clear guidance for implementing the full-stack application

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation with /sp.implement