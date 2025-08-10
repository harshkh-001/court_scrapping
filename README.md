# Court Scraping Django Project

This Django project scrapes case data from the **Delhi High Court** website and presents it in a clean tabular format. The main Django project is `court`, and the scraping logic is inside the `info` app.

---

## 🏛 Court Chosen

- **Delhi High Court**
- Scrapes case listings, case details, and hearing dates directly from the official court site.

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/harshkh-001/court_scrapping.git
cd court_scrapping
```


## ⚙️ Setup Instructions

### 2. Create & activate a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
Copy
Edit
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory with:

```env
# Django secret key
DJANGO_SECRET_KEY=your_secret_key_here

# Selenium WebDriver path
WEBDRIVER_PATH=/path/to/chromedriver

# Tesseract OCR path (if needed)
TESSERACT_PATH=/usr/bin/tesseract

# Any other required environment variables
```

## 🤖 CAPTCHA Strategy

The scraper handles CAPTCHA challenges encountered on the Delhi High Court site using Tesseract OCR.

- Make sure Tesseract OCR is installed and accessible.
- Paths to Tesseract can be configured via the `TESSERACT_PATH` environment variable.

---

## 🐳 Docker Instructions

### Build Docker image

```bash
docker build -t court_scraper .
```

### Run container
```bash
docker run -d -p 8000:8000 --name court_scraper_container court_scraper

//or

docker-compose up
```

### Run Django migrations & start server
```bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## 🏗 Project Structure
```bash
court_scrapping/
│
├── court/                 # Django project (settings.py here)
│
├── info/                  # Django app - scraping logic & output
│   ├── management/commands/  # Custom scrape commands
│   ├── templates/           # HTML templates for tables
│   ├── static/              # Static files if any
│   └── views.py             # Views for output display
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── manage.py
└── README.md
```

## Optional Run using django
```bash
python manage.py runserver
```

## 📄 Sample Output

Tabular display of cases scraped from Delhi High Court.

Includes case numbers, parties, hearing dates, statuses, etc.

---

## 📜 License

This project is licensed under the MIT License — see the LICENSE file.
