# Example Dockerfile for AWS Lambda with Python
FROM public.ecr.aws/lambda/python:3.8

# Copy function code and any required scripts
COPY app.py ./
COPY requirements.txt ./

# Install OS packages for SAP NWRFC SDK if necessary
RUN yum install gcc -y
RUN yum install gcc-c++ -y

#Install NWRFC SDK
RUN mkdir -p /usr/sap
RUN mkdir -p /usr/sap/log
RUN mkdir -p /usr/sap/tmp
RUN mkdir -p /usr/sap/prog
COPY nwrfc750P_8-70002752.zip /usr/sap/tmp # download this pacakg from SAP Marketplace
RUN unzip /usr/sap/tmp/nwrfc750P_8-70002752.zip -d /usr/sap
RUN chmod -R 755 /usr/sap
RUN rm -f /usr/sap/tmp/nwrfc750P_8-70002752.zip

#Set NWRFC SDK Environment
COPY nwrfcsdk.conf /etc/ld.so.conf.d/nwrfcsdk.conf
ENV SAPNWRFC_HOME=/usr/sap/nwrfcsdk
ENV LD_LIBRARY_PATH=/usr/lib:/usr/lib64:/usr/sap/nwrfcsdk/lib

# Install the Python libraries at /var/task, which is the directory where the Lambda handler is expected to be
RUN pip install --no-cache-dir -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler" ]
