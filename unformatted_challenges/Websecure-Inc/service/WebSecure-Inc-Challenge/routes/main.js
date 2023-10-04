const express = require('express');
const router = express.Router();
const path = require('path');
const jwt = require('jsonwebtoken');
require('dotenv').config();



router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'views', 'index.html'));
});

router.get('/about', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'views', 'index.html'));
});

router.get('/services', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'views', 'index.html'));
});

router.get('/contact', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'views', 'index.html'));
});

router.get('/hidden-portal', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'views', 'login.html'));
});

if (!process.env.WEBSECURE_SECRET_KEY) {
    console.error("Secret key is not set!");
    process.exit(1);
}

// DO NOT COMMIT THIS SECRET TO GIT!
const SECRET_KEY = process.env.WEBSECURE_SECRET_KEY;

router.post('/hidden-portal/auth', (req, res) => {
    const { username, password } = req.body;

    // Simplified auth logic for demonstration
    if (username === "admin" && password === "password123") {
        const token = jwt.sign({ user: 'admin', elevatedPrivileges: false }, SECRET_KEY, { expiresIn: '1h' });
        res.send(`Welcome Admin! Your JWT is: ${token}. But it seems you don't have elevated privileges to access the admin panel.`);
    } else {
        res.status(401).send("Unauthorized!");
    }
    
});

router.post('/debug', (req, res) => {
    const data = req.body;

    if (data) {
        const signedData = jwt.sign(data, SECRET_KEY);
        res.json({ signedData: signedData });
    } else {
        res.status(400).send("Bad Request");
    }
});

router.get('/admin-panel', (req, res) => {

    const authHeader = req.headers['authorization'];
    console.log(authHeader)

    if (!authHeader) {
        return res.status(401).send("Unauthorized: No token provided!");
    }

    const token = authHeader.split(' ')[1];

    try {
        const decoded = jwt.verify(token, SECRET_KEY);

        if (decoded.user === 'admin' && decoded.elevatedPrivileges === 'true') {
            res.send("Congratulations! Here's your flag: GCTF23{4lw4ys_Keep_Y0ur_S3crets_S4fe_fr0m_g1t_9174896}");
        } else {
            res.status(403).send("Forbidden: Insufficient privileges!");
        }
    } catch (err) {
        res.status(401).send("Unauthorized: Invalid token!");
    }
});



module.exports = router;