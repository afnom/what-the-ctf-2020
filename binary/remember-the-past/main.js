var express = require('express')
var app = express()

const { spawn } = require('child_process');

app.use(express.json())
app.use(express.urlencoded())

app.route('/')
  .get(function (req, res) {
    res.send('Try posting "code" to me...')
  })
  .post(function (req, res) {
    if (req.body.code) {
      let node = spawn('node', ['-e', 'console.log(' + req.body.code + ')'])
      node.stdout.on('data', (data) => {
        res.write(data.toString('utf-8'))
      })
      node.stderr.on('data', (data) => {
        res.write(data.toString('utf-8'))
      })
      node.on('close', () => {
        res.end()
      })
    }
  })

const port = 4000;
app.listen(port, () => {
  console.log(`app listening on port ${port}!`)
})
