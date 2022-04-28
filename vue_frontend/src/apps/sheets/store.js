import  { defineStore } from 'pinia';
import client from '../../utils/http-client.js';

export default defineStore('sheet', {
    state: () => {
        let sheetJson = document.getElementById('sheet-json').text;

        return {
            staticPath: window.staticPath,
            sheets: JSON.parse(sheetJson),
            sheet: null,
        }
    },
    actions: {
        updateBudget(budget, data) {
            data.category = budget.category;
            console.log(budget.id, data)
            return client.put(`/budgets/${budget.id}/`, data);
        },
        deleteSheet(sheet) {
            client.delete(`/budgets-sheets/${sheet.id}`).then(() => {
                for (let i in this.sheets) {
                    if (this.sheets[i].id == sheet.id) {
                        this.sheets.splice(i, 1);
                        break;
                    }
                }
            });
        }
    }
})