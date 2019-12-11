<template>
  <div class="container">
    <search-bar @inputChange="onInputChange"></search-bar>
    <div class="row">
      <video-detail :video="selectedVideo"></video-detail>
      <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list> <!--videos를 videos라는 이름으로 videolist로 보내겠다 -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from "./components/SearchBar" // 1. emit 받는 과정: 임포트하기
import VideoList from "./components/VideoList"
import VideoDetail from "./components/VideoDetail"

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'app',
  data(){
    return {
      videos: [],
      selectedVideo: null, 
    }
  },
  components:{ // 2. 컴포넌트에 등록
    SearchBar,
    VideoList,
    VideoDetail,
  },
  methods:{
    onVideoSelect(video){
      console.log(video)
      this.selectedVideo=video
    },
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params:{
          //1. 위에서 가져온 키
          key:API_KEY,
          //2. (optio) 특정 리소스 유형만 검색(channel, playlis, video)
          type: 'video',
          //3. (required) API 응답이 포함하는 search 리소스 속성
          part: 'snippet',
          //4. (option) string -> 검색어(사용자에게 받은 input value)
          q: inputValue
        }
      })
      .then((response) => {
        console.log(response)
        this.videos = response.data.items 
      })
      .catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>

<style>
  
</style>
