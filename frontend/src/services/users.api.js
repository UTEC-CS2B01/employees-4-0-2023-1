import axios from "axios";

const BASE_URL = "http://127.0.0.1:5004/users";

export const signUp = async (payload) => {
  const { data } = await axios.post(BASE_URL, payload);

  return data;
};
