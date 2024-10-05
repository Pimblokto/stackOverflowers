import pymongo
from pymongo import MongoClient

uri = "mongodb+srv://rajaramanishwar:VaGhUt2Ej7niI1Rb@stackoverflowers.4ri5c.mongodb.net/"
conn = MongoClient(uri,tls = True)


def retrieve_user_data(conn, user_name):
    """Retrieves data of a specific user from MongoDB.

    Args:
        conn (pymongo.MongoClient): MongoDB connection object.
        user_id (int): ID of the user to retrieve data for.

    Returns:
        dict: A dictionary containing the user's data or None if the user is not found.
    """
    db = conn["User"]
    collection = db["user_info"]
    user = collection.find_one({"Username": user_name})
    return user


def update_productive_time(conn, user_id, data):
    """Updates the ProductiveTime of a user in MongoDB.
    Args:
        conn (pymongo.MongoClient): MongoDB connection object.
        user_id (int): ID of the user to update.
        data (dict): Dictionary containing the updated ProductiveTime.
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    db = conn["User"]  
    collection = db["users"]  
    result = collection.update_one(
        {"Id": user_id}, {"$set": {
            "ProductiveTime": data["ProductiveTime"]
        }})
    return result.acknowledged


user_id = 1
new_productive_time = {"ProductiveTime": 150}
success = update_productive_time(conn, user_id, new_productive_time)

if success:
    print("ProductiveTime updated successfully")
else:
    print("Failed to update ProductiveTime")
