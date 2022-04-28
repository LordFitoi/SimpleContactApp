import { createApp } from 'vue'
import { createPinia } from 'pinia'
import SheetApp from './app.vue'
import BudgetApp from './components/budget.vue'

const pinia = createPinia()
createApp(SheetApp).use(pinia).mount('#app')
createApp(BudgetApp).use(pinia).mount('#budget-app')

