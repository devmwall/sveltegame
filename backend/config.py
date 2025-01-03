ollamaApiConfig = 'localhost'
ollamaPrompt = '''
Design an engaging adventure game using a JSON configuration.

Your task is to create a JSON object that defines multiple paths for the player to explore. Each path must include:

    text: A detailed description of the scenario or challenge.
    options: A set of possible actions the player can take, each mapped to the next path. Use aliases separated by | for each option.

Rules:

    At least 4 unique paths must be included.
    Each option must link to another path (except for victory or restart scenarios).
    Use optional properties like:
        "restart": true for losing paths.
        "victory": true for winning paths.

Example Structure:

{
  "paths": {
    "start": {
      "text": "You are in a mysterious forest. A fork in the road lies ahead. What will you do?",
      "options": {
        "take left path|left": "river_crossing",
        "take right path|right": "dark_cave"
      }
    },
    "river_crossing": {
      "text": "You reach a river. You can swim across or search for a bridge.",
      "options": {
        "swim across|swim": "treasure_room",
        "search for bridge|bridge": "wolf_encounter"
      }
    },
    "dark_cave": {
      "text": "The cave is dark and eerie. You hear noises inside.",
      "options": {
        "venture deeper|venture": "treasure_room",
        "exit cave|exit": "restart"
      }
    },
    "wolf_encounter": {
      "text": "A wolf blocks your path! You must fight or flee.",
      "options": {
        "fight wolf|fight": "treasure_room",
        "flee|run": "restart"
      }
    },
    "treasure_room": {
      "text": "You discover a room filled with gold and jewels. You win!",
      "victory": true
    },
    "restart": {
      "text": "Your journey ends here. Restart your adventure.",
      "restart": true
    }
  }
}

Instructions:
    Be creative! Use themes like ancient temples, space exploration, or haunted houses.
    Ensure the JSON is well-structured and valid, starting with { and ending with }.

IMPORTANT:
    The really important thing is to check the response multiple times to make sure it is valid json. 
    Check the json against yourself to ensure it can be parsed as json.
    Do not include any extra text or explanations—only output the JSON object!!!!

    I am going to be passing exactly what you respond with to a json parser.

'''