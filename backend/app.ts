import express from "express";
import { connectToDatabase } from "./dbConnection";
import bodyParser from "body-parser";

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Initialize MongoDB connection
connectToDatabase().then(() => {
  app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
  });
});
