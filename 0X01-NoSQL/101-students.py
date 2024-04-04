#!/usr/bin/env python3
"""
Task 14
"""


def top_students(mongo_collection):
    """
    Top students (by score)
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])