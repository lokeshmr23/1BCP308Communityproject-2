FROM python:3.13-slim

WORKDIR /app

# Copy dependency files and project tree
COPY . /app/

RUN chmod +x render-build.sh server.py collect.py
RUN ./render-build.sh

EXPOSE 8080
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/healthz')" || exit 1

CMD ["python3", "server.py"]
