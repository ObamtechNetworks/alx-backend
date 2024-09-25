const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// create the Redis client
const client = redis.createClient();

// Promisify Redis methods for async/await usage
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);  // Corrected this line

// list products
const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// Function to get a product by ID
function getItemById(id) {
    return listProducts.find((product) => product.id === id);
}

// Function to reserve stock by product ID (store in Redis)
async function reserveStockById(itemId, stock) {
    return await setAsync(`item.${itemId}`, stock);  // Corrected this line
}

// Function to get the current reserved stock by item ID
async function getCurrentReservedStockById(itemId) {
    const stock = await getAsync(`item.${itemId}`);
    return stock !== null ? parseInt(stock, 10) : 0;  // Return 0 if stock is null
}

// Create Express server
const app = express();
const port = 1245;

// Route to get all products
app.get('/list_products', (req, res) => {
    const formattedProducts = listProducts.map((product) => ({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
    }));
    res.json(formattedProducts);
});

// Route to get product details by ID (includes current stock)
app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const product = getItemById(itemId);

    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    // Get current reserved stock
    const reservedStock = await getCurrentReservedStockById(itemId);
    const currentQuantity = product.stock - reservedStock;

    res.json({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity: currentQuantity,
    });
});

// Route to reserve a product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const product = getItemById(itemId);

    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    // Get current reserved stock
    const reservedStock = await getCurrentReservedStockById(itemId);

    // Check if there's enough stock to reserve
    if (reservedStock >= product.stock) {
        return res.json({
            status: 'Not enough stock available',
            itemId: itemId,
        });
    }

    // Reserve one item by incrementing reserved stock
    await reserveStockById(itemId, reservedStock + 1);

    res.json({
        status: 'Reservation confirmed',
        itemId: itemId,
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
