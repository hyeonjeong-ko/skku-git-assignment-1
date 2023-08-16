import os

# Get user information from environment variables
user_name = os.environ.get('USER_NAME')
commit_time = os.environ.get('COMMIT_TIME')
commit_message = os.environ.get('COMMIT_MESSAGE')

# Print the user information
print("User Name:", user_name)
print("Commit Time:", commit_time)
print("Commit Message:", commit_message)

# import os

# # Get the value of the environment variable
# my_env_var = os.environ.get('MY_ENV_VAR')

# # Use the environment variable value
# print("Value of MY_ENV_VAR:", my_env_var)
