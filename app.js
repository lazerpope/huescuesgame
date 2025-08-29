const express = require('express')
const cors = require('cors')
const path = require('path')

const app = express()
const PORT = 3000

app.use(cors({ origin: '*' }))
app.use(express.static('public'))

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'))
})

app.listen(PORT)