# Set Python version for the image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /code

# Copy he dependencies file to the working directory
COPY ./requirements.txt /code/requirements.txt

# Run the requirements.txt file inside the container to install dependencies
RUN pip install -r /code/requirements.txt

# Copy the contents of the local app directory to the working directory
COPY . /app /code/app

# Set the environment variables
ENV WANDB_API_KEY=""
ENV WANDB_ORG=""
ENV WANDB_PROJECT=""
ENV WANDB_MODEL_NAME=""
ENV WANDB_MODEL_VERSION=""

# Choose port to expose
EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "0000]