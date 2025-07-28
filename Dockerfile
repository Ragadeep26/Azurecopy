FROM python:3.7-slim

COPY ./*.py /app/
COPY ./src/ /app/src/
COPY ./common/ /app/common/
COPY ./*.txt /app/
COPY ./*.toml /app/
WORKDIR /app
RUN pip install -r requirements.txt

# default streamlit port is 8501 but config.toml sets port to 80
EXPOSE 80

RUN mkdir ~/.streamlit
RUN cp config.toml ~/.streamlit/config.toml
RUN cp credentials.toml ~/.streamlit/credentials.toml

WORKDIR /app
#ENTRYPOINT ["streamlit", "run", "--server.port", "80"]
#ENTRYPOINT ["streamlit", "run", "--server.port", "80", "--server.enableXsrfProtection", "false"]
#ENTRYPOINT ["streamlit", "run", "--server.port", "80", "--server.enableXsrfProtection", "true", "--server.cookieSecret", "116b64dbf5041452f031ca55bbc98a23ac6fbd8a7ed905c75e4e7cf39fd9dd7c"]
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit_app.py"]