import sys
import os
import django

sys.path.append('../../../platform_manage')
sys.path.append('../../../spiders')
os.environ['DJANGO_SETTINGS_MODULE'] = 'platform_manage.settings'
django.setup()