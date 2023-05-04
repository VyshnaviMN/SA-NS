<template>
  <v-container>
    <v-row>
      <v-col cols="md-6">
        <v-select
          label        = "Train Id"
          variant      = "outlined"
          prepend-icon = "mdi-train"
          v-model      = "trainId"
          :items       = "trains"
          >
        </v-select>
      </v-col>
    </v-row>
    <v-table density="compact" fixed-header>
      <thead>
        <tr>
          <th colspan="2" class="font-weight-black">Schedule</th>
        </tr>
        <tr>
          <th>Station</th>
          <th>Time</th>
          <th v-if="trainSchedule.delay > 0">Delay</th>
          <th v-else>On Time</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for = "stationTime of trainSchedule.schedule" :key = "stationTime.station.id" >
          <td>{{ stationTime.station.id }}</td>
          <td>{{ new Date(stationTime.time * 1000) }}</td>
          <td v-if="trainSchedule.delay > 0"> + {{ trainSchedule.delay }} minute{{ trainSchedule.delay > 1 ? 's' : '' }}</td>
          <td v-else>On time</td>
        </tr>
      </tbody>
    </v-table>
  </v-container>
</template>

<script lang="ts">
import { mapActions, mapGetters } from 'pinia'
import { useTrainStore } from '@/store/train'

export default {
  data: () => ({
    trainId: null as unknown
  }),
  mounted() {
    if (this.$route.params.id) {
      this.trainId = this.$route.params.id
    }
  },
  computed: {
    ...mapGetters(useTrainStore, ['trains', 'trainSchedules']),
    trainIdInRouteParam() {
      return this.$route.params.id as string
    },
    trainSchedule() {
      let trainSchedule
      if (this.trainIdInRouteParam) {
        trainSchedule = this.trainSchedules[this.trainIdInRouteParam]
      }
      return trainSchedule
    }
  },
  methods: {
    ...mapActions(useTrainStore, ['loadTrainSchedule']),
  },
  watch: {
    trainId: {
      immediate: false,
      handler: function(newValue) {
        this.$router.push({
          name: "train-schedule",
          params: {
            id: newValue
          }
        })
      }
    }
  }
}
</script>
