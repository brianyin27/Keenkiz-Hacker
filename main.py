
# Import library of functions we will use for filewriting .etc
import lib.backend

# Create virtual profile/channel stats
channel_name = ""
sub_count = 0
videos_list = []
subscriptions = []

# This function opens up the file of the channel you subscribed, increases the sub count by 1, and then adds the channel to your subscriptions list
def subscribe_to_channel(channel_name):
    subscriptions.append(channel_name)
    lib.backend.subscribe_to_channel(channel_name)

'''
    PART 1: COMPLETE THE FOLLOWING FUNCTIONS
'''

# TODO: COMPLETE THE 3 FOLLOWING FUNCTIONS
def print_menu():
    # Add more options and implement each option as a function
    print("1 - Search bar")
    print("2 - Check your channel")

def print_channel_stats(channel_name):
    print("Name: ", lib.backend.get_channel_name(channel_name))
    print("Sub count", lib.backend.get_channel_subscriber_number(channel_name))
    print("Videos: ", lib.backend.get_channel_videos(channel_name))
    # TODO: LOOK IN BACKEND.py TO FIND HOW TO GET A LIST OF A CHANNEL'S SUBSCRIPTIONS, PRINT THAT LIST

def search_bar():

    channel_search = input("Enter channel name: ")
    print_channel_stats(channel_search)

    # TODO: ASK USER IF THEY WOULD LIKE TO SUBSCRIBE, AND USE SUBSCRIBE FUNCTION IF YES
    check_subscribe = input("Would you like to subscribe: ")
    # WRITE CODE HERE:


'''
    PART 2: EXTENSION FUNCTIONS (ADD EACH NEW FUNCTION YOU CHOOSE TO IMPLEMENT TO THE MENU AND MAIN LOOP)
'''

# The following are some functions/ideas you can try implementing (if you are looking for inspiration!)
def use_sub_bot(channel_name):
    # Increase a channel's (other than yours') sub count by 100!
    pass

def explore_subscription_videos():
    # Iterate through list of subscriptions and retrieve complete list of all videos from all subscribed channels
    pass


'''
    PART 3: IMPLEMENTATION; COMPLETE MAIN EVENT LOOP AFTER FUNCTIONS
'''

# Step 1: Welcome screen

print("Welcome to this text only Youtube that I cloned!")
new_account = input("Do you have a channel (Y for yes, N for no): ")

if new_account == "Y":
    # Log in
    channel_name = input("Enter your existing channel name: ")
    sub_count = lib.backend.get_channel_subscriber_number(channel_name)
    videos_list = lib.backend.get_channel_videos(channel_name)
elif new_account == "N":
    # Sign up
    channel_name = input("Enter your new channel name: ")

# Step 2: Main event loop
while True:
    
    # Display user navigation
    print_menu()
    option = input("Enter option: ")

    if option == "1":
        # Run search bar code, allow user to search for channels/videos; implement this as a function
        search_bar()
    
    # TODO: IMPLEMENT NEW OPTIONS IN MENU

    if option == "QUIT":
        break

# Step 3: Save session info
if new_account == "Y":
    # If an existing accoutn already exists, we just need to update their file
    lib.backend.update_existing_channel(channel_name, sub_count, videos_list, subscriptions)
elif new_account == "N":
    # If a new account was created, we need to write/create a new channel text file
    lib.backend.create_channel(channel_name, sub_count, videos_list, subscriptions)
