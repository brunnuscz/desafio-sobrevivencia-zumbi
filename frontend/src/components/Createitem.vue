<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="text-center">
                <h2>Criar Item</h2>
            </div>
            <div class="container col-6">
                <div class="card p-3 mt-4">
                    <div class="form-group mt-3">
                        <label for="name">Nome:</label>
                        <input type="text" class="form-control" id="name" v-model="item.name" v-validate="'required'" name="name" placeholder="Digite o nome do item..." :class="{'is-invalid': errors.has('item.name') && submitted}">
                        <div class="invalid-feedback"> Porfavor digite um nome válido...</div>
                    </div>
                    <div class="form-group mt-3">
                        <label for="point">Pontos:</label>
                        <input type="number" class="form-control" id="name" v-model="item.point" v-validate="'required'" name="point" placeholder="Digite os pontos deste item..." :class="{'is-invalid': errors.has('item.point') && submitted}">
                        <div class="invalid-feedback"> Porfavor digite uma pontuação válida...</div>
                    </div>
                    <div class="text-center">
                        <button type="submit" class="btn btn-success mt-3">Criar</button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    name: 'CreateTeste',
    data() {
        return {
            item: {
                name: '',
                point: '',
            },
            submitted: false
        }
    },
    methods: {
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return e;
                }
                axios.post('http://127.0.0.1:8000/items/', this.item ).then(response => {
                    this.$router.push('/items/');
                    return response;
                });
            });
        }
    },
}
</script>