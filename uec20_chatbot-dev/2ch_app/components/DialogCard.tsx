import React from 'react'
import Box from '@mui/material/Box';

type Props = {
  index: number,
  username: string,
  text: string,
  others: string,
}

const DialogCard = ({index, username, text, others }: Props) => {
  return (
    <Box sx={
      {
        width: "90%",
        backgroundColor: "rgba(237, 237, 237)",
        m: 1,
        p: 1,
        boxShadow: "1px 1px 1px gray",
      }
    }>
      <Box sx={{display: 'flex'}}>
        <Box sx={{fontSize: "1.0em", mr:1}}>
          {index}
        </Box>
        <Box sx={{color: index%2==0?"blue":"green", fontSize: "1.0em", mr:1}}>
          {username}
        </Box>
        <Box sx={{fontSize: "1.0em"}}>
          {others}
        </Box>
      </Box>
      <Box sx={{fontSize: "1.2em", mt:1, mb:1}}>
        {text}
      </Box>
    </Box>
  )
}

export default DialogCard