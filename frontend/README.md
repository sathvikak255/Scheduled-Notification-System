<<<<<<< HEAD
# Frontend

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 17.3.17.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.
=======
# 📊 Scheduled Notification System

A sophisticated full-stack web application for automated daily email reporting with advanced PDF generation, graph embedding, and intelligent subscription management. Built with modern Django REST Framework backend and Angular standalone components frontend.

---

## 🎯 Key Features & Technical Highlights

### 📈 Advanced Report Generation
- **Multi-format Support**: HTML, PDF, or combined delivery
- **Dynamic Graph Embedding**: Charts seamlessly integrated into PDF reports using Matplotlib + ReportLab
- **Template-based HTML Reports**: Django templating with responsive design
- **Asynchronous Processing**: Non-blocking report generation via Celery workers

### 🔄 Intelligent Subscription Management
- **Automatic Lifecycle Management**: Smart activation/deactivation based on date ranges
- **State Persistence**: Robust subscription state tracking with Django ORM
- **Batch Processing**: Efficient handling of multiple subscriptions
- **Email Validation & Deduplication**: Prevents duplicate subscriptions

### 🏗️ Modern Architecture
- **RESTful API Design**: Clean, documented endpoints with DRF serializers
- **Reactive Frontend**: Angular standalone components with RxJS state management
- **Microservice-Ready**: Decoupled backend services with Redis message broker
- **Scalable Task Queue**: Celery + Redis for distributed processing

---

## 🛠️ Tech Stack & Architecture

### Backend (Django)
```
scheduled-notification-system/
│
├── backend/                          # Django backend
│   ├── manage.py                    # Django CLI
│   ├── backend/                     # Django project folder
│   │   ├── __init__.py
│   │   ├── settings.py              # Django settings (DB, email, installed apps, etc)
│   │   ├── urls.py                  # Root URLs (include api/)
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── subscriptions/               # Django app for subscriptions & reports
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py                # Subscription model: email, start_date, end_date, formats, is_active
│   │   ├── views.py                 # API views: subscribe, unsubscribe, list subscriptions
│   │   ├── serializers.py           # DRF serializers for Subscription
│   │   ├── urls.py                  # API endpoints for subscription app
│   │   ├── tasks.py or commands.py  # Scheduled report sending (custom management command)
│   │   ├── templates/               # HTML templates for reports
│   │   │   └── reports/
│   │   │       └── report_template.html
│   │   └── utils.py                 # PDF report generation function(s)
│   │
│   ├── requirements.txt
```

### Frontend (Angular)
```
├── frontend/                        # Angular frontend
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   │   ├── subscription-form/
│   │   │   │   │   ├── subscription-form.component.ts
│   │   │   │   │   ├── subscription-form.component.html
│   │   │   │   │   └── subscription-form.component.css
│   │   │   │   ├── subscriptions-list/
│   │   │   │   │   ├── subscriptions-list.component.ts
│   │   │   │   │   ├── subscriptions-list.component.html
│   │   │   │   │   └── subscriptions-list.component.css
│   │   │   │   ├── header/
│   │   │   │   │   ├── header.component.ts
│   │   │   │   │   ├── header.component.html
│   │   │   │   │   └── header.component.css
│   │   │   ├── app.component.ts
│   │   │   ├── app.routes.ts        # Angular routes
│   │   │   ├── interceptors/
│   │   │   │   └── auth.interceptor.ts  # Auth token handling
│   │   │   └── services/            # API services if used
│   │   ├── assets/
│   │   ├── environments/
│   │   └── main.ts                  # Angular bootstrap
│   ├── package.json
│   └── angular.json
│
├── README.md
└── .gitignore
```

---

## 

## 🎨 User Experience Highlights

### Intelligent Form Validation
- **Real-time validation** with visual feedback
- **Smart date picker** with business day selection
- **Email duplicate detection** with suggestions
- **Progressive enhancement** for accessibility

### Responsive Dashboard
- **Live subscription status** updates via WebSocket
- **Filterable subscription list** with search
- **Bulk operations** for admin efficiency
- **Mobile-optimized** interface

### Notification System
- **Toast notifications** for user actions
- **Email confirmations** for subscription changes
- **Admin alerts** for system events
- **Progress indicators** for long-running tasks

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- Redis Server
- PostgreSQL (recommended for production)

### Development Setup
```bash
# Clone and setup backend
git clone https://github.com/sathvikak255/Scheduled-Notification-System.git
cd Scheduled-Notification-System/backend

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Database setup
python manage.py migrate
python manage.py createsuperuser

# Start services
python manage.py runserver

# Setup frontend
cd ../frontend
npm install
ng serve
```

# 📋 Scheduled Notification System – API & Architecture Documentation

---

## 🚀 Core API Endpoints

### 📬 1. Subscription Management – `POST /api/v1/subscriptions/`
Create a new subscription by providing the user's email, subscription time range, preferred report format, delivery frequency, and timezone.

**Request Body includes:**
- `email`
- `start_date` and `end_date`
- `report_format`: `html`, `pdf`, or `both`

**Response:**
- Subscription ID
- Status (`active`)
- `created_at` timestamp
- `next_delivery` date & time

📌 _📷 **Image: `sub-form` (Subscription Form UI)**_

---

### 📂 2. Subscription Listing – `GET /api/v1/subscriptions/`
Retrieve a filtered list of all subscriptions.

**Supports query parameters like:**
- `status=active`
- `format=pdf`

📌 _📷 **Image: `subs-list` (Subscription List View)**_

---

### 🔄 3. Batch Update – `PATCH /api/v1/subscriptions/bulk-update/`
Update multiple subscriptions at once.

**Payload includes:**
- `subscription_ids`: list of subscription UUIDs

📌 _📷 **Image: `subs-list` with checkboxes + batch action buttons**_

---

## 🧾 Report Generation Endpoints

### 📈 4. Generate Report
Manually trigger report generation for a subscription.

**Fields include:**
- `subscription_id`
- `include_charts`: boolean
- `chart_types`: array like `["line", "bar", "pie"]`

📌 _📷 **Image: `report-history` (History with download links)**_

---

## ⚙️ System Architecture (High-Level)

---

### 🧠 Frontend (Angular)
- Modular component architecture
- Uses:
  - **Reactive Forms** for input handling
  - **Observables** for real-time state updates
- Clean UI for creating, listing, and managing subscriptions

📌 _📷 **Image: `sub-form`, `subs-list`, `report-history`**_

---

### 🧰 Backend (Django + Django REST Framework)
- RESTful APIs for subscription and report management
- Validations:
  - Prevent overlapping subscriptions
  - Ensure correct date range
- Optimized with:
  - Enum choices
  - Unique constraints
  - Indexed fields

📌 _📷 **Image: `admin-dashboard` or Django admin view**_

---

## 📄 Report & Chart Generation

- Reports support **PDF and HTML formats**
- Embedded charts using **Matplotlib**
- Modern themes and publication-quality rendering

📌 _📷 **Image: Sample PDF chart (embed a separate chart image here if available)**_

---

## ⏱️ Asynchronous Task Queue

- Powered by **Celery** and **Redis**
- Handles:
  - Daily/weekly report scheduling
  - Email notifications with attachments
- Uses:
  - Task chaining
  - Exponential backoff for retries
  - Auto recovery for transient failures

📌 _📷 **Image: architecture diagram (not in screenshot – insert manually)**_

---

## 📧 Email Notification System

- Sends scheduled emails with:
  - PDF/HTML report attachments
  - Formatted HTML content
- Supports:
  - Retry logic
  - Fallback for missing content
  - SMTP integration
 
---

## ✅ Extra Admin & Utility Views

- **`admin-login`**: Admin authentication
- **`admin-dashboard`**: Overview of all system stats
- **`admin-logout`**: Secure admin exit
- **`createsuperuser`**: For initial superuser setup
- **`unsub_success` / `unsubscribe`**: Unsubscription flow with success page

📌 _📷 **Image: each corresponding screen**_

---

## ✅ Summary

This system provides a powerful solution for **automated, subscription-based report delivery**, including:

- 🎨 A user-friendly Angular UI  
- 🔗 A scalable Django REST backend  
- ⚙️ Robust task automation using Celery  
- 📊 Rich, chart-embedded PDF reports  

Perfect for performance tracking, daily monitoring, or analytics distribution.



---

## 📝 Testing Strategy

### Backend Testing
```python
# Comprehensive test coverage
pytest backend/tests/ --cov=backend --cov-report=html

# API endpoint testing
class SubscriptionAPITestCase(APITestCase):
    def test_create_subscription_validation(self):
        # Test date validation, email format, etc.
        pass
    
    def test_bulk_operations(self):
        # Test batch subscription management
        pass
```

### Frontend Testing
```bash
# Unit tests with Jest
ng test --code-coverage

# E2E tests with Cypress
npm run e2e
```

---

## 📈 Performance Optimization

### Database Optimization
- **Indexed queries** for subscription lookups
- **Query optimization** with select_related/prefetch_related
- **Database connection pooling** with pgbouncer
- **Read replicas** for reporting queries

### Caching Strategy
- **Redis caching** for frequently accessed data
- **Template fragment caching** for report generation
- **API response caching** with ETags
- **Static file optimization** with CDN

---

## 🤝 Contributing

### Development Workflow
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Code Standards
- **Python**: PEP 8, Black formatting, mypy type checking
- **TypeScript**: ESLint, Prettier, strict type checking
- **Testing**: 90%+ code coverage required
- **Documentation**: Comprehensive docstrings and comments

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Sathvika K**
- GitHub: [@sathvikak255](https://github.com/sathvikak255)
- Email: sathvikak255@example.com
- LinkedIn: [Connect with me](https://linkedin.com/in/sathvikak255)

---

## 🙏 Acknowledgments

- Django REST Framework team for excellent API framework
- Angular team for modern frontend capabilities
- Celery community for robust task queue system
- ReportLab team for PDF generation excellence
>>>>>>> a4553e4a62ecf4130268242ea58a304e114a90dc
