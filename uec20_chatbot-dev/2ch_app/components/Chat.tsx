import React from 'react'
import Box from '@mui/material/Box';
import DialogCard from './DialogCard';
import PostRes from './PostRes';
import { getTime } from '@/const';
import { type } from 'os';

type Props = {}
type TypeDialogList = {
    username: string,
    text: string,
    others: string
}[]


const Chat = (props: Props) => {
  const [dialogList, setDialogList] = React.useState<TypeDialogList>([])

  return (
    <Box
      sx={
        {
          backgroundColor: "rgb(240, 241, 246)",
          minHeight: "100vh",
          p: 2,
        }
      }>

      {
        dialogList.length > 0 ?
          dialogList.map((data, index) =>
            <DialogCard index={index + 1} username={data.username} text={data.text} others={data.others} key={index} />
          ) : <></>
      }
      {/* // TODO: テキスト入力欄 */}
      <Box sx={{ textAlign: 'center' }}>
        <PostRes dialogList={dialogList} setDialogList={setDialogList}></PostRes>
      </Box>
    </Box>

  )
}

export default Chat