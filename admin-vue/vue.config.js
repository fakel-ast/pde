const path = require("path");
module.exports = {
    outputDir: path.resolve(__dirname, "../app/admin_build"),
    assetsDir: "admin-assets",
    indexPath: process.env.NODE_ENV === 'production' ? '../templates/admin_index.html' : 'index.html',
    transpileDependencies: [
        'vuetify'
    ],
    chainWebpack: config => {
        config
            .plugin('html')
            .tap(args => {
                args[0].title = 'Админка'
                return args
            })
    }
}
