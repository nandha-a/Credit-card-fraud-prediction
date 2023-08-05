# Import logging module
import logging

# Create a logger object
logger = logging.getLogger("my_logger")

# Set the level of the logger
logger.setLevel(logging.DEBUG)

# Create a file handler object
file_handler = logging.FileHandler("my_log.txt")

# Set the level of the file handler
file_handler.setLevel(logging.INFO)

# Create a stream handler object
stream_handler = logging.StreamHandler()

# Set the level of the stream handler
stream_handler.setLevel(logging.DEBUG)

# Create a formatter object
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Add the formatter to the handlers
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

