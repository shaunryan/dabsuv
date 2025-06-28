from pyspark.sql import SparkSession, DataFrame
import logging


def _get_taxis(spark: SparkSession) -> DataFrame:
    return spark.read.table("samples.nyctaxi.trips")


# Create a new Databricks Connect session. If this fails,
# check that you have configured Databricks Connect correctly.
# See https://docs.databricks.com/dev-tools/databricks-connect.html.
def _get_spark() -> SparkSession:
    try:
        from databricks.connect import DatabricksSession

        return DatabricksSession.builder.getOrCreate()
    except ImportError:
        return SparkSession.builder.getOrCreate()


def get_taxis():
    _get_taxis(_get_spark()).show(5)

def get_taxi_count():
    logging.info(_get_taxis(_get_spark()).count())


# if __name__ == "__main__":
    # get_taxi_count()
