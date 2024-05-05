import matplotlib.pyplot as plt
import numpy as np
import json
import urllib.request
import time



# Assuming you have a function to fetch streaming digits from your API
def fetch_streaming_digits(x):
    x = str(x)
    url = f"http://hefman.ddns.net:5000/returnValues"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    return result[x]

# Initialize empty lists to store x and y data
x_data1 = []
y_data1 = []

x_data2 = []
y_data2 = []

# Define the start time
start_time = time.time()

fig, axs = plt.subplots(2)
fig.suptitle('Readings From Potentiometers')

# Continuously update the graph
while True:
    # Calculate elapsed time in seconds
    elapsed_time = time.time() - start_time

    # Fetch streaming digit every 30 milliseconds
    if elapsed_time >= len(x_data1) * 0.001:



        for x in range (8):
            if x == 2:
               digit = fetch_streaming_digits(x-1)
               x_data1.append(elapsed_time)
               y_data1.append(digit)

               # Remove data older than 2 minutes
               while x_data1 and x_data1[0] < elapsed_time - 120:
                   del x_data1[0]
                   del y_data1[0]








            if x == 3:
               digit = fetch_streaming_digits(x-1)
               x_data2.append(elapsed_time)
               y_data2.append(digit)

               # Remove data older than 2 minutes
               while x_data2 and x_data2[0] < elapsed_time - 120:
                   del x_data2[0]
                   del y_data2[0]
    
    
    # Plot the data

    axs[0].clear()  # Clear the previous plot
    axs[0].plot(x_data1, y_data1, color='blue')
    axs[0].set_title('Streaming Digits 1')
    axs[0].xlabel=('Time (seconds)')
    axs[0].ylabel=('Value')
    #plt.pause(0.001)  # Pause for a very short time to update the plot

    
    # Plot the data
    axs[1].clear()  # Clear the previous plot
    axs[1].plot(x_data2, y_data2, color='red')
    axs[1].set_title('Streaming Digits 2')
    axs[1].xlabel=('Time (seconds)')
    axs[1].ylabel=('Value')
    plt.pause(0.001)  # Pause for a very short time to update the plot



