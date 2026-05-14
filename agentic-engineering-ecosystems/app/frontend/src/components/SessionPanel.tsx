import { Session } from '../App'

interface Props {
  sessions: Session[]
  selected: Session | null
  onSelect: (session: Session) => void
  onNew: () => void
  repoSelected: boolean
}

export default function SessionPanel({ sessions, selected, onSelect, onNew, repoSelected }: Props) {
  if (!repoSelected) {
    return (
      <aside className="panel panel-sessions">
        <div className="panel-header">Sessions</div>
        <div className="panel-empty">Select a repo</div>
      </aside>
    )
  }

  return (
    <aside className="panel panel-sessions">
      <div className="panel-header">
        <span>Sessions</span>
        <button className="panel-action" onClick={onNew}>+</button>
      </div>
      <div className="panel-list">
        {sessions.map(session => (
          <div
            key={session.id}
            className={`panel-item ${selected?.id === session.id ? 'active' : ''}`}
            onClick={() => onSelect(session)}
          >
            <span className={`session-dot session-dot-${session.status}`} />
            <span className="panel-item-name">{session.preview}</span>
            <span className="panel-item-meta">
              {new Date(session.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
            </span>
          </div>
        ))}
        {sessions.length === 0 && (
          <div className="panel-empty">
            <button className="btn btn-sm" onClick={onNew}>New session</button>
          </div>
        )}
      </div>
    </aside>
  )
}
