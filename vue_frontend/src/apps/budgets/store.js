import  { defineStore } from 'pinia'

export default defineStore('budget', {
    state: () => {
        return {
            budgets: [],
            hello: "Hola Pinia"
        }
    }
})