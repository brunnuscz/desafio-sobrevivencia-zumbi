<template>
    <div id="app">
        <router-link to="/create" class="btn btn-success mt-3">Criar item</router-link>
        <div v-if="items && items.length">
            <div class="text-center m-4">
                <h1>Itens</h1>
            </div>


            <div class="mt-3">
                <table class="table table-bordered">
                    <thead>
                        <tr class="text-center">
                            <th scope="row">#</th>
                            <th scope="col">Id</th>
                            <th scope="col">Item</th>
                            <th scope="col">Sobrevivente</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(inventory, index) in inventories" v-bind:key="inventory.id">
                            <td class="text-center" scope="row">{{ index+1 }}</td>
                            <td class="text-center">{{ inventory.id }}</td>
                            <td class="text-center">{{ inventory.item }}</td>
                            <td class="text-center">{{ inventory.survivor }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="text-center">
            <p  v-if="inventories.length == 0">Nennum Inventorio...</p>
        </div>
    </div>

</template>
<script>
import axios from 'axios';
export default {
    name: 'InventoryTeste',
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