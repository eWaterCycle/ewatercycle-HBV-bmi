FROM windows:python
MAINTAINER David Haasnoot daafips@gmail.com

# Install grpc4bmi
RUN pip install git+https://github.com/eWaterCycle/grpc4bmi.git#egg=grpc4bmi

# Install here your BMI model:
RUN git clone https://github.com/Daafip/HBV-bmi-numpy

# Run bmi server
ENTRYPOINT ["run-bmi-server", "--name", "HBV.HBV_bmi.HBV"]

# Expose the magic grpc4bmi port
EXPOSE 55555