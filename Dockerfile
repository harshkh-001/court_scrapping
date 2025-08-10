FROM python:3.11-slim

# Install Chromium and required dependencies (faster, cleaner)
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    fonts-liberation \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Set Chromium binary path
ENV CHROME_BIN=/usr/bin/chromium

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Run Gunicorn with longer timeout
CMD ["gunicorn", "court.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "90"]
