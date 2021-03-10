process.env.VUE_APP_API_BASE_URL = "http://localhost:8000/api/v1"
module.exports ={
    "transpileDependencies": [
        "vuetify"
      ],
      configureWebpack: {
        devtool: 'source-map'
      }
}