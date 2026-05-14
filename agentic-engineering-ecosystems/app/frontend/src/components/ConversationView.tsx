import { useState } from 'react'
import { Repo } from '../api'
import { Session } from '../App'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

interface Props {
  repo: Repo
  session: Session
}

export default function ConversationView({ repo, session }: Props) {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')

  const send = () => {
    if (!input.trim()) return
    setMessages(prev => [...prev, { role: 'user', content: input }])
    setInput('')
    // TODO: send to agent backend
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      send()
    }
  }

  return (
    <div className="conversation">
      <div className="conversation-header">
        <h2>{repo.full_name.split('/').pop()}</h2>
        <span className="conversation-desc">
          Session started {new Date(session.createdAt).toLocaleString()}
        </span>
      </div>
      <div className="conversation-messages">
        {messages.length === 0 && (
          <div className="empty-state">Send a message to start a session</div>
        )}
        {messages.map((msg, i) => (
          <div key={i} className={`message message-${msg.role}`}>
            <div className="message-content">{msg.content}</div>
          </div>
        ))}
      </div>
      <div className="conversation-input">
        <textarea
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={`Message about ${repo.full_name.split('/').pop()}...`}
          rows={3}
        />
        <button onClick={send} disabled={!input.trim()}>Send</button>
      </div>
    </div>
  )
}
