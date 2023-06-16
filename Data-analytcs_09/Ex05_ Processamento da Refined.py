import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1686923788833 = glueContext.create_dynamic_frame.from_catalog(
    database="filmes db",
    table_name="atores",
    transformation_ctx="AWSGlueDataCatalog_node1686923788833",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1686923964200 = glueContext.create_dynamic_frame.from_catalog(
    database="filmes db",
    table_name="filmes",
    transformation_ctx="AWSGlueDataCatalog_node1686923964200",
)

# Script generated for node Amazon S3
AmazonS3_node1686923801282 = glueContext.write_dynamic_frame.from_options(
    frame=AWSGlueDataCatalog_node1686923788833,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://lucasricardo2/Refined/atores/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1686923801282",
)

# Script generated for node Amazon S3
AmazonS3_node1686923972394 = glueContext.write_dynamic_frame.from_options(
    frame=AWSGlueDataCatalog_node1686923964200,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://lucasricardo2/Refined/filmes/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1686923972394",
)

job.commit()
