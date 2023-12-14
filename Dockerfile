# Gunakan base image Python yang sudah menyertakan pip
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Salin file-file yang diperlukan ke dalam kontainer
COPY app.py .
COPY requirements.txt .

# Install dependensi aplikasi
RUN pip install --no-cache-dir -r requirements.txt

# Expose port yang digunakan oleh aplikasi Flask
EXPOSE 5000

# Perintah untuk menjalankan aplikasi saat kontainer dijalankan
CMD ["python", "app.py"]
