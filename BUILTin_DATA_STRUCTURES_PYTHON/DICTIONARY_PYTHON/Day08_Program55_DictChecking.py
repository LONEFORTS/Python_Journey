user_profile = {"username": "coder17", "status": "active"}
key_to_find = "email"

if key_to_find in user_profile:
    print(user_profile[key_to_find])
else:
    print(f"Error: {key_to_find} not found in profile!")
