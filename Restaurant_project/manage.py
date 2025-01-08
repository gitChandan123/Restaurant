#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurant_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

import os


if __name__ == '__main__':
    main()
    port = int(os.getenv("PORT", 8000))  # Use the Render-assigned port, default to 8000 for local testing
    execute_from_command_line(["manage.py", "runserver", f"0.0.0.0:{port}"])


"""Start Command
Render runs this command to start your app with each deploy - python manage.py runserver

what wil be the Environment Variables for my project?
Set environment-specific config and secrets (such as API keys), then read those values from your code.

"""