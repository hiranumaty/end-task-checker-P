import Vue from 'vue'
import VueRouter from 'vue-router'
//ここに必要なページのテンプレートを記述する
import HomePage from '@/pages/HomePage'
import LoginPage from '@/pages/LoginPage'
import MainPage from '@/pages/MainPage'
import SearchMonth from '@/pages/SearchMonth'

import AdminMenu from '@/pages/AdminMenu'
import DeptMasterDetail from '@/pages/DeptMasterDetail'
import TaskMasterDetail from '@/pages/TaskMasterDetail'
import CreateTask from '@/pages/CreateTask'
import CreateDept from '@/pages/CreateDept'
import store from '@/store'
Vue.use(VueRouter)

const router= new VueRouter({
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
            name:'login',
            component:LoginPage
        },
        {
            path:'/AdminMenu',
            component:AdminMenu,
            name:'AdminMenu',
            meta:{requiresAdmin:true}
        },
        {
            path:'/DeptDetail/:target',
            component:DeptMasterDetail,
            name:'DeptDetail',
            meta:{requiresAdmin:true}
        },
        {
            path:'/TaskDetail/:target',
            component:TaskMasterDetail,
            name:'TaskDetail',
            meta:{requiresAdmin:true}
        },
        {
            path:'/CreateTask/',
            component:CreateTask,
            name:'CreateTask',
            meta:{requiresAdmin:true}
        },
        {
            path:'/CreateDept/',
            component:CreateDept,
            name:'CreateDept',
            meta:{requiresAdmin:true}
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
    const userinfo =  JSON.parse(sessionStorage.getItem('user'))
    //一回使うとisLoggedInが消える問題is何?
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
    }
    else if(to.matched.some(record => record.meta.requiresAdmin))
    {
        //ログイン状態の場合
        if(isLoggedIn){

            if(userinfo.is_adminAccess==true)
            {
                next()
            }else{
                forceToLoginPage(to,from,next)
            }
        }else{
            //トークンが残っているか
            if(token!=null){
                //auth//reloadをreloadに変更
                store.dispatch('reload')
                    .then(()=>{
                        if(userinfo.is_adminAccess==true)
                        {
                            next()
                        }else{
                            forceToLoginPage(to,from,next)
                        }
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

