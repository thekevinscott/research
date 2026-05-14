import { useState, useEffect, useRef } from 'react'
import { Repo, getSessionOutput, sendSessionInput } from '../api'
import { Session } from '../App'

interface Props {
  repo: Repo
  session: Session
}

export default function TerminalView({ repo, session }: Props) {
  const [output, setOutput] = useState('')
  const [input, setInput] = useState('')
  const [error, setError] = useState('')
  const outputRef = useRef<HTMLPreElement>(null)
  const intervalRef = useRef<number | null>(null)

  useEffect(() => {
    if (!session.machineSessionId) return

    const poll = () => {
      getSessionOutput(session.machineSessionId!)
        .then(data => {
          setOutput(data.output)
          setError('')
        })
        .catch(e => setError(e.message))
    }

    poll()
    intervalRef.current = window.setInterval(poll, 2000)

    return () => {
      if (intervalRef.current) clearInterval(intervalRef.current)
    }
  }, [session.machineSessionId])

  useEffect(() => {
    if (outputRef.current) {
      outputRef.current.scrollTop = outputRef.current.scrollHeight
    }
  }, [output])

  const send = () => {
    if (!input.trim() || !session.machineSessionId) return
    sendSessionInput(session.machineSessionId, input)
      .catch(e => setError(e.message))
    setInput('')
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      send()
    }
  }

  if (!session.machineSessionId) {
    return (
      <div className="terminal-view">
        <div className="terminal-header">
          <h2>{repo.full_name.split('/').pop()}</h2>
          <span className="terminal-status">Starting...</span>
        </div>
        <div className="terminal-loading">Launching Fly.io machine...</div>
      </div>
    )
  }

  return (
    <div className="terminal-view">
      <div className="terminal-header">
        <h2>{repo.full_name.split('/').pop()}</h2>
        <span className={`terminal-status terminal-status-${session.status}`}>
          {session.status}
        </span>
      </div>
      {error && <div className="terminal-error">{error}</div>}
      <pre ref={outputRef} className="terminal-output">{output || 'Waiting for output...'}</pre>
      <div className="terminal-input">
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type a command..."
        />
        <button onClick={send} disabled={!input.trim()}>Send</button>
      </div>
    </div>
  )
}
