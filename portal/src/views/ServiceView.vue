<template>

  <div class="flex justify-left">
    <div class="bg-stone-100 p-10 rounded-lg shadow-lg text-left relative">
      <h1 class="text-5xl font-bold text-gray-800 pb-16">Detalles del Servicio</h1>
      <div v-if="servicio">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <ul>
            <li>
              <h2 class="text-xl font-semibold">{{ servicio.nombre }}</h2>
            </li>
            <li>
              <p>{{ servicio.descripcion }}</p>
            </li>
            <li>
              <p>{{ servicio.tipo ? servicio.tipo.nombre : '' }}</p>
            </li>
            <li>
              <p class="mt-2">
                <span v-for="tag in servicio.palabras_claves" :key="tag"
                  class="mr-2 bg-[var(--blue-accent)] text-[var(--indigo-primary)] px-2 py-1 rounded-full">
                  {{ tag }}
                </span>
              </p>
            </li>
          </ul>
        </div>
      </div>
      <div v-else>
        <p>Cargando información del servicio...</p>
      </div>
      <div>
        <!-- Botón "Solicitar" -->
        <div v-if="user">
          <button type="button"
          class="absolute top-12 right-4 p-4 text-white bg-[var(--blue-primary)] rounded-full shadow-lg hover:bg-[var(--blue-secondary)]focus:outline-none">
            <router-link v-if="servicio" :to="{ name: 'request', params: { id: servicio.id } }">
              Solicitar
            </router-link>
          </button>
        </div>
        <div v-else>
          <button type="button"
            class="absolute top-12 right-4 p-4 text-white bg-[var(--blue-primary)] rounded-full shadow-lg hover:bg-[var(--blue-secondary)]focus:outline-none">
            <router-link :to="{ name: 'login' }">Solicitar</router-link>
          </button>
        </div>
      </div>
      <div v-if="errors.length">
        <p>Se produjo un error al cargar el servicio:</p>
        <ul>
          <li v-for="error in errors" :key="error">{{ error }}</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Detalle de la institucion -->
  <div class="flex justify-left">
    <div class="bg-stone-100 p-10 rounded-lg shadow-lg text-left mt-4">
      <h1 class="text-5xl font-bold text-gray-800 pb-16">Detalles de la institución del servicio</h1>
      <div v-if="servicio && servicio.institucion">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <ul>
            <li>
              <h2 class="text-xl font-semibold">{{ servicio.institucion.nombre }}</h2>
            </li>
            <li>
              <h2>{{ servicio.institucion.info }}</h2>
            </li>
            <li>
              <h2>{{ servicio.institucion.direccion }}</h2>
            </li>
          </ul>
        </div>
      </div>
      <div v-else>
        <p>Cargando institución...</p>
      </div>
    </div>

    <div ref="mapContainer" style="width: 400px; height: 400px"></div>





  </div>
</template>

<script>

import { onMounted,ref } from "vue";
import L from "leaflet"
import axios from 'axios';
import { useAuthStore } from '../stores/auth.store';

//const lat = ref(0);
//const lng = ref(0);

export default {
  data() {
    return {
      servicio: null,
      user: null,
      errors: [],
      map: null,
      mapContainer: null,
      marker:null
    };
  },
  mounted() {
 
    // Carga el servicio
    axios.get(``)
      .then(response => {
        this.servicio = response.data;
      })
      .catch(error => {
        this.errors.push(error);
      });

    // Obtiene el usuario
    this.user = useAuthStore().user;
  },
  watch: {
    servicio(newServicio) {
      this.mapContainer = this.$refs.mapContainer; // Referencia al contenedor del mapa

      if (newServicio.institucion) {
        this.map = L.map(this.mapContainer).setView([newServicio.institucion.latitud, newServicio.institucion.longitud], 16);
        L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }).addTo(this.map);
        if (this.marker) {
          this.marker.removeFrom(this.map); // elimino marcador previo
        }
        // el marcador que baje del back
        this.marker = L.marker([newServicio.institucion.latitud, newServicio.institucion.longitud])
          .addTo(this.map)
          .bindPopup(
            `<b>${newServicio.institucion.nombre}</b><br/>${newServicio.institucion.info}<br/>${newServicio.institucion.horario_atencion}`
          )

          

      }
    },
  },
};

</script>