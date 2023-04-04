from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)


@app.route("/")
def index():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    jobs_list = []

    for job in db_sess.query(Jobs).all():
        d = {
            "title-of-activity": job.job,
            "team-leader": job.team_leader,
            "duration": job.work_size,
            "collaborators": job.collaborators,
            "is-finished": job.is_finished
        }
        jobs_list.append(d)
    print(jobs_list)
    return render_template("works_log.html", jobs_list=jobs_list)


if __name__ == "__main__":
    app.run()
