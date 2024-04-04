#!/usr/bin/env python3
"""
Task 10
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update/change school topic
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )