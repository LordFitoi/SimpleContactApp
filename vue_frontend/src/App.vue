<template>
    <div class="container mx-auto flex gap-4">
        <budget></budget>
        <budget-summary></budget-summary>
    </div>
</template>
<script>
import Budget from "./components/budget.vue"
import BudgetSummary from "./components/summary.vue"
import BudgetStore from './store.js'

export default {
    setup() {
        return { store: BudgetStore() }
    },
    mounted() {
        console.log(this.store.hello)
    },

    components: {
        Budget,
        BudgetSummary
    }
}
</script>