<template>
    <div class="container mx-auto flex gap-5 grid grid-col-8">
        <budget class="col-span-6"></budget>
        <budget-summary class="col-span-2"></budget-summary>
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