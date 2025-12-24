from src.logger import get_logger
from src.CustomException import CustomException
import sys
logger = get_logger(__name__)

def divide_number(a,b):
    try:
        result = a/b
        logger.info(f"divided numbers a= {a}, b={b}")
        return result
    except Exception as e:
        logger.error("error occured")
        raise CustomException("zero error custom",sys)


if __name__ == "__main__":
    try:
        logger.info("strted program")
        divide_number(10,0)
    except CustomException as ce:
        logger.error(str(ce))