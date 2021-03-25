<template>
    <!-- ヘッダナビゲーション -->
    <div id="header">
        <b-navbar type="dark" variant="dark">
            <a class="navbar-brand" href="/">DRF Sample</a>
            <a class="navbar-brand" href="/AdminMenu" v-if="$route.meta.requiresAuth && this.data.is_staff">管理画面へ</a>
            <b-navbar-nav class="ml-auto" v-if="$route.meta.requiresAuth">
                <b-nav-item-dropdown right v-if="isLoggedIn">
                    <template slot="button-content">{{ user_id }}</template>
                    <b-dropdown-item href="#" @click="clickLogout">ロ グ ア ウ ト
                </b-dropdown-item>
            </b-nav-item-dropdown>
            <b-nav-item href="#" @click="clickLogin" v-else>ログイン</b-nav-item>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>
<script>
    export default{
        computed: {
            user_id:function(){
                return this.data['user_id']
            },
            isLoggedIn:function(){
                return this.data['is_activate']
            },
        },
        data(){
            return{
                data:[]
            }
        },
        created(){
           this.data = JSON.parse(sessionStorage.getItem('user')) ;
        },
        methods:{
            clickLogout:function(){
                this.$store.dispatch('logout')
                this.$store.dispatch('setInfoMessage',{message:'ログアウトしました'})
                this.$router.replace({path:'/login'})
            },clickLogin:function(){
                this.$store.dispatch('clearMessages')
                this.$router.replace({path:'/login'})
            },
        }
    }
</script>