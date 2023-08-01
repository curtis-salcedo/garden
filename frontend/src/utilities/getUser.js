import axios from 'axios';

export async function getUser() {
  try {
    const userResponse = await axios.get("http://localhost:8000/api/user/get");
    const loggedInUser = userResponse.data;
    // console.log(userResponse, loggedInUser)
    if (loggedInUser) {
      return loggedInUser;
    } else {
      return null;
    }
  } catch (error) {
    console.log(error);
    return null;
  }
}

