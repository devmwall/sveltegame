<script>
  import paths from '../config.json';

  let userInput = "";
  let currentPath = "start";
  let storyText = paths[currentPath].text;

  const handleInput = () => {
    const action = userInput.toLowerCase();
    if (paths[currentPath].options[action]) {
      currentPath = paths[currentPath].options[action];
      storyText = paths[currentPath].text;
    } else {
      storyText = "Nothing happens. Try something else.";
    }
    userInput = "";
  };
</script>

<main>
  <h1>Word Adventure Game</h1>
  <p>{storyText}</p>

  <input 
    type="text" 
    bind:value={userInput} 
    placeholder="Type your action here" 
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
