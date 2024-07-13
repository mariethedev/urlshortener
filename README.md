UrlShortener

A simple URL shortener application built with Django. This application allows users to input a long URL and receive a shortened version that redirects to the original URL.


![URL-Shortener 1 pic](https://github.com/user-attachments/assets/12d7fd01-c38d-410a-8f38-4a3ce3b0c6ff)# 
![URL-Shortener 2](https://github.com/user-attachments/assets/a3ce744c-a07d-4486-849e-f43e91948748)



## Table of Contents

- [UrlShortener](#urlshortener)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Project File Structure](#project-file-structure)

## Features

- Shorten long URLs
- Redirect shortened URLs to the original URLs
- Copy shortened URL to clipboard with tooltip feedback
- URL validation

## Technologies Used

- Django
- HTML, CSS, JavaScript, jQuery

## Setup and Installation

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3 and above
- Django

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mariethedev/urlshortener.git
   cd urlshortener

2. **Create a virtual environment:**
   
   ```python
    python -m venv urlenv
    source urlenv/bin/activate  # On Windows use `urlenv\Scripts\activate`

3. **Install the required packages:**
   
   ```bash
   pip install -r requirements.txt

4. **Apply migrations:**
   
   ```bash
   python manage.py migrate

5. **Run the Django development server:**
   ```bash
   python manage.py runserver


## Usage

1. Open your web browser and navigate to http://localhost:8000.
2. Enter a long URL in the input field and click the "Shorten" button.
3. A shortened URL will be displayed. Click the copy button to copy the shortened URL to your clipboard.
4. Paste the shortened URL into your browser to be redirected to the original URL.
   
## Project File Structure
- `shortener/`: Contains the Django app for URL shortening.
  - `models.py`: Defines the URL model.
  - `views.py`: Contains the views for creating and redirecting URLs.
  - `urls.py`: Maps URLs to the views.


- `templates/`: Contains the HTML templates for the Django app.
  
- `static/`: Contains static files (CSS, JavaScript, images) for the Django app.




