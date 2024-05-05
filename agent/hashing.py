import hashlib

def hash_message(message):
    # Convert the message to bytes
    message_bytes = message.encode('utf-8')

    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the message bytes
    hash_object.update(message_bytes)

    # Get the hexadecimal representation of the hash
    hashed_message = hash_object.hexdigest()

    return hashed_message

