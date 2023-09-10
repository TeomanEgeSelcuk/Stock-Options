# Use Python 3.11 as the base image
FROM python:3.11

# Copy the requirements.txt file to the container
COPY requirements.txt /app/requirements.txt

# Update pip
RUN pip install --upgrade pip

# Install the dependencies from the requirements.txt file
RUN pip install -r /app/requirements.txt

# Install PostgreSQL client tools
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Copy contents of the notebook directory to /app in the container
COPY notebooks /app

# Set working directory
WORKDIR /app

# Run pip install -e . to install pyproject.toml
RUN pip install -e .

# Expose Jupyter Notebook port
EXPOSE 8888

# Copy the custom Jupyter configuration file
COPY jupyter_notebook_config.py /root/.jupyter/

# Run Jupyter Notebook on container startup
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
