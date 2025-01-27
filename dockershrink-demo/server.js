const express = require("express");
const csv = require("csv-parser");
const fs = require("fs");

const app = express();

app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  next();
});

app.get("/csv", (req, res) => {
  const results = [];

  fs.createReadStream("article.csv")
    .pipe(csv())
    .on("data", (data) => results.push(data))
    .on("end", () => {
      res.json(results);
    });
});

app.get("/", (_, res) => {
  res.send(
    "привет это сервер, приложение находится по адресу http://localhost:8085"
  );
});

app.listen(3001, () => {
  console.log("Server is running on port 3001");
});
