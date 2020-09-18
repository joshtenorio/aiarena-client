#########################################################
#                                                       #
# DEFAULT CONFIG                                        #
#                                                       #
# !!!! DO NOT UPDATE THIS FILE WITH LOCAL SETTINGS !!!! #
# Create a config.py file to override config values     #
#                                                       #
#########################################################
import logging
import os
import platform

# GENERAL
from ..match.matches import FileMatchSource

ARENA_CLIENT_ID = "aiarenaclient_000"  # ID of arenaclient. Used for AiArena
API_TOKEN = "12345"  # API Token to retrieve matches and submit results. Used for AiArena
ROUNDS_PER_RUN = 5  # Set to -1 to ignore this
BASE_WEBSITE_URL = ""
SHUT_DOWN_AFTER_RUN = True  # Write a .shutdown file after running games. Used for AiArena
USE_PID_CHECK = False
RUN_REPLAY_CHECK = False  # Validate replays
DEBUG_MODE = True  # Enables debug mode for more logging
PYTHON = "python3"  # Which python version to use
RUN_LOCAL = False  # Run on AiArena or locally
CLEANUP_BETWEEN_ROUNDS = True  # Clean up files between rounds
SYSTEM = platform.system()  # What OS are we on?
SC2_PROXY = {"HOST": "127.0.0.1", "PORT": 8765}  # On which host and port to run the proxy between SC2 and bots
SECURE_MODE = False  # Used for AiArena

# LOGGING
LOGGING_HANDLER = logging.FileHandler("../supervisor.log", "a+")
LOGGING_LEVEL = 10

# PATHS AND FILES
TEMP_PATH = "/tmp/aiarena/"
LOCAL_PATH = os.path.dirname(__file__)
WORKING_DIRECTORY = LOCAL_PATH  # same for now
LOG_FILE = os.path.join(WORKING_DIRECTORY, "client.log")
REPLAYS_DIRECTORY = os.path.join(WORKING_DIRECTORY, "replays")
BOTS_DIRECTORY = os.path.join(WORKING_DIRECTORY, "bots")

MATCH_SOURCE_CONFIG = FileMatchSource.FileMatchSourceConfig(
    matches_file=os.path.join(WORKING_DIRECTORY, "matches"),
    results_file=os.path.join(WORKING_DIRECTORY, "results")
)

# STARCRAFT
SC2_HOME = "/home/aiarena/StarCraftII/"
SC2_BINARY = os.path.join(SC2_HOME, "Versions/Base75689/SC2_x64")
MAX_GAME_TIME = 60486
MAX_FRAME_TIME = 1000
STRIKES = 10
REALTIME = False
VISUALIZE = False

# MATCHES
DISABLE_DEBUG = True
VALIDATE_RACE = False
# Override values with environment specific config
try:
    from config import *
except ImportError as e:
    if e.name == "config":
        pass
    else:
        raise
