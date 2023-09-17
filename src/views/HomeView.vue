<template>
  <div class="home">
    <TeamsCollection msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import TeamsCollection from '@/components/TeamsCollection.vue'

export default {
  name: 'HomeView',
  components: {
    TeamsCollection
  }
}
</script>
