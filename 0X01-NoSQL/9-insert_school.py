#!/usr/bin/env python3
"""
Task 9
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert documents into school
    """
    return mongo_collection.insert_one(kwargs).inserted_id