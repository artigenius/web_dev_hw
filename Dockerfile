FROM python:3.12.6-slim

#копируем все файлы проекта в рабочую директорию
COPY . /app

#устанавливаем рабочую директорию
WORKDIR /app 

#устанавливаем зависимости
RUN pip install -r requirements.txt

#пробрасываем порты
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  
