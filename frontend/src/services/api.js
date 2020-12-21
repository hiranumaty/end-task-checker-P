import axios from 'axios'
import store from '@/store'

const api = axios.create({
    baseURL:ProcessingInstruction.env.VUE_APP_ROOT_API,
    timeout:5000,
    headers:{
        'Content-Type':'application/json',
        'X-Requested-with':'XMLHttpRequest'
    }
})

//共通前処理
api.interceptors.request.use(function(config){
    store.dispatch('message/clearMessages')
    const token = sessionStorage.getItem('token')
    if(token){
        config.headers.Authorization = 'JWT'+token
        return config
    }
    return config
},function(error){
    return Promise.reject(error)
})
//共通エラー処理
api.interceptors.response.use(function(response){
    return response
},function(error){
    const status = error.response ? error.response.status:500

    //エラー内容に応じてメッセージの更新
    let message
    if (status === 400) {
        // バリデーションNG
        let messages = [].concat.apply([], Object.values(error.response.data))
        store.dispatch('message/setWarningMessages', { messages: messages })

    } else if (status === 401) {
    // 認証エラー
        const token = sessionStorage.getItem('token')
        if (token != null) {
            message = 'ログイン有効期限切れ'
        } else {
            message = '認証エラー'
        }
        store.dispatch('auth/logout')
        store.dispatch('message/setErrorMessage', { message: message })

    } else if (status === 403) {
        // 権限エラー
        message = '権限エラーです。'
        store.dispatch('message/setErrorMessage', { message: message })

    } else {
    // その他のエラー
        message = '想定外のエラーです。'
        store.dispatch('message/setErrorMessage', { message: message })
    }
    return Promise.reject(error)
})

export default api