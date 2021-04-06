#!/usr/bin/env python3
import logging
from app import app

if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", filename="logs/app.log", level=logging.DEBUG)
    logging.info("Starting app")
    app.run(debug=True)
    logging.info("Ending app")