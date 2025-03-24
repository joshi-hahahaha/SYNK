// dbConnection.ts
import dotenv from "dotenv";
import mongoose from "mongoose";

dotenv.config();

//details from the env
const username = process.env.USERNAME;
const password = process.env.PASSWORD;
const uri = `mongodb+srv://${username}:${password}@synk-db.ukrbi.mongodb.net/?retryWrites=true&w=majority&appName=synk-db`;

//db connection
export const db = mongoose
  .connect(uri)
  .then((res) => {
    if (res) {
      console.log(`Database connection successfully established`);
    }
  })
  .catch((err) => {
    console.log(err);
  });
