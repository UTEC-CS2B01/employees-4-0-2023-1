import axios from "axios";

const BASE_URL = "http://127.0.0.1:5004/employees";

export const createEmployee = async (employee) => {
  const { data } = await axios.post(BASE_URL, employee);
  console.log("data: ", data);

  return data;
};

export const fetchEmployees = async () => {
  const { data } = await axios.get(BASE_URL);
  console.log("data: ", data);

  return data;
};
