const express = require('express');
const path = require('path');
const app = express();
const PORT = 8080;

// Middleware to parse JSON
app.use(express.json());

// Serve the landing page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/index.html'));
});

// Handle passkey validation
app.post('/validate', (req, res) => {
    const { passkey } = req.body;

    if (passkey =='707') {
        // Send the redirect URL only after successful validation
        res.status(200).json({ redirectUrl: 'https://youtube.com' });
    } else {
        res.status(403).send('Invalid passkey');
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
