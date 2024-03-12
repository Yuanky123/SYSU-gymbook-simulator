<script>
import ZoneTweet from "@/components/ZoneTweet";
import Tweet from "@/components/Tweet";

export default {
  name: "Home",
  components: {
    ZoneTweet,
    Tweet,
  },
  methods: {
    check() {
      this.$router.push("/explore");
    },
  },
};
</script>

<template>
  <div id="home-page" class="home">
    <div class="title">
      <img src="../assets/img/Home1.png"  class="Homeimg1" />
    </div>
    <div class="title">
      <!-- <p class="book1">订单 <span style="font-weight:bold">1710000917028003</span></p>
      <p class="book2">预定成功</p> -->
      <!-- <p class="book3">珠海校区健身房</p> -->
      <p class="book3" @click="check">预订日期:2024-03-11</p>
      <!-- <button class="button">再来一单</button>
      <p class="book4">金额： ￥5 数量: 1</p> -->
    </div>
    <div class="title">
      <p class="book4" @click="check">下单日期:2024-03-10 15:17:34</p>
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
      font-size: 18px;
      color: #0f8f44;
      margin: 0;
      padding: 0;
      margin-left: 30px;
      margin-top: 10px;
      width:400px;
      // font-weight: bold;
    }
    .book4 {
      font-size: 18px;
      color: #0f8f44;
      margin: 0;
      padding: 0;
      margin-top: 20px;
      margin-left: 30px;
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
}
.Homeimg2 {
  width : 100%;
  border: 0cm;
  position: center;
  margin-right: 0;
  padding: 0;
  
  
}
</style>