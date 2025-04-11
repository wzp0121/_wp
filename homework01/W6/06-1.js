import { DB } from "https://deno.land/x/sqlite/mod.ts";

// Open a database
const db = new DB("test.db");
db.query("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT,time TEXT,body TEXT)");

const data = [
    { title: "Peter Parker",time:"2021-12-15", body: "nobody remember" },
    { title: "Clark Kent", time:"2018-09-23",body: "Journalist" },
    { title: "Bruce Wayne", time:"2008-07-16",body: "no parents" },
  ];


  for (const post of data) {
    db.query(
      "INSERT INTO posts (title, time, body) VALUES (?, ?, ?)",
      [post.title, post.time, post.body]
    );
  }


  for (const [id, title, time, body] of db.query("SELECT id, title, time, body FROM posts")) {
    console.log(`ID: ${id}, Title: ${title}, Time: ${time}, Body: ${body}`);
  }
// Close connection
db.close();