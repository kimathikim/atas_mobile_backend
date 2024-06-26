"""This module defines all the paths for the user moijdule"""
from app.models import storage
from app.views import app_views, token_required
from app.models.JobPostings import Job
from flask import jsonify, request, abort, session
from datetime import datetime, timedelta
from flasgger import Swagger, swag_from
from app.views.jobs import token_required


@app_views.route('/jobs', methods=['POST'])
@token_required
def create_job(current_user):
    if current_user.user_type != 'Employer':
        return jsonify({'message': 'Cannot perform that function!'})
    data = request.get_json()
    new_job = Job(
        EmployerID=current_user.id,
        JobTitle=data['JobTitle'],
        JobDescription=data.get('JobDescription'),
        JobType=data.get('JobType'),
        SalaryRange=data.get('SalaryRange'),
        Location=data.get('Location'),
        Requirements=data.get('Requirements')
    )
    new_job.save()
    return jsonify({'message': 'New job created!'})

# get all jobs
@app_views.route('/jobs', methods=['GET'], strict_slashes=False)
@token_required
def get_jobs(current_user):
    jobs = storage.all(Job)
    jobs = [job.to_dict() for job in jobs.values()]
    return jsonify(jobs), 200

# get a single job
@app_views.route('/jobs/<job_id>', methods=['GET'], strict_slashes=False)
@token_required
@swag_from('swagger_config/get_job.yml')
def get_job(current_user, job_id):
    job = storage.get(Job, job_id)
    if not job:
        return jsonify({'message': 'Job not found!'})
    return jsonify(job.to_dict()), 200

# update a job
@app_views.route('/jobs/<job_id>', methods=['PUT'], strict_slashes=False)
@token_required
@swag_from('swagger_config/update_job.yml')
def update_job(current_user, job_id):
    job = storage.get(Job, job_id)
    if not job:
        return jsonify({'message': 'Job not found!'})
    data = request.get_json()
    for key, value in data.items():
        setattr(job, key, value)
    job.save()
    return jsonify({'message': 'Job updated!'})

# delete a job
@app_views.route('/jobs/<job_id>', methods=['DELETE'], strict_slashes=False)
@token_required
@swag_from('swagger_config/delete_job.yml')
def delete_job(current_user, job_id):
    job = storage.get(Job, job_id)
    if not job:
        return jsonify({'message': 'Job not found!'})
    job.delete()
    return jsonify({'message': 'Job deleted!'})



@app_views.route('/jobs/<job_id>/applications', methods=['GET'], strict_slashes=False)
@token_required
# @swag_from('swagger_config/get_job_applications.yml')
def get_job_applications(current_user, job_id):
    job = storage.get(Job, job_id)
    if not job:
        return jsonify({'message': 'Job not found!'})
    applications = job.applications
    applications = [app.to_dict() for app in applications]
    return jsonify(applications), 200

