import newrelic.agent
import sys
import os
from django.core.wsgi import get_wsgi_application

newrelic.agent.initialize('newrelic.ini') # newrelic.ini 파일의 절대경로
sys.path.append('/home/honsuri/myvenv/lib/python3.8/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

# newrelic
application = newrelic.agent.wsgi_application()(application) 
