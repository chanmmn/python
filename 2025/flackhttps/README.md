# Flask HTTPS Web Application

A simple Python web application with HTTPS support featuring a textbox, button, and label.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate SSL Certificate
Before running the app with HTTPS, generate a self-signed SSL certificate:
```bash
python generate_cert.py
```

This will create `cert.pem` and `key.pem` files needed for HTTPS.

### 3. Run the Application
```bash
python app.py
```

### 4. Access the Application
Open your browser and navigate to:
```
https://localhost:5000
```

**Note:** Since this uses a self-signed certificate, your browser will show a security warning. This is normal for development. Click "Advanced" and proceed to the site.

## Features
- Secure HTTPS connection
- Text input field
- Button to display text
- Output label that shows the entered text
- Responsive design

## Files
- `app.py` - Flask application with HTTPS support
- `templates/index.html` - Frontend interface
- `generate_cert.py` - Script to generate SSL certificates
- `requirements.txt` - Python dependencies
