# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    if 'FLASK_ENV' in os.environ:
        environment=os.environ['FLASK_ENV']
        return f'Starting in {environment} mode...'
    return "Starting in production mode..."

if __name__ == "__main__":
    print(start())
