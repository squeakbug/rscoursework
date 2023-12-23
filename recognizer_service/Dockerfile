FROM swipl

COPY . /app
EXPOSE 8080

WORKDIR /app/src
ENTRYPOINT ["swipl"]
CMD ["main.pro",  "--user=daemon", "--fork=false", "--port=8080"]
