const body = document.querySelector("body");

function makeSnow() {
  const snowflake = document.createElement("div");

  snowflake.classList.add("snowflake");
  snowflake.style.left = `${Math.random() * window.screen.width}px`;

  body.appendChild(snowflake);
}

for (let i = 0; i < 50; i++) {
  makeSnow();
}
