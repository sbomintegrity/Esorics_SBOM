const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

const app = express();
const PORT = 3000;
const SECRET_KEY = "your_secret_key";  // Replace with a strong secret key

app.use(express.json());  // Middleware to parse JSON request body

// Dummy user database (replace with real database in production)
let users = [];
let items = [
  { id: 1, name: 'Item One' },
  { id: 2, name: 'Item Two' }
];

// 🛠 Middleware to Verify JWT
function verifyToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) return res.status(401).json({ message: "Access denied. No token provided." });

  try {
    const verified = jwt.verify(token.split(" ")[1], SECRET_KEY);  // Extract token after "Bearer "
    req.user = verified;  // Attach user data to the request
    next();  // Proceed to next middleware
  } catch (err) {
    res.status(403).json({ message: "Invalid token" });
  }
}

//  User Registration (Sign Up)
app.post('/register', async (req, res) => {
  const { username, password } = req.body;
  const hashedPassword = await bcrypt.hash(password, 10);  // Hash the password
  users.push({ username, password: hashedPassword });
  res.status(201).json({ message: "User registered successfully" });
});

//  User Login (Sign In)
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username);
  if (!user) return res.status(400).json({ message: "Invalid username or password" });

  const validPassword = await bcrypt.compare(password, user.password);
  if (!validPassword) return res.status(400).json({ message: "Invalid username or password" });

  const token = jwt.sign({ username }, SECRET_KEY, { expiresIn: '1h' });  // Generate JWT (valid for 1 hour)
  res.json({ token });
});

// GET All Items (Protected Route)
app.get('/items', verifyToken, (req, res) => {
  res.json(items);
});

//  Start Server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
