FROM python:3.11

# Copy the requirements.txt file to the container
COPY requirements.txt /app/requirements.txt

# Install the dependencies from the requirements.txt file
RUN pip install -r /app/requirements.txt

# Copy contents of the notebook directory to /app in the container
COPY notebook /app

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
