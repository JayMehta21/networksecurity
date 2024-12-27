import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        # If error_details is None or doesn't have traceback, we handle it gracefully
        if error_details and hasattr(error_details, 'exc_info'):
            _, _, exc_tb = error_details.exc_info()
            if exc_tb:
                self.lineno = exc_tb.tb_lineno
                self.filename = exc_tb.tb_frame.f_code.co_filename
            else:
                # If no traceback, use default info
                self.lineno = 'N/A'
                self.filename = 'N/A'
        else:
            self.lineno = 'N/A'
            self.filename = 'N/A'

    def __str__(self):
        return "error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
            self.filename, self.lineno, str(self.error_message))


if __name__ == "__main__":
    try:
        logger.logging.info("enter the try block ")
        a = 1 / 0  # This will raise a ZeroDivisionError
        print("this will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
