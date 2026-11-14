# To-Do API: Requirements
## Users can
- Create a task with a title
- See all tasks
- Mark a task as done
- Delete a task

## Rules
- Asking for a task that does not exist returns a clear "not found" error
- A health-check address reports whether the service is up

## Non-functional
- Every change is covered by automated tests that run on each pull request
- The app runs in a container and can be deployed with no manual steps

## Out of scope (for now)
- User accounts, a database, a web front end