from pathlib import Path

from pyspark.sql import SparkSession

from amazon_reviews_analysis.schemas import METADATA_SCHEMA, REVIEWS_SCHEMA


def build_spark(app_name: str = "AmazonReviews") -> SparkSession:
    """
    Create a SparkSession configured for stable JSON ingestion.
    Case sensitivity ON prevents collisions like 'Color' vs 'color'.
    """
    return SparkSession.builder.appName(app_name)\
        .config("spark.sql.caseSensitive", "true")\
        .config("spark.driver.memory", "4g")\
        .config("spark.executor.memory", "4g").getOrCreate()


def load_reviews(spark: SparkSession, path: str | Path):
    """
    Read reviews JSONL using the custom REVIEWS_SCHEMA.
    """
    return (
        spark.read.schema(REVIEWS_SCHEMA)
        .option("mode", "PERMISSIVE")
        .option("columnNameOfCorruptRecord", "_corrupt_record")
        .json(str(path))
    )


def load_metadata(spark: SparkSession, path: str | Path):
    """
    Read product metadata JSONL using the custom METADATA_SCHEMA.
    """
    return (
        spark.read.schema(METADATA_SCHEMA)
        .option("mode", "PERMISSIVE")
        .option("columnNameOfCorruptRecord", "_corrupt_record")
        .json(str(path))
    )


if __name__ == "__main__":
    spark = build_spark("AmazonReviewsIO")
    reviews_path = "data/raw/meta_categories/meta_Musical_Instruments.jsonl"
    metadata_path = "data/raw/review_categories/Musical_Instruments.jsonl"

    df_reviews = load_reviews(spark, reviews_path)
    df_meta = load_metadata(spark, metadata_path)

    print("=== Reviews Schema ===")
    df_reviews.printSchema()
    print("=== Metadata Schema ===")
    df_meta.printSchema()

    spark.stop()
