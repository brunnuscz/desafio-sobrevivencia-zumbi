<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="text-center">
                <h2>Editar Item</h2>
            </div>
            
            <div class="container col-6">
                <div class="card p-3 mt-4">
                    <div class="form-group mt-3">
                        <label for="name">Nome:</label>
                        <input type="text" class="form-control" id="name" v-model="item.name" v-validate="'required'" name="name" placeholder="Digite o nome do item..." :class="{'is-invalid': errors.has('item.name') && submitted}">
                        <div class="invalid-feedback"> Porfavor digite um nome válido... </div>
                    </div>
                    <div class="form-group mt-3">
                        <label for="point">Pontos:</label>
                        <input type="number" name="point" v-validate="'required'" class="form-control" id="point" v-model="item.point" placeholder="Digite os pontos deste item..." :class="{'is-invalid': errors.has('item.point') && submitted}">
                        <div class="invalid-feedback"> Porfavor digite uma pontuação válida... </div>
                    </div>
                    <div class="text-center mt-3">
                        <button type="submit" class="btn btn-success">Editar</button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'EditTeste',
    data() {
        return { 
            item: {
                name: '',
                point: '',
            }, 
            submitted: false,
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/items/' + this.$route.params.id) .then(response => {
            console.log(response.data);
            this.item = response.data;
        });
    },
    methods: {
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) { return e; }
                axios.put(`http://127.0.0.1:8000/items/${this.item.id}/`, this.item ).then(response => {
                    this.$router.push('/');
                    return response;
                });
            });
        }
    },
}
</script>