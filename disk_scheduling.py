#!/usr/bin/env python3
'''
CST232 Disk Scheduling Algorithms (SCAN, C-SCAN, C-LOOK)
Author: Marcus Chan <marcus-hao>
'''

import random
import matplotlib.pyplot as plt


def CLOOK(requests, head, direction):
    distance = 0
    current_track = 0
    seek_sequence = []

    n = len(requests)   # Initial number of requests

    # Create a copy of the requests list
    working_requests = requests.copy()

    # Append end values which must be visited
    working_requests.append(head)
    working_requests.sort()

    num_of_tracks = len(working_requests)

    # Find the index of initial disk head position
    for i in range(num_of_tracks):
        if working_requests[i] == head:
            current_track = i
            break

    # If direction is left
    if direction == 'left':
        for i in range(current_track, -1, -1):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

        # Jump to the end of opposite direction and begin scanning
        for i in range(num_of_tracks-1, current_track, -1):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

    # If direction is right
    elif direction == 'right':
        for i in range(current_track, num_of_tracks):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

        # Jump to the start of opposite direction and begin scanning
        for i in range(current_track):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

    # The jump to the end of opposite direction is not counted towards seek time
    # So we subtract the max and min from the distance
    distance -= max(seek_sequence) - min(seek_sequence)

    title = f'CLOOK with n={n}'
    print(f'\n{title}')
    print("Total number of seek operations = ", distance)
    print("Seek Sequence is", seek_sequence)
    plot_graph(seek_sequence, title)


def CSCAN(requests, head, direction):
    distance = 0
    current_track = 0
    seek_sequence = []

    n = len(requests)   # Initial number of requests

    # Create a copy of the requests list
    working_requests = requests.copy()

    # Append end values which must be visited before reversing direction
    working_requests.append(0)  # The first track
    working_requests.append(head)
    working_requests.append(199)  # The last track
    working_requests.sort()

    num_of_tracks = len(working_requests)

    # Find the index of initial disk head position
    for i in range(num_of_tracks):
        if working_requests[i] == head:
            current_track = i
            break

    # If direction is left
    if direction == 'left':
        for i in range(current_track, -1, -1):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

        # Jump to the end of opposite direction and begin scanning
        for i in range(num_of_tracks-1, current_track, -1):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

    # If direction is right
    elif direction == 'right':
        for i in range(current_track, num_of_tracks):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

        # Jump to the end of opposite direction and begin scanning
        for i in range(current_track):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

    # The jump to the end of opposite direction is not counted towards seek time
    # So we subtract the max and min from the distance
    distance -= max(seek_sequence) - min(seek_sequence)

    title = f'CSCAN with n={n}'
    print(f'\n{title}')
    print("Total number of seek operations = ", distance)
    print("Seek Sequence is", seek_sequence)
    plot_graph(seek_sequence, title)


def SCAN(requests, head, direction):
    distance = 0
    current_track = 0
    seek_sequence = []

    n = len(requests)   # Initial number of requests

    # Create a copy of the requests list
    working_requests = requests.copy()

    # Append end values which must be visited before reversing direction
    working_requests.append(0)
    working_requests.append(head)
    working_requests.sort()

    num_of_tracks = len(working_requests)

    # Find the index of initial disk head position
    for i in range(num_of_tracks):
        if working_requests[i] == head:
            current_track = i
            break

    # If direction is left
    if direction == 'left':
        for i in range(current_track, -1, -1):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

        # Reverse the direction
        for i in range(current_track+1, num_of_tracks):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

    # If direction is right
    elif direction == 'right':
        for i in range(current_track, num_of_tracks):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

        # Reverse the direction
        for i in range(current_track-1, -1, -1):
            seek_sequence.append(working_requests[i])
            # Difference between head and request position
            distance += abs(working_requests[i]-head)
            head = working_requests[i]  # Update head position

    title = f'SCAN with n={n}'
    print(f'\n{title}')
    print("Total number of seek operations = ", distance)
    print("Seek Sequence is", seek_sequence)
    plot_graph(seek_sequence, title)


def plot_graph(seek_sequence, filename):
    plt.plot(seek_sequence, range(len(seek_sequence)), '-go')
    plt.xlabel('Track Number')
    ax = plt.gca()
    ax.invert_yaxis()
    ax.tick_params(top=True, bottom=False, labeltop=True,
                   labelbottom=False)    # Set x ticks to the top
    ax.get_yaxis().set_visible(False)   # Hide y axis
    ax.xaxis.set_label_position('top')  # Set x label to the top
    # plt.show()    # Uncomment to show graph in window

    # Save graph as png, comment to disable save
    plt.savefig(f'{filename}.png')
    plt.clf()  # Clear plot


if __name__ == '__main__':
    cylinders = 200
    head = 50
    sets = [10, 20, 50, 100]

    for n in sets:
        requests = random.sample(range(cylinders), n)
        # Randomly choose initial direction
        direction = random.choice(['left', 'right'])
        SCAN(requests, head, direction)
        CSCAN(requests, head, direction)
        CLOOK(requests, head, direction)
