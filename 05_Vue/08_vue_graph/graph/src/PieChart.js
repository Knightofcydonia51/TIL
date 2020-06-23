import { Doughnut, mixins } from "vue-chartjs";  // eslint-disable-line no-unused-vars
export default {
  extends: Doughnut,
  props: ["data", "options"],
  mounted() {
    this.renderChart(this.data, {
      borderWidth: "10px",
      hoverBackgroundColor: "red",
      hoverBorderWidth: "10px"
    });
  }
};
