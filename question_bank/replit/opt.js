const assert = require('assert')

function isValid(stale, latest, otjson) {
    ot_ops = JSON.parse(otjson)

    let transform = ""
    let start = 0
    let end = 0
    console.log(stale, stale.length, otjson)

    for (let ot of ot_ops) {         
        if (ot.op === 'skip') {
            end += ot.count

            if (end > stale.length) return false

            transform += stale.substring(start, end)
            start += ot.count

            console.log('skip', end)
        } else if (ot.op === 'delete') {
            end += ot.count

            console.log('delete', end)
            if (end > stale.length) return false

            start += ot.count
        } else if (ot.op === 'insert') {
            transform += ot.chars
        }
    }

    transform += stale.substring(start, stale.length)

    if (transform.length === latest.length) {
        return true
    }

    return false
}


assert(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]'
  ) === true)
  

assert(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]'
  ) === false)
  
assert(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]'
  ) === false) // skip past end
  
assert(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'We use operational transformations to keep everyone in a multiplayer repl in sync.',
    '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
  ) === true)
    
assert(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'We can use operational transformations to keep everyone in a multiplayer repl in sync.',
    '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
  ) === false)
  
assert(isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    '[]'
  ) === true)
