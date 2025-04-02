## Tiberbu Engineering Challenge

# Healthcare Appointment Scheduling System

### Overview

This project is a healthcare appointment scheduling system built with FastAPI and PostgreSQL. The system allows patients to book appointments with doctors, manage their profiles, and ensure scheduling conflicts are avoided. It also supports authentication, role-based access control, and doctor availability management.

### Features

- Patient Management: Register and manage patient profiles.

- Doctor Management: Maintain doctor profiles and availability.

- Appointment Scheduling: Book, update, and cancel appointments.

- Authentication & Security: OAuth2 authentication with JWT and role-based access control.

- Error Handling & Validation: Proper input validation and meaningful error responses.

- Performance Optimizations: Asynchronous processing and Redis-based message queuing.

### Technology Stack

- Backend: FastAPI (Python)

- Database: PostgreSQL

- Authentication: OAuth2 (JWT-based)

- Task Queue: Redis (for async processing, optional)

- Documentation: OpenAPI (Swagger UI)

### Folder Structure

```
healthcare_api/
│-- app/
│   │-- models/        # Database models (SQLAlchemy)
│   │-- schemas/       # Pydantic models for validation
│   │-- routes/        # API route handlers
│   │-- services/      # Business logic & core functions
│   │-- utils/         # Helper functions & utilities
│   │-- config.py      # Application settings
│   │-- main.py        # Entry point for FastAPI
│-- migrations/        # Database migrations
│-- tests/             # Unit and integration tests
│-- .env               # Environment variables
│-- README.md          # Project documentation
│-- requirements.txt   # Dependencies
│-- docker-compose.yml # Dockerized setup (optional)

```