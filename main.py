from sensor.exception import SensorException
from sensor.logger import logging

def test():
    try:
        int('kiran')
    except Exception as e:
        logging.info(f"The error is :[{e}]")
        raise SensorException(e)


if __name__ == "__main__":
    try:
        test()
    except Exception as e:
        print(e)