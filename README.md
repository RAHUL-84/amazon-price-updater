# 🛒 Amazon Price Updater API

An automated Amazon product price tracking application developed using Python, FastAPI, and Playwright. This project automatically searches products on Amazon, extracts product details like product name, MRP, selling price, and discount, and stores the data into an Excel file.

## 🚀 Features

- JWT Based User Authentication
- Secure Login System
- Protected Dashboard Access
- Password Hashing using Bcrypt
- Automated Amazon Product Scraping
- Browser Automation using Playwright
- Product Name Extraction
- MRP Extraction
- Selling Price Extraction
- Discount Extraction
- Excel Report Generation
- FastAPI REST API Integration
- SQLAlchemy Database Integration


## 🛠️ Technologies Used

- Python
- FastAPI
- Playwright
- JWT Authentication
- Python-Jose
- Passlib
- Bcrypt
- SQLAlchemy
- SQLite
- OpenPyXL
- Jinja2
- HTML
- CSS
- Uvicorn


## 📂 Project Structure

```
amazon-price-updater/

│── app/
│   │── main.py
│   │── routes.py
│   │── scraper.py
│   │── excel.py
│   │── config.py
│   │── auth.py
│
│── templates/
│   │── login.html
│   │── dashboard.html
│
│── products.xlsx
│── requirements.txt
│── README.md
```


## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/RAHUL-84/amazon-price-updater.git
```

Go to project directory:

```bash
cd amazon-price-updater
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```


Install dependencies:

```bash
pip install -r requirements.txt
```


Install Playwright browser:

```bash
playwright install
```


## ▶️ Run Project

Start FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

Open browser:

```
http://127.0.0.1:8000/
```


## 🔐 Authentication

- JWT based authentication system
- Secure user login with password hashing using Bcrypt
- Protected dashboard access using JWT tokens
```


## 🔄 Project Workflow

1. User logs into the application.
2. JWT token is generated after successful authentication.
3. User accesses the protected dashboard.
4. Playwright opens Amazon automatically.
5. Products are searched from the configured product list.
6. Product details are extracted:
   - Product Name
   - MRP
   - Selling Price
   - Discount
7. Extracted data is stored in Excel file.


## 📊 Excel Output

Generated Excel file contains:

| S.No | Product Name | MRP | Selling Price | Discount |
|-----|--------------|-----|---------------|----------|
| 1 | Samsung Galaxy S25 | ₹80,999 | ₹59,999 | -26% |


## 📡 API Features

- User Login API
- JWT Token Generation
- Protected Dashboard Route
- Amazon Scraping Trigger API
- Excel Data Export


## 🔮 Future Enhancements

- Price history tracking
- Scheduled automatic scraping
- Email price alerts
- Multiple user support
- Cloud deployment
- Database product storage