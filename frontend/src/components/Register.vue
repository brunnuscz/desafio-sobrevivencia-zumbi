<template>
    <div class="pt-5">
        <form @submit.prevent="register" method="post">
            <div class="text-center">
                <h2>Cadastrar Sobrevivente</h2>
            </div>
            <div class="container card p-3 col-10">
                <!-- SOBREVIENTE -->
                <div class="card p-3 mt-4">
                    <div class="text-center">
                        <h2>Dados</h2>
                    </div>
                    <div class="row">
                        <!-- Nome -->
                        <div class="form-group col-8">
                            <label for="name">Nome:</label>
                            <input type="text" class="form-control" id="name" v-model="survivor.name" v-validate="'required'" name="name" :class="{'is-invalid': errors.has('survivor.name') && submitted}">
                            <div class="invalid-feedback"> Porfavor digite um nome válido...</div>
                        </div>
                        <!-- Idade -->
                        <div class="form-group col">
                            <label for="age">Idade:</label>
                            <input type="number" class="form-control" id="age" v-model="survivor.age" v-validate="'required'" name="age" :class="{'is-invalid': errors.has('survivor.age') && submitted}">
                            <div class="invalid-feedback"> Porfavor digite uma idade válida...</div>
                        </div>
                    </div>
                    <div class="row">
                        <!-- Sexo -->
                        <div class="form-group mt-3 col-4">
                            <label for="sex">Sexo:</label>
                            <select name="sex" class="form-control" v-validate="'required'" id="sex" v-model="survivor.sex" :class="{'is-invalid': errors.has('survivor.sex') && submited}">
                                <option value="M">Masculino</option>
                                <option value="F">Feminino</option>
                            </select>
                            <div class="invalid-feedback"> Porfavor selecione o sexo...</div>
                        </div>
                        <!-- Latitude -->
                        <div class="form-group mt-3 col-4">
                            <label for="latitude">Latitude:</label>
                            <input type="number" class="form-control" id="latitude" v-model="survivor.latitude" v-validate="'required'" name="latitude" :class="{'is-invalid': errors.has('survivor.latitude') && submitted}">
                            <div class="invalid-feedback"> Porfavor digite um valor válido...</div>
                        </div>
                        <!-- Longitude -->
                        <div class="form-group mt-3 col">
                            <label for="longitude">Longitude:</label>
                            <input type="number" class="form-control" id="longitude" v-model="survivor.longitude" v-validate="'required'" name="longitude" :class="{'is-invalid': errors.has('survivor.longitude') && submitted}">
                            <div class="invalid-feedback"> Porfavor digite um valor válido...</div>
                        </div>
                    </div>
                </div>
                <!-- FIM SOBREVIVENTE -->

                <!-- INVENTARIO -->
                <div class="card p-3 mt-4">
                    <div class="text-center mb-4">
                        <h2>Item do sobrevivente</h2>
                    </div>
                    <table class="table table-bordered">
                        <thead>
                            <tr class="text-center">
                                <th scope="row">#</th>
                                <th scope="col">Item</th>
                                <th scope="col">Pontos</th>
                                <th scope="col">Quantidade</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(item, index) in items" :key="item.id">
                                <td class="text-center">{{ index+1 }}</td>
                                <td class="text-center">{{ item.name }}</td>
                                <td class="text-center">{{ item.point }}</td>
                                <td class="text-center">
                                    <input class="center-align form-control" type="number" placeholder="Quantidade..." v-model="items[index].amount" >
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p  v-if="items.length == 0">Nenhum Item Criado...</p>
                </div>
                <!-- FIM INVENTARIO -->
                <div class="text-center">
                    <button type="submit" class="btn btn-success mt-3">Cadastrar</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    name: 'RegisterTeste',
    data() {
        return {
            survivors: [],
            survivor: {
                name: '',
                age: '',
                sex: '',
                latitude: '',
                longitude: '',
                inventory: []
            },
            items: [],
            inventory: [],
            submitted: false
        }
    },

    created() {
        this.all();
    },
    methods: {
        register: function (e) {
            this.items.forEach(item =>{
                if(parseInt(item.amount) > 0){
                    this.inventory.push({
                        id: item.id,
                        amount: parseInt(item.amount)
                    })
                }
            })
            this.survivor.inventory = this.inventory

            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return e;
                }
                axios.post('http://127.0.0.1:8000/survivors/', this.survivor ).then(response => {
                    this.$router.push('/survivors/');
                    return response;
                });
            });
        },
        all: function () { axios.get('http://127.0.0.1:8000/items/').then(response => {
                this.items = response.data
            });
        }
    },
}
</script>