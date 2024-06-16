const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const app = express();
const port = 6969;

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.render('index', { errorMessage: null });
});

app.post('/submit', (req, res) => {
    const { name, email, mobile } = req.body;
    if (!name || !email || !mobile) {
        res.render('index', { errorMessage: 'All fields are required!' });
    } else if (!/\S+@\S+\.\S+/.test(email)) {
        res.render('index', { errorMessage: 'Invalid email address!' });
    } else {
        res.render('response', { name, email, mobile });
    }
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
