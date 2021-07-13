
'''
    Channel file:
        Line 0: Channel name
        Line 1: Number of subscribers
        Lines 2 - N: List of videos
'''

'''
    This function will allow you to open a file and read its contents line by line
        returns a list of strings, each string is a line in the file
'''
def read_file_as_list(filename):

    # Open the file
    file = open(filename, "r")
    # Retrieve contents of file as lines; note that each line will end with a newline character, will strip later
    lines_from_file = file.readlines()

    lines = []
    for line in lines_from_file:
        lines.append(line.strip())

    file.close()
    return lines

'''
    This function takes in a channel name
        returns the channel information: name, subscribers, videos
'''
def get_channel_from_file(channel):

    # Name of the file containing the channel data
    filename = channel + ".txt"
    channel_list = read_file_as_list(filename)

    channel_name = channel_list[0]
    channel_subscribers = int(channel_list[1])
    channel_videos = []

    sub_index = 3

    # Videos exist
    if len(channel_list) > 2:
        for c_vid in channel_list[2:]:
            if c_vid == "SUBSCRIPTIONS":
                break
            channel_videos.append(c_vid)
            sub_index += 1
    
    channel_subscriptions = channel_list[sub_index:]

    return channel_name, channel_subscribers, channel_videos, channel_subscriptions

def get_channel_name(channel):

    channel_name, channel_subscribers, channel_videos, channel_subscriptions = get_channel_from_file(channel)
    return channel_name

def get_channel_subscriber_number(channel):

    channel_name, channel_subscribers, channel_videos, channel_subscriptions = get_channel_from_file(channel)
    return channel_subscribers

def get_channel_videos(channel):
    
    channel_name, channel_subscribers, channel_videos, channel_subscriptions = get_channel_from_file(channel)
    return channel_videos

def get_channel_subscriptions(channel):

    channel_name, channel_subscribers, channel_videos, channel_subscriptions = get_channel_from_file(channel)
    return channel_subscriptions

'''
    This function creates a new text file from a channel's data
        nothing is returned
'''
def create_channel_name(channel_name):

    # Create a new text file for the channel
    filename = channel_name + ".txt"
    file = open(filename, "x")

    # Write the channel name and the number of subscribers into the file
    file.write(channel_name + "\n")
    file.write("0 \n")
    file.write("SUBSCRIPTIONS")
    file.close()

def create_channel_subs(channel_name, channel_subscribers):

    # Create a new text file for the channel
    filename = channel_name + ".txt"
    file = open(filename, "x")

    # Write the channel name and the number of subscribers into the file
    file.write(channel_name + "\n")
    file.write(str(channel_subscribers) + "\n")
    file.write("SUBSCRIPTIONS")
    file.close()

def create_channel(channel_name, channel_subscribers, channel_videos, channel_subscriptions):

    # Create a new text file for the channel
    filename = channel_name + ".txt"
    file = open(filename, "x")

    # Write the channel name and the number of subscribers into the file
    file.write(channel_name + "\n")
    file.write(str(channel_subscribers) + "\n")

    for video in channel_videos:
        file.write(video + "\n")

    file.write("SUBSCRIPTIONS \n")

    for subscription in channel_subscriptions:
        file.write(subscription + "\n")

    file.close()

'''
    This function updates an existing channel file
        nothing is returned
'''
def update_existing_channel(channel_name, channel_subscribers, channel_videos, channel_subscriptions):

    # Name of text file for the existing channel
    filename = channel_name + ".txt"
    file = open(filename, "w")

    # Erase the contents in the current file; we will update the file by rewriting it
    file.truncate(0)
    file.close()

    # Same code below as creating a new channel file! Write the channel name and the number of subscribers into the file
    file = open(filename, "w")
    file.write(channel_name + "\n")
    file.write(str(channel_subscribers) + "\n")

    for video in channel_videos:
        file.write(video + "\n")

    file.write("SUBSCRIPTIONS \n")

    for subscription in channel_subscriptions:
        file.write(subscription + "\n")

    file.close()

def subscribe_to_channel(channel_name):

    channel_name, channel_subscribers, channel_videos, channel_subscriptions = get_channel_from_file(channel_name)
    channel_subscribers += 1
    update_existing_channel(channel_name, channel_subscribers, channel_videos, channel_subscriptions)