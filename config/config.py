import os
from distutils.util import strtobool
import platform

# ===================================DIRECTORIES==========================================

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_DIR = os.path.join(ROOT_DIR, "tests")
LIBS_DIR = os.path.join(ROOT_DIR, "libs")
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

# ================================== DJANGO ==============================================
DJANGO_PORT = (
    os.getenv("DJANGO_WINDOWS_PORT", 5000)
    if platform.system() == "Windows"
    else os.getenv("DJANGO_DEFAULT_PORT", 5000)
)
DJANGO_SSL_PORT = os.getenv("DJANGO_SSL_PORT", 5000)
DJANGO_SSL_PORT_WIN = (
    os.getenv("DJANGO_WINDOW_SSL_PORT")
    if platform.system() == "Windows"
    else DJANGO_SSL_PORT
)
DJANGO_DEBUG_MODE = strtobool(os.getenv("DJANGO_DEBUG_MODE", "true"))
DJANGO_HOST = os.getenv("DJANGO_HOST", "0.0.0.0")
DJANGO_SSL_CERT = os.getenv("DJANGO_CERT", None)
DJANGO_PRIVATE_KEY = os.getenv("DJANGO_PRIVATE_KEY", None)

# ===================================PROGRAM OPTIONS==========================================
LOG_VERBOSITY = strtobool(os.getenv("LOG_VERBOSITY", "true"))
