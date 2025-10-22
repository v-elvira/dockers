import express from "express";
const app = express();

app.get("/", (req, res) => {
  res.send("Hello from an advanced Node.js Dockerfile!");
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
