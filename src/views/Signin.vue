<script>
import axios from 'axios';

export default {
  name: "Signin",
  data() {
  },
  methods: {
    signin() {
      async function login() {
        const res = await axios.post("http://localhost:3000/signin", {
          username: document.getElementById("inputusername").value,
          password: document.getElementById("inputpassword").value,
        });
      }
      console.log(res)
      if (res.data === 1) {
        this.$router.push("/home");
      } else {
        alert("用户名或密码错误");
      }
    },
  },
    signin() {
        this.$router.push("/signin");
    },
};
</script>

<template>
  <div>
    <div id="home-page" class="home">
        <!-- 输入用户名和密码 -->
        <p class="login">用户名：<input id="inputusername"></p>
        <p class="login" style="margin-top:20px">密码：<input id="inputpassword"></p>
    </div>

    <div style="margin-top:10px">
        <button class="button1" @click="login">登录</button>
        <button class="button1" @click="signin" style="margin-left: 250px;">注册</button>
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