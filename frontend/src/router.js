import Vue from 'vue'
import VueRouter from 'vue-router'
//ここに必要なページのテンプレートを記述する
import HomePage from '@/pages/HomePage'
import LoginPage from '@/pages/LoginPage'
import MainPage from '@/pages/MainPage'
import SearchMonth from '@/pages/SearchMonth'

import AdminMenu from '@/pages/AdminMenu'
import store from '@/store'
Vue.use(VueRouter)

const router= new VueRouter({
    //先にStoreを完成させて認証の状態の取得を実装すべきか
    mode:'history',
    routes:[
        {
            path: '/',
            component:HomePage,
            name:'Root',
            meta:{requiresAuth:true}
        },
        {
            path:'/login',
            component:LoginPage
        },
        {
            path:'/AdminMenu',
            component:AdminMenu,
            name:'AdminMenu',
            meta:{requiresAuth:true}
        },
        {
            path:'/MainPage',
            component:MainPage,
            name:'MainPage',
            meta:{requiresAuth:true}
        },
        {
            path:'/SearchMonth/:target',
            component:SearchMonth,
            name:'SearchMonth',
            meta:{requiresAuth:true}
        },
        {
            path:'*',
            redirect:'/'
        },
    ]
})
//Routerによる画面遷移の際に毎回実行される

router.beforeEach((to,from,next) =>{
    const isLoggedIn = store.getters['isLoggedIn']
    const token = sessionStorage.getItem('token')
    if(to.matched.some(record => record.meta.requiresAuth))
    {
        //ログイン状態の場合
        if(isLoggedIn){
            next()
        }else{
            //トークンが残っているか
            if(token!=null){
                //auth//reloadをreloadに変更
                store.dispatch('reload')
                    .then(()=>{
                        next()
                    })
                    .catch(()=>{
                        forceToLoginPage(to,from,next)
                    })
            }else{
                forceToLoginPage(to,from,next)
            }
        }
    }else{
        //ログイン不要なページであればすぐに遷移
        next()
    }
})
//ログイン画面へ強制遷移する
function forceToLoginPage(to,from,next){
    next({
        path:'/login',
        query:{
            next:to.fullPath
        }
    })
}

export default router

