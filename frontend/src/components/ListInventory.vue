<template>
    <div id="app">
        <div v-if="inventories && inventories.length">
            <div class="text-center m-4">
                <h1>Inventário</h1>
            </div>


            <div class="mt-3">
                <table class="table table-bordered">
                    <thead>
                        <tr class="text-center">
                            <th scope="row">#</th>
                            <th scope="col">Id</th>
                            <th scope="col">Sobrevivente</th>
                            <th scope="col">Item</th>
                            <th scope="col">Quantidade</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(inventory, index) in inventories" v-bind:key="inventory.id">
                            <td class="text-center" scope="row">{{ index+1 }}</td>
                            <td class="text-center">{{ inventory.id }}</td>
                            <td class="text-center">{{ inventory.survivorId }}</td>
                            <td class="text-center">{{ inventory.item_id }}</td>
                            <td class="text-center">{{ inventory.amount }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

</template>
<script>
import axios from 'axios';
export default {
    name: 'ListInventoryTeste',
    data() {
        return { inventories: [] }
    },
    created() {
        this.all();
    },
    methods: {
        all: function () { axios.get('http://127.0.0.1:8000/inventories/').then(response => {
                this.inventories = response.data
            });
        }
    },
}
</script>