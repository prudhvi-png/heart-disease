import logging
from datetime import datetime
import os,sys
from exception import CustomException

try:

    file_name_format = f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log"

    logs_path = os.path.join("Logs",file_name_format)

    os.makedirs(os.path.dirname(logs_path),exist_ok=True)

    logging.basicConfig(
        filename=logs_path,
        level=logging.INFO,
        format="%(asctime)s -- %(levelname)s -- %(message)s"
    )
except Exception as e:
    raise CustomException(e,sys)


if __name__ == "__main__":
    logging.info("You logger is working !!!!")