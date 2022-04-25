import  { defineStore } from 'pinia';
import client from '../../utils/http-client.js';

export default defineStore('sheet', {
    state: () => {
        let sheetJson = document.getElementById('sheet-json').text;

        return {
            budgets: [],
            sheets: JSON.parse(sheetJson)
        }
    },
    actions: {
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