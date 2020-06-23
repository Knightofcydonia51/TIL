<template>
  <div>
    <h1> cos_name </h1>
    <div id="app"  style="width:400px;">
      <pie-chart :data="chartData" :options="chartOptions"></pie-chart>
    </div>
    평균값  : {{average(chartData.datasets[0].data)}}

  </div>
</template>

<script>
import PieChart from "./PieChart.js";
export default {
  name: "App",
  components: {
    PieChart
  },
  methods:{
    average(array){
      var sum = 0.0;

      for (var i = 0; i < array.length; i++)
        sum += array[i];
      
      return sum / array.length;
   }
  },
  data() {
    return {
      chartOptions: {
        hoverBorderWidth: 20
      },
      chartData: {
        hoverBackgroundColor: "red",
        hoverBorderWidth: 10,
        labels: ["유해도 1", "유해도 2", "유해도 3"],
        datasets: [
          {
            label: "Data One",
            backgroundColor: ["#41B883", "#E46651", "#00D8FF"],
            data: [1, 3, 4]
          }
        ]
      }
    };
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>



