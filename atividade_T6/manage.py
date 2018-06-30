#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

#https://www.extra.com.br/Informatica/Notebook/notebook-samsung-core-i5-7200u-8gb-1tb-tela-15-6-windows-10-expert-x22-np300e5m-kd3br-11463383.html?recsource=busca-int&rectype=busca-57