<template>
    <div id="app">
        <div v-if="survivors && survivors.length">
            <div class="text-center m-4">
                <h1>Sobreviventes</h1>
            </div>
            <table class="table table-bordered mt-3">
                <thead>
                    <tr class="text-center">
                        <th scope="col">#</th>
                        <th scope="col">Id</th>
                        <th scope="col">Nome</th>
                        <th scope="col">Idade</th>
                        <th scope="col">Sexo</th>
                        <th scope="col">Latitude</th>
                        <th scope="col">Longitude</th>
                        <th scope="col">Nº de Sinalizações</th>
                        <th scope="col">Ações</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(survivor, index) in survivors" v-bind:key="survivor.id">
                        <td class="text-center">{{ index+1 }}</td>
                        <td class="text-center">{{ survivor.id }}</td>
                        <td class="text-center">{{ survivor.name }}</td>
                        <td class="text-center">{{ survivor.age }}</td>
                        <td class="text-center">{{ survivor.sex }}</td>
                        <td class="text-center">{{ survivor.latitude }}</td>
                        <td class="text-center">{{ survivor.longitude }}</td>
                        <td class="text-center">{{ survivor.reports }}</td>
                        <td class="text-center">
                            <router-link :to="{name: 'edit', params: { id: survivor.id }}" class="btn btn-primary m-2 botao">Editar</router-link>
                            <button class="btn btn-danger m-2 botao" v-on:click="deleteSurvivor(survivor)">Deletar</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <p  v-if="survivors.length == 0">Nenhum Sobrevivente Cadastrado...</p>
    </div>
    
</template>
<script>

import axios from 'axios';

export default {
    name: 'ListSurvivorTeste',
    data() {
        return { survivors: [] }
    },
    created() {
        this.all();
    },
    methods: {
        deleteSurvivor: function(survivor) {
            if (confirm('Delete ' + survivor.name)) {
                axios.delete(`http://127.0.0.1:8000/survivors/${survivor.id}`).then( response => {
                    this.all();
                    return response;
                });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/survivors/').then( response => {
                this.survivors = response.data;
            });
        }
    },
}
</script>