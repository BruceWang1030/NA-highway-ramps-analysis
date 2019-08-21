const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cors = require("cors");

app.use(bodyParser.json());
app.use(cors());

app.get("/data", function(req, res) {
  var sql = "SELECT * FROM users where username='" + req.query.username + "'";
  db.query(sql, (err, result) => {
    if (err) throw err;
    // console.log(result);
    res.send(result);
  });
});

app.listen(8080, () => {
  console.log("Server listening to port 8080");
});
