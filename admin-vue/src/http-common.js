import axios from "axios";

export const Axios = axios.create({
  baseURL: process.env.NODE_ENV === "production" ? "/api/v1/admin" : "http://localhost:5000/api/v1/admin/",
  headers: {
    post: {
      "Content-Type": "application/json"
    }
  }
});

export const AxiosApi = axios.create({
  baseURL: process.env.NODE_ENV === "production" ? "/api/v1/" : "http://localhost:5000/api/v1/",
  headers: {
    post: {
      "Content-Type": "application/json"
    }
  }
});

