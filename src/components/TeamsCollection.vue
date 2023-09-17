<template>
  <div>
  <v-container fluid>
  <br />
  <br />
  <span>Welcome to the Stuyvesant Data Corner.</span>
  <br />
  <span>Here, you will find player and team stats collected from Catapult wearable technology.</span>
  <br />
  <br />
  <span>Please select your sport below.</span>
  <br />
  <br />
  <br />
  <v-btn @click="soccer">Boys Soccer 22-23</v-btn>
</v-container>
</div>
</template>

<script>
  export default {
    data () {},
	methods: {
    soccer () {
      this.$router
        .push({
          path: "/soccer"
        })
        .then(() => {
          this.$router.go();
        });
    },
  }  
};
</script>
