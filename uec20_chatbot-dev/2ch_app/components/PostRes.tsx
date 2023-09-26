import React from 'react'
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { API_URL, getTime } from '@/const';
import axios from 'axios';


type Props = {
  dialogList: {
    username: string,
    text: string,
    others: string
  }[]
  setDialogList: React.Dispatch<React.SetStateAction<{
    username: string;
    text: string;
    others: string;
  }[]>>
}
const postStyle = { m: 2, mr: "auto", ml: "auto", width: "700px", height: "360px", borderRadius: "30px", backgroundColor: "white", p: 2 }


const PostRes = ({ dialogList, setDialogList }: Props) => {

  const [inputText, setInputText] = React.useState("")

  const Post = (text: string) => {

    console.log(text);
    const saveData = {
      username: "あなた",
      text: text,
      others: getTime()
    }
    setDialogList([...dialogList, saveData])

    //TODO POST通信を行い、setDialogListで内容を入れる
    axios.post(API_URL + "api/v1/nanj", {
      "query": text
    })
      .then(function (response: { data: any; }) {
        console.log(response.data);
        console.log(dialogList)
        setDialogList([...dialogList,saveData, {
          username: "nannJPT",
          text: response.data.reply,
          others: getTime()
        }])
      })
      .catch((error: any) => {
        console.log(error)
      })

  }

  return (
    <Box sx={postStyle}>
      <Typography variant="h5" sx={{ mb: 1, color: "rgb(63, 73, 94)" }}>
        レスを投稿する
      </Typography>
      <Typography variant="subtitle1" sx={{ mb: 1 }}>
        なんJPT(なんJのチャットボット)と会話してみよう！！！
      </Typography>
      <TextField
        id=""
        sx={{ width: "600px", mb: 1 }}
        multiline
        rows={7}
        defaultValue=""
        variant='outlined'
        onChange={(event) => setInputText(event.target.value)}
      />
      <Box>
        <Button variant="outlined" onClick={() => Post(inputText)}>投稿</Button>
      </Box>
    </Box>
  )
}

export default PostRes