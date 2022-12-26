const assert = require('assert')

function isValid(stale, latest, otjson) {
    ot_ops = JSON.parse(otjson)
    let s_cursor = 0
    let t_cursor = 0

    function match(s, s_start, s_end, t, t_start, t_end) {
        if (s.substring(s_start, s_end) === t.substring(t_start, t_end))
            return true
        return false
    }

    for (let ot of ot_ops) {
        if (ot.op === 'skip') {
            if (s_cursor + ot.count > stale.length) return false
            if (t_cursor + ot.count > latest.length) return false
            if (!match(stale, s_cursor, s_cursor + ot.count, latest, t_cursor, t_cursor + ot.count)) return false
            s_cursor += ot.count
            t_cursor += ot.count
        } else if (ot.op === 'delete') {
            if (s_cursor + ot.count > stale.length) return false
            s_cursor += ot.count
        } else if (ot.op === 'insert') {
            if (t_cursor + ot.chars.length > latest.length) return false
            if (!match(ot.chars, 0, ot.chars.length, latest, t_cursor, t_cursor + ot.chars.length)) return false
            t_cursor += ot.chars.length
        }
    }
    if (!match(stale, s_cursor, stale.length, latest, t_cursor, latest.length)) return false
    return true
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
