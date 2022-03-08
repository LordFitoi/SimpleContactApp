<template>
    <div class="w-full bg-primary rounded-2 px-4 py-6 flex flex-col gap-2 h-max">
        <h2 class="font-md">PRESUPUESTO</h2>
        <div class="w-full border border-secondary mb-4"></div>
        <div class="rounded-1 flex gap-2 border border-primary px-1 py-1">
            <input class="w-full bg-primary border-none" type="text" v-model="budgetTitle" placeholder="Inserte un título...">
            <div class="border border-primary"></div>
            <div class="w-full flex gap-1">
                <p>$</p><input class="w-full bg-primary border-none" type="number" v-model="budgetAmount">
            </div>
            <button @click="addBudget()">
                <img width="20" height="20" :src="staticPath + 'images/icons/add-circle.svg'">
            </button>
        </div>
        <div class="rounded-1 flex gap-2 border border-primary px-1 py-1 show-on" v-for="(budget, index) in budgets" :key="budget">
            <input class="w-full bg-primary border-none" type="text" v-model="budget.title">
            <div class="border border-primary"></div>
            <div class="w-full flex gap-1">
                <p>$</p><input class="w-full bg-primary border-none" type="number" v-model="budget.amount">
            </div>
            <button class="it-child" @click="removeBudget(index)">
                <img width="20" height="20" :src="staticPath + 'images/icons/remove-circle.svg'" >
            </button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            budgetTitle: "",
            budgetAmount: 0,
            budgets: [
                {
                    title: "Desayuno",
                    amount: 10
                }
            ],
            staticPath: window.staticPath
        }
    },
    methods: {
        addBudget() {
            this.budgets.push({
                title: this.budgetTitle,
                amount: this.budgetAmount
            })

            this.budgetTitle = "";
            this.budgetAmount = 0;
        },
        removeBudget(index) {
            this.budgets.splice(index, 1);
        }
    }
}
</script>