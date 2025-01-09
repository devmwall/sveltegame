
<script>
  import { onMount } from "svelte";
  import fallbackPaths from '../lib/fallback.json';

  let userInput = "";
  let currentPath = "start";
  let storyText = 'Loading story....this might take a few minutes....It\'s running on a raspberry pi';
  let paths = [];

  const normalizeInput = (input) => {
    return input.toLowerCase().trim().replace(/[^a-z0-9 ]/g, "");
  };

  const findPath = (action, options) => {
    for (const [key, value] of Object.entries(options)) {
      const aliases = key.split("|").map(alias => alias.trim());
      if (aliases.includes(action)) {
        return value;
      }
    }
    return null;
  };

  const handleInput = (event) => {
    if(event.key != null && event.key !== 'Enter') {
      return;
    }
    const action = normalizeInput(userInput);
    const nextPath = findPath(action, paths[currentPath].options);

    if (nextPath) {
      currentPath = nextPath;
      if (paths[currentPath].restart) {
        storyText = paths[currentPath].text;
        currentPath = "start";
      } else if (paths[currentPath].victory) {
        storyText = paths[currentPath].text;
      } else {
        storyText = paths[currentPath].text;
      }
    } else {
      storyText = `You ${userInput}.\r\n Nothing happens. Try something else.\r\n${paths[currentPath].text}`;
    }
    userInput = "";
  };

  const fetchPaths = async () => {
    try {
      const response = await fetch("https://pi-routerapp.ddns.net"); // Replace with your API endpoint
      paths = (await response.json()).message.paths;
      storyText = paths[currentPath].text;
    } catch (error) {
      storyText = "Failed to load the game paths. Please try again later.";
    }
    finally{
      paths = fallbackPaths.paths
      storyText = "Server returned something invalid! Using a default path! \r\n" + paths[currentPath].text;
    }
  };

  onMount(() => {
    fetchPaths();
  });
</script>

<main>
  <h1>Word Adventure Game</h1>
  <p>This adventure game is AI generated running llama3.2:3b.</p>
  <p>This was really the only smallish model that could generate correct json.</p>
  <br/>
  <br/>
  <br/>
  <pre>{storyText}</pre>

  <input 
    type="text" 
    bind:value={userInput} 
    placeholder="Type your action here" 
    on:keydown={handleInput}
  />
  <button on:click={handleInput}>Submit</button>
</main>

<style>
  main {
    font-family: Arial, sans-serif;
    text-align: center;
    padding: 2rem;
  }

  input {
    margin: 1rem;
    padding: 0.5rem;
    font-size: 1rem;
  }

  button {
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
  }
</style>