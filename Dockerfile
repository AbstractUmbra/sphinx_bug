FROM python:3.9-slim

RUN apt update; apt install -y build-essential curl git unzip vim
RUN git clone -b main https://github.com/AbstractUmbra/sphinx_bug
WORKDIR sphinx_bug
RUN pip install -U -r requirements.txt
RUN sphinx-build -a -n -E -W -T --keep-going docs/ docs/_build
