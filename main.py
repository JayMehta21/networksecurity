from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try: 
        # Instantiate training pipeline configuration
        training_pipeline_config = TrainingPipelineConfig()

        # Instantiate data ingestion configuration
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)

        # Create data ingestion object
        data_ingestion = DataIngestion(data_ingestion_config)

        # Log the initiation of data ingestion
        logging.info("Initiating the data ingestion process.")

        # Execute the data ingestion process
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        # Log and print the data ingestion artifact
        logging.info(f"Data Ingestion Completed. Artifact: {data_ingestion_artifact}")
        print(data_ingestion_artifact)

    except Exception as e:
        # Handle exceptions by wrapping them in NetworkSecurityException
        logging.error(f"An error occurred: {e}")
        raise NetworkSecurityException(e, sys)
