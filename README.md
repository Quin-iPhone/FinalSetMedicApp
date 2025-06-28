# 🎬 Set Medic App – Web Application

A full-featured **Flask-based web application** tailored for **Events, Film, and Television production companies**. The Set Medic App allows users to:

- Explore services
- Request quotes
- Book medical support
- Receive invoices
- Make secure payments
- Download receipts

It also includes a blog, social media integration, and a responsive, branded user interface.

---

## 🚀 Features

- **🩺 Service Overview & Booking**  
  Browse detailed service listings and request a custom quote or booking.

- **💳 Invoicing & Payment**  
  Auto-generated invoices, secure payment processing, and downloadable receipts.

- **📰 Blog & Social Media Integration**  
  Stay updated with our blog and connect with us on social platforms.

- **🎨 Responsive & Branded UI**  
  Consistent use of our logo, color palette, and typography across devices.

---

## 🖥️ Running Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Quin-iPhone/RetrySetMedicApp.git
   cd RetrySetMedicApp
   ```

2. **(Optional) Create a Virtual Environment**

   ```bash
   gunicorn app:app env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

      - **Environment:** Python 3
   - **Build Command:**
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:**
     ```bash
     gunicorn app:app
     ```


5. Open your browser and go to http://localhost:5000

---

## ☁️ Deployment on Render.com

To deploy the Set Medic App on Render.com:

   - **Environment:** Python 3
   - **Build Command:**
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:**
     ```bash
     gunicorn app:app
     ```

---

## 🎨 Customization

- **Styling**  
  Modify `static/css/style.css` to adjust colors, fonts, and layout.

- **Payment & Data Integration**  
  Expand `app.py` to integrate real payment gateways (e.g., Stripe, PayPal) and databases.

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.