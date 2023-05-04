// Utilities
import { defineStore } from 'pinia'
import axios from "axios"

export const useTrainStore = defineStore('train', {
  state: () => ({
    _trains: [] as string[],
    _trainSchedules: {} as any,
  }),
  getters: {
    trains       : state => state._trains,
    trainSchedules: state => state._trainSchedules
  },
  actions: {
    async loadTrains() {
      const url = `${import.meta.env.VITE_API_BASE_URL}/Scheduler/ids`
      const result = await axios.get(url)
      if (result.status === 200) {
        this._trains = result.data
      }
    },
    async loadTrainSchedule(trainId: string) {
      const url = `${import.meta.env.VITE_API_BASE_URL}/Scheduler/schedule/${trainId}`
      const result = await axios.get(url)
      if (result.status === 200) {
        this._trainSchedules[trainId] = result.data
      }
    }
  }
})