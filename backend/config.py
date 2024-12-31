ollamaApiConfig = 'localhost'
ollamaPrompt = '''
Create a JSON configuration file for a word-based adventure game. You should only return a valid json object.   

Only return the json object. Do not include any other details or text. The first character will be '{' and the last character will be '}'

Each path in the game should include:

    text: A description of the scenario the player encounters.
    options: A set of possible actions the player can take, mapped to the next path. Each action can have multiple aliases separated by a pipe |.
    Optional Properties:
        restart: A boolean indicating if the path forces the player to restart.
        victory: A boolean indicating if the path represents a victory condition.

Ensure the JSON is structured and easy to modify. Example output:

{
  "start": {
    "text": "You find yourself at the edge of a mysterious cave. What will you do?",
    "options": {
      "enter cave|enter": "inside_cave",
      "walk away|leave": "outside_cave"
    }
  },
  "inside_cave": {
    "text": "The cave is dark and damp. You see two tunnels ahead. What next?",
    "options": {
      "left tunnel|left": "left_tunnel",
      "right tunnel|right": "right_tunnel"
    }
  },
  "outside_cave": {
    "text": "You walk away, leaving the cave unexplored.",
    "restart": true
  },
  "left_tunnel": {
    "text": "You find treasure hidden deep within the cave. You win!",
    "victory": true
  },
  "right_tunnel": {
    "text": "A sudden collapse traps you inside. You lose!",
    "restart": true
  }
}

The above example is just an example. Use some creativity to design a scenario that someone might be on an adventure in. 
It can vary in length but should be at least 3 steps to get to the end. 

The most important thing, is it needs to be in the same format of the example. Otherwise it will not work at all.
'''