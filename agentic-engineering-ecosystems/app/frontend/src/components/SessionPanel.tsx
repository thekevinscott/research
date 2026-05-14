import { MachineSession, GitHubIssue } from '../api'

interface Props {
  sessions: MachineSession[]
  selected: MachineSession | null
  onSelect: (session: MachineSession) => void
  onNew: () => void
  onClose: (session: MachineSession) => void
  repoSelected: boolean
  issues: GitHubIssue[]
  width: number
}

function timeAgo(dateStr: string): string {
  const diff = Date.now() - new Date(dateStr).getTime()
  const mins = Math.floor(diff / 60000)
  if (mins < 60) return `${mins}m`
  const hours = Math.floor(mins / 60)
  if (hours < 24) return `${hours}h`
  const days = Math.floor(hours / 24)
  return `${days}d`
}

export default function SessionPanel({ sessions, selected, onSelect, onNew, onClose, repoSelected, issues, width }: Props) {
  if (!repoSelected) {
    return (
      <aside className="panel panel-sessions" style={{ width }}>
        <div className="panel-header">Sessions</div>
        <div className="panel-empty">Select a repo</div>
      </aside>
    )
  }

  return (
    <aside className="panel panel-sessions" style={{ width }}>
      <div className="panel-header">
        <span>Sessions</span>
        <button className="panel-action" onClick={onNew}>+</button>
      </div>
      <div className="panel-list" style={{ flex: 1, overflow: 'hidden', display: 'flex', flexDirection: 'column' }}>
        <div style={{ overflowY: 'auto', flexShrink: 0 }}>
          {sessions.map(session => (
            <div
              key={session.id}
              className={`panel-item ${selected?.id === session.id ? 'active' : ''}`}
              onClick={() => onSelect(session)}
            >
              <span className={`session-dot session-dot-${session.state}`} />
              <span className="panel-item-name">{session.name || session.id}</span>
              <button
                className="session-close"
                onClick={(e) => { e.stopPropagation(); onClose(session) }}
                title="Close session"
              >x</button>
            </div>
          ))}
          {sessions.length === 0 && (
            <div className="panel-empty" style={{ padding: '0.75rem' }}>
              <button className="btn btn-sm" onClick={onNew}>New session</button>
            </div>
          )}
        </div>
        <div className="panel-divider" />
        <div className="panel-section-header">Issues</div>
        <div style={{ overflowY: 'auto', flex: 1 }}>
          {issues.map(issue => (
            <a
              key={issue.number}
              className="panel-item issue-item"
              href={issue.html_url}
              target="_blank"
              rel="noopener"
            >
              <span className="issue-number">#{issue.number}</span>
              <span className="panel-item-name">{issue.title}</span>
              <span className="panel-item-meta">{timeAgo(issue.updated_at)}</span>
            </a>
          ))}
          {issues.length === 0 && (
            <div className="panel-empty" style={{ padding: '0.75rem', flex: 'none' }}>No issues</div>
          )}
        </div>
      </div>
    </aside>
  )
}
