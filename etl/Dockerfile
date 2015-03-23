FROM phusion/baseimage:0.9.16

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Install required packages
RUN apt-get update
RUN apt-get install -y python-setuptools

# Install pip
RUN easy_install pip

# Add our python app code to the image
RUN mkdir -p /etl
ADD . /etl
WORKDIR /etl

# Install Python modules
RUN cd /etl; pip install -r requirements.txt

# Set the default command to execute
CMD ["python", "etl.py"]

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
