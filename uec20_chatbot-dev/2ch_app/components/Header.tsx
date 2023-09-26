import React from 'react'
import Box from '@mui/material/Box';
import Image from 'next/image'

type Props = {}

const Header = (props: Props) => {
  return (
    <Box
      sx=
      {{
        backgroundColor: "rgb(248, 248, 248)",
        height: "80px",
        p:1,
      }}
    >
      <Box sx={{width: 200}}>
        <Image src={'/5ch_logo.png'} alt={''} width={200} height={100}/>
      </Box>
    </Box>
  )
}

export default Header