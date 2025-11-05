# amv names Generator
import random
# AMV naming conventions. 
#
# introduction in homestuck quirk. Terezi. 
# user can input the pairings or random names combine them randomly to create amv names.
bottom = input(("Put names of characters here, uke: "))
top = input(("then seme: "))
song_list = [
    "Angel with a Shotgun",
    "Sweater Weather",
    "Daddy Issues",
    "Seven Nation Army",
    "Loving You is a Losing Game",
    "Take Me to Church",
    "Youth",
    "Stressed Out",
    "Ride",
    "Heathens", 
    "Numb", 
    "Snuff", 
    "In the End", "Creep", "Mad World", "Tears Ricochet", "Cellophane"
    "Born to Die",
    "Boulevard of Broken Dreams",
]
song_choice = random.choice(song_list)
# add random symbols japanese quote brackets, normal brackets, |, ♡, ★, ☆, ♥
symbols = [ "♡", "★", "‣", "♥", "♢", "◆", "✦", "✧"]
#"「」", "()", "|", "♢", "◆", "✦", "✧"
# generate the random apperance of the symbols (once, after 5 generated names, etc.) range the extent of clutterness in name.
symbols_choice = random.choice(symbols)

# add style options - all caps, lowercase, title case, alternating caps.

def generate_amv_name(bottom, top):
    song_choice = random.choice(song_list)
    symbols_choice = random.choice(symbols)
    amv_name = f"{bottom} x {top} AMV - {song_choice} {symbols_choice}" 
    # how to alternate the order of elements?
    return amv_name

print(generate_amv_name(bottom, top))

