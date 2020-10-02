# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7.4

EXPOSE 8000

ENV VAR1=10


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

# Creates /app in container if it does not already exist
# Ports code into /app
WORKDIR /app
ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder: 'Django2'. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "127.0.0.1:8000", "django_tutorial.wsgi"]
