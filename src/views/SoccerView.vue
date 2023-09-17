<template>
<div>
<span>This is the soccer selection page. Please select the athletes, metric, and sessions range before proceeding to the Graph page.</span>
<br />
<br />
<div>
  <v-btn @click="squad">Squad Selection</v-btn>
  <br />
  <br />
  <v-btn @click="metrics">Metrics Selection</v-btn>
  <br />
  <br />
  <v-btn @click="date_range">Session Selection</v-btn>
  <br />
  <br />
  <v-btn @click="graph">Graph</v-btn>
  <br />
  <br />
  <v-btn @click="back_home">Back</v-btn>
</div>
</div>
</template>

<script>
export default {
  components: {},
  data: () => ({}),
  methods: {
    back_home() {
      this.$router.push("/");
      this.$router.go();
    },
    metrics() {
      this.$router.push("/metrics");
    },
    squad() {
      this.$router.push("/squad");
    },
    date_range() {
      this.$router.push("/dates");
    },
    graph() {
      this.$router.push("/graph");
    },
  },
};
</script>