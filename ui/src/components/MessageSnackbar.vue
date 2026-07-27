<!-- eslint-disable prefer-const -->
<script setup lang="ts">
import { useMessageStore } from '@/stores/message';
import { ref, watch } from 'vue';

const messageStore = useMessageStore()
let snackbar = ref(false);

function closeSnackbar() {
  snackbar.value = false;
  messageStore.clearMessage();
}

watch(() => messageStore.message, (newMessage: string) => {
  if (newMessage) {
    snackbar.value = true;
  }
});

</script>

<template>
  <v-snackbar v-model="snackbar" :timeout="messageStore.getMessageType === 'error' ? 5000 : 3000" :color="messageStore.getMessageType === 'error' ? 'red' : 'green'" top right>
      {{ messageStore.getMessage }}
      <template v-slot:actions>
        <v-btn color="blue" variant="text" @click="closeSnackbar()">Close</v-btn>
      </template>
    </v-snackbar>

</template>
