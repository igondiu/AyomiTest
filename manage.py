#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging
import config.config as cfg
from setup.setup import logger_setup

logger = logging.getLogger(__name__)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AyomiTest.settings')

    try:
        import django.core.management.commands.runserver as runserver
        runserver.DEFAULT_PORT = cfg.DJANGO_PORT
        logger.info("PORT set to 5000")
        from django.core.management import execute_from_command_line
    except ImportError:
        logger.exception("Django was not found, install django and retry")
        sys.exit(1)

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    logger_setup(cfg)
    main()
