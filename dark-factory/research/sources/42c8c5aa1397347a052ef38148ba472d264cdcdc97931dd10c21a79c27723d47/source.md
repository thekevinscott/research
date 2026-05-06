Agentic Data Engineering with Genie Code and Lakeflow | Databricks Blog

[Skip to main content](#main "#main")

[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMyIiBoZWlnaHQ9IjIyIiB2aWV3Qm94PSIwIDAgMTMyIDIyIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Im0xOC4zMTggOS4yNzUtOC42MzEgNC44NTlMLjQ0NSA4Ljk0MiAwIDkuMTgydjMuNzdsOS42ODcgNS40MzEgOC42My00Ljg0djEuOTk1bC04LjYzIDQuODYtOS4yNDItNS4xOTItLjQ0NS4yNHYuNjQ2bDkuNjg3IDUuNDMyIDkuNjY4LTUuNDMydi0zLjc2OWwtLjQ0NS0uMjQtOS4yMjMgNS4xNzMtOC42NS00Ljg0VjEwLjQybDguNjUgNC44NCA5LjY2OC01LjQzVjYuMTE0bC0uNDgyLS4yNzctOS4xODYgNS4xNTVMMS40ODIgNi40MWw4LjIwNS00LjYgNi43NDEgMy43ODcuNTkzLS4zMzJ2LS40NjJMOS42ODcuNjg0IDAgNi4xMTV2LjU5Mmw5LjY4NyA1LjQzMiA4LjYzLTQuODZ6IiBmaWxsPSIjRUUzRDJDIi8+PHBhdGggZD0iTTM3LjQ0OSAxOC40NDNWMS44NTJoLTIuNTU2djYuMjA3YzAgLjA5My0uMDU2LjE2Ny0uMTQ4LjIwNGEuMjMuMjMgMCAwIDEtLjI0LS4wNTZjLS44NzEtMS4wMTYtMi4yMjMtMS41ODktMy43MDUtMS41ODktMy4xNjcgMC01LjY1IDIuNjYtNS42NSA2LjA2IDAgMS42NjMuNTc1IDMuMTk3IDEuNjMgNC4zMjRhNS40NCA1LjQ0IDAgMCAwIDQuMDIgMS43MzZjMS40NjMgMCAyLjgxNS0uNjEgMy43MDQtMS42NjIuMDU2LS4wNzQuMTY3LS4wOTMuMjQtLjA3NC4wOTMuMDM3LjE1LjExLjE1LjIwM3YxLjIzOHptLTYuMDkzLTIuMDE0Yy0yLjAzOCAwLTMuNjMtMS42NDQtMy42My0zLjc1IDAtMi4xMDcgMS41OTItMy43NTEgMy42My0zLjc1MXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NW0xOS43NjIgMi4wMTZWNi44OTZoLTIuNTM3VjguMDZjMCAuMDkzLS4wNTYuMTY2LS4xNDkuMjAzYS4yLjIgMCAwIDEtLjI0LS4wNzNjLS44NTItMS4wMTctMi4xODYtMS41OS0zLjcwNS0xLjU5LTMuMTY3IDAtNS42NDkgMi42NjEtNS42NDkgNi4wNiAwIDMuNCAyLjQ4MiA2LjA2IDUuNjUgNi4wNiAxLjQ2MyAwIDIuODE1LS42MSAzLjcwNC0xLjY4LjA1NS0uMDc1LjE2Ni0uMDkzLjI0LS4wNzUuMDkzLjAzNy4xNDkuMTExLjE0OS4yMDR2MS4yNTZoMi41Mzd6bS02LjA1Ni0yLjAxNGMtMi4wMzggMC0zLjYzLTEuNjQ1LTMuNjMtMy43NSAwLTIuMTA3IDEuNTkyLTMuNzUxIDMuNjMtMy43NTFzMy42MyAxLjY0NCAzLjYzIDMuNzUtMS41OTMgMy43NS0zLjYzIDMuNzVtMjcuNzgxIDIuMDE1VjYuODk2aC0yLjUzOFY4LjA2YzAgLjA5My0uMDU1LjE2Ni0uMTQ4LjIwM3MtLjE4NSAwLS4yNC0uMDczYy0uODUzLTEuMDE3LTIuMTg2LTEuNTktMy43MDUtMS41OS0zLjE4NiAwLTUuNjQ5IDIuNjYxLTUuNjQ5IDYuMDggMCAzLjQxNyAyLjQ4MiA2LjA2IDUuNjQ5IDYuMDYgMS40NjMgMCAyLjgxNS0uNjEgMy43MDQtMS42ODIuMDU2LS4wNzQuMTY3LS4wOTMuMjQxLS4wNzQuMDkzLjAzNy4xNDguMTEuMTQ4LjIwM3YxLjI1NnptLTYuMDU3LTIuMDE0Yy0yLjAzNyAwLTMuNjMtMS42NDUtMy42My0zLjc1IDAtMi4xMDcgMS41OTMtMy43NTEgMy42My0zLjc1MXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NW0xMC43MDYuNjQ3Yy4wMTkgMCAuMDU2LS4wMTkuMDc0LS4wMTkuMDU2IDAgLjEzLjAzNy4xNjcuMDc0Ljg3IDEuMDE2IDIuMjIyIDEuNTg5IDMuNzA0IDEuNTg5IDMuMTY3IDAgNS42NS0yLjY2IDUuNjUtNi4wNiAwLTEuNjYzLS41NzUtMy4xOTYtMS42My00LjMyM2E1LjQ0IDUuNDQgMCAwIDAtNC4wMi0xLjczN2MtMS40NjMgMC0yLjgxNS42MS0zLjcwNCAxLjY2My0uMDU2LjA3NC0uMTQ4LjA5Mi0uMjQuMDc0LS4wOTMtLjAzNy0uMTQ5LS4xMTEtLjE0OS0uMjA0VjEuODUyaC0yLjU1NnYxNi41OWgyLjU1NlYxNy4yOGMwLS4wOTMuMDU2LS4xNjYuMTQ4LS4yMDNtLS4yNi00LjM5OGMwLTIuMTA2IDEuNTk0LTMuNzUgMy42MzEtMy43NXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NS0zLjYzLTEuNjYyLTMuNjMtMy43NW0xNy4yNDQtMy40MTZjLjI0IDAgLjQ2My4wMTkuNjEuMDU2VjYuNjk1YTIuNCAyLjQgMCAwIDAtLjQyNS0uMDM3Yy0xLjMzNCAwLTIuNTU2LjY4NC0zLjIwNCAxLjc3NC0uMDU2LjA5Mi0uMTQ5LjEzLS4yNDEuMDkyYS4yMi4yMiAwIDAgMS0uMTY3LS4yMDNWNi44OThoLTIuNTM3djExLjU2NmgyLjU1NnYtNS4xYzAtMi41MyAxLjI5Ni00LjEgMy40MDgtNC4xbTQuODE1LTIuMzY3aC0yLjU5M3YxMS41NjZoMi41OTN6TTk3Ljk1OCAxLjg3YTEuNTcxIDEuNTcxIDAgMSAwIDAgMy4xNDEgMS41NzEgMS41NzEgMCAxIDAgMC0zLjE0bTguOTI4IDQuNzI5Yy0zLjU1NiAwLTYuMTMxIDIuNTUtNi4xMzEgNi4wOCAwIDEuNzE3LjYxMiAzLjI1IDEuNzA0IDQuMzYgMS4xMTIgMS4xMDggMi42NjcgMS43MTggNC40MDggMS43MTggMS40NDUgMCAyLjU1Ni0uMjc3IDQuNjY4LTEuODNsLTEuNDYzLTEuNTMzYy0xLjAzOC42ODQtMi4wMDEgMS4wMTYtMi45NDUgMS4wMTYtMi4xNDkgMC0zLjc2LTEuNjA3LTMuNzYtMy43MzJzMS42MTEtMy43MzIgMy43Ni0zLjczMmMxLjAxOCAwIDEuOTYzLjMzMyAyLjkwOCAxLjAxNmwxLjYyOS0xLjUzM2MtMS45MDctMS42MjYtMy42My0xLjgzLTQuNzc4LTEuODNtOS4xNDkgNi43NjJhLjIuMiAwIDAgMSAuMTQ5LS4wNTVoLjAxOGMuMDU2IDAgLjExMS4wMzcuMTY3LjA3M2w0LjA5MyA1LjA2M2gzLjE0OWwtNS4yOTctNi4zOTNjLS4wNzUtLjA5Mi0uMDc1LS4yMjIuMDE4LS4yOTVsNC44NzEtNC44NmgtMy4xM2wtNC4yMDQgNC4yMTNjLS4wNTYuMDU1LS4xNDguMDc0LS4yNDEuMDU1YS4yMy4yMyAwIDAgMS0uMTMtLjIwM1YxLjg3aC0yLjU3NHYxNi41OTFoMi41NTZ2LTQuNTA4YzAtLjA1NS4wMTgtLjEzLjA3NC0uMTY2eiIgZmlsbD0iIzAwMCIvPjxwYXRoIGQ9Ik0xMjcuNzc2IDE4LjczOWMyLjA5MyAwIDQuMjIzLTEuMjc1IDQuMjIzLTMuNjk1IDAtMS41ODktMS0yLjY4LTMuMDM3LTMuMzQ0bC0xLjM5LS40NjJjLS45NDQtLjMxNC0xLjM4OS0uNzU4LTEuMzg5LTEuMzY3IDAtLjcwMi42My0xLjE4MyAxLjUxOS0xLjE4My44NTIgMCAxLjYxMS41NTUgMi4wOTMgMS41MTVsMi4wNTYtMS4xMDhjLS43NTktMS41NTItMi4zMzQtMi41MTMtNC4xNDktMi41MTMtMi4yOTcgMC0zLjk2MyAxLjQ3OC0zLjk2MyAzLjQ5MiAwIDEuNjA3Ljk2MyAyLjY3OSAyLjk0NCAzLjMwN2wxLjQyNy40NjJjMSAuMzE0IDEuNDI2LjcyIDEuNDI2IDEuMzY3IDAgLjk4LS45MDggMS4zMy0xLjY4NiAxLjMzLTEuMDM3IDAtMS45NjMtLjY2NS0yLjQwNy0xLjc1NWwtMi4wOTMgMS4xMDljLjY4NSAxLjc1NSAyLjM3IDIuODQ1IDQuNDI2IDIuODQ1bS02OS41NDYtLjExMWMuODE1IDAgMS41MzgtLjA3NCAxLjk0NS0uMTN2LTIuMjE2YTE0IDE0IDAgMCAxLTEuMjc4LjA3M2MtMS4wMzcgMC0xLjgzMy0uMTg0LTEuODMzLTIuNDJWOS4xODdjMC0uMTMuMDkyLS4yMjIuMjIyLS4yMjJoMi41VjYuODc3aC0yLjVhLjIxNC4yMTQgMCAwIDEtLjIyMi0uMjIxVjMuMzNoLTIuNTU2djMuMzQ0YzAgLjEzLS4wOTMuMjIyLS4yMjMuMjIyaC0xLjc3OHYyLjA4OGgxLjc3OGMuMTMgMCAuMjIzLjA5Mi4yMjMuMjIxdjUuMzc3YzAgNC4wNDYgMi43MDQgNC4wNDYgMy43MjIgNC4wNDYiIGZpbGw9IiMwMDAiLz48L3N2Zz4=)](/ "/")

[Login](https://login.databricks.com/?dbx_source=www&itm=main-cta-login&l=en-EN "https://login.databricks.com/?dbx_source=www&itm=main-cta-login&l=en-EN")

[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMyIiBoZWlnaHQ9IjIyIiB2aWV3Qm94PSIwIDAgMTMyIDIyIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Im0xOC4zMTggOS4yNzUtOC42MzEgNC44NTlMLjQ0NSA4Ljk0MiAwIDkuMTgydjMuNzdsOS42ODcgNS40MzEgOC42My00Ljg0djEuOTk1bC04LjYzIDQuODYtOS4yNDItNS4xOTItLjQ0NS4yNHYuNjQ2bDkuNjg3IDUuNDMyIDkuNjY4LTUuNDMydi0zLjc2OWwtLjQ0NS0uMjQtOS4yMjMgNS4xNzMtOC42NS00Ljg0VjEwLjQybDguNjUgNC44NCA5LjY2OC01LjQzVjYuMTE0bC0uNDgyLS4yNzctOS4xODYgNS4xNTVMMS40ODIgNi40MWw4LjIwNS00LjYgNi43NDEgMy43ODcuNTkzLS4zMzJ2LS40NjJMOS42ODcuNjg0IDAgNi4xMTV2LjU5Mmw5LjY4NyA1LjQzMiA4LjYzLTQuODZ6IiBmaWxsPSIjRUUzRDJDIi8+PHBhdGggZD0iTTM3LjQ0OSAxOC40NDNWMS44NTJoLTIuNTU2djYuMjA3YzAgLjA5My0uMDU2LjE2Ny0uMTQ4LjIwNGEuMjMuMjMgMCAwIDEtLjI0LS4wNTZjLS44NzEtMS4wMTYtMi4yMjMtMS41ODktMy43MDUtMS41ODktMy4xNjcgMC01LjY1IDIuNjYtNS42NSA2LjA2IDAgMS42NjMuNTc1IDMuMTk3IDEuNjMgNC4zMjRhNS40NCA1LjQ0IDAgMCAwIDQuMDIgMS43MzZjMS40NjMgMCAyLjgxNS0uNjEgMy43MDQtMS42NjIuMDU2LS4wNzQuMTY3LS4wOTMuMjQtLjA3NC4wOTMuMDM3LjE1LjExLjE1LjIwM3YxLjIzOHptLTYuMDkzLTIuMDE0Yy0yLjAzOCAwLTMuNjMtMS42NDQtMy42My0zLjc1IDAtMi4xMDcgMS41OTItMy43NTEgMy42My0zLjc1MXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NW0xOS43NjIgMi4wMTZWNi44OTZoLTIuNTM3VjguMDZjMCAuMDkzLS4wNTYuMTY2LS4xNDkuMjAzYS4yLjIgMCAwIDEtLjI0LS4wNzNjLS44NTItMS4wMTctMi4xODYtMS41OS0zLjcwNS0xLjU5LTMuMTY3IDAtNS42NDkgMi42NjEtNS42NDkgNi4wNiAwIDMuNCAyLjQ4MiA2LjA2IDUuNjUgNi4wNiAxLjQ2MyAwIDIuODE1LS42MSAzLjcwNC0xLjY4LjA1NS0uMDc1LjE2Ni0uMDkzLjI0LS4wNzUuMDkzLjAzNy4xNDkuMTExLjE0OS4yMDR2MS4yNTZoMi41Mzd6bS02LjA1Ni0yLjAxNGMtMi4wMzggMC0zLjYzLTEuNjQ1LTMuNjMtMy43NSAwLTIuMTA3IDEuNTkyLTMuNzUxIDMuNjMtMy43NTFzMy42MyAxLjY0NCAzLjYzIDMuNzUtMS41OTMgMy43NS0zLjYzIDMuNzVtMjcuNzgxIDIuMDE1VjYuODk2aC0yLjUzOFY4LjA2YzAgLjA5My0uMDU1LjE2Ni0uMTQ4LjIwM3MtLjE4NSAwLS4yNC0uMDczYy0uODUzLTEuMDE3LTIuMTg2LTEuNTktMy43MDUtMS41OS0zLjE4NiAwLTUuNjQ5IDIuNjYxLTUuNjQ5IDYuMDggMCAzLjQxNyAyLjQ4MiA2LjA2IDUuNjQ5IDYuMDYgMS40NjMgMCAyLjgxNS0uNjEgMy43MDQtMS42ODIuMDU2LS4wNzQuMTY3LS4wOTMuMjQxLS4wNzQuMDkzLjAzNy4xNDguMTEuMTQ4LjIwM3YxLjI1NnptLTYuMDU3LTIuMDE0Yy0yLjAzNyAwLTMuNjMtMS42NDUtMy42My0zLjc1IDAtMi4xMDcgMS41OTMtMy43NTEgMy42My0zLjc1MXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NW0xMC43MDYuNjQ3Yy4wMTkgMCAuMDU2LS4wMTkuMDc0LS4wMTkuMDU2IDAgLjEzLjAzNy4xNjcuMDc0Ljg3IDEuMDE2IDIuMjIyIDEuNTg5IDMuNzA0IDEuNTg5IDMuMTY3IDAgNS42NS0yLjY2IDUuNjUtNi4wNiAwLTEuNjYzLS41NzUtMy4xOTYtMS42My00LjMyM2E1LjQ0IDUuNDQgMCAwIDAtNC4wMi0xLjczN2MtMS40NjMgMC0yLjgxNS42MS0zLjcwNCAxLjY2My0uMDU2LjA3NC0uMTQ4LjA5Mi0uMjQuMDc0LS4wOTMtLjAzNy0uMTQ5LS4xMTEtLjE0OS0uMjA0VjEuODUyaC0yLjU1NnYxNi41OWgyLjU1NlYxNy4yOGMwLS4wOTMuMDU2LS4xNjYuMTQ4LS4yMDNtLS4yNi00LjM5OGMwLTIuMTA2IDEuNTk0LTMuNzUgMy42MzEtMy43NXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NS0zLjYzLTEuNjYyLTMuNjMtMy43NW0xNy4yNDQtMy40MTZjLjI0IDAgLjQ2My4wMTkuNjEuMDU2VjYuNjk1YTIuNCAyLjQgMCAwIDAtLjQyNS0uMDM3Yy0xLjMzNCAwLTIuNTU2LjY4NC0zLjIwNCAxLjc3NC0uMDU2LjA5Mi0uMTQ5LjEzLS4yNDEuMDkyYS4yMi4yMiAwIDAgMS0uMTY3LS4yMDNWNi44OThoLTIuNTM3djExLjU2NmgyLjU1NnYtNS4xYzAtMi41MyAxLjI5Ni00LjEgMy40MDgtNC4xbTQuODE1LTIuMzY3aC0yLjU5M3YxMS41NjZoMi41OTN6TTk3Ljk1OCAxLjg3YTEuNTcxIDEuNTcxIDAgMSAwIDAgMy4xNDEgMS41NzEgMS41NzEgMCAxIDAgMC0zLjE0bTguOTI4IDQuNzI5Yy0zLjU1NiAwLTYuMTMxIDIuNTUtNi4xMzEgNi4wOCAwIDEuNzE3LjYxMiAzLjI1IDEuNzA0IDQuMzYgMS4xMTIgMS4xMDggMi42NjcgMS43MTggNC40MDggMS43MTggMS40NDUgMCAyLjU1Ni0uMjc3IDQuNjY4LTEuODNsLTEuNDYzLTEuNTMzYy0xLjAzOC42ODQtMi4wMDEgMS4wMTYtMi45NDUgMS4wMTYtMi4xNDkgMC0zLjc2LTEuNjA3LTMuNzYtMy43MzJzMS42MTEtMy43MzIgMy43Ni0zLjczMmMxLjAxOCAwIDEuOTYzLjMzMyAyLjkwOCAxLjAxNmwxLjYyOS0xLjUzM2MtMS45MDctMS42MjYtMy42My0xLjgzLTQuNzc4LTEuODNtOS4xNDkgNi43NjJhLjIuMiAwIDAgMSAuMTQ5LS4wNTVoLjAxOGMuMDU2IDAgLjExMS4wMzcuMTY3LjA3M2w0LjA5MyA1LjA2M2gzLjE0OWwtNS4yOTctNi4zOTNjLS4wNzUtLjA5Mi0uMDc1LS4yMjIuMDE4LS4yOTVsNC44NzEtNC44NmgtMy4xM2wtNC4yMDQgNC4yMTNjLS4wNTYuMDU1LS4xNDguMDc0LS4yNDEuMDU1YS4yMy4yMyAwIDAgMS0uMTMtLjIwM1YxLjg3aC0yLjU3NHYxNi41OTFoMi41NTZ2LTQuNTA4YzAtLjA1NS4wMTgtLjEzLjA3NC0uMTY2eiIgZmlsbD0iIzAwMCIvPjxwYXRoIGQ9Ik0xMjcuNzc2IDE4LjczOWMyLjA5MyAwIDQuMjIzLTEuMjc1IDQuMjIzLTMuNjk1IDAtMS41ODktMS0yLjY4LTMuMDM3LTMuMzQ0bC0xLjM5LS40NjJjLS45NDQtLjMxNC0xLjM4OS0uNzU4LTEuMzg5LTEuMzY3IDAtLjcwMi42My0xLjE4MyAxLjUxOS0xLjE4My44NTIgMCAxLjYxMS41NTUgMi4wOTMgMS41MTVsMi4wNTYtMS4xMDhjLS43NTktMS41NTItMi4zMzQtMi41MTMtNC4xNDktMi41MTMtMi4yOTcgMC0zLjk2MyAxLjQ3OC0zLjk2MyAzLjQ5MiAwIDEuNjA3Ljk2MyAyLjY3OSAyLjk0NCAzLjMwN2wxLjQyNy40NjJjMSAuMzE0IDEuNDI2LjcyIDEuNDI2IDEuMzY3IDAgLjk4LS45MDggMS4zMy0xLjY4NiAxLjMzLTEuMDM3IDAtMS45NjMtLjY2NS0yLjQwNy0xLjc1NWwtMi4wOTMgMS4xMDljLjY4NSAxLjc1NSAyLjM3IDIuODQ1IDQuNDI2IDIuODQ1bS02OS41NDYtLjExMWMuODE1IDAgMS41MzgtLjA3NCAxLjk0NS0uMTN2LTIuMjE2YTE0IDE0IDAgMCAxLTEuMjc4LjA3M2MtMS4wMzcgMC0xLjgzMy0uMTg0LTEuODMzLTIuNDJWOS4xODdjMC0uMTMuMDkyLS4yMjIuMjIyLS4yMjJoMi41VjYuODc3aC0yLjVhLjIxNC4yMTQgMCAwIDEtLjIyMi0uMjIxVjMuMzNoLTIuNTU2djMuMzQ0YzAgLjEzLS4wOTMuMjIyLS4yMjMuMjIyaC0xLjc3OHYyLjA4OGgxLjc3OGMuMTMgMCAuMjIzLjA5Mi4yMjMuMjIxdjUuMzc3YzAgNC4wNDYgMi43MDQgNC4wNDYgMy43MjIgNC4wNDYiIGZpbGw9IiMwMDAiLz48L3N2Zz4=)](/ "/")

* Why Databricks

  + - Discover

      * [For App Developers](/developers "/developers")
      * [For Executives](/why-databricks/executives "/why-databricks/executives")
      * [For Startups](/product/startups "/product/startups")
    - Customers

      * [Customer Stories](/customers "/customers")
    - Partners

      * [Partner Overview

        Explore the Databricks partner ecosystem](/partners "/partners")
      * [Partner Spotlight

        Featured partner announcements](/partners/partner-spotlight "/partners/partner-spotlight")
      * [Partner Program

        Explore benefits, tiers and how to become a partner](/partners/partner-program "/partners/partner-program")
      * [Cloud Providers

        Databricks on AWS, Azure and GCP](/partners/cloud-partners "/partners/cloud-partners")
      * [Find a Partner

        Discover Databricks partners for your needs](/partners/partner-directory "/partners/partner-directory")
      * [Partner Solutions

        Find custom industry and migration solutions](/partners/consulting-and-si/partner-solutions "/partners/consulting-and-si/partner-solutions")
* Product

  + - Databricks Platform

      * [Platform Overview

        A unified platform for data, analytics and AI](/product/data-intelligence-platform "/product/data-intelligence-platform")
      * [Data Management

        Data reliability, security and performance](/product/delta-lake-on-databricks "/product/delta-lake-on-databricks")
      * [Sharing

        Open, secure, zero-copy sharing for all data](/product/delta-sharing "/product/delta-sharing")
      * [Data Warehousing

        Serverless data warehouse for SQL analytics](/product/databricks-sql "/product/databricks-sql")
      * [Governance

        Unified governance for all data, analytics and AI assets](/product/unity-catalog "/product/unity-catalog")
      * [Data Engineering

        ETL and orchestration for batch and streaming data](/product/data-engineering "/product/data-engineering")
      * [Artificial Intelligence

        Build and deploy ML and GenAI applications](/product/artificial-intelligence "/product/artificial-intelligence")
      * [Business Productivity

        Unified search, chat, dashboards and apps](/product/genie "/product/genie")
      * [Business Intelligence

        Intelligent analytics for real-world data](https://www.databricks.com/product/business-intelligence "https://www.databricks.com/product/business-intelligence")
      * [Application Development

        Quickly build secure data and AI apps](/product/databricks-apps "/product/databricks-apps")
      * [Database

        Postgres for data apps and AI agents](/product/lakebase "/product/lakebase")
      * [Security

        Open agentic SIEM built for the AI era](/product/lakewatch "/product/lakewatch")
    - Integrations and Data

      * [Marketplace

        Open marketplace for data, analytics and AI](/product/marketplace "/product/marketplace")
      * [IDE Integrations

        Build on the Lakehouse in your favorite IDE](/product/data-science/ide-integrations "/product/data-science/ide-integrations")
      * [Partner Connect

        Discover and integrate with the Databricks ecosystem](/partnerconnect "/partnerconnect")
    - Pricing

      * [Databricks Pricing

        Explore product pricing, DBUs and more](/product/pricing "/product/pricing")
      * [Cost Calculator

        Estimate your compute costs on any cloud](/product/pricing/product-pricing/instance-types "/product/pricing/product-pricing/instance-types")
    - Open Source

      * [Open Source Technologies

        Learn more about the innovations behind the platform](/product/open-source "/product/open-source")
* Solutions

  + - Databricks for Industries

      * [Communications](/solutions/industries/communications "/solutions/industries/communications")
      * [Media and Entertainment](/solutions/industries/media-and-entertainment "/solutions/industries/media-and-entertainment")
      * [Financial Services](/solutions/industries/financial-services "/solutions/industries/financial-services")
    - Cross Industry Solutions

      * [AI Agents](/solutions/ai-agents "/solutions/ai-agents")
      * [AI Governance](/solutions/industries/ai-governance "/solutions/industries/ai-governance")
      * [Cybersecurity](/solutions/industries/cybersecurity "/solutions/industries/cybersecurity")
    - Migration & Deployment

      * [Data Migration](/solutions/migration "/solutions/migration")
      * [Professional Services](/professional-services "/professional-services")
    - Solution Accelerators

      * [Explore Accelerators

        Move faster toward outcomes that matter](/solutions/accelerators "/solutions/accelerators")
* Resources

  + - Learning

      * [Training

        Discover curriculum tailored to your needs](https://www.databricks.com/learn/training/home "https://www.databricks.com/learn/training/home")
      * [Databricks Academy

      * [Certification

        Gain recognition and differentiation](https://www.databricks.com/learn/training/certification "https://www.databricks.com/learn/training/certification")
      * [Free Edition

        Learn professional Data and AI tools for free](/learn/free-edition "/learn/free-edition")
      * [University Alliance

        Want to teach Databricks? See how.](/university "/university")
    - Events

      * [Data + AI Summit](https://www.databricks.com/dataaisummit "https://www.databricks.com/dataaisummit")
      * [Data + AI World Tour](/dataaisummit/worldtour "/dataaisummit/worldtour")
      * [AI Days](https://www.databricks.com/ai-days "https://www.databricks.com/ai-days")
    - Blog and Podcasts

      * [Databricks Blog

        Explore news, product announcements, and more](/blog "/blog")
      * [AI Blog

        Explore our AI research and engineering work](/blog/category/ai "/blog/category/ai")
      * [Data Brew Podcast

        Let’s talk data!](/discover/data-brew "/discover/data-brew")
      * [Champions of Data + AI Podcast

        Insights from data leaders powering innovation](/discover/champions-of-data-and-ai "/discover/champions-of-data-and-ai")
    - Get Help

      * [Customer Support](https://www.databricks.com/support "https://www.databricks.com/support")
      * [Documentation](https://www.databricks.com/databricks-documentation "https://www.databricks.com/databricks-documentation")
      * [Community](https://community.databricks.com/s/ "https://community.databricks.com/s/")
    - Dive Deep

      * [Resource Center](/resources "/resources")
      * [Demo Center](/resources/demos "/resources/demos")
      * [Architecture Center](/resources/architectures "/resources/architectures")
* About

  + - Company

      * [Who We Are](/company/about-us "/company/about-us")
      * [Our Team](/company/leadership-team "/company/leadership-team")
      * [Databricks Ventures](/databricks-ventures "/databricks-ventures")
    - Careers

      * [Working at Databricks](/company/careers "/company/careers")
      * [Open Jobs](/company/careers/open-positions "/company/careers/open-positions")
    - Press

      * [Awards and Recognition](/company/awards-and-recognition "/company/awards-and-recognition")
      * [Newsroom](/company/newsroom "/company/newsroom")
    - Security and Trust

      * [Security and Trust](/trust "/trust")
* DATA + AI SUMMIT[![Data+ai summit promo](https://www.databricks.com/sites/default/files/2026-03/dais26-nav-promo-240x96-2x.svg)

  JUNE 15–18|SAN FRANCISCO

  Join us at the world’s largest data, apps and AI event.

  Register](/dataaisummit?itm_source=www&itm_category=home&itm_page=home&itm_location=navigation&itm_component=navigation&itm_offer=dataaisummit "/dataaisummit?itm_source=www&itm_category=home&itm_page=home&itm_location=navigation&itm_component=navigation&itm_offer=dataaisummit")

* Ready to get started?
* [Get a Demo](/resources/demos "/resources/demos")

DATA + AI SUMMIT[![Data+ai summit promo](https://www.databricks.com/sites/default/files/2026-03/dais26-nav-promo-240x96-2x.svg)

JUNE 15–18|SAN FRANCISCO

Join us at the world’s largest data, apps and AI event.

Register](/dataaisummit?itm_source=www&itm_category=home&itm_page=home&itm_location=navigation&itm_component=navigation&itm_offer=dataaisummit "/dataaisummit?itm_source=www&itm_category=home&itm_page=home&itm_location=navigation&itm_component=navigation&itm_offer=dataaisummit")

* [Login](https://login.databricks.com/?dbx_source=www&itm=main-cta-login&l=en-EN "https://login.databricks.com/?dbx_source=www&itm=main-cta-login&l=en-EN")
* [Try Databricks](https://www.databricks.com/signup?dbx_source=www&itm_data=dbx-web-nav&l=en-EN&itm_source=www&itm_category=home&itm_page=home&itm_offer=signup "https://www.databricks.com/signup?dbx_source=www&itm_data=dbx-web-nav&l=en-EN&itm_source=www&itm_category=home&itm_page=home&itm_offer=signup")

1. [All blogs](/blog "/blog")
2. /

   [Platform](/blog/category/platform "/blog/category/platform")

Table of contents

* [Build and orchestrate complete, production-ready pipelines and jobs using natural language](#section-1 "#section-1")
* [Monitor, diagnose, and debug pipelines and jobs](#section-2 "#section-2")
* [What’s next](#section-3 "#section-3")

Table of contents

Table of contents

* [Build and orchestrate complete, production-ready pipelines and jobs using natural language](#section-1 "#section-1")
* [Monitor, diagnose, and debug pipelines and jobs](#section-2 "#section-2")
* [What’s next](#section-3 "#section-3")

[Product](/blog/category/platform/product "/blog/category/platform/product")April 28, 2026

Agentic Data Engineering with Genie Code and Lakeflow
=====================================================

Genie Code streamlines data pipeline development, orchestration, and deployment

by  [Gal Oshri](/blog/author/gal-oshri "/blog/author/gal-oshri"), [Camiel Steenstra](/blog/author/camiel-steenstra "/blog/author/camiel-steenstra"), [Lennart Kats](/blog/author/lennart-kats "/blog/author/lennart-kats")  and  [Joanna Zouhour](/blog/author/joanna-zouhour "/blog/author/joanna-zouhour")

Summary

* Genie Code is an autonomous AI partner built specifically for data
* Data engineers can use Genie Code directly within Lakeflow, from building pipelines in the Pipeline Editor to orchestrating workflows in Lakeflow Jobs
* Genie Code supports the full data engineering lifecycle - from development and orchestration to monitoring and debugging - within a single agent experience

With [Genie Code](https://www.databricks.com/blog/introducing-genie-code "https://www.databricks.com/blog/introducing-genie-code"), data engineers can use natural language to generate production-ready data pipelines, orchestrate them with jobs, and debug failures. Tasks that used to take weeks - finding data, building transformations, stitching together jobs, and fixing failures - can now be done in hours, while staying aligned with governance and operational standards.

Below, we'll walk through how this works in practice: discovering data, building pipelines, orchestrating jobs, and debugging failures, all from a single conversation.

Build and orchestrate complete, production-ready pipelines and jobs using natural language
------------------------------------------------------------------------------------------

Genie Code can now take you from exploration to scheduled pipelines and jobs in one thread, helping you author and operate them end-to-end.

It accelerates the development of [Lakeflow Spark Declarative Pipelines](https://www.databricks.com/product/data-engineering/spark-declarative-pipelines "https://www.databricks.com/product/data-engineering/spark-declarative-pipelines") and simplifies how pipelines and notebooks are orchestrated and run through [Lakeflow Jobs](https://www.databricks.com/product/data-engineering/lakeflow-jobs "https://www.databricks.com/product/data-engineering/lakeflow-jobs"). Genie Code understands your pipeline and job context, accessing the code, configuration, and run results.

Genie Code helps across key stages of the data engineering lifecycle:

* **Search over data assets, not just code**: Genie Code uses popularity, lineage, code samples, and Unity Catalog metadata to identify the most relevant datasets for your task. For example, you can ask Genie Code to explain how tables relate or trace how data flows through a pipeline. At [SiriusXM](https://www.databricks.com/blog/introducing-genie-code "https://www.databricks.com/blog/introducing-genie-code"), teams use Genie Code to understand table relationships more quickly.
* **Build and modify pipelines**: Start by describing the pipeline you want in plain language, such as a fraud detection pipeline built on a medallion architecture. Genie Code generates a Spark Declarative Pipeline with Bronze, Silver, and Gold layers, including sources, transformations, data quality expectations, and outputs. From there, you can ask for changes, review the proposed diffs, and run and test the pipeline.  

  ![Lakeflow Spark Declarative Pipelines](https://www.databricks.com/sites/default/files/inline-images/agentic-data-engineering-genie-code-lakeflow-blog-img-1.png)
* **Define and orchestrate jobs:** No need to manually define and maintain orchestration logic. You describe the job you want, including tasks, dependencies, and schedule. Genie Code configures it for you, then helps modify, debug, and fix orchestration issues in natural language.  

  ![Orchestrate Jobs](https://www.databricks.com/sites/default/files/inline-images/agentic-data-engineering-genie-code-lakeflow-blog-img-2.png)
* **Extend and evolve existing workflows**: As requirements change, Genie Code helps you update pipelines and jobs with new datasets and transformations. It understands the current structure and results of your pipelines, and can extend them by writing [AutoCDC](https://docs.databricks.com/aws/en/ldp/cdc "https://docs.databricks.com/aws/en/ldp/cdc") flows for change data capture, configuring [Auto Loader](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/ "https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/"), applying [data quality expectations](https://docs.databricks.com/aws/en/ldp/expectations "https://docs.databricks.com/aws/en/ldp/expectations"), and following the medallion architecture.
* **Embrace best practices with** [Declarative Automation Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/ "https://docs.databricks.com/aws/en/dev-tools/bundles/") (DABs): Genie Code can work directly within your existing DABs projects: adding resources, updating configurations, validating bundles, and deploying to your targets. So you can adopt software engineering best practices like source control, testing, and CI/CD for your data projects without hand-writing YAML.
* **Work faster without lowering standards:** These capabilities reduce manual effort while keeping workflows aligned with enterprise requirements. Pipelines remain governed through Unity Catalog and follow established patterns for performance and data quality, while jobs inherit consistent configuration for scheduling, retries, and dependencies. Data engineers stay in control, but spend less time on repetitive work.

Monitor, diagnose, and debug pipelines and jobs
-----------------------------------------------

* **Understanding and improving pipeline behavior**: Genie Code can inspect datasets and pipeline outputs to help you understand a pipeline end-to-end. For example, it can summarize transformations, trace how data flows into downstream tables, and highlight unexpected changes in row counts or schemas.
* **Debug and diagnose job and pipeline failures**: When a pipeline or job fails, Genie Code helps you work through the issue. It analyzes errors, proposes updates across the relevant files, and shows you the diffs before applying any changes. You can review each update and decide what moves forward. This turns long, manual debug cycles into faster guided iterations.  

  ![Debug Pipelines and Jobs](https://www.databricks.com/sites/default/files/inline-images/agentic-data-engineering-genie-code-lakeflow-blog-img-3.png)
* **Extend and customize Genie Code:** Genie Code is not limited to built-in capabilities. Teams can extend it with [custom instructions](https://docs.databricks.com/aws/en/genie-code/instructions "https://docs.databricks.com/aws/en/genie-code/instructions"), [agent skills](https://docs.databricks.com/aws/en/genie-code/skills "https://docs.databricks.com/aws/en/genie-code/skills") and integrate external systems [through MCP servers](https://docs.databricks.com/gcp/en/genie-code/mcp "https://docs.databricks.com/gcp/en/genie-code/mcp"), allowing Genie Code to operate on domain-specific logic, internal tools, and custom workflows. This ensures Genie Code adapts to your environment and domain knowledge.

What’s next
-----------

More capabilities are coming to extend Genie Code across pipelines, jobs, and the broader platform. One exciting feature on the horizon is **AI-optimized workloads**. In the future, you can allow Genie Code to also run in the background to keep your platform working efficiently, so you can hand off those repetitive and time-consuming tasks. This includes responding to job failures and managing routine upgrades, but also automatically right-sizing cluster use.

Curious to learn more about these updates and best practices? Make sure to [register for Data+AI Summit](https://www.databricks.com/dataaisummit "https://www.databricks.com/dataaisummit") where we have hundreds of sessions covering Genie Code, Lakeflow and much more!

### Try Genie Code’s data engineering capabilities

Open Genie Code in agent mode and ask it to help you build or update your pipelines and jobs. Check out the [demo](https://www.databricks.com/resources/demos/videos/get-know-genie-code "https://www.databricks.com/resources/demos/videos/get-know-genie-code") for more details .

Review the [documentation](https://docs.databricks.com/aws/en/ldp/de-agent "https://docs.databricks.com/aws/en/ldp/de-agent") to learn more.

### Get the latest posts in your inbox

-------

[View all blogs](/blog "/blog")

[![databricks logo]()![databricks logo](https://www.databricks.com/sites/default/files/2023-08/databricks-default.png?v=1712162038)](https://www.databricks.com/ "https://www.databricks.com/")

Why Databricks

Discover

* [For App Developers](/developers "/developers")
* [For Executives](/why-databricks/executives "/why-databricks/executives")
* [For Startups](/product/startups "/product/startups")

Customers

* [Customer Stories](https://www.databricks.com/customers "https://www.databricks.com/customers")

Partners

* [Partner Overview](/partners "/partners")
* [Partner Program](/partners/partner-program "/partners/partner-program")
* [Find a Partner](/partners/partner-directory "/partners/partner-directory")

Why Databricks

Discover

* [For App Developers](/developers "/developers")
* [For Executives](/why-databricks/executives "/why-databricks/executives")
* [For Startups](/product/startups "/product/startups")

Customers

* [Customer Stories](https://www.databricks.com/customers "https://www.databricks.com/customers")

Partners

* [Partner Overview](/partners "/partners")
* [Partner Program](/partners/partner-program "/partners/partner-program")
* [Find a Partner](/partners/partner-directory "/partners/partner-directory")

Product

Databricks Platform

* [Platform Overview](/product/data-intelligence-platform "/product/data-intelligence-platform")
* [Sharing](/product/delta-sharing "/product/delta-sharing")
* [Governance](/product/unity-catalog "/product/unity-catalog")

Pricing

* [Pricing Overview](/product/pricing "/product/pricing")
* [Pricing Calculator](/product/pricing/product-pricing/instance-types "/product/pricing/product-pricing/instance-types")

[Open Source](/product/open-source "/product/open-source")

Integrations and Data

* [Marketplace](/product/marketplace "/product/marketplace")
* [IDE Integrations](/product/data-science/ide-integrations "/product/data-science/ide-integrations")
* [Partner Connect](/partnerconnect "/partnerconnect")

Product

Databricks Platform

* [Platform Overview](/product/data-intelligence-platform "/product/data-intelligence-platform")
* [Sharing](/product/delta-sharing "/product/delta-sharing")
* [Governance](/product/unity-catalog "/product/unity-catalog")

Pricing

* [Pricing Overview](/product/pricing "/product/pricing")
* [Pricing Calculator](/product/pricing/product-pricing/instance-types "/product/pricing/product-pricing/instance-types")

Open Source

Integrations and Data

* [Marketplace](/product/marketplace "/product/marketplace")
* [IDE Integrations](/product/data-science/ide-integrations "/product/data-science/ide-integrations")
* [Partner Connect](/partnerconnect "/partnerconnect")

Solutions

Databricks For Industries

* [Communications](/solutions/industries/communications "/solutions/industries/communications")
* [Financial Services](/solutions/industries/financial-services "/solutions/industries/financial-services")
* [Healthcare and Life Sciences](/solutions/industries/healthcare-and-life-sciences "/solutions/industries/healthcare-and-life-sciences")

Cross Industry Solutions

* [AI Agents](/solutions/ai-agents "/solutions/ai-agents")
* [AI Governance](/solutions/industries/ai-governance "/solutions/industries/ai-governance")
* [Cybersecurity](/solutions/industries/cybersecurity "/solutions/industries/cybersecurity")

[Data Migration](/solutions/migration "/solutions/migration")

[Professional Services](/professional-services "/professional-services")

[Solution Accelerators](/solutions/accelerators "/solutions/accelerators")

Solutions

Databricks For Industries

* [Communications](/solutions/industries/communications "/solutions/industries/communications")
* [Financial Services](/solutions/industries/financial-services "/solutions/industries/financial-services")
* [Healthcare and Life Sciences](/solutions/industries/healthcare-and-life-sciences "/solutions/industries/healthcare-and-life-sciences")

Cross Industry Solutions

* [AI Agents](/solutions/ai-agents "/solutions/ai-agents")
* [AI Governance](/solutions/industries/ai-governance "/solutions/industries/ai-governance")
* [Cybersecurity](/solutions/industries/cybersecurity "/solutions/industries/cybersecurity")

Data Migration

Professional Services

Solution Accelerators

Resources

[Documentation](https://www.databricks.com/databricks-documentation "https://www.databricks.com/databricks-documentation")

[Customer Support](https://www.databricks.com/support "https://www.databricks.com/support")

[Community](https://community.databricks.com/ "https://community.databricks.com/")

Learning

* [Training](/learn/training/home "/learn/training/home")
* [Certification](https://www.databricks.com/learn/training/certification "https://www.databricks.com/learn/training/certification")
* [Free Edition](/learn/free-edition "/learn/free-edition")

Events

* [Data + AI Summit](/dataaisummit "/dataaisummit")
* [Data + AI World Tour](/dataaisummit/worldtour "/dataaisummit/worldtour")
* [AI Days](https://www.databricks.com/ai-days "https://www.databricks.com/ai-days")

Blog and Podcasts

* [Databricks Blog](/blog "/blog")
* [AI Blog](/blog/category/ai "/blog/category/ai")
* [Data Brew Podcast](/discover/data-brew "/discover/data-brew")

Resources

Documentation

Customer Support

Community

Learning

* [Training](/learn/training/home "/learn/training/home")
* [Certification](https://www.databricks.com/learn/training/certification "https://www.databricks.com/learn/training/certification")
* [Free Edition](/learn/free-edition "/learn/free-edition")

Events

* [Data + AI Summit](/dataaisummit "/dataaisummit")
* [Data + AI World Tour](/dataaisummit/worldtour "/dataaisummit/worldtour")
* [AI Days](https://www.databricks.com/ai-days "https://www.databricks.com/ai-days")

Blog and Podcasts

* [Databricks Blog](/blog "/blog")
* [AI Blog](/blog/category/ai "/blog/category/ai")
* [Data Brew Podcast](/discover/data-brew "/discover/data-brew")

About

Company

* [Who We Are](/company/about-us "/company/about-us")
* [Our Team](/company/leadership-team "/company/leadership-team")
* [Databricks Ventures](/databricks-ventures "/databricks-ventures")

Careers

* [Open Jobs](/company/careers/open-positions "/company/careers/open-positions")
* [Working at Databricks](/company/careers "/company/careers")

Press

* [Awards and Recognition](/company/awards-and-recognition "/company/awards-and-recognition")
* [Newsroom](/company/newsroom "/company/newsroom")

[Security and Trust](/trust "/trust")

About

Company

* [Who We Are](/company/about-us "/company/about-us")
* [Our Team](/company/leadership-team "/company/leadership-team")
* [Databricks Ventures](/databricks-ventures "/databricks-ventures")

Careers

* [Open Jobs](/company/careers/open-positions "/company/careers/open-positions")
* [Working at Databricks](/company/careers "/company/careers")

Press

* [Awards and Recognition](/company/awards-and-recognition "/company/awards-and-recognition")
* [Newsroom](/company/newsroom "/company/newsroom")

Security and Trust

[![databricks logo]()![databricks logo](https://www.databricks.com/sites/default/files/2023-08/databricks-default.png?v=1712162038)](https://www.databricks.com/ "https://www.databricks.com/")

Databricks Inc.  
160 Spear Street, 15th Floor  
San Francisco, CA 94105  
1-866-330-0121

![]()![](https://www.databricks.com/sites/default/files/2021/02/telco-icon-2.png?v=1715274112)

[See Careers](https://www.databricks.com/company/careers "https://www.databricks.com/company/careers")

© Databricks 2026. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the [Apache Software Foundation](https://www.apache.org/ "https://www.apache.org/").

* [Privacy Notice](https://www.databricks.com/legal/privacynotice "https://www.databricks.com/legal/privacynotice")
* |[Terms of Use](https://www.databricks.com/legal/terms-of-use "https://www.databricks.com/legal/terms-of-use")
* |[Modern Slavery Statement](https://www.databricks.com/legal/modern-slavery-policy-statement "https://www.databricks.com/legal/modern-slavery-policy-statement")
* |[California Privacy](https://www.databricks.com/legal/supplemental-privacy-notice-california-residents "https://www.databricks.com/legal/supplemental-privacy-notice-california-residents")
* |[Your Privacy Choices](#yourprivacychoices "#yourprivacychoices")
* ![](https://www.databricks.com/sites/default/files/2022-12/gpcicon_small.png)