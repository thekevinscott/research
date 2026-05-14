package handlers

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

func ListIssues(w http.ResponseWriter, r *http.Request) {
	token, err := getToken(r)
	if err != nil {
		http.Error(w, "unauthorized", http.StatusUnauthorized)
		return
	}

	owner := r.PathValue("owner")
	repo := r.PathValue("repo")
	if owner == "" || repo == "" {
		http.Error(w, "missing owner or repo", http.StatusBadRequest)
		return
	}

	url := fmt.Sprintf("https://api.github.com/repos/%s/%s/issues?sort=updated&direction=desc&per_page=30&state=open", owner, repo)
	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Set("Authorization", "Bearer "+token)
	req.Header.Set("Accept", "application/vnd.github.v3+json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		http.Error(w, "github api error", http.StatusBadGateway)
		return
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		body, _ := io.ReadAll(resp.Body)
		http.Error(w, string(body), resp.StatusCode)
		return
	}

	var issues []struct {
		Number    int    `json:"number"`
		Title     string `json:"title"`
		State     string `json:"state"`
		UpdatedAt string `json:"updated_at"`
		HTMLURL   string `json:"html_url"`
		User      struct {
			Login string `json:"login"`
		} `json:"user"`
		Labels []struct {
			Name  string `json:"name"`
			Color string `json:"color"`
		} `json:"labels"`
		PullRequest *struct{} `json:"pull_request"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&issues); err != nil {
		http.Error(w, "decode error", http.StatusInternalServerError)
		return
	}

	// Filter out pull requests (GitHub API returns PRs in issues endpoint)
	filtered := make([]interface{}, 0, len(issues))
	for _, issue := range issues {
		if issue.PullRequest != nil {
			continue
		}
		filtered = append(filtered, issue)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(filtered)
}
