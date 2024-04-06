module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/twitter-clone/'
    : '/',
    devServer: {
      disableHostCheck: true,
      proxy: {
        '/apis': {
            // target: '',//接口的前缀
            target:'http://172.0.0.1:5000/', //改成你自己的后端接口
            ws:true,//代理websocked
            changeOrigin:true,//虚拟的站点需要更管origin
            pathRewrite:{
                '/apis':''//重写路径
            }
        }
    }
    }
};