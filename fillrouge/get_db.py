import os
import re
from dotenv import load_dotenv

load_dotenv()


def db_setup():
    url = os.getenv("DATABASE_URL")
    database_setup = re.match(
        r"postgres://(?P<DB_USER>.*):(?P<DB_PASS>.*)@(?P<DB_HOST>.*):(?P<DB_PORT>.*)/(?P<DB_NAME>.*)$",
        url,
    )
    return database_setup.groupdict()
