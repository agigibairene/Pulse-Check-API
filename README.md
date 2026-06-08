# Pulse-Check-API ("Watchdog" Sentinel)

The API allows clients to:

- Register monitors/devices
- Send heartbeat (pulse) signals
- Pause monitoring
- Check monitor status
- View API documentation through Swagger UI


## Tech Stack


| Component         | Technology                          |
|-------------------|-------------------------------------|
| Backend           | Django 6                            |
| Database          | Sqlite                              |
| Package management| uv                                  |  


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/agigibairene/Pulse-Check-API.git
cd Pulse-Check-API
```

### 2. Create a Virtual Environment

Using uv:

```bash
uv venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
uv sync
```

### 4. Apply Migrations

```bash
cd pulse_check_api
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

## API Endpoints

### Home

Returns a welcome message and available routes.

### Request

```http
GET /
```

### Response

```json
{
  "message": "Welcome to the Pulse Check API",
  "available_endpoints": {
    "admin": "/admin/",
    "monitors": "/monitors/",
    "openapi_schema": "/schema/",
    "swagger_docs": "/schema/swagger-ui/"
  }
}
```

## Register a Monitor

Creates a new monitor/device.

### Endpoint

```http
POST /monitors/
```

### Request Body

```json
{
  "id": "device-1",
  "timeout": 60,
  "alert_email": "test@gmail.com"
}
```

### Success Response

```json
{
  "message": "Monitor device-1 successfully created"
}
```

### Status Code

```text
201 Created
```
### Retrieve All Monitors

Returns a list of all registered monitors.

#### Endpoint

```http
GET /monitors/
```

#### Success Response

```json
[
  {
    "id": "device-123",
    "timeout": 60,
    "alert_email": "test@gmail.com",
    "status": "Healthy",
    "last_beat": "2026-06-08T20:37:58.058631Z"
  }
]
```

## Send Heartbeat

Updates the monitor's last heartbeat timestamp, indicating the device is alive.

### Endpoint

```http
POST /monitors/{id}/heartbeat/
```

### Example

```http
POST /monitors/device-1/heartbeat/
```

### Success Response

```json
{
  "message": "Heartbeat received"
}
```

### Status Code

```text
200 OK
```

---

## Pause a Monitor

Temporarily disables monitoring for a device.

### Endpoint

```http
PATCH /monitors/{id}/pause/
```

### Example

```http
PATCH /monitors/device-1/pause/
```

### Success Response

```json
{
  "message": "Monitor paused successfully"
}
```

### Status Code

```text
200 OK
```

---

## Monitor Device Status

Retrieves the current monitoring status of a specific device.

### Endpoint

```http
GET /monitors/{id}/monitor-device/
```

### Example

```http
GET /monitors/device-1/monitor-device/
```

### Success Response

```json
{
  "id": "device-1",
  "status": "paused",
  "timeout": 60,
  "last_beat": "2026-06-08T20:37:58.058631Z",
  "alert_email": "test@gmail.com"
}
```

### Status Code

```text
200 OK
```

---

# API Documentation

## OpenAPI Schema

```http
GET /schema/
```

Returns the raw OpenAPI specification.

---

## Swagger UI

Open the interactive API documentation:

```text
http://127.0.0.1:8000/schema/swagger-ui/
```
