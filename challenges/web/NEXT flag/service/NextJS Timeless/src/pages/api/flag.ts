// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'
import nookies from 'nookies'
type Data = {
  flag: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {

  if (!nookies.get({ req }).session || nookies.get({ req }).session !== 'ca65fb7e5a62cc4133ea9cb3a486f910') {
    res.status(200).json({ flag: 'Z2N0ZjIwMjN7ZmFrZV9mbGFnfQ==' })
  }else{
    res.status(200).json({ flag: 'GCTF2023{nExT_jS_1s_4w3s0m3}' })
  }
  
}
