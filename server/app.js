const express = require("express");
const bodyParser = require("body-parser");
const axios = require('axios');
// const request = require("request");


// import mailchimp from "@mailchimp/mailchimp_marketing";

// mailchimp.setConfig({
//   apiKey: "YOUR_API_KEY",
//   server: "YOUR_SERVER_PREFIX",
// });

// async function run() {
//   const response = await mailchimp.ping.get();
//   console.log(response);
// }

// run();



const app = express();
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));



const data = require('../checkers/data.json')

app.get('/', function (req, res) {
  res.header("Content-Type",'application/json');
  res.send(JSON.stringify(data));
})



app.post('/', (req, res) => {
    console.log('Got body:', req.body);
    res.sendStatus(200);
});

// app.get("/", function (req, res) {
//     res.sendFile(__dirname + "/signup.html")
// });

// app.post("/", function (freq, fres) {
//     var fname = freq.body.fname;
//     var lname = freq.body.lname;
//     var mail = freq.body.mail;
//     console.log(fname, lname, mail);
// });

app.listen(3000, function () {
    console.log("The server is running on port 3000");
});
