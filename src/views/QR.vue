<script>
import ZoneTweet from "@/components/ZoneTweet";
import Tweet from "@/components/Tweet";

export default {
  name: "QR",
  components: {
    ZoneTweet,
    Tweet,
  },
  methods: {
    back() {
      this.$router.push("/explore");
    },
  },
};
</script>

<template>
  <div id="home-page" class="home">
    <div class="title">
      <img src="../assets/img/QR.png"  class="Homeimg1" @click="back"/>
    </div>
    <div class="title">
      <p class="book3" >预定日期: <span style="font-weight: bold"> 2024-03-11 16:00-18:00 </span> </p>
    </div>
  </div>
</template>

<style scoped lang="scss">
.home {
  // max-width: 600px;
  // min-width: 598px;
  // border: 1px solid rgba(0, 0, 0, 0.08);

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
      margin-left: 50px;
      // position: center;
      margin-top: 10px;
      width:100%;
      // font-weight: bold;
    }
  }
}
.Homeimg1 {
  width : 100%;
  border: 0cm;
  // position: center;
  margin-right: 0;
  padding: 0;
}
.Homeimg2 {
  width : 100%;
  border: 0cm;
  position: center;
  margin-right: 0;
  padding: 0;
  
  
}
</style>