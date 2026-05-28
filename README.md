# Food Order Management API - FastAPI Modular Starter

Created for testing a modular FastAPI food ordering backend.

## Features

- Modular FastAPI structure
- SQLite database using SQLAlchemy
- Menu item management
- Customer management
- Order creation
- Order status update
- Basic service layer separation
- Seed data for testing
- Swagger UI included

## Project Structure

```text
food_order_fastapi_modular/
├── app/
│   ├── main.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── database.py
│   │   └── seed.py
│   ├── models/
│   │   ├── customer.py
│   │   ├── menu.py
│   │   └── order.py
│   ├── routers/
│   │   ├── customers.py
│   │   ├── menu.py
│   │   └── orders.py
│   ├── schemas/
│   │   ├── customer.py
│   │   ├── menu.py
│   │   └── order.py
│   └── services/
│       ├── customer_service.py
│       ├── menu_service.py
│       └── order_service.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the API

```bash
uvicorn app.main:app --reload
```

### 4. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

## Seed Data

To load sample menu and customer data:

```bash
python -m app.db.seed
```

## Main API Endpoints

### Customers

```http
POST /customers
GET /customers
GET /customers/{customer_id}
```

### Menu

```http
POST /menu
GET /menu
GET /menu/{menu_item_id}
PATCH /menu/{menu_item_id}/availability
```

### Orders

```http
POST /orders
GET /orders
GET /orders/{order_id}
PATCH /orders/{order_id}/status
```

## Sample Order Request

```json
{
  "customer_id": 1,
  "items": [
    {
      "menu_item_id": 1,
      "quantity": 2
    },
    {
      "menu_item_id": 3,
      "quantity": 1
    }
  ]
}
```

## Order Status Values

```text
PENDING
CONFIRMED
PREPARING
READY
DELIVERED
CANCELLED
```
