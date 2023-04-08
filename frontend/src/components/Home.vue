<template>
    <div id="app">
        <div v-if="items && items.length">
            <div class="text-center m-5">
                <h1>Bem-vindo Sobrevivente</h1>
            </div>

            <router-link to="/create" class="btn btn-success mt-3">Criar item</router-link>

            <div class="mt-3">
                <table class="table table-bordered">
                    <thead>
                        <tr class="text-center">
                        <th scope="row">#</th>
                        <th scope="col">Id</th>
                        <th scope="col">Nome</th>
                        <th scope="col">Pontos</th>
                        <th scope="col">Ações</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item, index) in items" v-bind:key="item.id">
                            <td class="text-center" scope="row">{{ index+1 }}</td>
                            <td class="text-center">{{ item.id }}</td>
                            <td class="text-center">{{ item.name }}</td>
                            <td class="text-center">{{ item.point }}</td>
                            <td class="text-center">
                                <router-link :to="{name: 'edit', params: { id: item.id }}" class="btn btn-primary m-2 botao">Editar</router-link>
                                <button class="btn btn-danger m-2 botao" v-on:click="deleteItem(item)">Deletar</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p  v-if="items.length == 0">Nenum Item Criado...</p>
        </div>
    </div>

</template>
<script>

import axios from 'axios';

export default {
    name: 'IndexTeste',
    data() {
        return { items: [] }
    },
    created() {
        this.all();
    },
    methods: {
        deleteItem: function(item) {
            if (confirm('Delete ' + item.name)){ 
                axios.delete(`http://127.0.0.1:8000/items/${item.id}`).then(response => {
                    this.all();
                    return response;
                });
            }
        },
        all: function () { axios.get('http://127.0.0.1:8000/items/').then(response => {
                this.items = response.data
            });
        }
    },
}
</script>