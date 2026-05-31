const fs = require("fs");

const readData = (filePath) => {
  try {
    const data = fs.readFileSync(filePath, "utf-8");

    return JSON.parse(data);
  } catch (error) {
    console.log(error);

    return [];
  }
};

module.exports = readData;