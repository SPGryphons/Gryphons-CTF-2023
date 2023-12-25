import type { NextApiRequest, NextApiResponse } from 'next'
import {Md5} from 'ts-md5'
import nookies from 'nookies'
export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse
) {
    const data = req.body

    //md5 hash function
    const hash = (str: string) => {
        return Md5.hashStr(str)
    }

    if (!data.name || !data.password) {
        res.status(400).json({ error: 'Missing name or password' })
    }

    const name = "aaf2339fa6f2b21cc7027c894634e216"
    const password = "eb46bde69f955bf3723c8c9a1318b38e"


    if (hash(data.name) === name && hash(data.password) === password) {
        //set cookie session
        const session = hash(data.name + data.password)
        
        nookies.set({ res }, 'session', session, {
            maxAge: 30 * 24 * 60 * 60,
            path: '/',
        })

        res.status(200).json({ msg: 'Login Successful' })
    }else{
        res.status(401).json({ error: 'Invalid name or password' })
    }
}