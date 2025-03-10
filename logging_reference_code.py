import logging

# Basic logging to console with filename and line number
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)

def example_function():
    logging.info("Function started")
    try:
        result = 10 / 2
        logging.debug(f"Result: {result}") #debug
    except Exception as e:
        logging.error(f"Error: {e}", exc_info=True) #error with traceback
    logging.info("Function ended")

example_function()
logging.warning("This is a warning message.")