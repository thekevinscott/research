package main

import (
	"log"
	"net/http"
	"os"

	"github.com/agent-sandbox/api/handlers"
	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/joho/godotenv"
)

func main() {
	godotenv.Load()

	r := chi.NewRouter()
	r.Use(middleware.Logger)
	r.Use(corsMiddleware)

	r.Get("/auth/github", handlers.GitHubLogin)
	r.Get("/auth/callback", handlers.GitHubCallback)
	r.Get("/auth/dev", handlers.DevLogin)
	r.Get("/auth/me", handlers.Me)
	r.Get("/api/repos", handlers.ListRepos)
	r.Get("/api/repos/{owner}/{repo}/issues", handlers.ListIssues)
	r.Get("/api/sessions", handlers.ListSessions)
	r.Post("/api/sessions", handlers.CreateSession)
	r.Delete("/api/sessions/{id}", handlers.DestroySession)
	r.Post("/api/sessions/{id}/message", handlers.SendMessage)
	r.Get("/api/sessions/{id}/events", handlers.StreamEvents)
	r.Get("/api/sessions/{id}/health", handlers.ChannelHealth)

	port := os.Getenv("PORT")
	if port == "" {
		port = "9090"
	}
	addr := "0.0.0.0:" + port
	log.Printf("Blunderdome API listening on %s", addr)
	log.Fatal(http.ListenAndServe(addr, r))
}

func corsMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		origin := r.Header.Get("Origin")
		if origin == "" {
			origin = "http://localhost:9091"
		}
		w.Header().Set("Access-Control-Allow-Origin", origin)
		w.Header().Set("Access-Control-Allow-Credentials", "true")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type")
		if r.Method == "OPTIONS" {
			w.WriteHeader(http.StatusOK)
			return
		}
		next.ServeHTTP(w, r)
	})
}
