import os

from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename

from app import db
from app.models.project import Project
from app.services.pylint_service import PylintService
from app.services.bandit_service import BanditService
from app.services.radon_service import RadonService

upload_bp = Blueprint("upload", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@upload_bp.route("/file", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return jsonify({"message": "No file selected"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"message": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)
    pylint_report = PylintService.analyze(filepath)
    bandit_report = BanditService.analyze(filepath)
    radon_report = RadonService.analyze(filepath)
    project = Project(
        project_name=filename,
        uploaded_file=filepath
    )

    db.session.add(project)
    db.session.commit()

    return jsonify({
    "message": "File uploaded successfully",
    "filename": filename,
    "pylint": pylint_report,
    "bandit": bandit_report,
    "radon": radon_report
}), 200