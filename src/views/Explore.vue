<script>
import axios from "axios";

export default {
  name: "Explore",
  data() {
    return {
      tobookdate: "",
      bookdate: "",
      username: "",
      schoolnumber: "",
      username: "",
      schoolnumber: "",
      timeperiod: "",
    };
  },
  methods: {
    back() {
      this.$router.push({path:"/home", query:{username: this.username}});
    },
    QR(){
      this.$router.push({path:"/qr", query:{username: this.username}});
    },
    async changetimeperiod(){
        console.log(this.username)
        var res = ""
        res = await axios.post("apis/changetimeperiod", {username: this.username});
        this.timeperiod = res.data
      },
    async getdata(){
        var res = ""
        res = await axios.post("apis/gethomedata", {username: this.username});
        console.log(res)
        res = res.data
        this.bookdate = res.data[0]
        this.tobookdate = res.data[1]
        this.schoolnumber = res.data[4]
        this.timeperiod = res.data[2]
    },
  },
  mounted() {
      this.username = this.$route.query.username;
      this.getdata()
  },
};
</script>

<template>
  <div id="home-page" class="home">
    <div class="title">
      <img src="../assets/img/Explore1.png"  class="Homeimg1" @click="back"/>
    </div>
    <p class="tobookdate">{{ tobookdate }}</p>
    <!-- <p class="tobookdate">{{ tobookdate }}</p> -->
    <div class="title">
      
      <p class="book3" >珠海校区健身房 </p>
      <p class="book4">{{ bookdate }} <span @click="changetimeperiod">{{ timeperiod }}</span></p>
    </div>
    <p class="name">{{ username }}</p>
    <p class="name" style="top: 616px;">{{ schoolnumber }}</p>
    <div class="title">
      <img src="../assets/img/Explore2.png" class="Homeimg2" @click="QR"/>
    </div>
  </div>
</template>

<style scoped lang="scss">
.home {
  // max-width: 100%;
  // width:100%;
  // min-width: 100%;
  // border: 1px solid rgba(0, 0, 0, 0.08);
  // width:100vw;
  .name{
    font-size: 14px;
    color: #4d4d4d;
    margin: 0;
    padding: 0;
    position:absolute;
    left: 30%;
    top: 588px;
    width:100%;
    // font-weight: bold;
    z-index: 2;
  }
  .tobookdate{
    font-size: 14px;
    color: #808080;
    margin: 0;
    padding: 0;
    position: absolute;
    right: 5%;
    top: 27.8vh;
    // width:100%;
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
      font-size: 16px;
      color: #000000;
      margin: 0;
      padding: 0;
      margin-left: 20px;
      margin-top: 10px;
      width:100%;
      // font-weight: bold;
    }
    .book4 {
      font-size: 16px;
      color: #000000;
      // margin: 0;
      padding: 0;
      margin-top: 1.5vh;
      margin-right: 30px;
      // width:100%;
      white-space: nowrap;
    }
  }
}
.Homeimg1 {
  width : 100%;
  border: 0cm;
  // position: center;
  margin-right: 0;
  padding: 0;
  z-index: 1;
}
.Homeimg2 {
  width : 100%;
  border: 0cm;
  position: center;
  margin-right: 0;
  padding: 0;
  z-index: 1;
  
}
</style>