<template >
    <div class="auth_main_block">
        <div class="info_block">
            <p>Образование и EdTech</p>
            <div>
                <p class="main_logo">EdTech</p>
                <p class="subtitle_logo">Платформа ведения системы управления обучения</p>
            </div>
            <p class="end_logo">Дагестанский государственный технический университет</p>
        </div>
        <div class="auth_block">
            <img src="" alt="" class="logo">
            <p class="auth_title">Авторизация</p>
            <div>
                <label for="login">Логин:</label><br>
                <input class="login_input" type="text" id="login" v-model="login" placeholder="username">
                <label for="login">Пароль:</label><br>
                <input class="login_input" type="password" id="login" v-model="password" placeholder="**************">
            </div>
            <button @click="loginFetch" class="login_button" type="button">Войти в систему</button>
            <div><br></div>
        </div>
    </div>
</template>
<script>
export default {
    data () {
        return {
            baseURL: 'http://localhost:8000',
            userAuth: '/users/api/token/',
            login: "",
            password: ""
        }
    },
    mounted () {
        const token = localStorage.getItem("token")
        if (token == null){
            console.log("TEST")
        }
        else {
            this.$router.push('/')
        }
    },
    methods: {
        async loginFetch(){
            const response = await fetch(this.baseURL + this.userAuth, 
                {
                    method: "POST",
                    headers: {
                        "Content-Type":"application/json"
                    },
                    body: JSON.stringify({
                        username: this.login,
                        password: this.password
                    })
                }
            )
            if (response.ok) {
                const data = await response.json()
                localStorage.setItem("token", data.access)
                this.$router.push({
                    name: 'Main'
                })

            }
        }
    }
}
</script>
<style scoped>
    * {
        transition: all 1s ease;
    }
    body {
        margin: 0;

    }
    .auth_main_block {
        display: flex;
    }
    .info_block {
        padding-left: 30px;
        display: flex;
        justify-content: space-between;
        flex-direction: column;
        background-color: #2DD2FF;
        width: 50%;
        height: 100vh;
    }
    .auth_block{
        width: 50%;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
    }
    .auth_block div{
        margin-top: 2px;

    }
    .main_logo{ 
        font-size: 96px;
        font-weight: 900;
    }
    .subtitle_logo{
        font-size: 32px;
    }
    .login_input{
        background-color: #EAEAEA;
        padding: 17px;
        border: none;
        border-radius: 6px;
        width: 100%;
    }
    label {
        font-size: 20px;
        font-weight: 600;
    }
    .auth_title{
        font-size: 48px;
    }
    .login_button{
        padding: 20px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        background-color: #2DD2FF;
        font-size: 20px;
    }
    .login_button:hover{    
        background-color: white;
        border: 3px solid #0d8bad;
        color: #0d8bad;
    }
    @media (max-width: 910px) {
        .auth_main_block{
            flex-direction: column;
        }
        .info_block{
            width: 94%;
        }
        .auth_block{
            width: 100%;
        }
        .auth_block div{
            margin: auto;
        }
    }
    @media (max-width: 475px) {
        .auth_main_block{
            flex-direction: column;
        }
        .main_logo{
            font-size: 60px;
        }
        .auth_block{
            width: 100%;
        }
    }

</style>