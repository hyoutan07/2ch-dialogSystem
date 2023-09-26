export const getTime = () => {
  const now = new Date();
  const year = now.getFullYear();
  const month = ("0" + (now.getMonth() + 1)).slice(-2);
  const day = ("0" + now.getDate()).slice(-2);
  const hour = ("0" + now.getHours()).slice(-2);
  const minute = ("0" + now.getMinutes()).slice(-2);
  const second = ("0" + now.getSeconds()).slice(-2);
  const millisecond = ("00" + now.getMilliseconds()).slice(-3);
  const dayOfWeek = ["日", "月", "火", "水", "木", "金", "土"][now.getDay()];

  const formattedTime = `${year}/${month}/${day}(${dayOfWeek}) ${hour}:${minute}:${second}.${millisecond}`;
  return formattedTime;
}

export const API_URL = "http://localhost:8070/"