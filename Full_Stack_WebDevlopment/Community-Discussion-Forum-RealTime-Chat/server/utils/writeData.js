const fs = require("fs");

const writeData = (filePath, data) => {
  fs.writeFileSync(
    filePath,
    JSON.stringify(data, null, 2),
    "utf-8"
  );
};

module.exports = writeData;