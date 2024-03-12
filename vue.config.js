module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/twitter-clone/'
    : '/',
    devServer: {
      disableHostCheck: true
    }
};