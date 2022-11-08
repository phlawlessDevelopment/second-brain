---
date created: Monday, November 7th 2022, 3:07:54 pm
date modified: Tuesday, November 8th 2022, 5:27:06 pm
date_created: Monday, November 7th 2022, 3:07:54 pm
date_modified: Tuesday, November 8th 2022, 5:30:19 pm
---
Object oriented programming is such a deep part of our developer culture, it's quite difficult to avoid, when I was first learning to code
something I feel was missing was a good explination of why it came about, what problem / problems it was designed to solve.

Take for example these python function declarations
(i've ommited the function bodies as they would just distract from what's important)

```python

def read_csv(csv):
    ...

def scale_vector(vector, scalar)
    ...

def move_player(player, direction):
    ...

```

Do you see what they all have in common ? It may be a little tricky to notice, you have to for a minute forget about datatypes and variable names
and think more abstractly about what the function arguments represent.
Here are examples of those functions being called, which might help.

read_csv("data.csv")

scale_vector(my_vector, 5)

move_player(player_1, up)

The first argument in every one of these functions 
(csv,vector and player respectively) represents the same thing, the piece of data the function operates on 
(you could think about it as the "subject" of the function) and se every time you call that function you need to pass in that argument.


now let's take the last function move_player and remiagine it as a method of a Player class
(again ommiting any noise)
class Player:

```python
def move_player(self, direction):
	...
```

player_1 = Player()
player_1.move(up)


