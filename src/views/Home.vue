<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
       username: "",
       bookdate: "",
       tobookdate: "",
    };
  },
  methods: {
    check() {
      this.$router.push({path:"/explore", query:{username: this.username}});
    },
    back(){
      this.$router.push("/login");
    },
    async getdata(){
        var res = ""
        res = await axios.post("apis/gethomedata", {username: this.username});
        console.log(res)
        res = res.data
        console.log(res.data[0])
        this.bookdate = res.data[0]
        this.tobookdate = res.data[1]
    },
  },
  mounted() {
      // console.log(this.$route.query.username)
      this.username = this.$route.query.username;
      this.getdata()
    }
};
</script>

<template>
  <div id="home-page" class="home">
    <!-- 这里是上半部分,需要姓名username -->
    <div class="title">
      <img src="../assets/img/Home1.png"  class="Homeimg1" @click="back"/>
    </div>
    <p class="name">{{username}}</p>
    <div class="title">
      <!-- 自动获取当天信息 -->
      <p class="book3" @click="check"><span style="font-weight: 400">预订日期:</span>{{ bookdate }}</p>
    </div>
    <div class="title">
      <!-- 自动获取前一天信息 -->
      <p class="book4" @click="check"><span style="font-weight: 400">下单日期:</span>{{ tobookdate }}</p>
    </div>
    <div class="title">
      <img src="../assets/img/Home2.png" class="Homeimg2"/>
    </div>
    <div class="title">
      <img src="../assets/img/Home3.png" class="Homeimg2"/>
    </div>
    <div class="title">
      <img src="../assets/img/Home3.png" class="Homeimg2"/>
    </div>
  </div>
</template>

<style scoped lang="scss">
.home {
  // max-width: 600px;
  // width:50%;
  // min-width: 100%;
  // border: 1px solid rgba(0, 0, 0, 0.08);
  width:100vw;
  .name {
      font-size: 28px;
      color: #ecfff1;
      margin: 0;
      padding: 0;
      position:absolute;
      margin-left: 28vw;
      top: 16vh;
      // width:400px;
      // font-weight: bold;
      z-index: 2;
    }
  .title {
    display: flex;
    justify-content: space-between;
    padding: 0;
    h3 {
      font-weight: 900;
      font-size: 23px;
      line-height: 22.27px;
      color: #000;
      cursor: pointer;
    }
    img {
      cursor: pointer;
    }
    .book3 {
      font-size: 14.5px;
      color: #0f8f44;
      margin: 0;
      padding: 0;
      margin-left: 6.8vw;
      margin-top: 10px;
      width:400px;
      font-weight: 400;
    }
    .book4 {
      font-size: 14.5px;
      color: #0f8f44;
      font-weight: 400;
      margin: 0;
      padding-bottom: 8px;
      margin-top: 16px;
      margin-left: 6.8vw;
      width:400px;
    }
  }
}
.Homeimg1 {
  width : 100%;
  border: 0cm;
  // position: center;
  margin-right: 0;
  padding: 0;
  position: relative;
  z-index: 1;
}
.Homeimg2 {
  width : 100%;
  border: 0cm;
  position: center;
  margin-right: 0;
  padding: 0;
  
  
}
</style>