# Quickstart Guide: UI/UX Enhancement for Todo App

**Date**: 2025-12-31
**Feature**: UI/UX Enhancement for Todo App
**Branch**: 001-ui-ux-enhancement

## Overview

This guide provides instructions for setting up and running the UI/UX enhanced Todo app. It covers the development environment setup, dependencies installation, and basic usage patterns.

## Prerequisites

- Node.js 18+ (for frontend development)
- Python 3.11+ (for backend development)
- npm or yarn package manager
- PostgreSQL database (or Neon Serverless PostgreSQL account)
- Git for version control

## Frontend Setup

### 1. Install Dependencies

```bash
cd frontend
npm install
# or
yarn install
```

### 2. Install UI/UX Enhancement Dependencies

```bash
# Install theme management
npm install next-themes

# Install animation library
npm install framer-motion

# Install accessible UI components
npm install @headlessui/react

# Install form management
npm install react-hook-form @hookform/resolvers

# Install validation
npm install zod

# Install toast notifications
npm install sonner

# Install icons
npm install lucide-react
```

### 3. Configure Tailwind CSS

Update `tailwind.config.js` to include dark mode and custom configurations:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: 'class', // Enable class-based dark mode
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          500: '#3b82f6',
          600: '#2563eb',
        },
        secondary: {
          50: '#f0fdfa',
          500: '#10b981',
          600: '#059669',
        }
      }
    },
  },
  plugins: [],
}
```

## Backend Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the backend directory:

```env
DATABASE_URL="postgresql://user:password@localhost:5432/todo_app"
SECRET_KEY="your-super-secret-key-here"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running the Application

### Development Mode

#### Frontend
```bash
cd frontend
npm run dev
# App will be available at http://localhost:3000
```

#### Backend
```bash
cd backend
python -m uvicorn src.main:app --reload --port 8000
# API will be available at http://localhost:8000
```

### Production Mode

#### Frontend Build
```bash
cd frontend
npm run build
npm start
```

## Key UI/UX Enhancement Features

### 1. Dark Mode Toggle

The application includes a theme toggle component that allows users to switch between light and dark modes:

```tsx
// Example usage in a component
import { useTheme } from "next-themes"

export function ThemeToggle() {
  const { theme, setTheme } = useTheme()

  return (
    <button
      onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
      aria-label="Toggle theme"
    >
      {theme === "dark" ? "☀️" : "🌙"}
    </button>
  )
}
```

### 2. Task Card Component

The enhanced task card includes hover effects, priority indicators, and smooth animations:

```tsx
// Example task card structure
<div className="task-card p-4 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 bg-white dark:bg-gray-800">
  <div className="flex items-start justify-between">
    <div className="flex items-center space-x-2">
      <input
        type="checkbox"
        className="w-5 h-5 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
      />
      <span className="text-lg font-medium">Task Title</span>
    </div>
    <span className="px-2 py-1 text-xs font-medium bg-red-100 text-red-800 rounded-full">
      High Priority
    </span>
  </div>
  <p className="mt-2 text-gray-600 dark:text-gray-300">Task description</p>
  <div className="mt-3 flex justify-end space-x-2">
    <button className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200">
      Edit
    </button>
    <button className="text-red-500 hover:text-red-700">
      Delete
    </button>
  </div>
</div>
```

### 3. Modal Component

The application uses accessible modal components for task creation and editing:

```tsx
// Example modal usage with Headless UI
import { Dialog, Transition } from '@headlessui/react'

function MyModal({ isOpen, onClose }) {
  return (
    <Transition appear show={isOpen} as={Fragment}>
      <Dialog as="div" className="relative z-10" onClose={onClose}>
        <Transition.Child
          as={Fragment}
          enter="ease-out duration-300"
          enterFrom="opacity-0"
          enterTo="opacity-100"
          leave="ease-in duration-200"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
        >
          <div className="fixed inset-0 bg-black bg-opacity-25" />
        </Transition.Child>

        <div className="fixed inset-0 overflow-y-auto">
          <div className="flex min-h-full items-center justify-center p-4 text-center">
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0 scale-95"
              enterTo="opacity-100 scale-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100 scale-100"
              leaveTo="opacity-0 scale-95"
            >
              <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all">
                {/* Modal content */}
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </div>
      </Dialog>
    </Transition>
  )
}
```

## API Endpoints

### Theme Management
- `GET /api/users/theme` - Get user's theme preference
- `PUT /api/users/theme` - Update user's theme preference

### Enhanced Task Operations
- `GET /api/tasks/search?q={query}&status={status}&priority={priority}` - Search and filter tasks
- `PUT /api/tasks/{id}/position` - Update task position for drag-and-drop
- `GET /api/tasks/stats` - Get task statistics for progress tracking

## Testing

### Frontend Testing
```bash
# Run unit tests
npm run test

# Run end-to-end tests
npm run test:e2e
```

### Backend Testing
```bash
# Run API tests
python -m pytest tests/
```

## Deployment

### Environment Variables

Ensure these environment variables are set in your deployment environment:

**Frontend:**
- `NEXT_PUBLIC_API_URL` - Base URL for the backend API

**Backend:**
- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - JWT secret key
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time

### Build and Deploy

1. Build the frontend application:
```bash
cd frontend
npm run build
```

2. Deploy both frontend and backend to your preferred hosting platform (Vercel, Netlify, AWS, etc.)