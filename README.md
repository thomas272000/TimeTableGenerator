# Timetable Generation

## Features

- **Course Management**: Add, view, update, and delete courses.
- **Subject Management**: Add, view, update, and delete subjects assigned to courses.
- **Staff Management**: Register staff members and assign them to teach specific subjects.
- **Assignment Management**: Allocate subjects to specific staff members for each course.
- **Period Management**: Define periods within each course, including assigning subjects and teachers per day.
- **Timetable Generation**: Generate weekly timetables for courses, ensuring conflict-free scheduling.

## Technologies Used

- **Backend**: Django, Django ORM
- **Frontend**: HTML, CSS
- **Database**: SQLite (or your preferred database)
- **Admin Interface**: Django Admin

## Models

1. **CourseModel**: Stores course information.
2. **SubjectModel**: Represents subjects within each course.
3. **StaffModel**: Manages staff data.
4. **StaffSubjectAssignmentModel**: Links staff to subjects for specific courses.
5. **PeriodModel**: Manages daily periods, associating subjects and staff.

## TO SETUP

1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver



| Endpoint                    | View Function        | Description                     |
|-----------------------------|----------------------|---------------------------------|
| `/admin/`                   | -                    | Admin interface                 |
| `/Coursereg/`               | `register_course`    | Register a new course           |
| `/viewcourse/`              | `view_courses`       | View all courses                |
| `/coursedel/<int:id>/`      | `course_delete`      | Delete a course                 |
| `/courseupd/<int:id>/`      | `course_update`      | Update course details           |
| `/subregister/`             | `register_subject`   | Register a new subject          |
| `/viewsub/`                 | `view_subjects`      | View all subjects               |
| `/subdel/<int:id>/`         | `subject_delete`     | Delete a subject                |
| `/subupd<int:id>/`          | `subject_update`     | Update subject details          |
| `/staffreg/`                | `register_staff`     | Register a new staff member     |
| `/viewstaff/`               | `view_staffs`        | View all staff members          |
| `/staffdel/<int:id>/`       | `staff_delete`       | Delete a staff member           |
| `/staffupd/<int:id>/`       | `staff_update`       | Update staff details            |
| `/assignmentsview/`         | `assignment_list`    | View all staff assignments      |
| `/assigncr/`                | `assignment_create`  | Create a new staff assignment   |
| `/assignmentsupd/<int:id>/` | `assignment_update`  | Update a staff assignment       |
| `/assignmentsdel/<int:id>/` | `assignment_delete`  | Delete a staff assignment       |
| `/periodsview/`             | `period_list`        | View all periods                |
| `/periodscr/`               | `period_create`      | Create a new period             |
| `/periodsupd/<int:id>/`     | `period_update`      | Update a period                 |
| `/periodsdel/<int:id>/`     | `period_delete`      | Delete a period                 |
| `/timetable/`               | `generate_timetable` | Generate a weekly timetable     |
