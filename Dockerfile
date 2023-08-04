# For more information, please refer to 
# https://aka.ms/vscode-docker-python/
# use miniconda to handle python environment
FROM python:3.11

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# set working directory
WORKDIR /app
# switch shell to bash 
# SHELL ["/bin/bash", "-c"]

COPY ./requirements.txt .
# Install pip requirements
RUN pip install -r requirements.txt

COPY ./ECO .

# Creates a non-root user with an explicit UID and adds permission to 
# access the /app folder
# For more info, please refer to 
# https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Set environment variable
# host:port the django server going to listen
ENV HOST=0.0.0.0
ENV PORT=8000

EXPOSE 8000

# During debugging, this entry point will be overridden. For more 
# information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["sh","-c", "python manage.py runserver ${HOST}:${PORT}"]



