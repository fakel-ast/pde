import axios from "axios";


let refreshRequest = null;

export const Axios = axios.create({
  baseURL: process.env.NODE_ENV === "production" ? "/api/v1/" : "http://localhost:5000/api/v1/",
  transformRequest: [
    function(data) {
      // Added csrf token in avery request
      const csrfToken = document.querySelector("[csrf-token]")?.getAttribute("csrf-token") || "11111111111";
      return JSON.stringify(Object.assign(data || {}, { "csrf-token": csrfToken }));
    }]
});


Axios.interceptors.request.use(config => {
    if (!localStorage.getItem("jwt")) {
      return config;
    }
    const newConfig = {
      headers: {},
      ...config
    };
    // Added Authorization in every request
    newConfig.headers.Authorization = `Bearer ${localStorage.getItem("jwt") || ""}`;
    return newConfig;
  }
);

Axios.interceptors.response.use(successResponse => successResponse, async error => {
  if (error?.response?.status !== 401 || error?.config?.retry) {
    throw error;
  }
  if (!refreshRequest) {
    // sending post request on refresh-token. Because of that refresh_token set in session. You mustn't send it.
    refreshRequest = Axios.post("users/refresh-token");
  }

  const { data } = await refreshRequest;

  localStorage.setItem("jwt", data.token);

  const newRequest = {
    ...error.config,
    retry: true
  };
  refreshRequest = null;
  return Axios(newRequest);

});
