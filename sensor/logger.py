import logging
import os
from datetime import datetime


log_file = f"{datetime.now().strftime('%m_%d_%Y-%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(logs_path, exist_ok=True)
log_file_path = os.path.join(logs_path, log_file)


logging.basicConfig(filename=log_file_path,
                    format= '[%(asctime)s] | %(name)s | %(levelname)s | %(lineno)d | %(message)s',
                    level=logging.INFO,
                    )