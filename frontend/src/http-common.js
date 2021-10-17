import axios from "axios";

export const Axios = axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? '' : 'http://localhost:8000/api/',
  headers: {
    post: {
      'Content-Type': 'application/json'
    }
  },
  transformRequest: [function (data) {
    return JSON.stringify(Object.assign(data || {}, {'csrf-token': '11'}))
  }]
})