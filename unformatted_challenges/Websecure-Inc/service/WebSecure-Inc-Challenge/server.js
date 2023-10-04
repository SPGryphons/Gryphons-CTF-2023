const express = require('express');
const mainRoutes = require('./routes/main');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// To serve static files like CSS, Images
app.use(express.static('public'));

// Setting up the routes
app.use('/', mainRoutes);

app.get('/reflect', (req, res) => {
    const message = req.query.message || '';
    res.send(`Received message: ${message}`);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
