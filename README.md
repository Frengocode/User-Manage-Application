# Interview Test Project

## Overview

This project was developed as a test assignment with a strong focus on software architecture, maintainability, and clean code principles.

The application is built using **Clean Architecture**, which separates business logic from frameworks, databases, and external services, making the system easier to maintain, test, and extend.

---

## Technologies

* Python 3.14
* FastAPI
* SQLAlchemy (Async)
* PostgreSQL
* Redis
* RabbitMQ
* Dishka (Dependency Injection)
* APScheduler
* Docker & Docker Compose
* JWT Authentication
* Pydantic

---

## Architecture

The project follows the principles of **Clean Architecture**.

### Layers

* **Domain** – business entities and rules
* **Application** – use cases and business logic
* **Infrastructure** – database, messaging, email, and external services
* **Controllers** – API controllers and request/response models

This structure helps keep the business logic independent from implementation details.

---

## Background Tasks

For scheduled background jobs, **APScheduler** was chosen instead of Celery.

### Why APScheduler?

For the current project requirements, APScheduler provides a simpler and more lightweight solution.

Examples of scheduled tasks:

* Deleting inactive users
* Cleanup jobs
* Periodic maintenance tasks

Using APScheduler reduces infrastructure complexity and is easier to integrate when distributed task processing is not required.

---

## Running the Project

### Requirements

* Docker
* Docker Compose

### Start Application

```bash
sudo docker compose up
```

or

```bash
sudo docker-compose up
```

After startup, all required services will be launched automatically:

* Application
* PostgreSQL
* Redis
* RabbitMQ

---

## Features

* User registration
* User authentication
* JWT Access Token
* JWT Refresh Token
* Role-based authorization
* RabbitMQ event publishing
* Email notifications
* Scheduled background tasks
* Dependency Injection with Dishka
* Asynchronous database operations

---

## Project Goal

The goal of this project was not only to implement the required functionality but also to demonstrate:

* Clean Architecture principles
* Dependency Injection
* Domain-Driven Design concepts
* Asynchronous programming
* Scalable application structure
* Clean and maintainable code

---

## Thank You

Thank you for taking the time to review this project.

I truly appreciate your time, attention, and consideration. It was a great opportunity to work on this assignment and demonstrate my approach to software development and architecture.

Have a great day!
