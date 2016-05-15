#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print('永岁飘零,殢无伤!')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


