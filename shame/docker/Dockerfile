FROM amazoncorretto:21-al2023-jdk

RUN dnf update && \
  dnf install python3.11 -y && \
  dnf install python3.11-pip -y && \
  alternatives  --install /usr/bin/python python /usr/bin/python3.11 0 