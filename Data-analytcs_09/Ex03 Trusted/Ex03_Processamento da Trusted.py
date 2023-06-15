import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = spark.read.option("multiline", "true").json("s3://lucasricardo2/Raw/Local/Json/JSON/2023/05/29/")

df.write.parquet("s3://lucasricardo2/trusted/neosoro/")


job.commit()


"""========================================================================================================="""

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

bob = spark.read.csv("s3://lucasricardo2/Raw/Local/CSV/Movies/2023/05/26/movies.csv", sep="|")

bob.write.parquet("s3://lucasricardo2/trusted/neosorocopy/")

job.commit()