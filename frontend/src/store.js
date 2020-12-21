import Vue from 'vue'
import Vuex, { Store } from 'vuex'

import api from '@/services/api'

Vue.use(Vuex)

//認証に使用するモジュール
const authModule = {
    strict: process.env.NODE_ENV !== 'production',
    namedspaced:true,
    state:{
        isLoggedIn:false,
        user_id = '',
    },
    getters:{
        isLoggedIn:state => state.isLoggedIn
    },
    mutations:{
        set(state,payload){
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
            var host = process.env.VUE_APP_API_BASE_URL;
            //ここのURL定義を確認すべし
            return api.post(host +'/auth/jwt/create/',{
                'user_id':payload.user_id,
                'password':payload.password
            }).then(response =>{
                sessionStorage.setItem('token',response.data.auth_token)
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
            return api.get(host + '/auth/users/me/')
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
            context.commit('set',{'info':payload.message})
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
const store = new Vuex.Store({
    modules:{
        auth:authModule,
        message:messageModule
    }
})
export default store