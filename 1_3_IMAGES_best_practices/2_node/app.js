const express = require("express");
const app = express();

// Считываем переменную окружения, заданную в Dockerfile
// Можно также использовать PORT из переменной окружения Docker
const port = process.env.PORT || 3000;
const message = process.env.NODE_MSG || "Hello from Docker!";

app.get("/", (req, res) => {
  res.send(message);
});

app.listen(port, () => {
  console.log("App is running on port " + port);
});

// docker run --rm -p 3000:3000 --name node2 -e NODE_MSG='Hellooo' just_build_image
