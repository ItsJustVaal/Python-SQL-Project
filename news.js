// This is a command for the live discord futbol bot
// It doesn't run in this project but this prototype
// was made after the backend python / sql was done

module.exports = {
  name: "news",
  execute(message) {
    const sql = require("sqlite3").verbose();
    const path = os.getenv("PATH");
    let db = new sql.Database({ path } + "/data/db");
    print(path);
    const fs = require("fs");
    const { EmbedBuilder } = require("discord.js");
    if (message.author.id === "288791370506829824") {
      message.reply("Imagine talking to a bot <:pepeLoser:833719194641236068>");
      return;
    }
    let input;
    let mainStuff = message.content.split(" ");
    switch (mainStuff[1]) {
      case undefined:
      case "":
      case " ":
        input = "";
        break;
      case "manu":
      case "ManU":
      case "ManUnited":
        input = "manchester united";
        break;
      case "shit":
      case "spuds":
        input = "spurs";
        break;
      case "manc":
      case "mancity":
      case "ManCity":
        input = "manchester city";
        break;
      case "assnal":
        input = "arsenal";
        break;
      case "gzon":
        message.reply("Hi Gzon :D <:FeelsFistBumpMan:629852078734311424>");
        return;
      default:
        input = mainStuff[1].toLowerCase();
    }
    let search = "%" + input + "%";

    if (
      !mainStuff ||
      mainStuff.length > 2 ||
      input.includes("drop") ||
      input.includes("insert") ||
      input.includes("delete")
    ) {
      message.reply(
        "Use the right syntax nerd .news help for help smh my head"
      );
      return;
    }

    if (input === "help") {
      message.reply(
        "HOW TO USE NEWS COMMAND: \n .news | for all latest news \n .news {search term} | for specific news \n Only accepts 1 search term"
      );
      return;
    }

    const getData = (search) => {
      return new Promise((resolve, reject) => {
        db.serialize(() => {
          db.all(
            "SELECT site, source FROM news JOIN sources ON source_id = sources.id AND site LIKE ? ORDER BY datetime DESC LIMIT 9",
            search,
            (err, rows) => {
              if (err) reject(err);
              resolve(rows);
            }
          );
        });
      });
    };

    getData(search).then((results) => {
      let final = [];
      results.forEach((element) => {
        finalString = [
          `${element.site.charAt(0).toUpperCase() + element.site.slice(1)} -- ${
            element.source.charAt(0).toUpperCase() + element.source.slice(1)
          }`,
        ];
        final.push(finalString);
      });

      let flat = final.flat();
      if (flat.length === 0) {
        message.reply(`No current news for ${input}`);
        return;
      }

      const embed = new EmbedBuilder()
        .setTitle(`NEWS: ${input}`)
        .setColor("#FFD700");
      flat.forEach((line) => {
        embed.addFields({ name: "-------------", value: line, inline: true });
      });
      message.reply({ embeds: [embed] });

      // making json backup
      fs.writeFileSync(
        `jsons/news.json`,
        JSON.stringify(flat, null, 2),
        (err) => {
          if (err) {
            console.log(err);
            return;
          }
        }
      );
    });
  },
};
