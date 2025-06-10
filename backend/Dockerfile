# 1. Python 기반 슬림 이미지 사용
FROM python:3.12

# 2. 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. 작업 디렉토리 생성
WORKDIR /app

# 4. 시스템 패키지 및 MySQL 관련 의존성 설치
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# 5. 파이썬 패키지 설치
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 6. 프로젝트 소스 복사
COPY . .

# 7. 정적 파일 한 곳에 모아서 동작
RUN python manage.py collectstatic --noinput

# 8. Django 앱을 Gunicorn으로 실행 
CMD ["gunicorn", "backend.wsgi:application", "gunicorn.conf.py"]
