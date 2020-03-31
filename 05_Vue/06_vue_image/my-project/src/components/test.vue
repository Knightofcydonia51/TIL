<template>

    <div>
    <h2>hi</h2>
    <img id=image src="http://dy.gnch.or.kr/img/no-image.jpg">
    <br>
    <input id=file type=file @click="test">
    <button @click="exam"> hi </button>
    </div>
   
</template>

<script>

import Swal from 'sweetalert2';
import $ from 'jquery';
import Axios from 'axios';

var apiUrl='https://api.imgur.com/3/image';
var apiKey = 'ddbe62505149f6d';
var settings={
    processData:false,
    async:false,
    crossDomain: true,
    contentType: false,
    type:'POST',
    url:apiUrl,
    headers:{
        Authorization: 'Client-ID ' + apiKey,
        Accept: 'application/json'
    },
    mimeType: 'multipart/form-data'
}


export default {
    methods:{
        async exam(){
          

            const { value: file } = await Swal.fire({
            title: 'Select image',
            input: 'file',
            inputAttributes: {
                accept: 'image/*',
                'aria-label': 'Upload your profile picture'
            },
            
        })
            if (file) {
            var formData=new FormData();
            formData.append("image", file);
            settings.data=formData

            console.log('ready')
            
            $.ajax(settings).done(response => {
                console.log(response)
                console.log(JSON.parse(response).data.link);
            });
            const reader = new FileReader()
            reader.onload = (e) => {
                Swal.fire({
                title: 'Your uploaded picture',
                imageUrl: e.target.result,
                imageAlt: 'The uploaded picture'
                })
            }
            reader.readAsDataURL(file)
            }
        },    
    }
}
</script>

<style>

</style>