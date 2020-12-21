<template>
    <!-- ヘッダナビゲーション -->
    <div id="header">
        <b-navbar type="dark" variant="dark">
            <a class="navbar-brand" href="/">DRF Sample</a>
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
                return this.$store.getters['auth/user_id']
            },
            isLoggedIn:function(){
                return this.$store.getters['auth/isLoggedIn']
            },
        },
        methods:{
            clickLogout:function(){
                this.$store.dispatch('auth/logout')
                this.$store.dispatch('message/setInfoMessage',{message:'ログアウトしました'})
                this.$store.replace('/login')
            },clickLogin:function(){
                this.$store.dispatch('message/clearMessage')
                this.$router.replace('/login')
            }
        }
    }
</script>