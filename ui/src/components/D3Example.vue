<script setup lang="ts">
import * as d3 from "d3";
import { onMounted } from "vue";

onMounted(() => {
  d3.select("#d3-example")
    .append("svg")
    .attr("width", 200)
    .attr("height", 200)
    .append("circle")
    .attr("cx", 100)
    .attr("cy", 100)
    .attr("r", 50)
    .style("fill", "steelblue");
});

</script>

<template>
  <div>
    <h1>D3.js Example</h1>
    <p>This is an example of using D3.js in a Vue component.</p>
    <div id="d3-example" style="width: 100%; height: 400px;"></div>
  </div>
</template>
