FROM python:3.9
ARG BUILD_MODE=dev
LABEL version=1.0 maintainer=me
RUN echo $BUILD_MODE && useradd -m myapp && pip install Flask
USER myapp
VOLUME /home/myapp/data
ONBUILD COPY extra.txt /home/myapp/extra/extra.txt
STOPSIGNAL SIGQUIT
WORKDIR /home/myapp
HEALTHCHECK --interval=10s --retries=3 CMD curl --fail http://localhost:8080 || exit 1
SHELL ["/bin/bash", "-c"]
COPY app.py /home/myapp/app.py
EXPOSE 8080
ENTRYPOINT ["python", "app.py"]
