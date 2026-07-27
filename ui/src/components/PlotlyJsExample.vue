<script setup lang="ts">
import Plotly from 'plotly.js-dist-min';
import { onMounted } from 'vue';

const chartData: Plotly.Data[] = [{
  x: [1, 2, 3, 4, 5],
  y: [10, 15, 13, 17, 22],
  type: 'scatter',
  mode: 'lines+markers',
  marker: { color: 'red' },
}];

const chartLayout: Partial<Plotly.Layout> = {
  title: {
    text: "Pljotly.js Example Chart",
  },
  xaxis: {
    title: { text: "X Axis"}
  },
  yaxis: {
    title: { text: "X Axis"}
  },
};

onMounted(() => {
  Plotly.newPlot('plotly-example', chartData, chartLayout);
});

</script>

<template>
  <div>
    <h1>Plotly.js Example</h1>
    <p>This is an example of using Plotly.js in a Vue component.</p>
    <div id="plotly-example" style="width: 100%; height: 400px;"></div>
  </div>
</template>
