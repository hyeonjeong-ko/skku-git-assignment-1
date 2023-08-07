
const express = require('express')

const app = express()

app.use(express.static("public"))

app.get('/', (req, res) => (
    res.send("안녕, 웹앱")
))

const server = require("http").createServer({}, app)

server.listen(3000, function(){
    console.log("HTTP를 포트 3000에 오픈합니다")
})