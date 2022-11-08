---
type: web_development
date_created: Monday, November 7th 2022, 1:08:49 pm
date_modified: Tuesday, November 8th 2022, 5:30:19 pm
---
#nodejs #web/backend 

# About
Express is a lightweight backend js web framework.

# Snippets

## simple example

```node
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
```

