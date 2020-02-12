<template>
  

<div>
    
    <input id="file" type="file" name="image" @change="GetImage" style="display:none;">
    <button @click="buttonImage()">buttons
    </button>
    <img :src="avatar" alt="Image">
    

    <a href="#" class="btn btn-success" @click.prevent="upload">등록</a>

    <button @click="exam">hi</button>

</div>

</template>

<script>
import Swal from 'sweetalert2';

export default {
  
  
  data(){
    return{
      avatar:null
    }
  },
  methods:{
//   async exam(){
//   const { value: file } = await Swal.fire({
//   title: 'Select image',
//   input: 'file',
//   inputAttributes: {
//     accept: 'image/*',
//     'aria-label': 'Upload your profile picture'
//   }
// })

// if (file) {
//   const reader = new FileReader()
//   reader.onload = (e) => {
//     Swal.fire({
//       title: 'Your uploaded picture',
//       imageUrl: e.target.result,
//       imageAlt: 'The uploaded picture'
//     })
//   }
//   reader.readAsDataURL(file)
// }


//   },
    GetImage(e){
      let image = e.target.files[0]
      let reader
       = new FileReader();
      reader.readAsDataURL(image);
      reader.onload = e =>{
        this.avatar=e.target.result
      }
      console.log(e.target.files)
    },
    // upload(){
    //   axios.post('/upload',{'image': this.avatar})
    // }
  },
  buttonImage(){
    var i = document.getElementById(file)
    i.click();
    }
}
</script>

<style>

</style>