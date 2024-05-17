git pull origin production

cd script4all

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --noinput

cd ../frontend
npm i
npm run build

sudo systemctl restart nginx
sudo systemctl restart gunicorn
