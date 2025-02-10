# CatDanceSystem - Dance Tournament Management System

A web-based system for managing dance tournaments, built with **FastAPI** (backend) and **Refine.dev** (frontend).

## 🚀 Tech Stack

- **Backend:** FastAPI, PostgreSQL
- **Frontend:** Refine.dev (React + Ant Design)
- **Deployment:** Docker, Nginx

---

## 📦 Installation & Setup

### 1️⃣ Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/Ads369/CatDanceSystem
cd CatDanceSystem
```

### 3️⃣ Run the Project with Docker

```sh
docker-compose up --build
```

This will:

- Start the FastAPI backend
- Set up the PostgreSQL database
- Run the Refine-based frontend
- Serve everything via Nginx

---

## 📡 API Endpoints Example

| Method | Endpoint            | Description         |
| ------ | ------------------- | ------------------- |
| GET    | `/api/dancers/`     | Get list of dancers |
| POST   | `/api/dancers/`     | Add a new dancer    |
| GET    | `/api/dancers/{id}` | Get dancer by ID    |
| PUT    | `/api/dancers/{id}` | Update dancer info  |
| DELETE | `/api/dancers/{id}` | Remove dancer       |

---

## 🎨 Frontend (Refine.dev)

The frontend is built using Refine.dev and includes:

- **Admin Panel** for managing dancers

To run only the frontend locally:

```sh
cd frontend
npm install
npm run dev
```

---

## 🛠 Development & Debugging

To access the FastAPI interactive docs, visit:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

To access the PostgreSQL database:

```sh
docker exec -it dance-db psql -U postgres -d dance_db
```

---

## 📜 License

This project is licensed under the MIT License.

---

### 👨‍💻 Author

Developed by **Dmitriy Aleksandrov**
📧 Email: [adsis369@gmail.com](mailto:adsis369@gmail.com)
💬 Telegram: [@Ads_2s](https://t.me/Ads_2s)
