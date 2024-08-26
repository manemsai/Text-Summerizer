from text_Summerizer.config.configuration import ConfigurationManager
from text_Summerizer.conponents.data_validation import DataValiadtion
from text_Summerizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()
