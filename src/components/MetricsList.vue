<template>
<div>
<span>This is the metrics selection page. Please ensure that you click the Set Metric button after changing your metric.</span>
<br />
<br />
<v-app>
<v-select
  v-model="selected_metric"
  clearable
  chips
  v-on:change="onChange($event)"
  label="Select"
  :items="items"
  item-text="state"
  variant="outlined"
></v-select>
<v-btn @click="submit">Set Metric</v-btn>
<br />
<br />
<p>Message is: {{ message }}</p>
<br />
<br />
<v-btn @click="back_soccer">Back</v-btn>
</v-app>
</div>
</template>

<script>
import axios from "axios";
  export default {
    data () {
      return {
        selected_metric: "",
    items: [{state: 'Distance (miles)'}, {state: 'Power Plays'}, {state: 'Top Speed (mph)'}, {state: 'Player Load'}, {state: 'Distance Per Min (m/min)'}],
		message: "",
      }
    },
  methods: {
    back_soccer() {
      this.$router.push("/soccer");
    },
    onChange(event) {
      this.selected_metric = event.target.value;
    },
    submit() {
      console.log("Current value", this.selected_metric),
      console.log("Current msg", this.message),
      axios
        .post("http://localhost:5001/metrics_selection", {
          metric: this.selected_metric,
        })
        .then((response) => {
          this.message = response.data;
        });
    },
  },
};
</script>
