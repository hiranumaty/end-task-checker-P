process.env.VUE_APP_API_BASE_URL = "http://127.0.0.1:8000/api/v1/"
module.exports ={
    "transpileDependencies": [
        "vuetify"
      ],
      configureWebpack: {
        devtool: 'source-map'
      }
}