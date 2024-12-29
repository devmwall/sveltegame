<script>
  import paths from '../config.json';

  let userInput = "";
  let currentPath = "start";
  let storyText = paths[currentPath].text;

  const handleInput = (event) => {
    if(event.key != null && event.key !== 'Enter') {
      return;
    }
    const action = userInput.toLowerCase();
    const nextPath = paths[currentPath].options[action];

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
</script>

<main>
  <h1>Word Adventure Game</h1>
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