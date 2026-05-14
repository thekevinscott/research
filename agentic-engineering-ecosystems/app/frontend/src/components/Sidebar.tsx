import { useState } from 'react'
import { Repo, GitHubUser } from '../api'

export interface Session {
  id: string
  repoName: string
  createdAt: string
  status: 'active' | 'stopped' | 'done'
  preview: string
}

interface Props {
  repos: Repo[]
  selected: Repo | null
  onSelect: (repo: Repo) => void
  sessions: Session[]
  selectedSession: Session | null
  onSelectSession: (session: Session) => void
  onNewSession: (repo: Repo) => void
  user: GitHubUser
}

export default function Sidebar({
  repos,
  selected,
  onSelect,
  sessions,
  selectedSession,
  onSelectSession,
  onNewSession,
  user,
}: Props) {
  const [filter, setFilter] = useState('')

  const filtered = repos.filter(r =>
    r.full_name.toLowerCase().includes(filter.toLowerCase())
  )

  const repoSessions = (repoName: string) =>
    sessions.filter(s => s.repoName === repoName)

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <img src={user.avatar_url} alt="" width={20} height={20} />
        <span>{user.login}</span>
      </div>
      <input
        className="sidebar-search"
        type="text"
        placeholder="Search repos..."
        value={filter}
        onChange={e => setFilter(e.target.value)}
      />
      <div className="sidebar-list">
        {filtered.map(repo => {
          const isSelected = selected?.full_name === repo.full_name
          const repoSessionList = repoSessions(repo.full_name)
          return (
            <div key={repo.full_name}>
              <div
                className={`sidebar-item ${isSelected ? 'active' : ''}`}
                onClick={() => onSelect(repo)}
              >
                <span className="sidebar-item-name">
                  {repo.full_name.split('/').pop()}
                </span>
                {repo.language && (
                  <span className="sidebar-item-lang">{repo.language}</span>
                )}
              </div>
              {isSelected && (
                <div className="session-list">
                  {repoSessionList.map(session => (
                    <div
                      key={session.id}
                      className={`session-item ${selectedSession?.id === session.id ? 'active' : ''}`}
                      onClick={() => onSelectSession(session)}
                    >
                      <span className={`session-status session-status-${session.status}`} />
                      <span className="session-preview">{session.preview}</span>
                    </div>
                  ))}
                  <div
                    className="session-item session-new"
                    onClick={() => onNewSession(repo)}
                  >
                    + New session
                  </div>
                </div>
              )}
            </div>
          )
        })}
      </div>
    </aside>
  )
}
