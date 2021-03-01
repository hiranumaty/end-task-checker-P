<template>
    <v-app>
        <GlobalHeader />
        <GlobalMessage />
        <v-data-table
            :headers = "taskListColumns"
            :items = "taskList"
        >
    </v-app>
</template>
<script>
import GlobalHeader from "@/components/GlobalHeader.vue";
import GlobalMessage from "@/components/GlobalMessage.vue";
export default{
    components:{
        GlobalHeader,
        GlobalMessage,
    },
    data() => {
        taskListColumns:[],
        taskList:[],
    },
    created(){
        this.host = process.env.VUE_APP_API_BASE_URL;
        this.userinfo = JSON.parse(sessionStorage.getItem("user"));
    },
    methods:{
        getExStatesInfo(month){
            api.get(this.host+"/ExState/"+"202103"+"/list/")
            .then((response) =>{
                let List =response.data;
                
            }):
        },
    }
};

</script>