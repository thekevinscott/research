const BASE = ''

export async function fetchJSON<T>(path: string, opts?: RequestInit): Promise<T> {
  const res = await fetch(BASE + path, { credentials: 'include', ...opts })
  if (res.status === 401) throw new Error('unauthorized')
  if (!res.ok) throw new Error(`${res.status}: ${await res.text()}`)
  return res.json()
}

export interface GitHubUser {
  login: string
  avatar_url: string
  name: string
}

export interface Repo {
  full_name: string
  description: string
  language: string
  updated_at: string
  private: boolean
  html_url: string
}

export interface MachineSession {
  id: string
  app_name: string
  repo_name: string
  status: string
}

export function getMe(): Promise<GitHubUser> {
  return fetchJSON('/auth/me')
}

export function getRepos(): Promise<Repo[]> {
  return fetchJSON('/api/repos')
}

export function createSession(repoName: string): Promise<MachineSession> {
  return fetchJSON('/api/sessions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ repo_name: repoName }),
  })
}

export function getSessionOutput(sessionId: string): Promise<{ output: string }> {
  return fetchJSON(`/api/sessions/${sessionId}/output`)
}

export function sendSessionInput(sessionId: string, input: string): Promise<void> {
  return fetchJSON(`/api/sessions/${sessionId}/input`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ input }),
  })
}

export function destroySession(sessionId: string): Promise<void> {
  return fetchJSON(`/api/sessions/${sessionId}`, { method: 'DELETE' })
}
