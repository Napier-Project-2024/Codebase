import matplotlib.pyplot as plt
import numpy as np
import json
import urllib.request
import time



# Assuming you have a function to fetch streaming digits from your API
def fetch_streaming_digits():
    url = f"http://hefman.ddns.net:5000/returnValues"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    return result['1']

# Initialize empty lists to store x and y data
x_data = []
y_data = []

# Define the start time
start_time = time.time()

# Continuously update the graph
while True:
    # Calculate elapsed time in seconds
    elapsed_time = time.time() - start_time

    # Fetch streaming digit every 30 milliseconds
    if elapsed_time >= len(x_data) * 0.03:
        digit = fetch_streaming_digits()
        x_data.append(elapsed_time)
        y_data.append(digit)

        # Remove data older than 2 minutes
        while x_data and x_data[0] < elapsed_time - 120:
            del x_data[0]
            del y_data[0]

        # Plot the data
        plt.clf()  # Clear the previous plot
        plt.plot(x_data, y_data, color='blue')
        plt.title('Streaming Digits Graph')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Digit')
        plt.pause(0.001)  # Pause for a very short time to update the plot