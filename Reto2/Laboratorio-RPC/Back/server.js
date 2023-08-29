var express = require("express");
var app = express();

app.get("/listfiles", function (req, res) {
  res.send("Hola Mundo!");
});

app.get('/findfiles/:id', (req, res) => {
    const userId = req.params.id; 
    res.send(`Recibido el parámetro id: ${userId}`);
});

app.listen(3000, function () {
  console.log("Aplicación ejemplo, escuchando el puerto 3000!");
});