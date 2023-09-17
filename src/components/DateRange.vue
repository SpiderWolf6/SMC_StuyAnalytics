<template>
<div>
<span>This is the session selection page. Please ensure that the start date precedes the end date. Also, make sure to click the Set Sessions Range button after changing your date range.</span>
<br />
<br />
<div id="app">
  <v-app id="inspire">
    <v-row>
      <v-col
        cols="12"
        sm="6"
      >
        <v-date-picker
          v-model="dates"
          range
          min = "2022-08-25"
          max = "2022-09-20"
        ></v-date-picker>
        model: {{ "Dates selected between " + dates }}
      </v-col>
    </v-row>
  </v-app>
<br />
<br />
<v-btn @click="submit">Set Sessions Range</v-btn>
<br />
<br />
<p>Message is: {{ message }}</p>
<br />
<br />
<v-btn @click="back_soccer">Back</v-btn>
</div>
</div>
</template>

<script>
import axios from "axios";
  export default {
    data () {
      return {
    dates: ["2022-08-25"],
		message: "",
      }
    },
	computed: {
    dateRangeText () {
      return this.dates.join(' ~ ')
      },
    },
	methods: {
	back_soccer () {
      this.$router.push("/soccer");
	},  
	submit() {
      axios
        .post("http://localhost:5003/dates_selection", {
          date_range: this.dates,
        })
        .then((response) => {
          this.message = response.data;
        });
    },
  },
};
</script>
