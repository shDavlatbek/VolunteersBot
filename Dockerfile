# Pull official base image
FROM python:3.11.9

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# Install pip and project dependencies
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt


# Set the appropriate directories and switch to the app user
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
WORKDIR $APP_HOME

# Copy project files and entrypoint script
COPY . $APP_HOME
COPY ./entrypoint.sh $APP_HOME

# Ensure entrypoint script is executable
RUN chmod +x /home/app/web/entrypoint.sh

# Run entrypoint script
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
