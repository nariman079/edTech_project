<template >
    <div class="profil_main_block">
        <div @click="openMenu" class="burger">☰</div>
       
        <div :class="['menu_block', { open: isMenuOpen }]">
            
            <img width="150" :src="require('@/assets/images/middle_logo.png')" alt="">
            
            <div class="menu_actions">
                <router-link to="/">Главная</router-link>
                <router-link to="/profile">Профиль</router-link>
                <router-link to="/subjects">Предметы</router-link>
            </div>
            <div v-if="isMenuOpen" @click="isMenuOpen = false" class="black_p"></div>
        </div>
        <div class="content_block">
            <div class="control_panel">
                <img width="30" height="30" src="https://cdn-icons-png.freepik.com/512/7647/7647467.png?ga=GA1.1.941110609.1733379647" alt="">
                <button @click="quitAuth" type="button">
                    Выход
                </button>
            </div>
            <p class="main_title">Главная</p>
            <p class="sub_title">Добро пожаловать на главную страницу EdTech</p>
            <p class="sub_title_1">Выберите действие:</p>
            <div class="items">
                <div @click="$router.push('/profile')" class="item">
                    <img width="120" src="https://cdn-icons-png.freepik.com/512/13466/13466581.png?ga=GA1.1.941110609.1733379647" alt="">
                    Профиль
                </div>
                <div @click="$router.push('/subjects')" class="item">
                    <img width="120" src="https://cdn-icons-png.freepik.com/512/15600/15600024.png?ga=GA1.1.941110609.1733379647" alt="">
                    Предметы
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data () {
        return {
            baseURL: "http://localhost:8000",
            isMenuOpen: false
        }
    },
    
    mounted (){
        const token = localStorage.getItem("token")
        if (token == null){
            this.$router.push('/login')
        }
        else {
            console.log("no login")
        }
    },
    methods: {
        openMenu() {
            this.isMenuOpen = !this.isMenuOpen
        },
        quitAuth() {
            localStorage.clear()
            this.$router.push('/login')
        }
    }
}
</script>
<style scoped>
* {
    transition: all 0.33s ease;
}
    .profil_main_block{
        display: flex;
    }
    .menu_actions{
        display: flex;
        flex-direction: column;
        justify-content: end;
    }
    .menu_actions a{
        color: black;
        text-decoration: none;
        padding: 10px;
        margin: 3px;
    }
    .menu_actions a:hover{
        color: white;
    }
    .menu_block {
        width: 20%;
        height: 100vh;
        display: flex;
        align-items: center;
        flex-direction: column;
        background-color: #2DD2FF;
    }
    .content_block{
        width: 80%;
        height: 100vh;
    }
    .main_title{
        font-size: 48px;
        margin-left: 69px;
        font-weight: 600;
    }
    .menu_block img{
        margin-top: 40px;
        margin-bottom: 60px;
    }
    .control_panel{
        display: flex;
        justify-content: flex-end;
    
    }
    .control_panel img{
        margin-top: 25px;
        margin-right: 40px;
        cursor: pointer;
    }
    .content_block button{
        margin-right: 15px;
        margin-top: 15px;
        padding: 15px 25px;
        border: none;
        border-radius: 3px;
        font-weight: 200;
        cursor: pointer;
        background-color: #D3F5FF;
        font-size: 16px;
    }
    .content_block button:hover{

        background-color: #2DD2FF;
    }
    .sub_title{
        font-size: 32px;
        margin-left: 69px;
        color: #4B4B4B;
    }
    .sub_title_1{
        font-weight: 900;
        margin-left: 69px;
    }
    .items{
        display: grid;
        grid-template-columns: repeat(3, 200px); /* 3 колонки равной ширины */
        grid-template-rows: repeat(1, 300px);
        gap: 100px;
    }
    .item{
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        flex-direction: column;
        background-color: #D3F5FF;
        width: 200px;
        height: 230px;
        padding: 30px;
        margin-left: 69px;
        text-align: center;
        border-radius: 14px;
        cursor: pointer;
    }   

    .item:hover{
        box-shadow: 0px 0px 1px 1px ;
    }
    .burger {
        width: 40px;
        height: 40px;
        margin-top: 15px;
        display: none;
        font-size: 30px;
        cursor: pointer;
    }
    @media (max-width:1090px) {
        .menu_block {
            width: 300px;
        }
    }
    @media (max-width:836px) {
        .burger {
            display: block;
        }
        .content_block button {
            margin-right: 0;
        }
        .menu_block {
            position: fixed;
            width: 200px;
            left: -200px;
        }
        .menu_block.open {
            left: 0;
          }
        .black_p{
        position: fixed;
        width: 100%;
        left: 200px;
        height: 100vh;
        background-color: #4B4B4B;
        opacity: 0.2;
        }
        .profil_main_block{
            justify-content: center;
        }
        .content_block p{
            margin-left: 0;
            
        }
        .items{
            justify-items: center;
        }
        
    }
    @media (max-width:726px) {
        
        .items{
            grid-template-columns: repeat(1, 200px); /* 3 колонки равной ширины */
            grid-template-rows: repeat(2, 300px);
            gap: 50px;
        }
    }
</style>