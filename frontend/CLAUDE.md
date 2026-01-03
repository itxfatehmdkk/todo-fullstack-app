# Claude Code Rules - Frontend (Next.js + TypeScript + Tailwind CSS)

You are an expert AI assistant specializing in frontend development for the Todo Full-Stack Web Application. Your primary goal is to implement the frontend components using Next.js 14+, TypeScript, and Tailwind CSS.

## Task Context

**Project**: Todo Full-Stack Web Application
**Frontend Stack**: Next.js 14+ (App Router), TypeScript, Tailwind CSS
**Target**: Responsive web application with multi-user authentication

## Core Frontend Components

### 1. Authentication Components
- Implement signup and login pages
- Manage JWT session storage and validation
- Redirect users to dashboard after successful authentication
- Handle authentication errors gracefully

### 2. Task Dashboard
- Display all tasks for the logged-in user
- Implement filtering and sorting functionality
- Create task cards with visual status indicators:
  - Green checkmark ✓ for completed tasks
  - Red circle ○ for incomplete tasks
- Add hover effects (shadow + scale) to task cards

### 3. Task Management Components
- Create modal/drawer for adding and updating tasks
- Implement required inputs: title (required), description (optional)
- Add submit (green) and cancel (gray) buttons
- Include inline validation for title field

### 4. Task Interaction Features
- Add delete button to each task card
- Implement toggle completion functionality
- Add smooth transitions for add, update, delete, and completion operations
- Create toast notifications (green for success, red for errors)

### 5. UI/UX Enhancements
- Implement responsive design:
  - Desktop: 3-column grid layout
  - Tablet: 2-column grid layout
  - Mobile: 1-column layout
- Add dark mode toggle (optional)
- Ensure all components are accessible with proper ARIA attributes

## Technical Guidelines

### Next.js Specific
- Use App Router (app directory structure)
- Implement server-side rendering where appropriate
- Use React Server Components when possible for performance
- Follow Next.js best practices for routing and data fetching

### TypeScript Guidelines
- Use strict TypeScript configuration
- Create proper type definitions for all components and data structures
- Implement type-safe API calls
- Use TypeScript interfaces for all data models

### Tailwind CSS Guidelines
- Use utility-first approach for styling
- Implement consistent spacing with Tailwind's spacing scale
- Use Tailwind's color palette consistently
- Implement responsive design with Tailwind's responsive prefixes
- Use Tailwind's animation utilities for smooth transitions

## API Integration
- Connect to backend API endpoints with proper JWT authentication
- Handle API errors gracefully with user-friendly messages
- Implement loading states for all async operations
- Ensure all API requests include the JWT token in the Authorization header

## Testing
- Write component tests using Jest and React Testing Library
- Test responsive behavior across different screen sizes
- Validate form inputs and error handling
- Test authentication flow and session management