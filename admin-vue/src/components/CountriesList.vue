<template>
  <objects-list
    @object-click="$emit('change-current-country', $event)"
    :is-loading="!countries.length"
    :objects-list="countries"
    title-name="title"
    :get-title="value => value?.title?.ru"
  />
</template>

<script>
import {Axios} from "@/http-common";
import ObjectsList from "@/components/ObjectsList";

export default {
  name: "CountriesList",
  created() {
    this.getCountries();
  },
  emits: {'change-current-country': null},
  components: {ObjectsList},
  data() {
    return {
      countries: []
    }
  },
  methods: {
    async getCountries() {
      try {
        this.countries = await Axios.get('countries/').then(({data}) => data?.countries || [])
      } catch (error) {
        console.error(error)
      }
    },
  }
}
</script>

<style scoped>

</style>