# init

```sh
cp -r ./__init/* ./
```

# create project and app
```sh
docker-compose run app1 django-admin startproject myapp .
sudo chown -R $USER:$USER .
```

# setting
```python
#sittings.py

ALLOWED_HOSTS = [*]

INSTALLED_APPS = [
    ...
    'myapp',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db1',
        'PORT': 5432,
    }
}
```

#