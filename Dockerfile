 
FROM python:3.8.16-slim
FROM gurobi/python:latest

# what code files to add
# COPY <from directory> <container directory> 
# COPY ./src /opt/app/ # if not working add /opt/
COPY . /app
# COPY requirements.txt /app/requirements.txt 
WORKDIR /app/

# Default installs (Linux based)
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    gcc \
    make

# create venv and load dep
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/python -m pip install pip --upgrade
RUN /opt/venv/bin/python -m pip install -r /app/requirements.txt

# remove unneeded system files
RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Make entrypoint file executable
RUN chmod +x src/entrypoint.sh

# or format:
# RUN <command> && \
#     <command>

# Run the app
CMD ["./src/entrypoint.sh"]