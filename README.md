Vendor Management System
Overview
The Vendor Management System is a Django-based application designed to help businesses manage their vendors, track purchase orders, and evaluate vendor performance metrics.

Installation
To install and run the project locally, follow these steps:
1.Clone the repository:
git clone https://github.com/ToshiJain15/djano_project.git
2.Navigate to the project directory:
cd vendor
3.Install dependencies:
pip install -r requirements.txt
4.Configure the database settings:
Open vendor_management/settings.py.
Update the database settings according to your environment.
py manage.py migrate
Usage
To run the project locally, follow these steps:

1.Start the Django development server:
py manage.py runserver
2.Open your web browser and navigate to http://localhost:8000.
3.You can now interact with the API endpoints and access the admin interface.
