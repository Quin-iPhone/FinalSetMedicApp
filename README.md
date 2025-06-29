Overview of Set Medic App

**Company Name**: Set Medic South Africa

**Mission Statement**:
"To provide professional and reliable medical services to film and television productions, ensuring the safety and well-being of all cast and crew members."

**Services Offered**:

1. **On-Set Medical Support**: Immediate medical assistance during filming.
2. **Health and Safety Training**: Training sessions for cast and crew on health and safety protocols.
4. **Medical Equipment Supply**: Provision of necessary medical equipment for on-set use.
5. **Consultation Services**: Expert advice on health and safety planning for productions.

**Key Features**:

- **Highly Qualified Staff**: Team of certified medical professionals with experience in the film industry.
- **24/7 Availability**: Round-the-clock medical support to accommodate all production schedules.
- **Customized Services**: Tailored medical services to meet the specific needs of each production.
- **Compliance with Regulations**: Adherence to all local and international health and safety regulations.

**Contact Information**:

- **Phone**: +27 066 220 8586
- **Email**: <info@setmedicsa.com>
- **Website**: <www.setmedicsa.com>

**Location**:

- **Head Office**: City of Tshwane, Gauteng, South Africa

**Client Testimonials**:

- "Set Medic South Africa provided exceptional medical support during our shoot. Their professionalism and expertise were invaluable." - Film Director
- "The team was always prepared and ready to handle any situation. Highly recommend their services!" - Production Manager
- "Set Medic South Africa was a lifesaver on our set. Their quick response and professional care ensured that our production continued smoothly without any major disruptions." - Producer
- "The team was incredibly knowledgeable and well-prepared. They handled every situation with utmost care and professionalism. We felt safe knowing they were on set." - Assistant Director
- "Their medical staff was not only skilled but also very approachable and friendly. They made everyone feel comfortable and well taken care of." - Actor
- "Set Medic South Africa provided top-notch medical support during our shoot. Their expertise and readiness were evident in every aspect of their service." - Production Coordinator
- "We were impressed by their attention to detail and commitment to safety. They went above and beyond to ensure the well-being of our cast and crew." - Line Producer

## Environment Setup

To set up the environment for this project, you will need to have the following tools installed:

- Python (version 3.9 or higher)
- pip

To run this application, you need to set up environment variables for configuration and authentication. Create a file named `env.txt` (or `.env` if your framework requires it) in your project directory with the following content:

```env
SECRET_KEY=bK9$z@1!fQw7^LrT#Xe3pVj8ZsM0uBnY
FLASK_ENV=production
PORT=5000
USERNAME=your_username_here
PASSWORD=your_password_here
DATABASE_URL=postgresql://your_db_username:your_db_password@localhost/setmedicapp.db
DATABASE_NAME=setmedicapp.db
DATABASE_USER=your_db_username
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5000
DATABASE_SSL_MODE=require
DATABASE_POOL_SIZE=5
DATABASE_MAX_OVERFLOW=10
DATABASE_TIMEOUT=30
DATABASE_QUERY_TIMEOUT=30
```

Replace `your_username_here`, `your_password_here`, `your_db_username`, and `your_db_password` with your actual credentials.  
**Important:** Never commit real secrets or passwords to version control. These environment variables are essential for secure authentication and proper application operation.

## Deployment Instructions

To deploy this application, follow these steps:

1. **Install Dependencies**  
    Ensure you have Python and pip installed. Then, install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

2. **Set Environment Variables**  
    Make sure your `env.txt` or `.env` file is configured as described above.

3. **Run Database Migrations**  
    If your application uses database migrations, apply them:

    ```sh
    flask db upgrade
    ```

4. **Start the Application**  
    Launch the application using:

    ```sh
    flask run --host=0.0.0.0 --port=5000
    ```

5. **Access the Application**  
    Open your browser and navigate to `http://localhost:5000` to access the app.

> **Note:** For production deployments, consider using a WSGI server like Gunicorn or uWSGI, and configure a reverse proxy (e.g., Nginx) for better performance and security.
