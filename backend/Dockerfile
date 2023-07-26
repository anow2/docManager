FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml environment.yml
RUN conda env create -f environment.yml

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
