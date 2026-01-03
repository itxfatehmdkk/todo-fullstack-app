# /sp.task – Todo Full-Stack Web Application: Task Breakdown

**Project**: Todo Full-Stack Web Application
**Phase**: II – Full-Stack Multi-User with Authentication
**Created**: 2025-12-28
**Status**: Draft

---

## 1. Backend Tasks (FastAPI + SQLModel)

### Task 1.1 – Database Setup
- [X] Create `users` table (managed by Better Auth)
- [X] Create `tasks` table (with fields: id, user_id, title, description, completed, created_at, updated_at)
- [X] Add indexes for `tasks.user_id` and `tasks.completed`

### Task 1.2 – API Endpoint: List Tasks
- [X] Method: GET `/api/{user_id}/tasks`
- [X] Include query parameters for `status` and `sort`
- [X] Filter tasks by authenticated user
- [X] Return JSON array of tasks

### Task 1.3 – API Endpoint: Create Task
- [X] Method: POST `/api/{user_id}/tasks`
- [X] Require title, optional description
- [X] Associate task with logged-in user
- [X] Return created task as JSON

### Task 1.4 – API Endpoint: Get Task Details
- [X] Method: GET `/api/{user_id}/tasks/{id}`
- [X] Validate task ownership
- [X] Return task as JSON

### Task 1.5 – API Endpoint: Update Task
- [X] Method: PUT `/api/{user_id}/tasks/{id}`
- [X] Validate task ownership
- [X] Update title and description
- [X] Return updated task as JSON

### Task 1.6 – API Endpoint: Delete Task
- [X] Method: DELETE `/api/{user_id}/tasks/{id}`
- [X] Validate task ownership
- [X] Return confirmation of deletion

### Task 1.7 – API Endpoint: Toggle Task Completion
- [X] Method: PATCH `/api/{user_id}/tasks/{id}/complete`
- [X] Validate task ownership
- [X] Toggle `completed` status
- [X] Return updated task as JSON

### Task 1.8 – JWT Authentication Integration
- [X] Configure Better Auth to issue JWT
- [X] Add middleware to FastAPI to validate JWT
- [X] Decode token to get user info
- [X] Reject unauthorized requests with `401 Unauthorized`

---

## 2. Frontend Tasks (Next.js + Tailwind CSS)

### Task 2.1 – Authentication Pages
- [X] Signup page
- [X] Login page
- [X] Session management using JWT
- [X] Redirect to task dashboard after login

### Task 2.2 – Task Dashboard
- [X] Display all tasks for logged-in user
- [X] Show filtering and sorting options
- [X] Use **task cards** with status indicators:
  - [X] Green ✓ for completed
  - [X] Red ○ for incomplete
- [X] Hover effect: shadow + scale

### Task 2.3 – Add / Update Task Form
- [X] Modal or drawer for adding/updating tasks
- [X] Inputs: title (required), description (optional)
- [X] Buttons: submit (green), cancel (gray)
- [X] Inline validation for title

### Task 2.4 – Delete Task
- [X] Add delete button to each task card
- [X] Show confirmation toast
- [X] Animate removal from task list

### Task 2.5 – Toggle Completion
- [X] Add toggle button/icon on task card
- [X] Animate status change
- [X] Update backend via PATCH API

### Task 2.6 – Filters & Sorting
- [X] Dropdown or buttons for:
  - [X] Status: All, Pending, Completed
  - [X] Sort: Created date, Title
- [X] Apply filter/sort to task list in UI
- [X] Update API requests accordingly

### Task 2.7 – UI/UX Enhancements
- [X] Responsive design: desktop (3-column), tablet (2-column), mobile (1-column)
- [X] Smooth transitions for add, update, delete, complete
- [X] Toast notifications:
  - [X] Success: green
  - [X] Error: red
- [X] Dark mode toggle (optional)

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
  - [X] Use all above tasks to generate **full-stack implementation**
  - [X] Include backend, frontend, database, authentication, styling, filtering, sorting, and all UI/UX enhancements
  - [X] Ensure task ownership, JWT validation, and responsive frontend