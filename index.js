const { PrismaClient } = require('@prisma/client');
const express = require('express');
const prisma = new PrismaClient();
require('dotenv').config();
const app = express();
app.use(express.json());


app.post('/api/v1/book', async (req,res) => {
    res.status(201).send("Created");
})

app.get('/api/v1/genre', async (req,res) => {
    const result = await prisma.genre.findMany({})
    res.status(200).send(result);
})

app.post('/api/v1/genre', async (req,res) => {
    const name = req.body.name;
    const url = req.body.url;

    const result = await prisma.genre.create({
        data: {
            name,
            url
        }
    })

    res.status(201).json(result);
})




app.listen(3001, () => {
    console.log(`Server started at http://localhost:3001`)
})