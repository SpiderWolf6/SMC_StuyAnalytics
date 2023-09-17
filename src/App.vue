<template>
  <div id="app">
    <nav>
      <router-link to="/">Stuy Analytics</router-link>
      <br />
      <br />
      <v-btn @click="openLinkInNewTab('https://stuyvesantsmc.weebly.com/')">Presented By Sports Management Club</v-btn>
    </nav>
    <router-view/>
  </div>
</template>

<script>
  export default {
    components: {},
    data: () => ({}),
    methods: {
      openLinkInNewTab (url) {
        window.open(url, '_blank');
      }
    }
  };
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
