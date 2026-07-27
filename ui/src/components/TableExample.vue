<!-- eslint-disable prefer-const -->
<script setup lang="ts">
import { onMounted, ref } from 'vue';
import type { User } from '@/types/users';

let users = ref([] as User[]);
let headers = ref([
  { text: 'ID', value: 'id' },
  { text: 'Name', value: 'name' },
  { text: 'Email', value: 'email' },
]);

onMounted(() => {
  fetch('/users')
    .then(response => response.json())
    .then(data => {
      users.value = data;
    })
});

</script>

<template>
  <v-data-table :items="users" :headers="headers"></v-data-table>
</template>
