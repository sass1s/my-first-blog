"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import time, multiprocessing

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()


# def count_num():
#     print('永岁飘零,殢无伤!')
#     print('百二秦关终属楚,三千越甲可吞吴!')
#     count = 0
#     while count < 100:
#         time.sleep(1)
#         print('清香白莲,素还真', count)
#         count += 1
#
#
# count_proc = multiprocessing.Process(target=count_num)
# count_proc.start()
# 不能加此行:count_proc.join()
# 多进程超帅啊,离成功又迈出重要的一步!
# 关注Celery+Django
