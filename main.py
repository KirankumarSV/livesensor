from sensor.exception import SensorException
from sensor.logger import logging
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.pipeline.training_pipeline import TrainPipeline


#from sensor.utils import dump_csv_file_to_mongodb_collection

# def test(): # checking if logging is working or not
#     try:
#         int('kiran')
#     except Exception as e:
#         logging.info(f"The error is :[{e}]")
#         raise SensorException(e)


# if __name__ == "__main__":  # checking if I can upload the data on the mongodb
#     try:
#         logging.info("Added the data to the mongodb database")
#         file_path = r"C:\Users\Lenovo\Downloads\sensorlive\aps_failure_training_set1.csv"
#         database_name = "mlproject"
#         collection_name = "sensor"
#         dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)
#     except Exception as e:
#         logging.info(f'The error is : [{e}]')
#         print(e)

if __name__ == "__main__":  #Testing if artifacts folder is created successfully. Yes it did!
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()