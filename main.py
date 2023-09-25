from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Stage: {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Stage: {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"Stage: {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} started")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"Stage: {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"Stage: {STAGE_NAME} started")
    model_trainer = ModelEvaluationTrainingPipeline()
    model_trainer.main()
    logger.info(f"Stage: {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e
