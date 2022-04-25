<template>
    <div class="container mx-auto flex gap-5 grid grid-col-12">
        <div class="box col-span-12 border border-primary shadow-sm">
            <div class="mb-8 flex items-center justify-between">
                <h1 class="font-xl">Presupuesto</h1>
                <button onclick="toggleModalState('create-sheet')" class="text-nowrap flex justify-center py-2 px-6 rounded-1 border mt-auto bg-primary">
                    Crear Hoja de Presupuesto
                </button>
            </div>
            <table class="w-full text-left" border="0" cellspacing="0" cellpadding="0">
                <thead>
                    <tr class="category-list divide-y-white">
                        <th>Nombre:</th>
                        <th style="width: 25%;">Categoria:</th>
                        <th style="width: 25%;">Fecha:</th>
                        <th style="width: 32px;">.</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="sheet in store.sheets" :key="sheet" class="divide-y-primary item-list">
                        <td>{{ sheet.name }}</td>
                        <td>{{ sheet.category }}</td>
                        <td>{{ toLocaleDate(sheet.date) }}</td>
                        <td>
                            <button class="it-child" @click="store.deleteSheet(sheet)">
                                <img width="20" height="20" :src="staticPath + 'images/icons/trash.svg'" >
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
import BudgetStore from './store.js'

export default {
    setup() {
        return { store: BudgetStore() }
    },
    data() {
        return {
            dateLocale: "en-US",
            dateConfig: {
                month: "long",
                day: "numeric",
                year: "numeric"
            },
            staticPath: window.staticPath
        }
    },
    methods: {
        toLocaleDate(dateString) {
            return new Date(dateString)
                .toLocaleDateString(this.dateLocale, this.dateConfig);
        }
    }
}
</script>