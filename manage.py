#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    settings_module = "django_newsapp.settings"  # Change this to your project's settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and available on your PYTHONPATH environment variable, and check if you've activated a virtual environment."
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
