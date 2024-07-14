UrlShortener

A simple URL shortener application built with Django. This application allows users to input a long URL and receive a shortened version that redirects to the original URL.

The URLShortener Web App has successfully been hosted and can be accessed at https://urlshortener-nhl6.onrender.com 

##First Look
![image](https://github.com/user-attachments/assets/31ea1f7b-c067-4ab2-9fb7-7229c75f0cc5)
![image](https://github.com/user-attachments/assets/11fcb2ce-1a77-46a2-8f0c-0424a799b166)





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




