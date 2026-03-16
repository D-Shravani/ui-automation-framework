import os

BASE_URL = os.getenv("BASE_URL", "https://example.com")
BROWSER = os.getenv("BROWSER", "chrome")
GRID_URL = os.getenv("GRID_URL", None)
HEADLESS = os.getenv("HEADLESS", "false")
