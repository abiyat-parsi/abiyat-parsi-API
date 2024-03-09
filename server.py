import os
from gunicorn.app.base import BaseApplication
from django.core.wsgi import get_wsgi_application


class DjangoGunicornApp(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parsi.settings')
    django_app = get_wsgi_application()

    options = {
        'bind': '127.0.0.1:80',
        'workers': 4,
    }
    DjangoGunicornApp(django_app, options).run()
