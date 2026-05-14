import { useState, useEffect } from 'react'
import { getMe, getRepos, createSession, GitHubUser, Repo } from './api'
import Login from './components/Login'
import RepoPanel from './components/RepoPanel'
import SessionPanel from './components/SessionPanel'
import TerminalView from './components/TerminalView'

export interface Session {
  id: string
  repoName: string
  createdAt: string
  status: 'active' | 'stopped' | 'done'
  preview: string
  machineSessionId?: string
}

let nextSessionId = 1

export default function App() {
  const [user, setUser] = useState<GitHubUser | null>(null)
  const [repos, setRepos] = useState<Repo[]>([])
  const [selectedRepo, setSelectedRepo] = useState<Repo | null>(null)
  const [sessions, setSessions] = useState<Session[]>([])
  const [selectedSession, setSelectedSession] = useState<Session | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getMe()
      .then(u => {
        setUser(u)
        return getRepos()
      })
      .then(setRepos)
      .catch(() => setUser(null))
      .finally(() => setLoading(false))
  }, [])

  const handleSelectRepo = (repo: Repo) => {
    setSelectedRepo(repo)
    const repoSessions = sessions.filter(s => s.repoName === repo.full_name)
    if (repoSessions.length > 0) {
      setSelectedSession(repoSessions[0])
    } else {
      setSelectedSession(null)
    }
  }

  const handleNewSession = async () => {
    if (!selectedRepo) return
    const localId = String(nextSessionId++)
    const session: Session = {
      id: localId,
      repoName: selectedRepo.full_name,
      createdAt: new Date().toISOString(),
      status: 'active',
      preview: 'Starting...',
    }
    setSessions(prev => [session, ...prev])
    setSelectedSession(session)

    try {
      const machineSession = await createSession(selectedRepo.full_name)
      setSessions(prev =>
        prev.map(s =>
          s.id === localId
            ? { ...s, machineSessionId: machineSession.id, preview: 'Claude session' }
            : s
        )
      )
      setSelectedSession(prev =>
        prev?.id === localId
          ? { ...prev, machineSessionId: machineSession.id, preview: 'Claude session' }
          : prev
      )
    } catch (e) {
      setSessions(prev =>
        prev.map(s =>
          s.id === localId
            ? { ...s, status: 'done', preview: `Error: ${e}` }
            : s
        )
      )
    }
  }

  if (loading) return <div className="container">Loading...</div>
  if (!user) return <div className="container"><Login /></div>

  const repoSessions = selectedRepo
    ? sessions.filter(s => s.repoName === selectedRepo.full_name)
    : []

  return (
    <div className="layout">
      <RepoPanel
        repos={repos}
        selected={selectedRepo}
        onSelect={handleSelectRepo}
        user={user}
      />
      <SessionPanel
        sessions={repoSessions}
        selected={selectedSession}
        onSelect={setSelectedSession}
        onNew={handleNewSession}
        repoSelected={!!selectedRepo}
      />
      <main className="main-pane">
        {selectedSession ? (
          <TerminalView repo={selectedRepo!} session={selectedSession} />
        ) : (
          <div className="empty-state">
            {selectedRepo ? 'Start a session' : 'Select a repo'}
          </div>
        )}
      </main>
      <aside className="right-panel" />
    </div>
  )
}
