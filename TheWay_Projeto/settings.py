INSTALLED_APPS = [
    'rest_framework',

    'clientes',
    'produtos',
    'vendas',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TheWayProjeto',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'core.handlers.custom_exception_handler'
}