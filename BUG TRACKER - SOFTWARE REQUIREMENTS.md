BUG TRACKER - SOFTWARE REQUIREMENTS

- User Login [✅]
	- Inside the app, create user [✅]
	- Assign user roles (Admin, Project Manager, Developer, Client / Ticket Submitter) [✅]
	- Upload user profile picture [✅]
	- Roles: [✅]
		- Admin: can do everything, including app settings []
		- Project manager: can see all projects, can create a project, is able to manage role assignment of his own projects, manage tickets, add comments, etc. []
		- Developer: Can only see the projects he's assigned to, can select and manage tickets, add comments, etc. []
		- Submitter: Can only see the projects he's assigned to, can only submit tickets, can only see the tickets he submitted, can add comments. []

- Projects [✅]
	- Dashboard: show all of projects this specific user is working on, show statistics, etc.
	- Kanban board: after selecting a project, show four cards:
		- Open tickets: a list of all of the tickets that have an 'open' status for this project []
		- TODO: a list of all the tickets that were assigned to me (by me, or by a project manager / admin) []
		- IN DEVELOPMENT: a list of all the tickets that the user is currently working on []
		- DONE: a list of all of the tickets that the user has finished []
	- Project List: Project name, description, logo, manage users, details []
	- Manage project users []
		- Add or remove users from project []
		- When a user is created, they are assigned the 'Tester' role by default []
		- Allow admin and project managers to change other user's roles []
		- Allow a user to edit his profile: name, last name, profile picture, etc. []
		- Allow a user to change his own password []
	- Project details [✅]
		- Show project title and description [✅]
		- Created by user, created at date [✅]
		- Number of tickets opened/closed [✅]
		- Number of developers assigned - name, email and role assigned (admin, developer, project manager, or submitter) [X]
		- List of tickets: (Condensed list of details) [✅]
			- Ticket title [✅]
			- Tester [✅]
			- Developer - name of the developer that was assigned to this ticket [✅]
			- Status (New, open, in progress, done / closed) [✅]
			- Created (date) [✅]
			- Details for a single ticket [✅]
				
- Tickets [✅]
	- Ticket title [✅]
	- Ticket description [✅]
	- Assigned developer (user) [✅]
	- Submitter (user) [✅]
	- Project title [✅]
	- Ticket priority (Low, Medium, High) [✅]
	- Ticket status (New, open, in progress, done / closed) [✅]
	- Ticket type (Feature request, bug / error, design) [✅]
	- Created at (datetime) [✅]
	- Closed at (datetime) [✅]
	- Lastest update (datetime) [✅]

- Ticket comments: [✅]
	- Commenter (user) [✅]
	- Message [✅]
	- Created at (datetime) [✅]

- Ticket change history: []
	- User that made the change []
	- Property (column) []
	- Old value []
	- New value []
	- Date changed (datetime) []

- Ticket files (Screenshots of the bug) [✅]
	- File (images only?: all files) [✅]
	- Uploader (user) [✅]
	- Title [✅]
	- Uploaded at (date) [✅]


POSSIBLE CHANGES:
	- Status:
		- Backlog (Tickets abiertos)
		- Selected for development (Asignado)
		- In progress (En desarrollo)
		- Done (Cerrado)
	- Priority:
		- Low
		- Medium
		- High
		- Highest [X]
	- Add labels to tickets
		- Design
		- Error
		- Feature
		- etc
		-more labels?
	- Projects
		- Sprints
			- User stories
				- Tickets


TABLES:
	- users
		- id
		- name
		- email
		- password
		- group_id
		- date_created
		- profile_picture

	- roles
		- id
		- description

	- roles_permissions
		- id
		- group_id
		- permissions_id

	- permissions
		- id
		- permission

	===

	- projects
		- id
		- title
		- short description
		- description
		- logo
		- status
		- user_id (user who created the project)
		- date_created

	- project_files (system requirement specifications, documentation, etc.)
		- id
		- project_id
		- filename
		- file

	- tickets
		- id
		- project_id
		- submitted_by (user who submitted this ticket)
		- assigned_to (which developer is assigned to resolve it)
		- title
		- description
		- priority (none, low, medium, high, highest)
		- type (feature, bug/error, design)
		- status (backlog/new, open/selected for development, in progress, closed/done)
		- created_at
		- latest_update
		- closed_at

	- ticket_files
		- id
		- ticket_id
		- uploaded_by (user who uploaded the files)
		- notes/description
		- file
		- date_uploaded

	- comments
		- id
		- user_id
		- ticket_id
		- comment
		- date_created

