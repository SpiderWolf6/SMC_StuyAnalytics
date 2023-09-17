<template>
<div>
<span>This is the graph page. Please click Send to view the graph below. If you wish to change your graph output, then please reinput the variables on their respective pages.</span>
<br />
<br />
<img :src="'data:image/png;base64,' + message" />
<br />
<br />
<v-btn @click="submit">Send</v-btn>
<br />
<br />
<p>Message is: {{ message }}</p>
<br />
<br />
<v-btn @click="back_soccer">Back</v-btn>
</div>
</template>

<script>
import axios from "axios";
  export default {
    data () {
      return {
        message: "",
      }
    },
	methods: {
	back_soccer () {
      this.$router.push("/soccer");
	},
  blobToData(blob) {
    return new Promise ((resolve) => {
      const reader = new FileReader();
      reader.onloadend = () => resolve(reader.result);
      reader.readAsDataURL(blob);
    })
  },  
	submit() {
      axios
        .get("http://localhost:5004/graph", { responseType: 'blob' })
        .then((response) => {
          var responseBlob = new Blob([response.data], {type: "image/png"});
          var reader = new window.FileReader();
          reader.readAsDataURL(responseBlob);
          reader.onload = function() {
            var base64result = reader.result.split(',')[1];
            String(base64result);
            this.message = "Check Console for Image Data";
            console.log("Message" + this.message);
          }
        })
        .catch(function (error) {
          console.log(error);
          alert("Please try inputting the variables again from the selections pages and ensure you've clicked the 'Set' button at the bottom each time. If you receive this error again, then there is no data available for the selected variables.")
      });
    },
  },
};
</script>
