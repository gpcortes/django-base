FROM python:3.8-slim

ENV LANG pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8
ENV LANGUAGE pt_BR.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1

RUN adduser -u 1000 --disabled-password --gecos "" appuser && chown -R appuser /home/appuser

RUN apt-get update && apt-get install git -y

RUN pip install pipenv

RUN apt install -y locales libc-bin locales-all
RUN sed -i '/pt_BR.UTF-8/s/^#//g' /etc/locale.gen \
    && locale-gen en_US en_US.UTF-8 pt_BR pt_BR.UTF-8 \
    && dpkg-reconfigure --frontend noninteractive locales \
    && update-locale LANG=pt_BR.UTF-8 LANGUAGE=pt_BR.UTF-8 LC_ALL=pt_BR.UTF-8

USER appuser

WORKDIR /home/appuser/app

ENV PIPENV_VENV_IN_PROJECT=True
ENV PIPENV_SITE_PACKAGES=True
ENV PATH="/home/appuser/app/.venv/bin:$PATH"

ADD Pipfile.lock ./
ADD Pipfile ./

RUN pipenv install --system

CMD [ "gunicorn", "--access-logfile", "-", "--workers", "3", "--bind", "0.0.0.0:8000", "core" ]