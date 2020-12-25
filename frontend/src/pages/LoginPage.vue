<template>
  <v-app>
    <GlobalHeader />
    <GlobalMessage />
    <v-card flat tile outlined>
      <v-card-text>
        <v-form @submit.prevent="submitLogin">
          <v-text-field v-model="form.user_id" prepend-icon="mdi-account-circle" label="ユーザーID" />
          <v-text-field
            v-model="form.password"
            v-bind:type="showPassword ? 'text' : 'password'"
            prepend-icon="mdi-lock"
            append-icon="mdi-eye-off"
            label="パスワード"
            @click:append="showPassword = !showPassword"
          />
          <v-card-actions>
            <v-btn type="submit" variant="primary" class="mx-auto">ログイン</v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
  </v-app>
</template>

<script>
import GlobalHeader from "@/components/GlobalHeader.vue";
import GlobalMessage from "@/components/GlobalMessage.vue";
export default {
  components: {
    GlobalHeader,
    GlobalMessage
  },
  data() {
    return {
      form: {
        user_id: "",
        password: ""
      },
      showPassword: false
    };
  },
  methods: {
    // ログインボタン押下
    submitLogin: function() {
      // ログイン ここの定義が間違っているのかも
      this.$store
        .dispatch("auth/login", {
          user_id: this.form.user_id,
          password: this.form.password
        })
        .then(() => {
          this.$store.dispatch("message/setInfoMessage", {
            message: "ログインしました。"
          });
          // クエリ文字列に「next」がなければ、ホーム画面へ
          const next = this.$route.query.next || "/";
          this.$router.replace(next);
        });
    }
  }
};
</script>