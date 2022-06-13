const path = require("path");

module.exports = {
  css: {
    loaderOptions: {
      sass: {
        additionalData: "@import \"@/assets/css/vars.scss\";"
      }
    }
  },
  outputDir: path.resolve(__dirname, "../backend/build"),
  assetsDir: "assets",
  indexPath: process.env.NODE_ENV === "production" ? "../templates/index.html" : "index.html"
};
