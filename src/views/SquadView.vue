<template>
<div>
<span>This is the squad selection page. Please select the player(s) that you would like to view the data of. Also, if you wish, you may turn on the Average button, which will take into account the average statistics of the selected players.</span>
<br />
<br />
<div>
<span>SELECT PLAYERS </span>
  <br />
  <v-checkbox
	v-model="average"
	label="Graph with Players Average"></v-checkbox>
  <br />
    <p>{{ selected }}</p>
    <v-checkbox v-for="item in players"
				:key = "item"
				v-model="selected"
				:label = "item"
				:value = "item"></v-checkbox>
<br />
<br />
<v-btn @click="submit">Set Players</v-btn>
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
				average: false,
        selected: [],
				message: "",
				players: ["#34", "#15", "#20", "#9", "#16", "#8", "#6", "#30", "#11", "#5", "#35", "#36", "#33", "#12", "#27", "#21", "#18", "#25", "#23", "#19", "#4", "#47"],

      };
    },
	methods: {
		back_soccer () {
			this.$router.push("/soccer");
		},  
		submit() {
			axios
				.post("http://localhost:5002/players_selection", {
					average: this.average,
					player_names: this.selected,
				})
				.then((response) => {
					this.message = response.data;
				});
		},
	},
};
</script>
