cd mysite_com
rm -f mysite.sqlite3
cp mysite-bak.sqlite3 mysite.sqlite3
python manage.py runserver &
sleep 1
echo "$!" > django.pid
curl -I http://localhost:8000/polls/ && echo "server started."
