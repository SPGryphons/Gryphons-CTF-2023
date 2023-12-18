const { initializeApp } = require('firebase-admin/app');
const express = require("express")
const admin = require("firebase-admin")
const secrets = require("./secrets.json")
const serviceAccount = require("./gctf-firebase.json");
const crypt = require("./crypt")
const firebaseApp = initializeApp({
    credential: admin.credential.cert(serviceAccount)
})
const bodyParser = require("body-parser")
const messaging = admin.messaging()

const app = express()
app.use(bodyParser.json())

app.post("/sendAuthorizationToken", (req, res) => {
    // Measure to ensure only the device has the auth token
    const authToken = secrets.authorization
    const {token} = req.body
    if (!token) {
        return res.json({error: "No token provided!"})
    }
    messaging.send({
        data: {
            authToken,
            endpoint: ""
        }, token
    })
    res.send("Thank you!")
})

function getAuthorization(bearer) {
    if (bearer && bearer.startsWith("Bearer ")) {
        return bearer.substring(7)
    } else {
        return null
    }
}

app.post("/flag", (req, res) => {
    const authToken = secrets.authorization
    const bearerAuthorization = getAuthorization(req.headers["authorization"])
    if (authToken !== bearerAuthorization) {
        // not equal
        // reject
        return res.status(403).json({error: "Authorization Token invalid!"})
    }
    
    const {publicKey} = req.body
    const flag = secrets.flag
    const encryptedFlag = crypt.encryptStringWithRsaPublicKey(flag, publicKey)

    return res.send(String(encryptedFlag))

})


app.listen(10083, () => {
    console.log("Server active!")
})


// app.post("/flah")