# TalkBox

A Django Rest Framework (DRF) app that allows users to have a real-time chat experience.
The app is built using the DRF framework and leverages Django's built-in user authentication system for managing user accounts. It uses WebSocket to handle real-time talking with users.



## QuickStart:

### - Using docker-compose:

Dependencies:

- `docker` and `docker-compose`

  ```bash
  # install
  $ git clone https://github.com/fatemeh-mgsdi/TalkBox.git
  $ cd TalkBox
  
  # configure (the defaults are fine for development)
  $ edit `.env.sample` and save as `.env`
  
  # run it
  $ docker-compose up --build
  ```

  Once it's done building and everything has booted up:

  - Access the app at: [http://localhost:8000](http://localhost:8000)

### - Running locally

- Dependencies:

  - Linux system
  - Python 3.8+
  - virtualenv
  - PostgreSQL
  - Redis

- Installation

  ```bash
  # install
  $ git clone https://github.com/fatemeh-mgsdi/TalkBox.git
  $ cd TalkBox
  $ virtualenv -p /path/to/python3 venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  
  # configure
  $ edit `.env.sample` and save as `.env`
  
  # run db migrations
  $ python manage.py migrate
  
  # backend dev server:
  $ uvicorn TalkBox.asgi:application
  ```
