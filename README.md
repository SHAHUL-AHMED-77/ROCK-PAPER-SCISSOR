
# Rock-Paper-Scissors Game

This repository contains two Python implementations of the classic Rock-Paper-Scissors game. The game allows you to play against the computer, and it will determine the winner based on the rules of Rock-Paper-Scissors.

## Method 1: Explicit Condition Checking

In this method, the game checks each possible outcome explicitly to determine the winner.

### Code

```python
import random as rad

def rps():
    print("Enter r for Rock\nEnter p for Paper\nEnter s for Scissor")
    
    com = rad.choice([1, 2, 3])
    player = input("Enter Your Choice: ")
    pdict = {"r": 1, "p": 2, "s": 3}
    rdict = {1: "Rock", 2: "Paper", 3: "Scissor"}
    x = pdict[player]
    print(f"You Chose: {rdict[x]}")
    print(f"Computer Chose: {rdict[com]}")
    if com == x:
        print("Match Tied")
    else:
        if com == 1 and x == 2:
            print("You win")
        elif com == 1 and x == 3:
            print("You lose")
        elif com == 2 and x == 1:
            print("You lose")
        elif com == 2 and x == 3:
            print("You win")
        elif com == 3 and x == 1:
            print("You win")
        elif com == 3 and x == 2:
            print("You lose")
        else:
            print("Error While Playing")

rps()
```

### How to Run

1. Save the code to a file named `rps_explicit.py`.
2. Run the script using a Python interpreter:
   ```bash
   python rps_explicit.py
   ```

## Method 2: Simplified Condition Checking

In this method, the game uses a more concise logic to determine the winner based on the difference between the player's and computer's choices.

### Code

```python
import random as rad

def rps():
    print("Enter r for Rock\nEnter p for Paper\nEnter s for Scissor")
    
    com = rad.choice([1, 2, 3])
    player = input("Enter Your Choice: ")
    pdict = {"r": 1, "p": 2, "s": 3}
    rdict = {1: "Rock", 2: "Paper", 3: "Scissor"}
    x = pdict[player]
    print(f"You Chose: {rdict[x]}")
    print(f"Computer Chose: {rdict[com]}")
    if com == x:
        print("Match Tied")
    else:
        a = com - x
        if a == -1 or a == 2:
            print("You win")
        else:
            print("You lose")

rps()
```

### How to Run

1. Save the code to a file named `rps_simplified.py`.
2. Run the script using a Python interpreter:
   ```bash
   python rps_simplified.py
   ```

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the directory containing the code.
3. Run either `rps_explicit.py` or `rps_simplified.py` to play the game.

Enjoy playing Rock-Paper-Scissors!
```
