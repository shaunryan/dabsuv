# Typings for Pylance in Visual Studio Code
# see https://github.com/microsoft/pyright/blob/main/docs/builtins.md
from databricks.sdk.runtime import *

from databricks.sdk.runtime import *
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import udf as U
from pyspark.sql.context import SQLContext

udf = U
spark: SparkSession
sc = spark.sparkContext
sqlContext: SQLContext
sql = sqlContext.sql
table = sqlContext.table
getArgument = dbutils.widgets.getArgument

def displayHTML(html): ...

def display(input=None, *args, **kwargs): ...

