#!/bin/bash
set -e

cd student-guidance-platform--main/student_guidance

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed!"