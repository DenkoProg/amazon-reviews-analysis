from pyspark.sql.types import (
    ArrayType,
    BooleanType,
    DoubleType,
    LongType,
    MapType,
    StringType,
    StructField,
    StructType,
)


REVIEWS_SCHEMA = StructType(
    [
        StructField("asin", StringType(), True),
        StructField("helpful_vote", LongType(), True),
        StructField(
            "images",
            ArrayType(
                StructType(
                    [
                        StructField("attachment_type", StringType(), True),
                        StructField("large_image_url", StringType(), True),
                        StructField("medium_image_url", StringType(), True),
                        StructField("small_image_url", StringType(), True),
                    ]
                )
            ),
            True,
        ),
        StructField("parent_asin", StringType(), True),
        StructField("rating", DoubleType(), True),
        StructField("text", StringType(), True),
        StructField("timestamp", LongType(), True),
        StructField("title", StringType(), True),
        StructField("user_id", StringType(), True),
        StructField("verified_purchase", BooleanType(), True),
    ]
)

METADATA_SCHEMA = StructType(
    [
        StructField(
            "author",
            StructType(
                [
                    StructField("about", ArrayType(StringType()), True),
                    StructField("avatar", StringType(), True),
                    StructField("name", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("average_rating", DoubleType(), True),
        StructField("bought_together", StringType(), True),
        StructField("categories", ArrayType(StringType()), True),
        StructField("description", ArrayType(StringType()), True),
        # `details` varies a lot by category → make it a flexible map
        # (keys/values as strings; you can promote selected keys later if needed)
        StructField("details", MapType(StringType(), StringType(), True), True),
        StructField("features", ArrayType(StringType()), True),
        StructField(
            "images",
            ArrayType(
                StructType(
                    [
                        StructField("hi_res", StringType(), True),
                        StructField("large", StringType(), True),
                        StructField("thumb", StringType(), True),
                        StructField("variant", StringType(), True),
                    ]
                )
            ),
            True,
        ),
        StructField("main_category", StringType(), True),
        StructField("parent_asin", StringType(), True),
        StructField("price", StringType(), True),
        StructField("rating_number", LongType(), True),
        StructField("store", StringType(), True),
        StructField("subtitle", StringType(), True),
        StructField("title", StringType(), True),
        StructField(
            "videos",
            ArrayType(
                StructType(
                    [
                        StructField("title", StringType(), True),
                        StructField("url", StringType(), True),
                        StructField("user_id", StringType(), True),
                    ]
                )
            ),
            True,
        ),
    ]
)
