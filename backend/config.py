ollamaApiConfig = 'localhost'
ollamaPrompt = '''
Create a JSON configuration file for a word-based adventure game. Make sure everything passed back is valid json.
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
}'''