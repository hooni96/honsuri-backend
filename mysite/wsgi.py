"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
# newrelic
import newrelic.agent
newrelic.agent.initialize('newrelic.ini') # 위에서 생성한 newrelic.ini 파일의 절대경로
import sys
sys.path.append('/home/honsuri/myvenv/lib/python3.8/site-packages')
# -----------------------------------------------

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

# newrelic
application = newrelic.agent.wsgi_application()(application) 
