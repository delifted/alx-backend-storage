#!/usr/bin/env python3
"""
Task 8
"""
import pymongo


def list_all(mongo_collection):
    """
    List all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())