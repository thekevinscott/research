import { useState, useEffect, useRef } from 'react'
import { Repo, MachineSession, sendMessage } from '../api'

interface Message {
  role: 'user' | 'assistant' | 'system'
  content: string
  ts: number
}

interface Props {
  repo: Repo
  session: MachineSession
}

export default function ChatView({ repo, session }: Props) {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [sending, setSending] = useState(false)
  const [connected, setConnected] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const eventSourceRef = useRef<EventSource | null>(null)

  useEffect(() => {
    const es = new EventSource(`/api/sessions/${session.id}/events`)
    eventSourceRef.current = es

    es.onopen = () => setConnected(true)
    es.onerror = () => setConnected(false)

    es.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data)
        if (data.event === 'reply') {
          setMessages(prev => [...prev, {
            role: 'assistant',
            content: data.data.text,
            ts: data.ts,
          }])
          setSending(false)
        } else if (data.event === 'permission_request') {
          setMessages(prev => [...prev, {
            role: 'system',
            content: `Wants to run **${data.data.tool_name}**: ${data.data.description}\n\n\`${data.data.input_preview}\``,
            ts: data.ts,
          }])
        }
      } catch {}
    }

    return () => {
      es.close()
      eventSourceRef.current = null
    }
  }, [session.id])

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const send = async () => {
    const text = input.trim()
    if (!text) return

    setMessages(prev => [...prev, { role: 'user', content: text, ts: Date.now() }])
    setInput('')
    setSending(true)

    try {
      await sendMessage(session.id, text)
    } catch (e) {
      setMessages(prev => [...prev, {
        role: 'system',
        content: `Failed to send: ${e}`,
        ts: Date.now(),
      }])
      setSending(false)
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      send()
    }
  }

  const repoShort = repo.full_name.split('/').pop()

  return (
    <div className="chat-view">
      <div className="chat-header">
        <div className="chat-header-title">
          <span className="chat-header-icon">~</span>
          <h2>{repoShort}</h2>
        </div>
        <div className="chat-header-status">
          <span className={`status-dot ${connected ? 'connected' : 'disconnected'}`} />
          <span>{connected ? 'connected' : 'connecting...'}</span>
        </div>
      </div>

      <div className="chat-messages">
        {messages.length === 0 && (
          <div className="chat-empty">
            <div className="chat-empty-icon">*</div>
            <p>Welcome to the blunderdome.</p>
            <p className="chat-empty-hint">Type something. See what happens.</p>
          </div>
        )}
        {messages.map((msg, i) => (
          <div key={i} className={`chat-msg chat-msg-${msg.role}`}>
            <div className="chat-msg-label">
              {msg.role === 'user' ? 'you' : msg.role === 'assistant' ? 'agent' : 'sys'}
            </div>
            <div className="chat-msg-content">{msg.content}</div>
          </div>
        ))}
        {sending && (
          <div className="chat-msg chat-msg-thinking">
            <div className="chat-msg-label">agent</div>
            <div className="chat-msg-content thinking-dots">thinking</div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-area">
        <textarea
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={`say something to the agent...`}
          rows={2}
          disabled={sending}
        />
        <button onClick={send} disabled={!input.trim() || sending}>
          {sending ? '...' : 'go'}
        </button>
      </div>
    </div>
  )
}
