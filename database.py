import pymongo
from pymongo import MongoClient

uri = "mongodb+srv://rajaramanishwar:VaGhUt2Ej7niI1Rb@stackoverflowers.4ri5c.mongodb.net/"
conn = MongoClient(uri)

def retrieve_user_data(conn, user_id):
    """Retrieves data of a specific user from MongoDB.

    Args:
        conn (pymongo.MongoClient): MongoDB connection object.
        user_id (int): ID of the user to retrieve data for.

    Returns:
        dict: A dictionary containing the user's data or None if the user is not found.
    """
    db = conn["your_database_name"]  # Replace "your_database_name" with the actual database name
    collection = db["users"]  # Replace "users" with the actual collection name
    user = collection.find_one({"Id": user_id})
    return user