const express = require("express")
const bodyParser = require("body-parser")
var fs = require("fs-extra");
const { randomUUID } = require("crypto");
const nodeChildProcess = require('node:child_process')
const app = express()

app.post("/", async (req, res) => {
    const {code} = req.body
    // code is the C++ code.
    const uu = randomUUID()
    const path = `/tmp/wokwi-${uu}`
    await fs.copy("./project", path)
    await fs.remove(`${path}/project/src/main.cpp`)
    await fs.writeFile(`${path}/project/src/main.cpp`, code)
    let childProcess
    try {
        childProcess = nodeChildProcess.execSync("cd ../project && pio run")
    } catch(err) {
        // failed compilation
        return res.json({error: "Failed compilation", details: err})
    }


    const verification = nodeChildProcess.exec("cd ../project && wokwi-cli . --scenario fv2.yml")
    if (verification.exitCode != 0) {
        // failed
        res.json({error: "Failed verification", details: err})
    } else {
        res.json({success: true, flag: "GCTF23{L0G1C_GAT3S_n_Fl1p_Fl0ps}"})
    }
    
})