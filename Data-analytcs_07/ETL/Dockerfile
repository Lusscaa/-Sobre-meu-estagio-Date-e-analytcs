FROM alpine/git

WORKDIR /app

RUN git clone https://github.com/Lusscaa/Date-e-analytcs

WORKDIR /app/seu_repositorio

RUN git lfs install
RUN git lfs track "*.csv"

CMD ["/bin/sh"]
