import random
import time as t

song_names = []
song_times = []

cases = int(input("How many songs are in your playlist? "))

print("Calculating...")
t.sleep(2)
print("Sending data to the cloud...")
t.sleep(2)
print("Calculating distance to the sun in ants...")
t.sleep(2)
print("Stealing your credit card information...")
t.sleep(2)
print("I mean, Not stealing your credit card information...")
t.sleep(2)
print("Draining your bank account...")
t.sleep(2)
print("Must've been the wind")
t.sleep(2)
print("Please add song names one by one and follow prompts!")
t.sleep(2)

for case in range(cases):

    name = input("Enter song name: ")
    length = float(input("Enter song length (minutes): "))

    print("Hacking into NASA databases...")
    t.sleep(.5)
    print("Opening a fradulent credit card in your name...")
    t.sleep(.5)

    song_names.append(name)
    song_times.append(length)

    print("Song Added!")

save = input("Save this playlist to file? (y/n): ").lower()

if save == "y":
    file = open("music.txt", "a")

    for i in range(len(song_names)):
        file.write(song_names[i] + "," + str(song_times[i]) + "\n")

    file.close()

print("Finalizing playlist...")
t.sleep(2)
print("Replacing all songs with Baby Shark...")
t.sleep(2)

drive = float(input("How long is your commute(minutes)? "))

print("Hijacking the nearest Tesla...")
t.sleep(.5)
print("Sending your location to nearby Teslas")
t.sleep(1)
print("Sending all available Ubers and Lyfts to the moon...")
t.sleep(1)

bestplaylist = []
goodtime = 0
tries = 1000
repeat_limit = 2

for attempt in range(tries):

    names = song_names.copy()
    times = song_times.copy()

    playlist = []
    realtime = 0

    while realtime < drive:

        remaining = drive - realtime
        possible = []

        if remaining > repeat_limit and len(names) > 0:
            for i in range(len(times)):
                if times[i] <= remaining:
                    possible.append(("new", i))
        else:
            for i in range(len(song_times)):
                if song_times[i] <= remaining:
                    possible.append(("repeat", i))

        if len(possible) == 0:
            break

        choice = random.choice(possible)

        if choice[0] == "new":
            i = choice[1]
            playlist.append(names[i])
            realtime += times[i]
            names.pop(i)
            times.pop(i)
        else:
            i = choice[1]
            playlist.append(song_names[i])
            realtime += song_times[i]

    if realtime > goodtime:
        goodtime = realtime
        bestplaylist = playlist.copy()

print("\nSongs for your commute:")

for song in bestplaylist:
    print("-", song)
    t.sleep(.5)

print("Total time:", goodtime, "minutes")