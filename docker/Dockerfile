FROM python:3.9

WORKDIR /app/

# Copy the requirements file into the container
COPY docker/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the code base 
COPY . /app/

# Run the app on port 8123 and reload it on changes
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8123", "--reload", "--reload-dir", "src"]
