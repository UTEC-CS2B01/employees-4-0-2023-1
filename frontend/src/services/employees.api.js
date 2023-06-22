import axios from "axios";

const BASE_URL = "http://127.0.0.1:5004/employees";

export const createEmployee = async (employee) => {
  const { data } = await axios.post(BASE_URL, employee);

  return data;
};

export const getAllEmployees = async () => {
  const { data } = await axios.get(BASE_URL);

  return data;
};
