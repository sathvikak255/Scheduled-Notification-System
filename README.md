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

📌 _📷 **Image: Sample email screenshot (not in folder – insert manually)**_

---

## ✅ Extra Admin & Utility Views

- **`admin-login`**: Admin authentication
- **`admin-dashboard`**: Overview of all system stats
- **`admin-logout`**: Secure admin exit
- **`createsuperuser`**: For initial superuser setup
- **`unsub_success` / `unsubscribe`**: Unsubscription flow with success page

📌 _📷 **Image: each corresponding screen**_

---

Would you like me to export this aligned `.md` file for you now?
