FROM python:3.9 

# Install dependencies
RUN pip install networkx requests
RUN mkdir /app

# Copy files
COPY . /app

# Run cmd
CMD ["python3", "app/live_data_generator.py"]