<template>
    <div class="container mx-auto flex gap-4">
        <budget></budget>
        <budget-summary></budget-summary>
    </div>
</template>
<script>
import Budget from "./components/budget.vue"
import BudgetSummary from "./components/summary.vue"

export default {
    components: {
        Budget,
        BudgetSummary
    }
}
</script>