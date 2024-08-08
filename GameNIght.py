gamers = []         # Empty list to store the players info

# Function for adding players to the current list
def add_gamer(gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        gamers.append(gamer)

# Example of creating a player's profile and adding it to the list by calling add_gamer()
kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)

# Populating the list of players
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# Creating a base frequency table for number of players available on each day
def build_daily_frequency_table():
    return {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
    
count_availability = build_daily_frequency_table()

# Populating the frequency table with the players' availability
def calculate_availability(gamers_list, available_frequency):
    for i in range(0, len(gamers_list)):
        gamer = gamers_list[i]
        availability = gamer["availability"]      # Pull the list for the available days
        for day in availability:
            if day in available_frequency:        # Identify available days gamers
                available_frequency[day] += 1     # Update availability count
            else:
                continue

calculate_availability(gamers, count_availability)
# UNCOMMENT TO SEE UPDATE FREQUENCY TABLE
#print(count_availability)

# Finding the best night for the comic book store to host Game Night
def find_best_night(availability_table):
    best_num = 0
    best_night = ""         # Empty string to be set as the best night to host
    for day in availability_table:
        if availability_table[day] > best_num:      # Checking for max availability
            best_num = availability_table[day]      # Setting the new best day thru iterations
            best_night = day        # Editing the best_night string to represent the best night to host after each iteration
        else:
            continue
    return best_night       # Return the best night to host Game Night

game_night = find_best_night(count_availability)
# UNCOMMENT TO SEE BEST NIGHT TO HOST GAME NIGHT
#print(game_night)

# Get a list of the players available on Game Night
def available_on_night(gamers_list, day):
    available = []
    for i in range(0, len(gamers_list)):
        gamer = gamers_list[i]
        name = gamer["name"]        # Pull the value associated with the "name" key
        availability = gamer["availability"]    # Pull the available days
        for days in availability:
            if days == day:
                available.append(name)      # Populate the available list with the names of the available players
    return available

attending_game_night = available_on_night(gamers, game_night)
# UNCOMMENT TO SEE LIST OF PLAYERS WHO CAN ATTEND GAME NIGHT
#print(attending_game_night)

# Create the email template
form_email = "Dear {name},\n\nCongratulations! You are able to attend our {game} night on {day_of_week}! Looking forward to gaming with you!\n\nBest,\nYa Motha's Game Shack\n"

# Format and print the emails for all available players
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        formatted = form_email.format(name = gamer, day_of_week = day, game = game)
        print(formatted)

send_email(attending_game_night, game_night, "Abruptly Goblins!")

# Begin process of finding the next best night for those who couldn't attend Game Night
unable_to_attend_best_night = []
for i in range(0, len(gamers)):
    gamer = gamers[i]
    name = gamer["name"]
    if name not in attending_game_night:        # Populate the list for those who couldn't attned Game Night
        unable_to_attend_best_night.append(gamer)
    else:
        continue

# UNCOMMENT TO SEE LIST OF PLAYERS WHO COULD NOT ATTEND GAME NIGHT
#print(unable_to_attend_best_night)

second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
# UNCOMMENT TO SEE UPDATE FREQUENCY TABLE FOR PLAYERS UNABLE TO ATTEND GAME NIGHT
#print(second_night_availability)
second_night = find_best_night(second_night_availability)
# UNCOMMENT TO SEE SECOND GAME NIGHT
#print(second_night)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")