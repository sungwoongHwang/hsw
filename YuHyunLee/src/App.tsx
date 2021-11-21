import type { Component } from "solid-js";

import logo from "./logo.svg";
import { css } from "@emotion/css";

const App: Component = () => {
  return (
    <div class={styles.App}>
      <header class={styles.header}>
        <img src={logo} class={styles.logo} alt="logo" />
        <p>
          Ediat <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          class={styles.link}
          href="https://github.com/solidjs/solid"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn Solid
        </a>
      </header>
    </div>
  );
};

export default App;

const styles = {
  App: css`
    text-align: center;
  `,
  header: css`
    background-color: #282c34;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: calc(10px + 2vmin);
    color: white;
  `,
  logo: css`
    animation: logo-spin infinite 20s linear;
    height: 40vmin;
    pointer-events: none;
  `,
  link: css`
    color: #b318f0;
  `,
};
