# KRO BACKEND

A sample backend for the kro test made with FastAPI

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.8 or higher
- pip (Python package installer)
- PostgreSQL (Neon PostgreSQL if you're using Neon for cloud-based database)

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. **Clone the repository**

   ```sh
   git clone https://github.com/isaaccodekill/kro-backend.git
   ```

2. Navigate to the project directory

   ```sh
   cd kro-backend
   ```

3. Create a virtual environment

   ```sh
   python -m venv venv
   source venv/bin/activate # for linux or mac
   source venv\Scripts\activate # for windows  
   ```   

4. Install the required packages

   ```sh
   pip install -r requirements.txt
   ```
   
5. Create a `.env` file in the root directory of the project and add the following environment variables:

   ```sh
    DATABASE_URL=postgresql://username:password@localhost:5432/kro
    ```

6. Run the fastapi server

   ```sh
   uvicorn app.main:app --reload
   ```   

7. Navigate to `http://127.0.0.1:8000/docs` in your browser to view the API documentation