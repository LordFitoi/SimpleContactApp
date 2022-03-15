<template>
    <div class="w-1d2 h-max bg-primary rounded-2 px-4 py-6 flex flex-col gap-2">
        <h2 class="font-md">RESUMEN</h2>
        <div class="w-full border border-secondary mb-4"></div>
        <div class="rounded-1 flex justify-between border border-primary px-1 py-1">
            <p>Ingresos:</p>
            <p>$ 0</p>
        </div>
        <div class="rounded-1 flex justify-between border border-primary px-1 py-1">
            <p>Egressos:</p>
            <p>$ 0</p>
        </div>
        <div class="w-full border border-secondary mt-2 mb-2"></div>
        
        <div class="rounded-1 flex justify-between border border-primary px-1 py-1">
            <p>Total:</p>
            <p>$ 0</p>
        </div>

    </div>
</template>

<script>
import BudgetStore from '../store.js'

export default {
    setup() {
        return { store: BudgetStore() }
    },
    mounted() {
        console.log(this.store.hello)
    }
}
</script>
