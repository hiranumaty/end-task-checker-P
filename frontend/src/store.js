import Vue from 'vue'
import Vuex from 'vuex'
import api from '@/services/api'

Vue.use(Vuex)

//認証に使用するモジュール
const authModule = {
    strict: process.env.NODE_ENV !== 'production',
    namedspaced:true,
    state:{
        isLoggedIn:false,
        user_id:'',
    },
    getters:{
        isLoggedIn:state => state.isLoggedIn,
        user_id:state => state.user_id
    },
    mutations:{
        set(state,payload){
            //accountにgetメソッドが必要か
            state.user_id = payload.user_id
            state.isLoggedIn = true
        },
        clear(state){
            state.isLoggedIn = false
            state.user_id = ''
        }
    },
    actions:{
        login(context,payload){
            //接続の状況でうまくいっていない可能性あり
            var host = process.env.VUE_APP_API_BASE_URL;
            //LoginPageからここに飛ばない
            return api.post(host+'/auth/jwt/create/',{
                'user_id':payload.user_id,
                'password':payload.password
            })
            .then(response =>{
                console.log(response)
                //response.data内部にrefresh accessありaccessを認証トークンに登録した
                sessionStorage.setItem('token',response.data.access)
                return context.dispatch('reload')
                    .then(user => user)
            })
        },
        logout(context){
           sessionStorage.removeItem('token')
           sessionStorage.removeItem('user')
           context.commit('clear')
        },
        reload(context){
            var host = process.env.VUE_APP_API_BASE_URL;
            return api.get(host+'/auth/users/me/')
                .then(response =>{
                    const user = response.data
                    context.commit('set',{user:user})
                    sessionStorage.setItem('user',JSON.stringify(user))
                    return user
                })
        }
    }
}

//メッセージモジュール
const messageModule ={
    strict: process.env.NODE_ENV !== 'production',
    namedspaced:true,
    state:{
        error:'',
        warnings:[],
        info:''
    },
    getters:{
        error:state => state.error,
        warnings:state => state.warnings,
        info: state => state.info
    },
    mutations:{
        set(state,payload){
            if(payload.error){
                state.error = payload.error
            }
            if(payload.warnings){
                state.warnings = payload.warnings
            }
            if(payload.info){
                state.info = payload.info
            }
        },
        clear(state){
            state.error =''
            state.warnings =[]
            state.info = ''
        }
    },actions:{
        setErrorMessage(context,payload){
            context.commit('clear')
            context.commit('set',{'error':payload.message})
        },
        setWarningMessage(context,payload){
            context.commit('clear')
            context.commit('set',{'warnings':payload.message})
        },
        setInfoMessage(context,payload){
            context.commit('clear')
            context.commit('set',{'info':payload.message})
        },
        clearMessages(context){
            context.commit('clear')
        }
    }
}
//何故階層化されないのであるか
const store = new Vuex.Store({
    modules:{
        auth:authModule,
        message:messageModule
    }
})
export default store