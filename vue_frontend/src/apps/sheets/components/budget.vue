<template>
    <div v-if="store.sheet">
        <div class="mb-8 flex items-center justify-between">
            <h1 class="font-xl">{{ store.sheet.category }}</h1>
            <button @click="add()" class="text-nowrap flex justify-center py-2 px-6 rounded-1 border mt-auto bg-primary">
               + Agregar Presupuesto
            </button>
        </div>
        <div class="rounded-1 flex gap-2 border border-primary px-1 py-1 show-on">
            <input class="w-full bg-primary border-none" type="text" v-model="title" placeholder="Inserte un título...">
            <div class="border border-primary"></div>
            <div class="w-full flex gap-1">
                <p>$</p><input class="w-full bg-primary border-none" type="number" v-model="amount">
            </div>
            <button class="it-child" @click.stop="removeBudget(index)">
                <img width="20" height="20" :src="store.staticPath + 'images/icons/remove-circle.svg'" >
            </button>
        </div>
        <hr class="border">
        <div v-if="budgets.length" class="flex flex-col gap-2 mb-6">
            <BudgetRow
                v-for="(budget, index) in budgets"
                :key="index"
                :budget="budget"
                @remove="remove"
                @update="update">
            </BudgetRow>
        </div>
        
        <!-- EMPTY BUDGET -->
        <div v-else class="flex justify-center items-center min-h-16">
            <p class="font-md">No hay presupuesto registrado</p>
        </div>
    </div>
</template>
<script>
import BudgetStore from '../store.js'
import client from '../../../utils/http-client.js';
import BudgetRow from './budget-row.vue'

export default {
    components: {
        BudgetRow
    },
    setup() {
        return { store: BudgetStore() }
    },
    data() {
        return {
            title: "",
            amount: 0,
            budgets: []
        }
    },
    watch: {
        'store.sheet': function(sheet) {
            client.get(`/budgets/?sheet=${sheet.id}`).then((response) =>  {
                this.budgets = response.data;
            });
        }
    },
    methods: {
        add() {
            this.budgets.push({
                title: this.title,
                amount: this.amount
            })
            this.title = "";
            this.amount = 0;
        },
        remove(index) {
            this.budgets.splice(index, 1);
        },
        update(index, data) {
            console.log(data)
            this.budgets[index] = data;
        }
    }
}
</script>