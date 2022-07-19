<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">

            <div class="form-group">
                <label for="costo">Costo Departamento</label>
                <input
                    type="number"
                    class="form-control"
                    id="costo"
                    v-model="departamento.costo"
                    v-validate="'required'"
                    name="costo"
                    placeholder="Ingres el costo"
                    :class="{'is-invalid': errors.has('departamento.costo') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid costo.
                </div>
            </div>

            <div class="form-group">
                <label for="numero_cuartos">Numero de Cuartos</label>
                <input
                    type="number"
                    class="form-control"
                    id="numero_cuartos"
                    v-model="departamento.numero_cuartos"
                    v-validate="'required'"
                    name="numero_cuartos"
                    placeholder="Ingres el numero de cuartos"
                    :class="{'is-invalid': errors.has('departamento.numero_cuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero cuartos.
                </div>
            </div>

            <div class="form-group">
                <label for="numero_banios">Numero de Baños</label>
                <input
                    type="number"
                    class="form-control"
                    id="numero_banios"
                    v-model="departamento.numero_banios"
                    v-validate="'required'"
                    name="numero_banios"
                    placeholder="Ingres el numero de baños"
                    :class="{'is-invalid': errors.has('departamento.numero_banios') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero baños.
                </div>
            </div>

            <div class="form-group">
                <label for="valor_alicuota">Valor Alicuota</label>
                <input
                    type="number"
                    class="form-control"
                    id="valor_alicuota"
                    v-model="departamento.valor_alicuota"
                    v-validate="'required'"
                    name="valor_alicuota"
                    placeholder="Ingrese el valor de Alicuota"
                    :class="{'is-invalid': errors.has('departamento.valor_alicuota') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid valor alicuota.
                </div>
            </div>

            <div class="form-group">
              <br>
                <label for="propietario">Propietario</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in propietariosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }} </option>
                        </select>
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Actualizar</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                costo: '',
                numero_cuartos: '',
                numero_banios: '',
                valor_alicuota: '',
                propietario: '',
            },
            propietariosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getPropietariosList(),
        axios.get('http://127.0.0.1:8000/api/numerost/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.departamento = response.data
        });
    },
    methods: {
      getPropietariosList() {
            axios
            .get('http://127.0.0.1:8000/api/propietario/')
            .then(response => {
                this.propietariosList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://127.0.0.1:8000/api/departamento/${this.departamento.id}/`,
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/departamentos');
                    })
            });
        }
    },
}
</script>
