FROM python:3.9-slim-buster

ENV USER appuser
RUN useradd --create-home --shell /bin/bash ${USER}
USER ${USER}
WORKDIR /home/${USER}

EXPOSE 5000

RUN python -m pip install -U pip

COPY requirements.txt .
COPY requirements_dev.txt .
RUN pip install -r requirements_dev.txt

# //// other packages ////////////////////
# RUN pip install Flask-WTF
# RUN pip install Flask-Bcrypt
# RUN pip install Flask-Login
# RUN pip install flask-mongoengine
# ////////////////////////////////////////

COPY . .

CMD ["python", "-m", "flask", "run"]