const fs = require('fs');
const readline = require('linebyline');
const {promisify} = require('util');
const {Client} = require('pg');

rl = readline('./dump.sql');
async function processLineByLine() {
    const connectionString = `postgres://drugbank:drugbank@localhost:5433/drugbank`
    const client = new Client({connectionString});
    await client.connect();

    rl.on('line', async function(line, lineCount, byteCount) {
        try{
            await client.query(line);
        } catch (e) {
            console.log(`error ${e} happened at line ${line}`)
        }
    })
}

processLineByLine().then(()=>{
    console.log("success");
})