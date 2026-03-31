# FastAPI Backend Template

This is a backend-only version of the [FastAPI Full Stack Template](https://github.com/fastapi/full-stack-fastapi-template), extracted to provide a pure REST API.

## Technology Stack and Features

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
  - 🧰 [SQLModel](https://sqlmodel.tiangolo.com) for the Python SQL database interactions (ORM).
  - 🔍 [Pydantic](https://docs.pydantic.dev), used by FastAPI, for the data validation and settings management.
  - 💾 [PostgreSQL](https://www.postgresql.org) as the SQL database.
- 🐋 [Docker Compose](https://www.docker.com) for development and production.
- 🔒 Secure password hashing by default.
- 🔑 JWT (JSON Web Token) authentication.
- 📫 Email based password recovery.
- ✅ Tests with [Pytest](https://pytest.org).
- 📞 [Traefik](https://traefik.io) as a reverse proxy / load balancer.
- 🏭 CI (continuous integration) and CD (continuous deployment) based on GitHub Actions.

## How To Use It

### Quick Start with Docker Compose

1. **Clone the repository** (if you haven't already).
2. **Setup environment variables**:
   Copy `.env` and adjust values if needed.
3. **Run the stack**:
   ```bash
   docker compose up -d
   ```
4. **Access the API Documentation**:
   Go to [http://localhost/docs](http://localhost/docs) (or [http://api.localhost](http://api.localhost) if using the Traefik setup).

### Backend Development

Detailed backend documentation can be found in [backend/README.md](./backend/README.md).

## Project Structure

- `backend/`: FastAPI application code.
- `scripts/`: Utility scripts for testing and pre-starting the app.
- `compose.yml`: Docker Compose configuration for production-like environments.
- `compose.override.yml`: Docker Compose configuration for local development.

## License

This project is licensed under the terms of the MIT license.
