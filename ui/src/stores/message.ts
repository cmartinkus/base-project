import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMessageStore = defineStore('message', () => {
  // ---------------------------------------------
  // 1. STATE (Refs)
  // ---------------------------------------------
  const message = ref('')
  const messageType = ref<'success' | 'error' | 'info'>('info')

  // ---------------------------------------------
  // 2. GETTERS (Computed)
  // ---------------------------------------------
  const getMessage = computed(() => message.value)
  const getMessageType = computed(() => messageType.value)

  // ---------------------------------------------
  // 3. ACTIONS (Functions)
  // ---------------------------------------------
  function addMessage(newMessage: string, type: 'success' | 'error' | 'info') {
    message.value = newMessage
    messageType.value = type
  }

  function clearMessage() {
    message.value = ''
    messageType.value = 'info'
  }

  // ---------------------------------------------
  // 4. CLEAN EXPORT GROUPS (Optional)
  // ---------------------------------------------
  const state = { message, messageType }
  const getters = { getMessage, getMessageType }
  const actions = { addMessage, clearMessage }

  // ---------------------------------------------
  // 5. UNPACKED RETURN
  // ---------------------------------------------
  return {
    ...state,
    ...getters,
    ...actions
  }
})
