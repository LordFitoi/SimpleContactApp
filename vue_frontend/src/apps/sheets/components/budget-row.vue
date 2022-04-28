<template>
    <div class="rounded-1 flex gap-2 border border-primary px-1 py-1 show-on">
        
        <input class="w-full bg-primary border-none" type="text" v-model.lazy="inputs.title" placeholder="Inserte un título...">
        <div class="border border-primary"></div>
        <div class="w-full flex gap-1">
            <p>$</p><input class="w-full bg-primary border-none" type="number" v-model.lazy="inputs.amount">
        </div>
        <button class="it-child" @click.stop="removeBudget(index)">
            <img width="20" height="20" :src="store.staticPath + 'images/icons/remove-circle.svg'" >
        </button>
    </div>
</template>

<script>
import BudgetStore from '../store.js'
export default {
    setup() {
        return { store: BudgetStore() }
    },
    props: {
        budget: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            inputs: {
                title: this.budget.title || "",
                amount: this.budget.amount || 0
            }
        }
    },
    watch: {
        inputs: {
            deep: true,
            handler() {
                this.store.updateBudget(this.budget, this.inputs).then((response) => {
                    this.$emit('update', this.$.vnode.key, response.data)
                });
            }
        }
    },
    methods: {
        onRemove() {
            this.$emit('remove', this.$.vnode.key)
        }
    }
}
</script>