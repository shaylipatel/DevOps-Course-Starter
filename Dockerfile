FROM python:3.12-rc-alpine as base
RUN apk update
RUN apk add curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"
WORKDIR /todo_app
COPY pyproject.toml poetry.lock ./
RUN poetry install 
EXPOSE 5000
COPY todo_app ./todo_app
FROM base as production
ENTRYPOINT ["poetry" , "run"]
CMD ["gunicorn",  "--bind", "0.0.0.0:5000", "todo_app.app:create_app()"]
FROM base as development
ENTRYPOINT [ "poetry" , "run" ]
CMD [ "flask","run", "--host=0.0.0.0" ]
