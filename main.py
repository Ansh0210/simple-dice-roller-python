import random 
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1:("┌─────────┐", 
       "│         │", 
       "│    ●    │", 
       "│         │", 
       "└─────────┘"),

    2:("┌─────────┐", 
       "│  ●      │", 
       "│         │", 
       "│      ●  │", 
       "└─────────┘"),

    3:("┌─────────┐", 
       "│  ●      │", 
       "│    ●    │", 
       "│      ●  │", 
       "└─────────┘"),

    4:("┌─────────┐", 
       "│  ●   ●  │", 
       "│         │", 
       "│  ●   ●  │", 
       "└─────────┘"),

    5:("┌─────────┐", 
       "│  ●   ●  │", 
       "│    ●    │", 
       "│  ●   ●  │", 
       "└─────────┘"),

    6:("┌─────────┐", 
       "│  ●   ●  │", 
       "│  ●   ●  │",  
       "│  ●   ●  │", 
       "└─────────┘")
}

dice = []
total = 0

num_of_dice = int(input('Enter number of dice to use: '))

for num in range(num_of_dice):
   #print(num)
   dice.append(random.randint(1,6))

#print(dice)

# for loop for vertical orientation of dice(s)
# for num in dice: 
#    print(*dice_art[num], sep='\n')

# for loop for horizontal orientation of dice(s)
for elem in range(len(dice_art[1])):
   #print(elem)
   for die in dice:
      print(dice_art[die][elem], end = '')
      
   print()    

#print(total)
total = sum(dice)
print("The total is", total)