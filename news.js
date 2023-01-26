let input = "city";
const sql = require("sqlite3").verbose();
let db = new sql.Database("C:/Temp/Code/Learn/Practice/Scraper/data.db");
const fs = require("fs");
const { EmbedBuilder } = require("discord.js");

let search = "%" + input + "%";

const getData = (search) => {
  return new Promise((resolve, reject) => {
    db.serialize(() => {
      db.all(
        "SELECT site, source, datetime FROM news JOIN sources ON source_id = sources.id AND site LIKE ?",
        search,
        (err, rows) => {
          if (err) reject(err);
          resolve(rows);
        }
      );
    });
  });
};

let result = getData(search).then((results) => {
  let final = [];
  results.forEach((element) => {
    let date = element.datetime.slice(0, 10);
    finalString = [
      `${element.site.charAt(0).toUpperCase() + element.site.slice(1)} - ${
        element.source
      } - ${date}`,
    ];
    final.push(finalString);
  });
  let flat = final.flat();
  fs.writeFileSync(`jsons/news.json`, JSON.stringify(flat, null, 2), (err) => {
    if (err) {
      console.log(err);
      return;
    }
  });
});
