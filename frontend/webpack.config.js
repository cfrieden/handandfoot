var path = require('path');

module.exports = {
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                  loader: "babel-loader"
                }
            }
        ]
    },
    // Taken from https://pascalw.me/blog/2020/04/19/webpack-django.html
    output: {
        path: path.resolve(__dirname, "static/frontend"),
        publicPath: "/static/",
        filename: "[name].js",
        chunkFilename: "[id]-[chunkhash].js"
    },
    devServer: {
        writeToDisk: true,
    }
}