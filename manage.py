#!/usr/bin/env python
import os
import sys
import pickle

def importAlgo():
    CV, NB = pickle.load(open('algo.pkl','rb'))
    return (CV,NB)
if __name__ == '__main__':
    CV,NB = importAlgo()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
