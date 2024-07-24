const express = require("express");
const mongoose = require("mongoose");
const app = express();
mongoose
  .connect(
    "mongodb+srv://Pranav:Watch_d0gs2157@cluster0.7s0eymc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
  )
  .then(() => console.log("SUCCESS"))
  .catch((err) => console.log(err));

app.get("/", function (req, res) {
  res.send("hello world");
});

app.listen(5000);
