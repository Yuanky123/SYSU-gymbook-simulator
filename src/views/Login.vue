<script>
import axios from 'axios';

export default {
  name: "Login",
  data() {
    return {
      username: "",
    };
  },
  methods: {
    async login() {
        this.username = document.getElementById("inputusername").value;
        console.log("login....")
        var res = 0
        // console.log(document.getElementById("inputusername").value)
        res = await axios.post("/apis/sign_in", 
        {
            // data: 1
            username:document.getElementById("inputusername").value,
            password: document.getElementById("inputpassword").value,
            schoolnumber: document.getElementById("inputschoolnumber").value,
        })
        .catch(function (error) {
            console.log(error);
        });
        console.log(res)
        if (res.data === 1) {
            this.$router.push({path:"/home", query: { username: this.username}});
        } else {
            alert("用户名/密码/学号错误/用户未注册");
        }
    },
    async signin() {
        console.log("signin....")
        var res = 0
        res = await axios.post("/apis/new_user", {
            username: document.getElementById("inputusername").value,
            password: document.getElementById("inputpassword").value,
            schoolnumber: document.getElementById("inputschoolnumber").value,
        });
        console.log(res)
        if (res.data === 1) {
            alert("注册成功,请登录");
        } else {
            alert("注册失败/用户已注册");
        }
    }
  },   
};
</script>

<template>
  <div>
    <div id="home-page" class="home">
        <!-- 输入用户名和密码 -->
        <p class="login">用户名：<input style="margin-top:20px" id="inputusername"></p>
        <p class="login" style="margin-top:20px">密码：<input style="margin-top:20px" id="inputpassword"></p>
        <p class="login" style="margin-top:20px">学号：<input style="margin-top:20px" id="inputschoolnumber"></p>
    </div>

    <div style="margin-top:10px">
        <button class="button1" @click="login">登录</button>
        <button class="button1" @click="signin" style="margin-left: 200px;">注册</button>
    </div>
  </div>
</template>

<style scoped lang="scss">
.home{
    // display: flex;
    margin-top:20%;
    align-items: center;
    // background-color: #f5f5f5;

}
p{
    font-size: 24px;
    margin: 0;
    padding: 0;

}
input{
    outline-style: none ;
    border: 1px solid #ccc; 
    border-radius: 3px;
    padding: 14px 14px;
    width: 100%;
    font-size: 24px;
}
button{
/* CSS */
  appearance: none;
  background-color: #2ea44f;
  border: 1px solid rgba(27, 31, 35, .15);
  border-radius: 6px;
  box-shadow: rgba(27, 31, 35, .1) 0 1px 0;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  font-family: -apple-system,system-ui,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";
  font-size: 20px;
  font-weight: 600;
  line-height: 20px;
  padding: 6px 16px;
  position: relative;
  text-align: center;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
  white-space: nowrap;

.button1:focus:not(:focus-visible):not(.focus-visible) {
  box-shadow: none;
  outline: none;
}

.button1:hover {
  background-color: #2c974b;
}

.button1:focus {
  box-shadow: rgba(46, 164, 79, .4) 0 0 0 3px;
  outline: none;
}

.button1:disabled {
  background-color: #94d3a2;
  border-color: rgba(27, 31, 35, .1);
  color: rgba(255, 255, 255, .8);
  cursor: default;
}

.button1:active {
  background-color: #298e46;
  box-shadow: rgba(20, 70, 32, .2) 0 1px 0 inset;
}
}
</style>