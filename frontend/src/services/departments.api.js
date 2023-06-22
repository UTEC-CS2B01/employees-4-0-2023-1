import axios from "axios";

const BASE_URL = "http://127.0.0.1:5004/departments";

export const createDepartment = async (department) => {
  const { data } = await axios.post(BASE_URL, department);

  return data;
};

export const getAllDepartments = async () => {
  const { data } = await axios.get(BASE_URL);

  return data;
};
