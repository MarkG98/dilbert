FROM python:3.8
WORKDIR /code
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
EXPOSE 8080
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY /src .
CMD [ "python", "./main.py" ]