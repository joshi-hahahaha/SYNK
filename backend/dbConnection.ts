import { MongoClient, ServerApiVersion } from "mongodb";
import dotenv from "dotenv";

dotenv.config();

const uri = `mongodb+srv://joshiha7:${process.env.DB_PASSWORD}@synk-db.ukrbi.mongodb.net/?retryWrites=true&w=majority&appName=synk-db`;

// Create a MongoClient instance
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  },
});

export const connectToDatabase = async () => {
  try {
    await client.connect();
    console.log("Connected to MongoDB");
    // Optionally ping the database to ensure the connection is successful
    await client.db("admin").command({ ping: 1 });
    console.log(
      "Pinged your deployment. You successfully connected to MongoDB!"
    );
  } catch (error) {
    console.error("Error connecting to MongoDB:", error);
  }
};

export const closeConnection = async () => {
  await client.close();
  console.log("MongoDB connection closed");
};
